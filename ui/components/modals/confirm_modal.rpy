screen bce_confirm_window():
    modal True
    
    frame:
        style "bce_confirm_window"
        padding (30, 20)


        vbox:
            spacing 20
            xalign 0.5

            xfill True
            yfill True
                        
            text "Сохранить изменения?" style "bce_error_title"

            hbox:
                spacing 20
                align (0.5, 0.5)

                textbutton "Да":
                    text_style "bce_confirm_button_text"
                    action [
                        Function(character_service.apply_to_game),
                        Function(flow_controller.reset),
                        Hide("bce_confirm_window")
                    ]

                textbutton "Нет":
                    text_style  "bce_confirm_button_text"
                    action Hide("bce_confirm_window")