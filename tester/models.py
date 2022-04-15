from django.db.models import CharField, TextField, Model
from django_mysql.models import ListTextField


class User(Model):
    name = TextField()
    childrenNames = ListTextField(
        base_field=CharField(max_length=30),
        size=5
    )

