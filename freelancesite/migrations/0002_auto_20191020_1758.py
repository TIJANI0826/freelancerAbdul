# Generated by Django 3.0 on 2019-10-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancesite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='subject',
            field=models.CharField(default='user', max_length=250),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='phone_number',
            field=models.CharField(max_length=250),
        ),
    ]
