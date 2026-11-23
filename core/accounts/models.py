from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.


class UserManager(BaseUserManager):
    """
    Custom manager for User model where email is the unique identifier and
    users are inactive by default, except for superusers. 
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and return a user.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fileds):
            """
            Create and return superuser.
            """
            extra_fileds.setdefault('is_staff', True)
            extra_fileds.setdefault('is_superuser', True)
            extra_fileds.setdefault('is_active',True)

            if extra_fileds.get('is_staff') is not True:
                 raise ValueError(_('Superuser must have is_staff=True.'))

            if extra_fileds.get('is_superuser') is not True:
                 raise ValueError(_('Superuser must have is_superuser=True.'))

            return self.create_user(email, password, **extra_fileds)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150, unique=True, blank=True, null=True)
    password = models.CharField(max_length=250)
    phone = models.CharField(max_length=15, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
         return self.email    
    


    
