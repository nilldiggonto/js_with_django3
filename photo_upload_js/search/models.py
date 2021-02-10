from django.db import models

# Create your models here.
class TestSearch(models.Model):
    title   = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title


##### Create A POST WITH PHOTOS
class PostUp(models.Model):
    title       = models.CharField(max_length=120)
    content     = models.TextField()
    image       = models.ImageField(upload_to='search/')
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title