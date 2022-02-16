# Generated by Django 4.0.2 on 2022-02-16 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_blogitem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_author',
        ),
        migrations.AlterField(
            model_name='blogitem',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]