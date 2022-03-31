from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=100)
  surname = models.CharField(max_length=100)
  email_address = models.EmailField(max_length=254, unique=True)
  password = models.CharField(max_length=254)

  def save(self, **kwargs):
    self.password = make_password(self.password)
    super().save(**kwargs)
