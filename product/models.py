from django.db import models
import datetime
from django.contrib.auth.models import User

# generally speaking, you will have one model per app
# Django documentation has info on model field types to choose from

class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    pub_date = models.DateTimeField(default=datetime.date.today)
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.CharField(max_length=400)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
