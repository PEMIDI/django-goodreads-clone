from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.constants import UserType


class CustomUser(AbstractUser):

    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(_("role"), max_length=10, choices=UserType.ROLE_CHOICES)


