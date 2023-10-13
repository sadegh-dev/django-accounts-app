from django.db import models
from django.contrib.auth.models import AbstractBaseUser



class User(AbstractBaseUser):
    pass


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)




