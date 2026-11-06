def search_by_category(items, category):
    if not category:
        return []
    return [dvd for dvd in items if dvd.category and category.lower() in dvd.category.lower()]

def search_by_title(items, keyword):
    return [item for item in items if keyword.lower() in item.title.lower()]