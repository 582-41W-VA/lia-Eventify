# Generated by Django 5.1.5 on 2025-02-13 21:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0005_alter_event_is_approved"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="is_approved",
        ),
        migrations.RemoveField(
            model_name="event",
            name="is_flagged",
        ),
    ]
