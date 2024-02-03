# Generated by Django 5.0 on 2024-01-30 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content',
            field=models.TextField(default=255),
        ),
        migrations.AddField(
            model_name='page',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
