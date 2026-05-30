class CharacterModel:

    def __init__(self):
        self.reset_all()

    # Состояния
    def reset_all(self):
        self.gender = None

        self.face = None
        self.hair = None
        self.suit = None

        self.name = ""
        self.name_color = "#FFFFFF"

    def reset_appearance(self):
        self.face = None
        self.hair = None
        self.suit = None

    # Сеттеры (используются сервисом)
    def set_gender(self, gender: str):
        if gender not in ("male", "female"):
            raise ValueError(f"Invalid gender: {gender}")

        # если меняем пол — сбрасываем внешний вид
        if self.gender != gender:
            self.gender = gender
            self.reset_appearance()

    def set_face(self, face_id: str):
        self.face = face_id

    def set_hair(self, hair_id: str):
        self.hair = hair_id

    def set_suit(self, suit_id: str):
        self.suit = suit_id

    def set_name(self, name: str):
        self.name = name.strip()

    def set_name_color(self, color: str):
        self.name_color = color


    # Сериализация (Для Сохранения)
    def to_dict(self) -> dict:
        return {
            "gender": self.gender,
            "face": self.face,
            "hair": self.hair,
            "suit": self.suit,
            "name": self.name,
            "name_color": self.name_color,
        }

    # Дебаг
    def __repr__(self):
        return (
            f"<CharacterModel "
            f"name={self.name}, "
            f"gender={self.gender}, "
            f"face={self.face}, "
            f"hair={self.hair}, "
            f"suit={self.suit}>"
        )