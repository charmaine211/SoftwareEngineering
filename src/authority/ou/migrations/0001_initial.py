# Generated by Django 3.1.6 on 2021-03-01 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=512)),
                ('role', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Signatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('digest', models.CharField(max_length=512)),
                ('salt', models.CharField(max_length=128)),
                ('signature', models.CharField(max_length=512)),
                ('time_stamp', models.DateTimeField(verbose_name='date signed')),
                ('key_used', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ou.keys')),
            ],
        ),
    ]
