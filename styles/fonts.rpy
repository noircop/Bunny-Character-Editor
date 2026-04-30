init python:
    FONT_BASE = "modules/bunny_character_editor/assets/ui/fonts/"

    def font(family, path):
        return FONT_BASE + family + "/" + path


    BCE_FONT_BODY_REGULAR = font("Manrope", "Manrope-Regular.ttf")
    BCE_FONT_BODY_MEDIUM = font("Manrope", "Manrope-Medium.ttf")
    BCE_FONT_BODY_SEMIBOLD = font("Manrope", "Manrope-SemiBold.ttf")

    BCE_FONT_HEADER_SEMIBOLD = font("NunitoSans", "NunitoSans-SemiBold.ttf")