# Сетка Элементов
screen bce_element_grid(cols=3, spacing=26):
    style_prefix "bce"

    $ items = editor.get_current_assets()

    viewport:
        style "bce_element_viewport"
        scrollbars "vertical"
        mousewheel True
        draggable True

        # vbox:
        #     vpgrid:
        #         cols cols
        #         spacing spacing

        #         for item in items:
        #             use bce_grid_item(
        #                 item,
        #                 editor.is_selected_item(item)
        #             )


        vbox:
            if not items:

                text "Ты думал здесь что-то будет ?" style "bce_p"

            else:
                vpgrid:
                    cols cols
                    spacing spacing

                    for item in items:
                        use bce_grid_item(
                            item,
                            editor.is_selected_item(item)
                        )


# Элемент
screen bce_grid_item(item, selected=False):

    $ step = editor.current_step
    $ gender = editor.character_gender
    $ img = item["path"]

    $ layer = step.get("layer")

    button:
        style "bce_grid_item_button"
        selected selected

        action Function(editor.apply_character_change, item)

        # ARCH 0.2 Костыль - подумать над системой thumb-изображений   
        if layer == "face":
            $ crop = (0, 0, 1200, 700)
            $ zoom = 0.5

            add Transform(
                    Image(img),
                    zoom=zoom,
                    crop=crop,
                    xalign=0.5,
                    yalign=0.5
                )

        elif layer == "hair":

            if gender == "female":
                $ crop = (0, 0, 1200, 700)
                $ zoom = 0.27
            else:
                $ crop = (0, 0, 1200, 600)
                $ zoom = 0.3

            add Transform(
                Image(img),
                zoom=zoom,
                crop=crop,
                xalign=0.5,
                yalign=0.5
            )

        elif layer == "suit":

            add Transform(
                img,
                fit="contain",
                xysize=(150, 150),
                xalign=0.5,
                yalign=0.5
            )