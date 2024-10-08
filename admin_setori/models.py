from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class Time(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True
        
class Faq(Time):
    pertanyaan = models.CharField(max_length=225)
    jawaban = models.CharField(max_length=225)
