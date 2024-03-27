from django.urls import path, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from home import views
from django.views.static import serve
# English URLs
urlpatterns = [
    path('robots.txt', views.robot, name='robot'),
    path('sitemap.xml', views.sitemap, name='sitemap'),


    
    path('', views.index, name='home'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('ask-question/', views.ask, name='ask'),
    path('search/', views.search, name='search'),
    path('<str:slug>/', views.redirect_without_slash, name='redirect_without_slash'),
    path('<str:slug>', views.open, name='open'),
    path('submit/add_comment/', views.add_comment, name='add_comment'), # English dynamic slug
]
# Hindi URLs
urlpatterns += [
    path('hi/home/', views.hi_index, name='hi_home'),
    path('hi/about-us/', views.hi_about, name='hi_about'),
    path('hi/contact-us/', views.hi_contact, name='hi_contact'),
    path('hi/privacy-policy/', views.hi_privacy, name='hi_privacy'),
    path('hi/ask-question/', views.hi_ask, name='hi_ask'),
    path('hi/search/', views.hi_search, name='hi_search'),
    path('hi/<str:slug>/', views.hi_redirect_without_slash, name='hi_redirect_without_slash'),
    path('hi/<str:slug>', views.hi_open, name='hi_open_no_slash'),
    path('hi/submit/add_comment/', views.hi_add_comment, name='hi_add_comment'), # Hindi dynamic slug
]
# Spanish URLs
urlpatterns += [
    path('es/home/', views.es_index, name='es_home'),
    path('es/about-us/', views.es_about, name='es_about'),
    path('es/contact-us/', views.es_contact, name='es_contact'),
    path('es/privacy-policy/', views.es_privacy, name='es_privacy'),
    path('es/ask-question/', views.es_ask, name='es_ask'),
    path('es/search/', views.es_search, name='es_search'),
    path('es/<str:slug>/', views.es_redirect_without_slash, name='es_redirect_without_slash'),
    path('es/<str:slug>', views.es_open, name='es_open_no_slash'),
    path('es/submit/add_comment/', views.es_add_comment, name='es_add_comment'), 
]
# Chinese URLs
urlpatterns += [
    path('zh/home/', views.zh_index, name='zh_home'),
    path('zh/about-us/', views.zh_about, name='zh_about'),
    path('zh/contact-us/', views.zh_contact, name='zh_contact'),
    path('zh/privacy-policy/', views.zh_privacy, name='zh_privacy'),
    path('zh/ask-question/', views.zh_ask, name='zh_ask'),
    path('zh/search/', views.zh_search, name='zh_search'),
    path('zh/<str:slug>/', views.zh_redirect_without_slash, name='zh_redirect_without_slash'),
    path('zh/<str:slug>', views.zh_open, name='zh_open_no_slash'),
    path('zh/submit/add_comment/', views.zh_add_comment, name='zh_add_comment'), 
]
# Arabic URLs
urlpatterns += [
    path('ar/home/', views.ar_index, name='ar_home'),
    path('ar/about-us/', views.ar_about, name='ar_about'),
    path('ar/contact-us/', views.ar_contact, name='ar_contact'),
    path('ar/privacy-policy/', views.ar_privacy, name='ar_privacy'),
    path('ar/ask-question/', views.ar_ask, name='ar_ask'),
    path('ar/search/', views.ar_search, name='ar_search'),
    path('ar/<str:slug>/', views.ar_redirect_without_slash, name='ar_redirect_without_slash'),
    path('ar/<str:slug>', views.ar_open, name='ar_open_no_slash'),
    path('ar/submit/add_comment/', views.ar_add_comment, name='ar_add_comment'), 
]
# French URLs
urlpatterns += [
    path('fr/home/', views.fr_index, name='fr_home'),
    path('fr/about-us/', views.fr_about, name='fr_about'),
    path('fr/contact-us/', views.fr_contact, name='fr_contact'),
    path('fr/privacy-policy/', views.fr_privacy, name='fr_privacy'),
    path('fr/ask-question/', views.fr_ask, name='fr_ask'),
    path('fr/search/', views.fr_search, name='fr_search'),
    path('fr/<str:slug>/', views.fr_redirect_without_slash, name='fr_redirect_without_slash'),
    path('fr/<str:slug>', views.fr_open, name='fr_open_no_slash'),
    path('fr/submit/add_comment/', views.fr_add_comment, name='fr_add_comment'), 
]
# Portuguese URLs
urlpatterns += [
    path('pt/home/', views.pt_index, name='pt_home'),
    path('pt/about-us/', views.pt_about, name='pt_about'),
    path('pt/contact-us/', views.pt_contact, name='pt_contact'),
    path('pt/privacy-policy/', views.pt_privacy, name='pt_privacy'),
    path('pt/ask-question/', views.pt_ask, name='pt_ask'),
    path('pt/search/', views.pt_search, name='pt_search'),
    path('pt/<str:slug>/', views.pt_redirect_without_slash, name='pt_redirect_without_slash'),
    path('pt/<str:slug>', views.pt_open, name='pt_open_no_slash'),
    path('pt/submit/add_comment/', views.pt_add_comment, name='pt_add_comment'), 
]
# Russian URLs
urlpatterns += [
    path('ru/home/', views.ru_index, name='ru_home'),
    path('ru/about-us/', views.ru_about, name='ru_about'),
    path('ru/contact-us/', views.ru_contact, name='ru_contact'),
    path('ru/privacy-policy/', views.ru_privacy, name='ru_privacy'),
    path('ru/ask-question/', views.ru_ask, name='ru_ask'),
    path('ru/search/', views.ru_search, name='ru_search'),
    path('ru/<str:slug>/', views.ru_redirect_without_slash, name='ru_redirect_without_slash'),
    path('ru/<str:slug>', views.ru_open, name='ru_open_no_slash'),
    path('ru/submit/add_comment/', views.ru_add_comment, name='ru_add_comment'), 
]
# German URLs
urlpatterns += [
    path('de/home/', views.de_index, name='de_home'),
    path('de/about-us/', views.de_about, name='de_about'),
    path('de/contact-us/', views.de_contact, name='de_contact'),
    path('de/privacy-policy/', views.de_privacy, name='de_privacy'),
    path('de/ask-question/', views.de_ask, name='de_ask'),
    path('de/search/', views.de_search, name='de_search'),
    path('de/<str:slug>/', views.de_redirect_without_slash, name='de_redirect_without_slash'),
    path('de/<str:slug>', views.de_open, name='de_open_no_slash'),
    path('de/submit/add_comment/', views.de_add_comment, name='de_add_comment'), 
]
# Japanese URLs
urlpatterns += [
    path('ja/home/', views.ja_index, name='ja_home'),
    path('ja/about-us/', views.ja_about, name='ja_about'),
    path('ja/contact-us/', views.ja_contact, name='ja_contact'),
    path('ja/privacy-policy/', views.ja_privacy, name='ja_privacy'),
    path('ja/ask-question/', views.ja_ask, name='ja_ask'),
    path('ja/search/', views.ja_search, name='ja_search'),
    path('ja/<str:slug>/', views.ja_redirect_without_slash, name='ja_redirect_without_slash'),
    path('ja/<str:slug>', views.ja_open, name='ja_open_no_slash'),
    path('ja/submit/add_comment/', views.ja_add_comment, name='ja_add_comment'), 
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
