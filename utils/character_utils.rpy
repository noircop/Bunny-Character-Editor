init python:
    def get_character_layers(model):
        if not model.gender:
            return []

        gender = model.gender.strip().lower()

        layers = []

        # 1. Основа - тело
        layers.append(
            f"{BCE_CHAR_PATH}base/bce_{gender}_base.png"
        )

        # 2. Лицо
        if model.face:
            layers.append(
                f"{BCE_CHAR_PATH}face/{gender}/{model.face}.png"
            )

        # 3. Одежда
        if model.suit:
            layers.append(
                f"{BCE_CHAR_PATH}suit/{gender}/{model.suit}.png"
            )

        # 4. Волосы
        if model.hair:
            layers.append(
                f"{BCE_CHAR_PATH}hair/{gender}/{model.hair}.png"
            )

        return layers

    def apply_character_change(item):
        t = item.get("category")
        i = item.get("id")

        if not t:
            print("Item has no category")
            return

        dispatch = {
            "face": character_service.set_face,
            "hair": character_service.set_hair,
            "suit": character_service.set_suit,
        }

        fn = dispatch.get(t)

        if fn:
            fn(i)
        else:
            print("Unknown category: {}".format(t))
    
    def get_character_active_element(category):
        return getattr(store.character_model, category, None)

    def is_selected_item(item):
        return (
            item.get("id")
            == get_character_active_element(item.get("category"))
        )