from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=100)
  surname = models.CharField(max_length=100)
  email_address = models.EmailField(max_length=254, unique=True)
  password = models.CharField(max_length=254)

  # Changes 'Users object' in 'Users' table to the surname and name of the registrated user.
  # https://stackoverflow.com/questions/48883868/how-to-change-table-object-name-in-django
  def __str__(self) -> str:
        return self.surname + ' ' + self.name

  def save(self, **kwargs):
    self.password = make_password(self.password)
    super().save(**kwargs)
