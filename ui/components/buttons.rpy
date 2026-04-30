# Кнопка Сохранения
screen bce_confirm_button():
    imagebutton:
        style "bce_save_button"
        idle Transform(BCE_UI_COMPONENTS + "bce_save_btn.png", size=(160, 80))
        hover Transform(BCE_UI_COMPONENTS + "bce_save_btn_active.png", size=(160, 80))
        action Show("bce_confirm_window")
