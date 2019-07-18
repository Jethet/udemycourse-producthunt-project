rom django.db import models

# generally speaking, you will have one model per app
# Django documentation has info on model field types to choose from

class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=400)
