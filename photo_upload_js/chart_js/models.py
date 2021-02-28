from django.db import models

# Create your models here.
class Salary(models.Model):
    month   = models.CharField(max_length=120)
    earing  = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.month)