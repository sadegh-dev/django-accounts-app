from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin  )



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)




