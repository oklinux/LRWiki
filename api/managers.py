from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password=None, **extra_fields):
        raise Exception('can not create user')

    def create_superuser(self, email, password=None, **extra_fields):
        raise Exception('can not create user')
