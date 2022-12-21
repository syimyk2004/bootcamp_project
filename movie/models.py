from django.db import models



class Genre(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'



class Movie(models.Model):
    title = models.CharField(max_length=100)
    decs = models.TextField()
    year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='movie')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'film'
        verbose_name_plural = 'films'
