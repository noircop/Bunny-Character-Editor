from renpy.store import store

class EditorFacade:

    def __init__(self, model, service, validator, flow, image_loader):
        self.model = model
        self.service = service
        self.validator = validator
        self.flow = flow
        self.image_loader = image_loader

        # dispatch выбор активного элемента внешности
        self._dispatch = {
            "face": self.service.set_face,
            "hair": self.service.set_hair,
            "suit": self.service.set_suit,
        }

    # FLOW
    @property
    def started(self):
        return self.flow.started


    @property
    def finished(self):
        return self.flow.finished


    @property
    def current_step(self):
        return self.flow.current
    
    @property
    def step_index(self):
        return self.flow.current_step

    @property
    def step_can_next(self):
        return not self.flow.is_last


    @property
    def step_can_prev(self):
        return not self.flow.is_first

    @property
    def step_count(self):
        return self.flow.step_count
    
    def step_next(self):
        self.flow.next()

    def step_prev(self):
        self.flow.prev()

    def step_go_to(self, index: int):
        self.flow.go_to(index)

    def choice_gender_and_start(self, gender: str):
        self.service.set_gender(gender)
        self.flow.start()
    
    def finish(self):
        self.flow.finish()
    
    # Character
    @property
    def character_gender(self):
        return self.model.gender

    def apply_character_change(self, item):
        t = item.get("category")
        i = item.get("id")

        fn = self._dispatch.get(t)
        if fn:
            fn(i)

    def get_character_attr(self, attr_name, default=None):
        return getattr(self.model, attr_name, default)
    
    def is_selected_item(self, item) -> bool:
        if not item:
            return False

        category = item.get("category")
        item_id = item.get("id")

        active = self.get_character_attr(category)

        return item_id == active
    
    # Assets
    def get_current_assets(self):
        step = self.current_step

        return self.image_loader.get_items(
            step.get("layer"),
            self.character_gender
        )

    # Save
    def apply_to_game(self):

        if not self.validator.validate():

            error = self.validator.get_first_error()

            self.flow.go_to_step_by_id(error["step"])

            return {
                "status": False,
                "error": error
            }

        store.bce_custom_character = self.model.to_dict()

        self.model.reset_all()

        return {
            "status": True,
            "error": None
        }
    
    # Render
    # TODO Вынести в Отдельный Класс
    # ARCH 0.2 у нас два вида Рендера Персонажа. 
    # Но скорее всего для рендера уже сохраненных персонажей будет использовать просто Утилита
    def get_character_layers(self):

        # Временный Костыль
        bce_char_path = "modules/bunny_character_editor/assets/character/"

        model = self.model


        if not model.gender:
            return []

        gender = model.gender.strip().lower()

        layers = []

        # 1. Основа - тело
        layers.append(
            f"{bce_char_path}base/bce_{gender}_base.png"
        )

        # 2. Лицо
        if model.face:
            layers.append(
                f"{bce_char_path}face/{gender}/{model.face}.png"
            )

        # 3. Одежда
        if model.suit:
            layers.append(
                f"{bce_char_path}suit/{gender}/{model.suit}.png"
            )

        # 4. Волосы
        if model.hair:
            layers.append(
                f"{bce_char_path}hair/{gender}/{model.hair}.png"
            )

        return layers
