# Generated by Django 4.2.5 on 2023-09-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomClasses', '0005_alter_customclass_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customclass',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
