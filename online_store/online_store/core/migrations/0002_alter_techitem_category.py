# Generated by Django 5.0.2 on 2024-05-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techitem',
            name='category',
            field=models.CharField(choices=[('TV', 'TV'), ('Computer', 'Computer'), ('Cell Phone', 'Cell Phone'), ('Laptop', 'Laptop'), ('Tablet', 'Tablet'), ('Other', 'Other')], max_length=100),
        ),
    ]
