init python early:
    import os
    
    from modules.bunny_character_editor import EditorContext
    from modules.bunny_character_editor import EditorFacade

    steps_list = [
        {
            "id": "face",
            "screen": "bce_element_grid",
            "type": "customization",
            "layer": "face",
            "title_key": "step_face",
        },
        {
            "id": "hair",
            "screen": "bce_element_grid",
            "type": "customization",
            "layer": "hair",
            "title_key": "step_hair",
        },
        {
            "id": "suit",
            "screen": "bce_element_grid",
            "type": "customization",
            "layer": "suit",
            "title_key": "step_suit",
        },
        {
            "id": "final",
            "screen": "bce_character_name",
            "type": "final",
            "title_key": "step_final",
        }
    ]

    # Хардкод путей, костыль на рефакторинге надо будет убирать.
    store.editor_context = EditorContext(
        steps_list,
        os.path.join(
            renpy.config.gamedir,
            "modules/bunny_character_editor/assets/character/"
        )
    )

    store.editor = EditorFacade(
        store.editor_context
    )