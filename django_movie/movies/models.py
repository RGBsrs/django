from django.db import models

class Category(models.Model):
    ***Категории***
    
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    ***Актеры и режиссеры***
    
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/s")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"

class Genre(models.Model):
    ***Категории***
    
    name = models.CharField("Жанр", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Movie(models.Model):
    ***Фильмы***

    title = models.CharField("", max_length=100)
    tagline = models.CharField("", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("", upload_to="movies/")
    year = models.PositiveSmallIntegerField("", default=2019)
    country = models.CharField("", max_length=30)

