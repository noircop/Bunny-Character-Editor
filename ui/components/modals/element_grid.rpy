# Сетка Элементов
screen bce_element_grid(cols=3, spacing=26):
    style_prefix "bce"

    $ step = flow_controller.current
    $ items = image_loader.get_items(step.get("layer"), character_model.gender)

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
        #             $ selected = is_selected_item(item)
                        
        #             use bce_grid_item(item, selected)


        vbox:
            if not items:

                text "Ты думал здесь что-то будет ?" style "bce_p"

            else:
                vpgrid:
                    cols cols
                    spacing spacing

                    for item in items:
                        $ selected = is_selected_item(item)
                        
                        use bce_grid_item(item, selected)


# Элемент
screen bce_grid_item(item, selected=False):

    $ step = flow_controller.current
    $ gender = character_model.gender
    $ img = item["path"]

    $ is_suit = step.get("layer") == "suit"
    $ is_face_or_hair = step.get("layer") in ["face", "hair"]

    button:
        style "bce_grid_item_button"
        selected selected

        action Function(apply_character_change, item)

        if is_face_or_hair:

            if gender == "female":
                $ crop = (0, 0, 1200, 700)
            else:
                $ crop = (0, 0, 1200, 600)

            add Transform(
                Image(img),
                zoom=BCE_PREVIEW_ZOOM,
                crop=crop,
                xalign=0.5,
                yalign=0.5
            )

        elif is_suit:

            add Transform(
                img,
                fit="contain",
                xysize=(150, 150),
                xalign=0.5,
                yalign=0.5
            )