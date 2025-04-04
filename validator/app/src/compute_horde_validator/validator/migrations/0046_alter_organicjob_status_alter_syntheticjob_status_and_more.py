# Generated by Django 4.2.16 on 2025-01-21 21:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("validator", "0045_organicjob_block_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organicjob",
            name="status",
            field=models.TextField(
                choices=[
                    ("PENDING", "Pending"),
                    ("COMPLETED", "Completed"),
                    ("FAILED", "Failed"),
                    ("EXCUSED", "Excused"),
                ],
                default="PENDING",
            ),
        ),
        migrations.AlterField(
            model_name="syntheticjob",
            name="status",
            field=models.TextField(
                choices=[
                    ("PENDING", "Pending"),
                    ("COMPLETED", "Completed"),
                    ("FAILED", "Failed"),
                    ("EXCUSED", "Excused"),
                ],
                default="PENDING",
            ),
        ),
        migrations.AlterField(
            model_name="systemevent",
            name="subtype",
            field=models.CharField(
                choices=[
                    ("SUCCESS", "Success"),
                    ("FAILURE", "Failure"),
                    ("SUBTENSOR_CONNECTIVITY_ERROR", "Subtensor Connectivity Error"),
                    ("COMMIT_WEIGHTS_SUCCESS", "Commit Weights Success"),
                    ("COMMIT_WEIGHTS_ERROR", "Commit Weights Error"),
                    ("COMMIT_WEIGHTS_UNREVEALED_ERROR", "Commit Weights Unrevealed Error"),
                    ("REVEAL_WEIGHTS_ERROR", "Reveal Weights Error"),
                    ("REVEAL_WEIGHTS_SUCCESS", "Reveal Weights Success"),
                    ("SET_WEIGHTS_SUCCESS", "Set Weights Success"),
                    ("SET_WEIGHTS_ERROR", "Set Weights Error"),
                    ("GENERIC_ERROR", "Generic Error"),
                    ("WRITING_TO_CHAIN_TIMEOUT", "Writing To Chain Timeout"),
                    ("WRITING_TO_CHAIN_GENERIC_ERROR", "Writing To Chain Generic Error"),
                    ("GIVING_UP", "Giving Up"),
                    ("MANIFEST_ERROR", "Manifest Error"),
                    ("MANIFEST_TIMEOUT", "Manifest Timeout"),
                    ("MINER_CONNECTION_ERROR", "Miner Connection Error"),
                    ("MINER_SEND_ERROR", "Miner Send Error"),
                    ("MINER_SCORING_ERROR", "Miner Scoring Error"),
                    ("JOB_NOT_STARTED", "Job Not Started"),
                    ("JOB_REJECTED", "Job Rejected"),
                    ("JOB_EXCUSED", "Job Excused"),
                    ("JOB_EXECUTION_TIMEOUT", "Job Execution Timeout"),
                    ("RECEIPT_FETCH_ERROR", "Receipt Fetch Error"),
                    ("RECEIPT_SEND_ERROR", "Receipt Send Error"),
                    ("SPECS_SENDING_ERROR", "Specs Send Error"),
                    ("HEARTBEAT_ERROR", "Heartbeat Error"),
                    ("UNEXPECTED_MESSAGE", "Unexpected Message"),
                    ("UNAUTHORIZED", "Unauthorized"),
                    ("SYNTHETIC_BATCH", "Synthetic Batch"),
                    ("SYNTHETIC_JOB", "Synthetic Job"),
                    ("CHECKPOINT", "Checkpoint"),
                    ("OVERSLEPT", "Overslept"),
                    ("WARNING", "Warning"),
                    ("FAILED_TO_WAIT", "Failed To Wait"),
                    ("TRUSTED_MINER_NOT_CONFIGURED", "Trusted Miner Not Configured"),
                    ("LLM_PROMPT_ANSWERS_MISSING", "Llm Prompt Answers Missing"),
                    ("INSUFFICIENT_PROMPTS", "Insufficient Prompts"),
                    ("UNPROCESSED_WORKLOADS", "Unprocessed Workloads"),
                    ("PROMPT_GENERATION_STARTED", "Prompt Generation Started"),
                    ("PROMPT_SAMPLING_SKIPPED", "Prompt Sampling Skipped"),
                    ("NEW_WORKLOADS_CREATED", "New Workloads Created"),
                    ("ERROR_UPLOADING_TO_S3", "Error Uploading To S3"),
                    ("ERROR_DOWNLOADING_FROM_S3", "Error Downloading From S3"),
                    (
                        "LLM_PROMPT_ANSWERS_DOWNLOAD_WORKER_FAILED",
                        "Llm Prompt Answers Download Worker Failed",
                    ),
                ],
                max_length=255,
            ),
        ),
    ]
