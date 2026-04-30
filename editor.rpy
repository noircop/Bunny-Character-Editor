screen bce_editor_main_screen():
    tag menu

    # Фон всего редактора
    add Solid(BCE_BG) 

    use bce_layout():

        if not flow_controller.started:
            use bce_gender_choice_window()

        else:
            $ step = flow_controller.current

            use bce_two_column_shell(
                title=step.get("title", ""),
                left_screen=step["screen"],
                right_screen="bce_character_preview"
            )