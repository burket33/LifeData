# Generated by Django 2.0.5 on 2018-07-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedtime', models.DateTimeField()),
                ('wakeup_time', models.DateTimeField()),
                ('quality', models.CharField(choices=[('POOR', 'Poor'), ('GOOD', 'Good'), ('EXCELLENT', 'Excellent')], default='GOOD', max_length=15)),
                ('description', models.TextField()),
            ],
        ),
    ]
