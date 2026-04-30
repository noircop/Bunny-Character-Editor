screen bce_layout():

    frame:
        style "bce_root"

        vbox:
            use bce_header()
            
            frame:
                style "bce_body"
                # TODO сделать адаптивным размер
                ysize 842
                transclude

            use bce_footer()