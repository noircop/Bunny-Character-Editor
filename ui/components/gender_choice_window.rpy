screen bce_gender_choice_window():

    frame:
        style "bce_choice_window"

        use bce_gender_choice_menu()

        

screen bce_gender_choice_menu():
    vbox:
        style "bce_choice_menu"

        text "Выберите Пол" style "bce_gender_choice_title"

        # Ладно хуй с вами будем потом ебаться на отображении в preview
        textbutton "Мужской":
            style "bce_choice_menu_button"
            action Function(character_service.set_gender, "male"), Function(flow_controller.start)

        textbutton "Женский":
            style "bce_choice_menu_button"
            action Function(character_service.set_gender, "female"), Function(flow_controller.start)