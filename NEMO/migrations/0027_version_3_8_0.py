# Generated by Django 2.2.13 on 2020-12-10 22:06

from django.db import migrations

from NEMO.migrations_utils import create_news_for_version


class Migration(migrations.Migration):
    dependencies = [
        ("NEMO", "0026_version_3_7_0"),
    ]

    def new_version_news(apps, schema_editor):
        create_news_for_version(apps, "3.8.0")

    operations = [
        migrations.RunPython(new_version_news),
    ]
