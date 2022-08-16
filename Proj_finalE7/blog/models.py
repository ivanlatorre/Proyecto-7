from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    #text = models.TextField()

    text = RichTextField(blank=True, null=True)

    created_date = models.DateTimeField(

            default=timezone.now)

    published_date = models.DateTimeField(

            blank=True, null=True)


    def publish(self):

        self.published_date = timezone.now()

        self.save()


    def __str__(self):

        return self.title

    def get_absolute_url(self):
    	return reverse('Inicio')