from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin  )

from .managers import CustomUserManager



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    @property
    def is_staff(self):
        self.is_admin

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)




