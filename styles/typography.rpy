# =========================== 
# Типография
# =========================== 

# H1 — заголовок
style bce_h1:
    font BCE_FONT_BODY_SEMIBOLD
    size 32
    bold False

# H2 — подзаголовок
style bce_h2:
    font BCE_FONT_BODY_MEDIUM
    size 28

# P — основной текст
style bce_p:
    font BCE_FONT_BODY_REGULAR
    size 16

# caption — вспомогательный
style bce_caption:
    font BCE_FONT_BODY_REGULAR
    size 13
    color BCE_TEXT_MUTED

# button_text — текст кнопок / акцент
style bce_button_text:
    font BCE_FONT_BODY_SEMIBOLD
    size 24

# =========================== 
# Стили Текста
# =========================== 

style bce_header_title:
    # Цвет надо вынести
    color BCE_TEXT_LIGHT
    font BCE_FONT_HEADER_SEMIBOLD
    size 38
    xalign 0.3 
    yalign 0.5

style bce_shell_title is bce_h2:
    xalign 0.5
    color BCE_TEXT

style bce_input_title is bce_button_text:
    color BCE_TEXT

style bce_gender_choice_title is bce_h1:
    color BCE_TEXT_MUTED
    xalign 0.5

style bce_choice_menu_button_text:
    xalign 0.5
    yalign 0.5

    color BCE_TEXT
    hover_color BCE_TEXT_LIGHT 

style bce_error_title is bce_h1:
    xalign 0.5
    textalign 0.5

    color BCE_TEXT_MUTED

style bce_error_text is bce_button_text:
    xalign 0.5
    textalign 0.5
    
    color BCE_TEXT

style bce_confirm_button_text is bce_button_text:
    xalign 0.5 
    yalign 0.5

    color BCE_TEXT
    hover_color BCE_HOVER



