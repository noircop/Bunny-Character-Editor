init python:

    # ARCH 0.2 Пока не появится Сохранение Персонажи в виде JSON, или готовых спрайтов. Не трогать Воообще.

    def get_character_image(char):
        if not char:
            return "images/character/default.png"

        gender = char.get("gender")

        face = char.get("face")
        hair = char.get("hair")
        suit = char.get("suit")

        return LiveComposite(
            (1920, 1080),

            (0, 0),
            f"modules/bunny_character_editor/assets/character/base/bce_{gender}_base.png",

            (0, 0),
            f"modules/bunny_character_editor/assets/character/face/{gender}/{face}.png",

            (0, 0),
            f"modules/bunny_character_editor/assets/character/hair/{gender}/{hair}.png",

            (0, 0),
            f"modules/bunny_character_editor/assets/character/suit/{gender}/{suit}.png",
        )
    
    