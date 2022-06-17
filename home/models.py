from django.db import models

# Create your models here.
class pickle(models.Model):
    def __str__(self):
        return self.pickle_name
    pickle_name=models.CharField(max_length=30)
    pickle_ingredients=models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=False)