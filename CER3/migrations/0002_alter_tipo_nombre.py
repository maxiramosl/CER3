# Generated by Django 4.2.6 on 2023-11-27 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CER3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo',
            name='nombre',
            field=models.CharField(default='', max_length=30, primary_key=True, serialize=False),
        ),
    ]