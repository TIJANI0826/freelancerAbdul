from django.db import models

CLASS = [
    ('SS1', 'ss1'),
    ('ss2', 'SS2'),
    ('SS3', 'ss3')
]


# Create your models here.
class ContactForm(models.Model):
    email = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    message = models.TextField(max_length=300)
    sender = models.EmailField()
    subject = models.CharField(max_length=250, default='user')
    cc_myself = models.BooleanField()


class FormMasters(models.Model):
    form_master_name = models.CharField(max_length=250)
    class_for = models.CharField(max_length=250)
