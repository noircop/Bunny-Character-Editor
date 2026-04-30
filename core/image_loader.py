import os


class ImageLoader:
    def __init__(self, base_path):
        self.base_path = base_path
        self.cache = {}

    # 1. Получение Списка Изображеий
    def get_items(self, category, gender=None):
        if not category:
            return []

        return self._load_category(category, gender)

    # 2. Загрузка по категории
    def _load_category(self, category, gender=None):

        # filesystem path (для os)
        if gender:
            fs_path = os.path.join(self.base_path, category, gender)
        else:
            fs_path = os.path.join(self.base_path, category)

        fs_path = os.path.normpath(fs_path)

        # cache key (ВАЖНО: учитываем gender)
        cache_key = (fs_path, gender)

        if cache_key in self.cache:
            return self.cache[cache_key]

        items = []

        if not os.path.exists(fs_path):
            return []

        try:
            files = os.listdir(fs_path)
        except Exception:
            return []

        # base path для Ren'Py (ВСЕГДА с /)
        renpy_base = self.base_path.replace("\\", "/")

        if gender:
            category_base = f"{renpy_base}/{category}/{gender}"
        else:
            category_base = f"{renpy_base}/{category}"

        for filename in files:

            if not self._is_image(filename):
                continue

            item_id = os.path.splitext(filename)[0]
            full_path = f"{category_base}/{filename}"

            items.append({
                "id": item_id,
                "category": category,
                "gender": gender,
                "file": filename,
                "path": full_path
            })

        # сохраняем в кэш
        self.cache[cache_key] = items
        return items

    # Хэлперы
    def _is_image(self, filename):
        return filename.lower().endswith(
            (".png", ".jpg", ".jpeg", ".webp")
        )

    def clear_cache(self):
        self.cache = {}