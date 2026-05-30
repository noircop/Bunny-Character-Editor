# Кнопка Сохранения
screen bce_confirm_button():
    imagebutton:
        style "bce_save_button"
        idle Transform(BCE_UI_COMPONENTS + bce_t_img("bce_save_btn.png"), size=(160, 80))
        hover Transform(BCE_UI_COMPONENTS + bce_t_img("bce_save_btn_active.png"), size=(160, 80))
        action Show("bce_confirm_window")

# Кнопка Переключения Языка
# ARCH 0.2 добавить локализацию UI как полноценную настройку в меню самого редактора.
screen bce_language_toggle_button():

    $ toggle_img = bce_switch_toggle("bce_toggle_button.png", "bce_toggle_button_active.png")

    frame:
        yalign 0.5
        xalign 0.7
        background Solid("#fccdd8")

        hbox:
            spacing 10
            text "Ru" style "bce_button_text"

            imagebutton:
                xsize 80
                ysize 40

                idle Transform(toggle_img, fit="contain")
                hover Transform(toggle_img, fit="contain")
                
                action Function(bce_switch_language)

            text "Eng" style "bce_button_text"