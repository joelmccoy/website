# Generated by Django 5.0.3 on 2024-03-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
