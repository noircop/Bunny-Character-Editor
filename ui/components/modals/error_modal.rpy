screen bce_error_window(title_key, text_key):
    frame:
        style "bce_error_window"
        padding (30, 20)

        vbox:
            spacing 15
            xfill True

            text bce_t(title_key) style "bce_error_title"

            text bce_t(text_key) style "bce_error_text"