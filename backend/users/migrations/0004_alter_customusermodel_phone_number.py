# Generated by Django 4.0.6 on 2022-07-29 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customusermodel_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='phone_number',
            field=models.CharField(max_length=32, null=True, verbose_name='Phone Number'),
        ),
    ]
