from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Book(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField()
    author = models.ForeignKey(
        "info.Author", related_name="books", on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )
