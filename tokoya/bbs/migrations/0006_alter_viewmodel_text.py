# Generated by Django 4.1 on 2023-11-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bbs", "0005_rename_data_viewmodel_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="viewmodel",
            name="text",
            field=models.CharField(help_text="返信", max_length=200),
        ),
    ]
