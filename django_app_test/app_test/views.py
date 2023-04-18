from django.shortcuts import render
from .models import Menu

def menu(request):
    return render(request, ('app_test/index.html'), {'title': 'Меню'})