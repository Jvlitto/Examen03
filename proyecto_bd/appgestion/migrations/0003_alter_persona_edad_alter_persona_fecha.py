# Generated by Django 4.0.5 on 2022-06-24 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appgestion', '0002_alter_persona_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha',
            field=models.CharField(max_length=30),
        ),
    ]
