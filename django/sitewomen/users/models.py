from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField, DateTimeField


class User(AbstractUser):
    photo = ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    date_birth = DateTimeField(blank=True, null=True, verbose_name="Дата рождения")
