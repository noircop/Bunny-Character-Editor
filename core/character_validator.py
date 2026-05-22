import re
from renpy.store import store

class CharacterValidator:

    BLACKLIST_WORDS = {
        "fuck", "shit", "bitch", "ass", "dick", "pussy",

        "хуй", "пизд", "еб", "хуе", "бля", "залуп",

        "пидор", "пидр", "пидар", "уеб", "мудак", "ебан",

        "пиздюк", "хуес", "ебуч", "залупа"
    } 

    def __init__(self, model):
        self.model = model
        self.errors = []

    def validate(self):
        self.errors = []

        self._validate_appearance()
        self._validate_name()

        return len(self.errors) == 0

    # -------------------------
    # Правила                  Таковы Правила! Тудудум Тудудум Тудум Тудум Тудум(это типа Hello Zepp)
    # -------------------------

    def _validate_appearance(self):

        if not self.model.face:
            self.errors.append({
                "field": "face",
                "type": "step",
                "step": "face",
                "title": "error_face_missing_title",
                "message": "error_face_missing_text"
            })

        if not self.model.hair:
            self.errors.append({
                "field": "hair",
                "type": "step",
                "step": "hair",
                "title": "error_hair_missing_title",
                "message": "error_hair_missing_text"
            })

        if not self.model.suit:
            self.errors.append({
                "field": "suit",
                "type": "step",
                "step": "suit",
                "title": "error_suit_missing_title",
                "message": "error_suit_missing_text"
            })

    def _validate_name(self):

        name_raw = (self.model.name or "").strip()

        if not name_raw:
            self.errors.append({
                "field": "name",
                "type": "popup",
                "step": "final",
                "title": "error_name_empty_title",
                "message": "error_name_empty_text"
            })
            return

        name = name_raw

        if self._is_blacklisted_name(name):
            self.errors.append({
                "field": "name",
                "type": "popup",
                "step": "final",
                "title": "error_name_banned_title",
                "message": "error_name_banned_text"
            })
            return

        if len(name_raw) < 3:
            self.errors.append({
                "field": "name",
                "type": "popup",
                "step": "final",
                "title": "error_name_too_short_title",
                "message": "error_name_too_short_text"
            })
    
    def _is_blacklisted_name(self, name: str) -> bool:
        name = name.lower()

        normalized = re.sub(r"[^a-zа-я0-9]", "", name)

        for word in self.BLACKLIST_WORDS:
            if word in normalized:
                return True

        compact = re.sub(r"\s+", "", name)
        if re.search(r"(х+у+й+|п+и+з+д+|е+б+а+т+|б+л+я+)", compact):
            return True

        return False
    
    # TODO Костыль - При внедрении Фасада Перетащить Туда. 
    def get_first_error(self):

        if not self.errors:
            return None

        error = self.errors[0]

        return {
            "title": error.get("title", "Ошибка"),
            "message": error.get("message", "Неизвестная ошибка"),
            "step": error.get("step")
        }