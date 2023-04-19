from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class MenuItem(MPTTModel):
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Пункт меню'

    name = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=255)
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True)

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return self.name