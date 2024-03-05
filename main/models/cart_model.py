from django.db import models


class CartItem(models.Model):
    """Модель товара корзины"""
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь')
    product = models.ForeignKey('main.Product', on_delete=models.CASCADE, verbose_name='продукт')
    quantity = models.PositiveIntegerField(default=1, verbose_name='количество')

    @property
    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'{self.quantity} x {self.product}'

    class Meta:
        unique_together = ('user', 'product')
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Cart(models.Model):
    """Модель корзины"""
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь')
    items = models.ManyToManyField('main.CartItem', blank=True, verbose_name='товары')

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())

    @property
    def total_quantity(self):
        return sum(item.quantity for item in self.items.all())

    def __str__(self):
        return f'Корзина пользователя: {self.user.email}'
