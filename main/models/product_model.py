from django.conf import settings
from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(
        max_length=255,
        verbose_name='наименование',
    )
    slug = models.SlugField(
        unique=True,
        **settings.NULLABLE,
        verbose_name='slug-имя',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='цена',
    )
    image_small = models.ImageField(
        upload_to='images/product/small/',
        verbose_name='изображение (маленькое)',
    )
    image_medium = models.ImageField(
        upload_to='images/product/medium/',
        verbose_name='изображение (среднее)',
    )
    image_large = models.ImageField(
        upload_to='images/product/large/',
        verbose_name='изображение (большое)',
    )
    category = models.ForeignKey(
        'main.Category',
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='категория',
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} ({self.price})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
