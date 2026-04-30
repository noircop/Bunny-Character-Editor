screen bce_error_window(error_title, error):
    frame:
        style "bce_error_window"
        padding (30, 20)


        vbox:
            spacing 15
            xfill True
                        
            text error_title style "bce_error_title"

            text error style "bce_error_text"
