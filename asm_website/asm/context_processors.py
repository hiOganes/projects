menu = [
    {'name': 'О нас', 'name_url': 'about'},
    {'name': 'Портфолио', 'name_url': 'portfolio'},
    {'name': 'Контакты', 'name_url': 'contacts'},
]

drop = [
    {'name': 'Логотипы фирменнный стиль', 'name_url': 'logos_corp'},
    {'name': 'Стикеры', 'name_url': 'stickers'},
    {'name': 'Иллюстрации и принты', 'name_url': 'illustrations'},
    {'name': 'Карточĸи WB и Ozon', 'name_url': 'cards'},
    {'name': 'Анимации', 'name_url': 'animations'},
]

def get_context_menu(self):
    return {'mainmenu': menu}

def get_context_drop(self):
    return {'maindrop': drop}