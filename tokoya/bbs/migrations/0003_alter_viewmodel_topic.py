# Generated by Django 4.1 on 2023-11-16 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("bbs", "0002_alter_viewmodel_topic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="viewmodel",
            name="topic",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="bbs.topicmodel",
            ),
        ),
    ]