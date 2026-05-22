screen bce_error_window(title_key, text_key):

    modal True

    frame:
        style "bce_error_window"

        vbox:
            xalign 0.5 
            yalign 0.5

            text bce_t(title_key) style "bce_error_title"
            text bce_t(text_key) style "bce_error_text"

            textbutton "OK" xalign 1.0 action Hide("bce_error_window")