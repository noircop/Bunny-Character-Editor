from modules.bunny_character_editor.core.character_model import CharacterModel

class CharacterService:
    def __init__(self, model: CharacterModel):
        self.model = model

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

    # Дебаг
    def debug(self):
        print(self.model)