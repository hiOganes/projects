from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'main_pages/home.html'

class AboutPage(TemplateView):
    template_name = 'main_pages/about.html'

class PortfolioPage(TemplateView):
    template_name = 'main_pages/portfolio.html'

class ContactsPage(TemplateView):
    template_name = 'main_pages/contacts.html'

class LogosCorpPage(TemplateView):
    template_name = 'main_pages/logos_corp.html'

class StickersPage(TemplateView):
    template_name = 'main_pages/stickers.html'

class IllustrationsPage(TemplateView):
    template_name = 'main_pages/illustrations.html'

class CardsPage(TemplateView):
    template_name = 'main_pages/cards.html'

class AnimationPage(TemplateView):
    template_name = 'main_pages/animation.html'