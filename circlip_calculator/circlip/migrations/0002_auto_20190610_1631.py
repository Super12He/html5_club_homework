# Generated by Django 2.1.7 on 2019-06-10 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circlip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='circlipmodel',
            name='circlip_deformed_radius',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AddField(
            model_name='circlipmodel',
            name='circlip_mises',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]
