from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        ''' Custom User Model Manager

            Here email is set as primary_key instead of username.
        '''
        if not email:
            raise ValueError(_("Email is required"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        ''' create superUser by sending data to the create_user method  '''

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_supseruser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('superuser must have is_superuser=True.'))
        
        return self.create_user(email, password, **extra_fields)
        
