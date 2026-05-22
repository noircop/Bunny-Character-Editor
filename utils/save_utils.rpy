init python:

    def confirm_save():
        success = store.character_service.apply_to_game()

        if success:
            store.flow_controller.finish()
            renpy.hide_screen("bce_confirm_window")

        else:
            renpy.hide_screen("bce_confirm_window")
            
            current_error = store.character_validator.get_first_error()
            get_to_error_step(current_error)

            renpy.show_screen("bce_error_window", title_key=current_error["title"], text_key=current_error["message"])
    
    def get_to_error_step(error):
        step_id = error.get("step")
        index = get_step_index(store.flow_controller.steps_list, step_id)

        if index is not None:
            store.flow_controller.go_to(index)
        
        return None
    
    def get_step_index(steps_list, step_id):
        for i, step in enumerate(steps_list):
            if step["id"] == step_id:
                return i
        return None
