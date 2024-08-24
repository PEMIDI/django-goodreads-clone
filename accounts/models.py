import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.constants import UserType


class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        default=f"user__{uuid.uuid4().hex[:8]}"
    )

    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(_("role"), max_length=10, choices=UserType.ROLE_CHOICES, default=UserType.MEMBER)
