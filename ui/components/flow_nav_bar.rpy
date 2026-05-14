
# Навигация по шагам редактора
screen bce_flow_navigation():
    hbox:
        style "bce_flow_nav_container"

        hbox:
            style "bce_flow_nav_inner"

            if not flow_controller.is_first:
                use bce_flow_prev_button()

            use bce_flow_dots(flow_controller.current_step, flow_controller.step_count)

            if not flow_controller.is_last:
                use bce_flow_next_button()

# Кнопка Назад Навигации
screen bce_flow_prev_button():
    imagebutton:
        style "bce_flow_nav_button"
        idle Transform(BCE_UI_COMPONENTS + bce_t_img("bce_flow_nav_prev_btn.png"), size=(100,50))
        hover Transform(BCE_UI_COMPONENTS + bce_t_img("bce_flow_nav_prev_btn_active.png"), size=(100, 50))

        action Function(flow_controller.prev)

        sensitive flow_controller.can_prev()

# Кнопка Вперед Навигации
screen bce_flow_next_button():
    imagebutton:
        style "bce_flow_nav_button"
        idle Transform(BCE_UI_COMPONENTS + bce_t_img("bce_flow_nav_next_btn.png"), size=(100, 50))
        hover Transform(BCE_UI_COMPONENTS + bce_t_img("bce_flow_nav_next_btn_active.png"), size=(100, 50))

        action Function(flow_controller.next)

        sensitive flow_controller.can_next()

#Шаги навигации
screen bce_flow_dots(current, total):

    $ dot_idle = BCE_UI_COMPONENTS + "flow_nav_dot.png"
    $ dot_active = BCE_UI_COMPONENTS + "flow_nav_dot_active.png"

    hbox:
        spacing 36
        xalign 0.5
        yalign 0.5

        for i in range(total):

            $ is_current = (i == current)

            imagebutton:
                at flow_nav_dot

                if is_current:
                    idle dot_active
                    hover dot_active
                    action NullAction()
                    sensitive False
                else:
                    idle dot_idle
                    hover dot_idle
                    action Function(flow_controller.go_to, i)
                    sensitive True

transform flow_nav_dot(size = 50):
    xsize size
    ysize size