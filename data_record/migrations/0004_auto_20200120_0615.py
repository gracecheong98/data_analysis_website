# Generated by Django 3.0.1 on 2020-01-20 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_record', '0003_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_record.Project'),
        ),
    ]