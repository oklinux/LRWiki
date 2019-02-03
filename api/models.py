# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager


class Doc(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30, blank=True, null=True)
    text = models.CharField(max_length=30000)
    create_time = models.DateField(auto_now=True)
    update_time = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'docs'


class User(AbstractBaseUser):
    account = models.CharField(max_length=30, primary_key=True, unique=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    last_login = None
    USERNAME_FIELD = 'account'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'wiki_user'

    def get_full_name(self):
        return self.account

    def get_short_name(self):
        return self.account

    def check_password(self, raw_password):
        return True
