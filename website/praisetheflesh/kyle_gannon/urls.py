from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MainPage, name='main_page'),
    path('kyle_gannon/', views.About, name='about'),
    #path(''. views.AboutPageview.as_view(), name='about'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)