from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.models import BaseModel

from apps.users.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'
        ordering = ['id']

    email = models.EmailField(unique=True)               # password is already in AbstractBaseUser
    is_active = models.BooleanField(default=True)        # is it possible to log in
    is_staff = models.BooleanField(default=False)        # is admin
    USERNAME_FIELD = 'email'          # log in via email
    # REQUIRED_FIELDS = ['password']

    objects = UserManager()
    
    
class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'
        ordering = ['id']

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
