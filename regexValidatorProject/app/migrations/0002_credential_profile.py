# Generated by Django 4.2.11 on 2024-05-15 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="credential",
            name="profile",
            field=models.ImageField(default=None, upload_to=""),
            preserve_default=False,
        ),
    ]