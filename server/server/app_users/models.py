from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from server.app_users.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        error_messages={
            'unique': "User with this email already exists."
        }
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    USERNAME_FIELD = 'email'
    objects = AppUserManager()
