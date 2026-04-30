init python early:
    import os
    
    from modules.bunny_character_editor import FlowController
    from modules.bunny_character_editor import CharacterModel
    from modules.bunny_character_editor import CharacterService
    from modules.bunny_character_editor import ImageLoader

    steps_list = [
        {
            "id": "face",
            "screen": "bce_element_grid",
            "type": "customization",
            "layer": "face",
            "title": "Лицо",
        },
        {
            "id": "hair",
            "screen": "bce_element_grid",
            "type": "customization",
            "layer": "hair",
            "title": "Прическа",
        },
        {
            "id": "suit",
            "screen": "bce_element_grid",
            "type": "customization",
            "layer": "suit",
            "title": "Одежда",
        },
        {
            "id": "final",
            "screen": "bce_character_name",
            "type": "final",
            "title": "Завершение",
        }
    ]

    store.flow_controller = FlowController(steps_list)
    store.character_model = CharacterModel()
    store.character_service = CharacterService(store.character_model)

    # Хардкод, костыль на рефакторинге надо будет убирать. ВРЕМЕНИ НЕТ!
    store.image_loader = ImageLoader(
        os.path.join(renpy.config.gamedir, "modules/bunny_character_editor/assets/character/")
    )