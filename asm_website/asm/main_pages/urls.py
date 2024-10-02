from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('portfolio/', views.PortfolioPage.as_view(), name='portfolio'),
    path('contacts/', views.ContactsPage.as_view(), name='contacts'),
    path('logos_corp/', views.LogosCorpPage.as_view(), name='logos_corp'),
    path('stickers/', views.StickersPage.as_view(), name='stickers'),
    path(
        'illustrations/', 
        views.IllustrationsPage.as_view(), 
        name='illustrations'
        ),
    path('cards/', views.CardsPage.as_view(), name='cards'),
    path('animations/', views.AnimationPage.as_view(), name='animations'),
]