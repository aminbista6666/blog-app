# Generated by Django 4.0.2 on 2022-02-16 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_author',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blogitem',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.author'),
        ),
    ]
