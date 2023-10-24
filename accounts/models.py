from django.db import models
from django.contrib.auth.models import AbstractBaseUser



class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)




