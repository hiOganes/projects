menu = [
    {'name': 'О нас', 'name_url': 'about'},
    {'name': 'Портфолио', 'name_url': 'portfolio'},
    {'name': 'Контакты', 'name_url': 'contacts'},
]

def get_context_menu(self):
    return {'mainmenu': menu}