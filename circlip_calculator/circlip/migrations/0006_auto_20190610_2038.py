# Generated by Django 2.1.7 on 2019-06-10 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circlip', '0005_auto_20190610_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circlipmodel',
            name='circlip_mises',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]