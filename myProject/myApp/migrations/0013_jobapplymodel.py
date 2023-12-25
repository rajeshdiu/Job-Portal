# Generated by Django 4.2.6 on 2023-12-25 07:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0012_job_model_update_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="jobApplyModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("applied_at", models.DateTimeField(auto_now_add=True)),
                ("skills", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "resume",
                    models.FileField(blank=True, null=True, upload_to="resumes/"),
                ),
                (
                    "applicant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applications",
                        to="myApp.job_model",
                    ),
                ),
            ],
        ),
    ]