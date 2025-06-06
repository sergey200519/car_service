# Generated by Django 5.2.1 on 2025-05-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivedOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_id', models.IntegerField()),
                ('client_username', models.CharField(max_length=150)),
                ('service_name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('technician_username', models.CharField(blank=True, max_length=150, null=True)),
                ('status', models.CharField(max_length=20)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
