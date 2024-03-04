from django.db import models

from constants import NULLABLE


class Category(models.Model):
    """Модель категории"""
    name = models.CharField(max_length=255, verbose_name='наименование')
    slug = models.SlugField(unique=True, verbose_name='slug-имя')
    image = models.ImageField(upload_to='category_images/', **NULLABLE, verbose_name='изображение')
    parent_category = models.ForeignKey('self', **NULLABLE,
                                        on_delete=models.CASCADE, related_name='subcategories',
                                        verbose_name='родительская категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
