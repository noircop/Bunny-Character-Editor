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



    # Модальное окно - Технические Шоколадки
    bce_translations["ru"].update({
        "tech_error_title": "А у нас технические шоколадки ;)",
        "tech_error_text": "Произошли технические шоколадки, мы над этим работаем. :("
    })

    bce_translations["en"].update({
        "tech_error_title": "Sorry, we have technical hiccups ;)",
        "tech_error_text": "Some technical hiccups occurred, we are working on it. :("
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