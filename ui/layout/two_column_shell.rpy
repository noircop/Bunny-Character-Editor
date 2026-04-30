screen bce_two_column_shell(title, left_screen, right_screen, left_width=0.3):

    # left_screen/right_screen должны быть строками с именами screen

    hbox:
        xfill True
        yfill True

        # Левая колонка
        frame:
            xsize int(config.screen_width * left_width)
            style "bce_left_column"

            vbox:
                style "bce_shell_header"

                null style "bce_shell_spacer"

                text title style "bce_shell_title"
                

                use expression left_screen

        # Правая колонка
        frame:
            style "bce_right_column"

            use expression right_screen