from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from ckeditor_uploader.fields import RichTextUploadingField

from user.countries import COUNTRIES_CHOOSE
# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    email = models.EmailField(_("Email Address"),max_length=255, unique=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)

class Profile(models.Model):
    class GENDER(models.TextChoices):
        MALE = "MALE", 'MALE'
        FEMALE = "FEMALE", 'FEMALE'
        OTHERS = "OTHERS", 'OTHERS'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="user/profile/avatar", default="default/default.png")
    bio = RichTextUploadingField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER.choices, null=True, blank=True)
    country = models.CharField(max_length=32, choices=COUNTRIES_CHOOSE.choices, null=True, blank=True)
    phone = PhoneNumberField(blank=True, null=True)
    github = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)
    linkedin = models.URLField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username.title()} Profile"
    
