# Generated by Django 2.1.5 on 2019-02-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='is_buy',
            field=models.IntegerField(choices=[(0, 'NO'), (1, '上架')], default=1, verbose_name='是否上架'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='seller',
            field=models.IntegerField(default=1, verbose_name='卖家编号'),
        ),
    ]
