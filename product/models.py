from django.db import models
import datetime

# generally speaking, you will have one model per app
# Django documentation has info on model field types to choose from

class Product(models.Model):
    title = models.CharField(max_length=255)
    product_url = models.URLField([source])
    pub_date = models.DateTimeField(default=datetime.date.today)
    votes_total = models.IntegerField([source])
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/', height_field=0, width_field=0)
    body = models.CharField(max_length=400)

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
