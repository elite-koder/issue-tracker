# Generated by Django 4.2.5 on 2023-10-05 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_ticket_project_delete_projectticketmapping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='desc',
            field=models.CharField(max_length=500),
        ),
    ]
