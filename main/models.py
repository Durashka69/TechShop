from django.db import models
from authentication.models import User


class Category(models.Model):
    title = models.CharField(verbose_name='Категория', max_length=255)
    slug = models.SlugField(verbose_name='Слаг')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = "Категория"


class Product(models.Model):
    title = models.CharField(verbose_name='Название продукта', max_length=255)
    photo = models.ImageField(verbose_name='Изброжение продукта', blank=True, upload_to='static/product')
    price = models.PositiveIntegerField(verbose_name='Цена', null=False)
    desc = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    data_create = models.DateField(auto_now_add=False, verbose_name='Дата добавления')
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    memory = models.IntegerField(default=128, verbose_name="Память GB")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = "Продукт"
        ordering = ['-data_create', 'title']


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    object_id = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE, related_name='products')
    qty = models.PositiveIntegerField(verbose_name='Количество', default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена', default=0)

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.user.user.first_name)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.object_id.price
        super().save(*args, **kwargs)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.user.first_name


class Customer(models.Model):
    name = models.CharField(verbose_name="Имя пользователя", max_length=255)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)

    def __str__(self):
        return self.name
