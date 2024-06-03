# Generated by Django 3.2.25 on 2024-04-04 00:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("NEMO", "0070_calendar_axis_time_format_rename"),
    ]

    operations = [
        migrations.AddField(
            model_name="tool",
            name="_operation_mode",
            field=models.IntegerField(
                choices=[(0, "Regular"), (1, "Wait List"), (2, "Hybrid")],
                default=0,
                help_text="The operation mode of the tool, which determines if reservations and wait list are allowed.",
            ),
        ),
        migrations.AddField(
            model_name="userpreferences",
            name="email_send_wait_list_notification_emails",
            field=models.PositiveIntegerField(
                choices=[(1, "Both emails"), (2, "Main email only")], default=1, help_text="Tool wait list notification"
            ),
        ),
        migrations.CreateModel(
            name="ToolWaitList",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "date_entered",
                    models.DateTimeField(auto_now_add=True, help_text="The date/time the user entered the wait list."),
                ),
                (
                    "date_exited",
                    models.DateTimeField(
                        blank=True, help_text="The date/time the user exited the wait list.", null=True
                    ),
                ),
                (
                    "last_turn_available_at",
                    models.DateTimeField(
                        blank=True, help_text="The last date/time the user's turn became available.", null=True
                    ),
                ),
                (
                    "expired",
                    models.BooleanField(
                        default=False, help_text="Whether the user's spot in the wait list has expired."
                    ),
                ),
                (
                    "deleted",
                    models.BooleanField(default=False, help_text="Whether the wait list entry has been deleted."),
                ),
                (
                    "tool",
                    models.ForeignKey(
                        help_text="The target tool for the wait list entry.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="NEMO.tool",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user in the wait list.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
