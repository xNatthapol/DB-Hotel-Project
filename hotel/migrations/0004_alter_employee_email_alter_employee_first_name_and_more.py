# Generated by Django 4.2.7 on 2023-11-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_rename_fname_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='facility',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='measure_type',
            field=models.CharField(choices=[('kg', 'Kilogram'), ('g', 'Gram'), ('l', 'Liter'), ('ml', 'Milliliter')], max_length=3),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='menu_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='room',
            name='floor',
            field=models.IntegerField(choices=[(1, 'Floor 1'), (2, 'Floor 2'), (3, 'Floor 3'), (4, 'Floor 4'), (5, 'Floor 5'), (6, 'Floor 6'), (7, 'Floor 7'), (8, 'Floor 8'), (9, 'Floor 9'), (10, 'Floor 10')]),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('Single', 'Single'), ('Double', 'Double'), ('Suite', 'Suite'), ('Penthouse', 'Penthouse')], max_length=30),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ingredient_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stock',
            name='type',
            field=models.CharField(choices=[('kg', 'Kilogram'), ('g', 'Gram'), ('l', 'Liter'), ('ml', 'Milliliter')], max_length=3),
        ),
    ]
