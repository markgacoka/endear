import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

class MyUserManager(UserManager):
    def create_user(self, email_address, username, password=None):
        user = self.model(
            email_address=self.normalize_email(email_address),
            username=username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email_address, username, password):
        user = self.create_user(
            email_address=self.normalize_email(email_address),
            username=username,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.first_name = 'Admin'
        user.last_name = 'Account'
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, blank=False, unique=True, default=uuid.uuid4, db_index=True, editable=False)
    first_name = models.CharField(max_length=30, unique=False, null=True)
    last_name = models.CharField(max_length=30, unique=False, null=True)    
    username = models.CharField(max_length=64, unique=True)
    email_address = models.EmailField(verbose_name='email_address', max_length=60, unique=True)
    profile_image = models.TextField(default='default.jpeg', max_length=250, unique=False, null=False, blank=False)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email_address'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'users'
        abstract = False

    @property
    def name(self):
        if self.first_name:
            return self.first_name
        elif self.username:
            return self.username
        else:
            return 'You'

    def __str__(self):
        return self.username