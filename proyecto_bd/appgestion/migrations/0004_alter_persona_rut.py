# Generated by Django 4.0.5 on 2022-06-25 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appgestion', '0003_alter_persona_edad_alter_persona_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='rut',
            field=models.CharField(max_length=10),
        ),
    ]