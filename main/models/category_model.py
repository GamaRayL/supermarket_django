from django.conf import settings
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class Category(models.Model):
    """Модель категории"""
    name = models.CharField(
        max_length=255,
        verbose_name='наименование',
    )
    slug = models.SlugField(
        unique=True,
        **settings.NULLABLE,
        verbose_name='slug-имя',
    )
    image = models.ImageField(
        upload_to='images/category/',
        **settings.NULLABLE,
        verbose_name='изображение',
    )
    parent_category = models.ForeignKey(
        'self',
        **settings.NULLABLE,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name='родительская категория',
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} {f"<- {self.parent_category}" if self.parent_category else ""}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
