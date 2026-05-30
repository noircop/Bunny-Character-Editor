init python early:
    import os
    
    from modules.bunny_character_editor import FlowController
    from modules.bunny_character_editor import CharacterModel
    from modules.bunny_character_editor import CharacterService
    from modules.bunny_character_editor import CharacterValidator
    from modules.bunny_character_editor import ImageLoader
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

    store.flow_controller = FlowController(steps_list)
    store.character_model = CharacterModel()
    store.character_validator = CharacterValidator(store.character_model)

    store.character_service = CharacterService(store.character_model)

    # Хардкод, костыль на рефакторинге надо будет убирать. ВРЕМЕНИ НЕТ!
    store.image_loader = ImageLoader(
        os.path.join(renpy.config.gamedir, "modules/bunny_character_editor/assets/character/")
    )

    # TODO сделать единый контекст для подключений в следующих обновлениях
    store.editor = EditorFacade(
        store.character_model,
        store.character_service,
        store.character_validator,
        store.flow_controller,
        store.image_loader
    )
