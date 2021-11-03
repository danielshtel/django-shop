from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Sneaker(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    color = models.CharField(max_length=50)
    size = models.IntegerField(validators=[MinValueValidator(33), MaxValueValidator(46)])
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.id, self.slug])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кроссовки'
        verbose_name_plural = 'Кроссовки'


class Category(models.Model):
    title = models.CharField(max_length=10, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
