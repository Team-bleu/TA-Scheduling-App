# Generated by Django 2.1.2 on 2018-11-19 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('lab', models.CharField(max_length=50)),
                ('assignment', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TA_Scheduling_App.Person'),
        ),
    ]