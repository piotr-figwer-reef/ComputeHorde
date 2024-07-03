# Generated by Django 4.2.13 on 2024-07-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("miner", "0006_remove_jobreceipt_job"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobStartedReceipt",
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
                ("validator_signature", models.CharField(max_length=256)),
                ("miner_signature", models.CharField(max_length=256)),
                ("job_uuid", models.UUIDField()),
                ("miner_hotkey", models.CharField(max_length=256)),
                ("validator_hotkey", models.CharField(max_length=256)),
                ("time_accepted", models.DateTimeField()),
                ("max_timeout", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
