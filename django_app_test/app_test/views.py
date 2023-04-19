from django.shortcuts import render
from .models import MenuItem

def menu(request):
    menu = MenuItem.objects.all()
    return render(request, ('app_test/index.html'), {'title': 'Меню', 'menu': menu})