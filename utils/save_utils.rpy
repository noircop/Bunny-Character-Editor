init python:

    def confirm_save():
        editor = store.editor

        result = editor.apply_to_game()

        renpy.hide_screen("bce_confirm_window")

        if result["status"]:

            editor.finish()

        else:

            error = result["error"]

            renpy.show_screen(
                "bce_error_window",
                title_key=error["title"],
                text_key=error["message"]
            )
