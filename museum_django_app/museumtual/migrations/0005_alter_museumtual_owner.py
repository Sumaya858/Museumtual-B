# Generated by Django 4.2.3 on 2023-07-20 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('museumtual', '0004_alter_museumtual_owner_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museumtual',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
