# Bunny Character Editor

Редактор персонажа для визуальных новелл на Ren'Py.
Позволяет игроку создать кастомного персонажа с выбором пола, внешности и имени, а затем использовать его в игре.

## 🚀 Быстрый Старт

1. В директории проекта на Renpy создайте папку modules/.
2. В modules/создайте папку bunny_character_editor/ и скопируйте туда исходники
3. Добавьте в script.rpy код из "2. Запуск Редактора"(Пункт Ниже)
4. Вызовите call open_character_editor
5. После вызова редактора  перед label start: объявите заранее:
        ```renpy
        default bce_custom_character = {} 
        ```
    и  вставьте в скрипт новеллы условие из "Примера использования" это важно.
6. Получите результат:
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
│
├── core/                  # Логика редактора
│   ├── character_model.py
│   ├── character_service.py
│   ├── flow_controller.py
│   └── image_loader.py
│
├── assets/                # Ресурсы
│   ├── character/         # Спрайты персонажа
│   └── ui/                # UI элементы
│
├── ui/                     # UI в виде Screens
│    ├── components/        # Компоненты UI 
│    └── layout/            # Layout UI - header,footer,layout и оболочка для колонок
│ 
├── styles/                # Стили
└── utils/                 # Утилиты

### 1. Установка

Из скаченной ВН Скопировать папку /modules и вставить в свою новеллу.

### 2. Инициализация

Редактор уже инициализируется в `bootstrap.rpy`:

```python
store.flow_controller = FlowController(steps_list)
store.character_model = CharacterModel()
store.character_service = CharacterService(store.character_model)
store.image_loader = ImageLoader(...)
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

### 🔹 CharacterModel

Хранит состояние персонажа:

* Пол
* Лицо
* Прическа
* Одежда
* Имя
* Цвет имени


### 🔹 CharacterService

Слой между UI и моделью:

* изменяет данные
* валидирует(пока это только в планах)
* экспортирует результат

---

### 🔹 FlowController

Управляет шагами редактора:

* текущий шаг
* навигация (next / prev)
* состояние (start / reset)

---

### 🔹 ImageLoader

Загружает изображения из файловой системы:

* поддержка категорий
* фильтрация по полу
* кеширование

---

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
character_service.apply_to_game()
```

Что делает:

* проверяет заполненность
* сохраняет в `store.bce_custom_character`
* сбрасывает модель

---

## Известные проблемы

* "Костыли" в коде (помечены комментариями)
* Жестко заданные пути в нескольких местах
* Нет полноценной валидации UI
* Нет системы слоев с приоритетами (hair поверх suit и т.д. — вручную)
* Нет проверки на битые ассеты
* Функции утилиты как Адаптеры UI
* Если не выбрать все элементы внешности и не задать имя - персонаж не отобразится. (Там срабатывает тихий Fallback при сохранении)

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

