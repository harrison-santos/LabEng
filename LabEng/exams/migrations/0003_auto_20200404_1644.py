# Generated by Django 3.0.4 on 2020-04-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20200404_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ethinicity',
            field=models.CharField(choices=[('Preto', 'Preto'), ('Branco', 'Branco'), ('Pardo', 'Pardo'), ('Indio', 'Indio'), ('Amarelo', 'Amarelo')], max_length=10),
        ),
    ]