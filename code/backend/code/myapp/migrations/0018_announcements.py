# Generated by Django 4.1 on 2022-04-17 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0017_criteria_instructor_criterialist_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="announcements",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uid", models.CharField(max_length=200, null=True)),
                ("name", models.CharField(max_length=200, null=True)),
                ("val", models.CharField(max_length=5000, null=True)),
                ("releaseTime", models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
