# Generated by Django 4.2.9 on 2024-02-07 11:27

import aifitness.workouts.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workouts", "0002_alter_uservideo_options_uservideo_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uservideo",
            name="video",
            field=models.FileField(blank=True, null=True, upload_to=aifitness.workouts.models.generate_filename),
        ),
    ]