from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class blog(models.Model): # change post to diff name
    name = models.CharField(max_length=64)
    author = models.TextField(default="")
    buyer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name and self.author

    def reverse_url(self):
        return reverse('blog_details', kwargs={'id': self.id})