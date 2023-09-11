# Generated by Django 3.2.20 on 2023-09-11 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0051_auto_20230829_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumable',
            name='allow_self_checkout',
            field=models.BooleanField(default=True, help_text='Allow users to self checkout this consumable, only applicable when self checkout customization is enabled'),
        ),
    ]
