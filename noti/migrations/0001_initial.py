# Generated by Django 3.0.5 on 2020-11-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('registered_time', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
        ),
    ]
