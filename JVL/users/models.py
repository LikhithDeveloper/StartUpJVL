from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=13)
    email = models.EmailField(max_length=30,null=True,blank=True)
    address = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
