# Generated by Django 4.0.1 on 2022-01-17 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.kind'),
        ),
    ]