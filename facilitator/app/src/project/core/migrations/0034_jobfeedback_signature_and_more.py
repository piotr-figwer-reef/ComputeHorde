# Generated by Django 4.2.16 on 2024-11-14 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0033_job_signature"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobfeedback",
            name="signature",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="jobfeedback",
            name="signature_info",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="core.signatureinfo"),
        ),
    ]
