# Generated by Django 4.2.3 on 2023-07-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museumtual', '0005_alter_museumtual_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
