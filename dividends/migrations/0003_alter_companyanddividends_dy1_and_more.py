# Generated by Django 4.0.5 on 2022-06-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dividends', '0002_companyanddividends_r1_companyanddividends_r3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyanddividends',
            name='dy1',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='dy1'),
        ),
        migrations.AlterField(
            model_name='companyanddividends',
            name='dy3',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='dy3'),
        ),
        migrations.AlterField(
            model_name='companyanddividends',
            name='dy5',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='dy5'),
        ),
        migrations.AlterField(
            model_name='companyanddividends',
            name='r1',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='r1'),
        ),
        migrations.AlterField(
            model_name='companyanddividends',
            name='r3',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='r3'),
        ),
        migrations.AlterField(
            model_name='companyanddividends',
            name='r5',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='r5'),
        ),
    ]
