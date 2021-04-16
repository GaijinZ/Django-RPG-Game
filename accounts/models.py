from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users mus have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    email = models.EmailField(max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(null=True, blank=True, verbose_name='first name', max_length=30)
    last_name = models.CharField(null=True, blank=True, verbose_name='last name', max_length=30)
    avatar = models.ImageField(null=True, blank=True,
                               upload_to='profile_pic',
                               default='profile_pic/default.jpg')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.is_superuser

    @property
    def is_user_active(self):
        return self.is_active

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return f'{self.user}'
