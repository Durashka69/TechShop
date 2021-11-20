from django.db import models


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
    image = models.ImageField(verbose_name='Изброжение продукта', blank=True, upload_to='static/product')
    price = models.PositiveIntegerField(verbose_name='Цена', null=False)
    desc = models.TextField()
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = "Продукт"
