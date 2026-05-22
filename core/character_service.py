from renpy.store import store
from modules.bunny_character_editor.core.character_model import CharacterModel
from modules.bunny_character_editor.core.character_validator import CharacterValidator

class CharacterService:
    def __init__(self, model: CharacterModel, validator: CharacterValidator):
        self.model = model
        self.validator = validator

    # Пол 
    def set_gender(self, gender):
        self.model.set_gender(gender)

    # Внешний Вид
    def set_face(self, face_id):
        self.model.set_face(face_id)

    def set_hair(self, hair_id):
        self.model.set_hair(hair_id)

    def set_suit(self, suit_id):
        self.model.set_suit(suit_id)

    # Имя
    def set_name(self, name):
        self.model.set_name(name)

    def set_name_color(self, color):
        self.model.set_name_color(color)

    # Сохранение
    def export(self):
        return self.model.to_dict()

    def apply_to_game(self):

        if not self.validator.validate():
            return False

        store.bce_custom_character = self.export()
        self.model.reset_all()

        return True

    # Дебаг
    def debug(self):
        print(self.model)