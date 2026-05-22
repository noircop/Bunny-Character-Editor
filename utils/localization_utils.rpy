init python:
    bce_current_language = "ru"

    bce_translations = {
        "ru": {},
        "en": {}
    }


    # Название Шагов в Редакторе(flow_list)
    bce_translations["ru"].update({
        "step_face": "Лицо",
        "step_hair": "Прическа",
        "step_suit": "Одежда",
        "step_final": "Завершение"
    })

    bce_translations["en"].update({
        "step_face": "Face",
        "step_hair": "Hair",
        "step_suit": "Clothes",
        "step_final": "Finish"
    })  



    # Настройки Выбора Пола
    bce_translations["ru"].update({
        "male": "Мужской",
        "female": "Женский",
        "choose_gender": "Выберите Пол"
    })

    bce_translations["en"].update({
        "male": "Male",
        "female": "Female",
        "choose_gender": "Choose Gender"
    })



    # Настройки Имени Персонажа
    bce_translations["ru"].update({
        "name_placeholder": "Введите имя",
        "name_color": "Выберите цвет"
    })

    bce_translations["en"].update({
        "name_placeholder": "Enter Name",
        "name_color": "Choose color"
    })



    # Модальное окно - Подтвержение Сохранения
    bce_translations["ru"].update({
        "confirm_save": "Сохранить изменения?",
        "confirm_yes": "да",
        "confirm_no": "нет"
    })

    bce_translations["en"].update({
        "confirm_save": "Save changes?",
        "confirm_yes": "yes",
        "confirm_no": "no"
    })



    # Технические Шоколадки - Неизвестные Ошибки
    bce_translations["ru"].update({
        "error_unknown_title": "А у нас технические шоколадки ;)",
        "error_unknown_text": "Произошли технические шоколадки, мы над этим работаем. :("
    })

    bce_translations["en"].update({
        "error_unknown_title": "Sorry, we have technical hiccups ;)",
        "error_unknown_text": "Some technical hiccups occurred, we are working on it. :("
    })

    # Ошибки
    bce_translations["ru"].update({
        # Face
        "error_face_missing_title": "Ошибка - Лицо",
        "error_face_missing_text": "Вы не выбрали лицо",

        # Hair
        "error_hair_missing_title": "Ошибка - Волосы",
        "error_hair_missing_text": "Вы не выбрали прическу",

        # Suit
        "error_suit_missing_title": "Ошибка - Одежда",
        "error_suit_missing_text": "Вы не выбрали одежду",

        # Name empty
        "error_name_empty_title": "Ошибка - Пустое имя",
        "error_name_empty_text": "Имя не может быть пустым",

        # Name too short
        "error_name_too_short_title": "Ошибка - Короткое имя",
        "error_name_too_short_text": "Имя слишком короткое",

        # Name banned
        "error_name_banned_title": "Ошибка — Имя отклонено",
        "error_name_banned_text": "Мы уже видели достаточно подобных имен"
    })

    bce_translations["en"].update({
        # Face
        "error_face_missing_title": "Error - Face",
        "error_face_missing_text": "You did not select a face",

        # Hair
        "error_hair_missing_title": "Error - Hair",
        "error_hair_missing_text": "You did not select a hairstyle",

        # Suit
        "error_suit_missing_title": "Error - Outfit",
        "error_suit_missing_text": "You did not select an outfit",

        # Name empty
        "error_name_empty_title": "Error - Empty name",
        "error_name_empty_text": "Name cannot be empty",

        # Name too short
        "error_name_too_short_title": "Error - Short name",
        "error_name_too_short_text": "Name is too short",

        # Name banned
        "error_name_banned_title": "Error - Name rejected",
        "error_name_banned_text": "We've seen enough of this type of input" 
    })

    # 1. Логика
    def bce_get_language() -> str:
        return bce_current_language

    def bce_set_language(lang_code):
        global bce_current_language

        if lang_code in bce_translations:
            bce_current_language = lang_code
            renpy.restart_interaction()
        else:
            renpy.log(f"[BCE] Язык {lang_code} не найден")

    # DEL Потом можно удалить нафиг при расширении, но это уже когда toggle не нужен
    def bce_switch_language():
        current_lang = bce_get_language()
        next_lang = "en" if current_lang == "ru" else "ru"
        bce_set_language(next_lang)
    
    # Переключение статуса кнопки - сделана универсальной но пока будет тут
    def bce_switch_toggle(active: str, inactive: str) -> str:
        current_lang = bce_get_language()
        if current_lang == "ru":
            img_name = active
        else:
            img_name = inactive
        return BCE_UI_COMPONENTS + img_name

    # 2. Перевод
    def bce_t(key: str) -> str:
        return bce_translations.get(bce_current_language, {}).get(key, key)

    def bce_t_img(img_name: str) -> str:
        return f"{bce_current_language}/{img_name}"