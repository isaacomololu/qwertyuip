# Generated by Django 4.2.7 on 2023-11-19 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0011_alter_exercise_equipment_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='description',
            field=models.TextField(),
        ),
    ]
