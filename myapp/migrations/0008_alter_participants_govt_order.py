# Generated by Django 4.2.9 on 2024-01-13 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_participants_govt_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants',
            name='govt_order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='myapp.govtorder'),
        ),
    ]
