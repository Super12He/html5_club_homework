# Generated by Django 2.1.7 on 2019-06-10 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circlip', '0004_remove_circlipmodel_circlip_deformed_radius'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circlipmodel',
            name='circlip_deformed_diameters',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='circlipmodel',
            name='circlip_mises',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
