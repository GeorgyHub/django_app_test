from django.contrib import admin
from django.urls import path
from app_test.views import menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='menu'),
]
