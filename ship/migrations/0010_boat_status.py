# Generated by Django 3.2.9 on 2021-12-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0009_alter_boat_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'pending'), ('paid', 'paid')], max_length=10, null=True),
        ),
    ]
