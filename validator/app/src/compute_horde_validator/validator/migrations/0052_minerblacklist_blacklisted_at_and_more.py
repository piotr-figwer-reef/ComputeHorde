# Generated by Django 4.2.16 on 2025-02-17 22:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("validator", "0051_organicjob_artifacts"),
    ]

    operations = [
        migrations.AddField(
            model_name="minerblacklist",
            name="blacklisted_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="minerblacklist",
            name="expires_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="minerblacklist",
            name="reason",
            field=models.TextField(
                choices=[("MANUAL", "Manual"), ("JOB_FAILED", "Job Failed")], default="MANUAL"
            ),
        ),
        migrations.AddField(
            model_name="minerblacklist",
            name="reason_details",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="minerblacklist",
            name="miner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="validator.miner"
            ),
        ),
        migrations.AlterField(
            model_name="minermanifest",
            name="executor_count",
            field=models.IntegerField(
                default=0,
                help_text="The total number of available executors of this class as reported by the miner",
            ),
        ),
        migrations.AlterField(
            model_name="minermanifest",
            name="online_executor_count",
            field=models.IntegerField(
                default=0,
                help_text="Number of executors that finished or properly declined a job request during the batch",
            ),
        ),
    ]
