# Generated by Django 4.0.2 on 2022-04-21 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_contact_prj_group_instructor_group_selection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
