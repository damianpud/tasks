from django.db.models import CASCADE, Model, OneToOneField
from django.contrib.auth.models import User


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)

