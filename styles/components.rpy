# =========================== 
# Окно Ошибок
# =========================== 
style bce_error_window:
    xalign 0.5 
    yalign 0.5

    xmaximum 500
    yminimum 200

    background BCE_PANEL

# =========================== 
# Окно Подтверждения
# =========================== 
style bce_confirm_window:
    xalign 0.5 
    yalign 0.5
        
    xsize 500
    yfill True

    background BCE_PANEL

# =========================== 
# Меню Выбора
# =========================== 
style bce_choice_window:
    xalign 0.5 
    yalign 0.5
        
    xsize 500
    ysize 300

    background BCE_PANEL

style bce_choice_menu:
    xalign 0.5
    yalign 0.5
    box_align 0.5

style bce_choice_menu_button:
    xsize 364
    ysize 97

    background BCE_TEXT_MUTED
    hover_background BCE_ACTIVE
    padding (10, 10)

# =========================== 
# Форма для имени персонажа
# =========================== 
style bce_character_name_background:
    xfill True
    ysize 156

    padding (10, 10)
    background BCE_PANEL

style bce_character_name_form:
    xfill True
    background None
    padding (10, 10)

# Предпросмотр имени персонажа в процессе редактирования, подумать о типографии
# Это просто отображеие введенного имени и его цвета, компонент интрефейса. Поэтому находиться здесь а не в файле с типографией 
style bce_character_name_preview:
    size 40
    bold True
    xalign 0.5
    yalign 0.5

# === INPUT ===
style bce_input_background:
    xfill True
    background BCE_PANEL
    padding (10, 8)

style bce_input:
    color BCE_TEXT
    xfill True

# Цветовая сетка
style bce_character_color_grid:
    background BCE_PANEL
    padding (10, 10)
    xfill True

# === COLOR BUTTON ===
style bce_color_button:
    xsize 100
    ysize 100

# ===========================
# Сетка элементов внешнего вида
# ===========================   
style bce_grid_item_button:
    xsize 150
    ysize 150

    # Сделать картинки
    background Frame(BCE_UI_COMPONENTS + "bce_char_element.png")
    selected_background Frame(BCE_UI_COMPONENTS + "bce_char_element_active.png")

# ===========================
# Предпросмотр Персонажа
# ===========================
style bce_preview_box:
    xalign 0.5
    yalign 0.5

style bce_preview_sprite_size:
    xsize 500
    ysize 780
    
# ===========================
# Панель навигации по шагам
# ===========================
style bce_flow_nav_container:
    xsize int(config.screen_width * 0.3)
    yfill True

style bce_flow_nav_inner:
    spacing 15
    yalign 0.5
    xalign 0.5

style bce_flow_nav_button:
    # базовый стиль кнопок навигации
    xpadding 10
    ypadding 6

# Кнопка сохранения персонажа
style bce_save_button:
    xalign 0.5
    xpadding 20
    ypadding 10