# Generated by Django 4.1 on 2022-03-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_alter_project_applied_stu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="applied_project",
            field=models.JSONField(null=True, unique=True),
        ),
    ]
