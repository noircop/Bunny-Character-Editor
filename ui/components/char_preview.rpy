# Окно предпросмотра персонажа
screen bce_character_preview():
    frame:
        style "bce_preview_box"
        use bce_character_sprite()

# Спрайт персонажа
screen bce_character_sprite():

    fixed:
    
        $ layers = editor.get_character_layers()

        style "bce_preview_sprite_size"

        if layers:
            for layer in layers:
                add Image(layer) at bce_preview_sprite_layer
        else:
            # Заглушка
            add Image(BCE_CHAR_PATH + "char_test.png") at bce_preview_sprite_layer

transform bce_preview_sprite_layer:
    xalign 0.5
    yalign 0.5

    zoom BCE_PREVIEW_ZOOM