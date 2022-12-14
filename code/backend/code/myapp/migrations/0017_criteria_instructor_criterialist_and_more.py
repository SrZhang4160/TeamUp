# Generated by Django 4.0.4 on 2022-04-14 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_profile_prod'),
    ]

    operations = [
        migrations.CreateModel(
            name='criteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteriaId', models.CharField(max_length=200, null=True)),
                ('criteriaName', models.CharField(max_length=200, null=True)),
                ('criteriaNum', models.SmallIntegerField(default=0, null=True)),
                ('criteriaPption', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='criteriaList',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='applied_project',
            field=models.JSONField(null=True),
        ),
    ]
