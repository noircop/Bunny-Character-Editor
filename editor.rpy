screen bce_editor_main_screen():
    tag menu

    # Фон всего редактора
    add Solid(BCE_BG) 

    use bce_layout():

        if not editor.started:
            use bce_gender_choice_window()

        else:
            $ step = editor.current_step

            $ translation = bce_t(step.get("title_key", ""))

            use bce_two_column_shell(
                title=translation,
                left_screen=step["screen"],
                right_screen="bce_character_preview"
            )
        
        if editor.finished:
            timer 0.01 action Return()