
screen bce_footer():

    frame:
        style "bce_footer"

        hbox:
            xfill True
            yfill True

            if flow_controller.started:
                use bce_flow_navigation()

            # Правая часть (оставшееся пространство)
            hbox:
                xfill True
                yfill True
                

                hbox:
                    xfill True
                    yalign 0.5

                    null width 0 xfill True

                    # Заготовка для взаимодействия с логикой
                    if flow_controller.is_last:
                        use bce_confirm_button()


