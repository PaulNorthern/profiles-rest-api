from django.db import models
# Используем эти классы для переопределения способа аутентификации нашего пользователя
# по email
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    '''Manager for user profieles'''

    def create_user(self, email, name, password=None):
        '''Create a new user profile'''
        if not email:
            raise ValueError('User must hava an email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) # encrypted
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        '''Create superuser'''
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Data model for users in the system .__doc__"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # Permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Указываем, что все objects для класса происходят от Manager
    objects = UserProfileManager()

    # Задаем USERNAME_FIELD–для определения уникального идентификатора в модели User со значением email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
         '''Retrieve full name of user'''
         return self.name

    def get_short_name(self):
        '''Retrieve short name of user'''
        return self.name

    def __str__(self):
        return self.email
