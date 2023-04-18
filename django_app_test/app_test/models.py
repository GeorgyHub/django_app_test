from django.db import models

class Menu(models.Model):
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Пункт меню'

    name = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return self.name