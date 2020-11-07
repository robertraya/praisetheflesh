from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Menu, SubMenu

# Create your views here.

# class MainPageView(generic.ListView):
#     template_name = 'main_page.html'
#     context_object_name = 'menu_items'

#     def get_queryset(self):
#         """Return the last five published menu items."""
#         return Menu.objects.order_by('-pub_date')[:5]

def MainPage(request):
    return render(request, "main_page.html")

def About(request):
    return render(request, "about.html")   


# class AboutPageView(generic.ListView):
#     template_name = 'about.html'
#     contenxt_object_name = 'menu_items'

