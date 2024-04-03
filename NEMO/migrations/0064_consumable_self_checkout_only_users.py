# Generated by Django 3.2.23 on 2024-03-07 14:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NEMO", "0063_knowledge_base"),
    ]

    operations = [
        migrations.AddField(
            model_name="consumable",
            name="self_checkout_only_users",
            field=models.ManyToManyField(
                blank=True,
                help_text="Selected users will be the only ones allowed to self checkout this consumable. Leave blank for all.",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
