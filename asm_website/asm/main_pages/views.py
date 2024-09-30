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

