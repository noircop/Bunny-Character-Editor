# Bunny Character Editor

Редактор персонажа для визуальных новелл на Ren'Py.
Позволяет игроку создать кастомного персонажа с выбором пола, внешности и имени, а затем использовать его в игре.

## 🚀 Быстрый Старт

1. Скопируйте папку modules/ в проект Ren'Py
2. Добавьте label open_character_editor
3. Объявите:

default bce_custom_character = {}

4. Вызовите:

call open_character_editor

5. Используйте:

store.bce_custom_character

## Возможности

* Выбор пола (мужской / женский)
* Настройка:
  * Лица
  * Прически
  * Одежды
* Ввод имени персонажа
* Выбор цвета имени
* Предпросмотр персонажа в реальном времени
* Пошаговая навигация (wizard flow)

## Структура

modules/bunny_character_editor/

├── assets/         # Спрайты элементов внешнего вида 
│   ├── character/
│   └── ui/
│
├── core/           # Ядро Редактора
│   ├── character_model.py
│   ├── character_service.py
│   ├── character_validator.py
│   ├── editor_context.py
│   ├── editor_facade.py
│   ├── flow_controller.py
│   └── image_loader.py
│
├── ui/             # Screens - UI
│   ├── components/
│   ├── layout/
│   └── modal/
│
├── styles/         # Стили UI
│
├── utils/          # Вспомогательные Утилиты
│   ├── localization_utils.rpy # Будущий класс лол
│   ├── render_utils.rpy       # Тоже будущий класс лол
│   └── save_utils.rpy         # А это похоже на React-handler web-лол
│
├── bootstrap.rpy
├── config.rpy
└── __init__.py

### 1. Установка

Из скаченной ВН Скопировать папку /modules и вставить в свою новеллу.

### 2. Инициализация

Редактор уже инициализируется в `bootstrap.rpy`:

```python
    store.editor_context = EditorContext(
        steps_list,
        assets_path
    )

    store.editor = EditorFacade(
        store.editor_context
    )
```

---

### 3. Запуск редактора

```renpy

Вставить в файл script.rpy

label open_character_editor:

    window hide
    $ quick_menu = False
    
    call screen bce_editor_main_screen

    $ quick_menu = True
    window show

    return

вызывать в главном label (обычно label start: ) новеллы
call open_character_editor() from _call_open_character_editor

```

---

### 4. Получение результата

После вызова редактора вставить в скрипт новеллы:

```renpy
if store.bce_custom_character:
    char = store.bce_custom_character
```

Структура данных:

```python
{
    "gender": "male",
    "face": "face_1",
    "hair": "hair_2",
    "suit": "suit_3",
    "name": "Alex",
    "name_color": "#FFFFFF"
}
```

---

### 5. Отображение персонажа

```renpy
# Получения данных
$ char = store.bce_custom_character

# Внешний вид
$ char_img = get_character_image(char)
show expression char_img

# Имя персонажа
$ player = Character(char["name"], color=char["name_color"])
player "Я говорю что-то"


```

## Архитектура

                    UI (Screens)
                        │
                        ▼
                 EditorFacade
                        │
         ┌──────────────┼──────────────┐
         │              │              │
         ▼              ▼              ▼
 CharacterService  FlowController  ImageLoader
         │
         ▼
 CharacterModel
         │
         ▼
 CharacterValidator

## 🎨 Добавление новых элементов

### Структура папок:

```
assets/character/
├── face/
│   ├── male/
│   └── female/
├── hair/
│   ├── male/
│   └── female/
├── suit/
│   ├── male/
│   └── female/
└── base/
```

---

### Требования:

* Формат: `.png`
* Имя файла = `bce_` категория элемента `_id`
* Разрешения: 1200 × 1800 px
* Пример:

  ```
  face/male/bce_face_01.png
  ```
Note: все ассеты подгонять по основам из assets/character/base
---

## ➕ Добавление нового шага

В `bootstrap.rpy`:

```python
steps_list = [
    {
        "id": "accessories",
        "screen": "bce_element_grid",
        "type": "customization",
        "layer": "accessories",
        "title": "Аксессуары",
    }
]
```

И добавить обработку в:

```python
apply_character_change()
CharacterModel
CharacterService
get_character_layers()
```

---

## 💾 Сохранение

Кнопка "Сохранить" вызывает:

```python
editor.apply_to_game()
```

Что делает:

* проверяет заполненность
* сохраняет в `store.bce_custom_character`
* сбрасывает модель

---
## Roadmap

## v0.2

- [ ] Система сохранения и экспорта персонажей
- [ ] Редактирование готового персонажа
- [ ] Рефакторинг архитектуры
- [ ] Система управления ассетами (часть движка)
- [ ] Устранение бутылочного горлышка при работе с ассетами
- [ ] Выделение логики сборки персонажа
- [ ] Масштабируемая система локализации

---

## Пример использования в игре

```renpy
label start:

    call open_charecter_editor

    if store.bce_custom_character:
        $ char = store.bce_custom_character
        $ char_img = get_character_image(char)

        $ player = Character(char["name"], color=char["name_color"])

        show expression char_img

        player "Я  живой !"

    return
```

---

## 🧾 Лицензия

Используйте свободно в своих проектах.
Редактируйте, ломайте, улучшайте

---

## ✍️ Автор

Nomad Renard

---

