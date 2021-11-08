from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Size(models.Model):
    size = models.PositiveIntegerField(validators=[MinValueValidator(33), MaxValueValidator(46)])

    def __str__(self):
        return f'{self.size}'

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Sneaker(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(db_index=True, max_length=50, unique=True, editable=False)
    color = models.CharField(max_length=50)
    size = models.ManyToManyField(Size)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Sneaker, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail',
                       kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кроссовки'
        verbose_name_plural = 'Кроссовки'


class Category(models.Model):
    title = models.CharField(max_length=10, db_index=True, verbose_name='Категория')
    slug = models.SlugField(db_index=True, max_length=50, unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
