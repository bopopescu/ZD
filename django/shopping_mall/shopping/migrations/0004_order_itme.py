# Generated by Django 2.1.5 on 2019-02-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_auto_20190225_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='itme',
            field=models.IntegerField(null=True, verbose_name='订单号'),
        ),
    ]