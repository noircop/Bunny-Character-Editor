screen bce_character_name():
    vbox:
        xfill True
        yfill True
        spacing 15
            
        use bce_character_name_preview()

        null height 0 yfill True

        use bce_character_name_form()


screen bce_character_name_preview():

    frame:
        style "bce_character_name_background"

        vbox:
            xfill True
            yfill True

            text "[character_model.name or 'Имя Персонажа']":
                style "bce_character_name_preview"
                color character_model.name_color


# Форма
screen bce_character_name_form():

    frame:
        style "bce_character_name_form"

        vbox:
            spacing 20
            xfill True

            use bce_character_name_input()
            use bce_character_color_grid()


# Input имени
screen bce_character_name_input():

    vbox:
        spacing 10

        text "Введите имя:" style "bce_input_title"
        
        frame:
            style "bce_input_background"

            input:
                style "bce_input"
                value FieldInputValue(character_model, "name")
                length 20


# Сетка цветов
screen bce_character_color_grid():
    
    frame:
        style "bce_character_color_grid"

        vbox:
            spacing 10

            text "Выберите цвет:" style "bce_input_title"

            grid 4 2:
                spacing 10

                $ colors = [
                    "#E74C3C", "#3498DB", "#E67E22", "#9B59B6",
                    "#2ECC71", "#F1C40F", "#1E1E1E", "#FFFFFF",
                ]

                for c in colors:
                    button:
                        style "bce_color_button"
                        background Solid(c)

                        if character_model.name_color == c:
                            add Solid("#00000020")

                        if "#FFFFFF" == c:
                            add Solid("#FFFFFF40")

                        action Function(character_service.set_name_color, c)