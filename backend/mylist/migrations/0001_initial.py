# Generated by Django 4.2.2 on 2023-07-27 07:08

from django.db import migrations, models
import django.db.models.deletion
import mylist.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myfolder',
            fields=[
                ('list_name', models.CharField(default='노래', max_length=30)),
                ('list_number', models.IntegerField(default=mylist.models.list_number, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('song_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(default='노래', max_length=30)),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('cmp', models.CharField(blank=True, default='none', max_length=255, null=True)),
                ('writer', models.CharField(blank=True, default='none', max_length=255, null=True)),
                ('key', models.CharField(blank=True, default='none', max_length=255, null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('ky_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mylist_set', to='song.kysong')),
                ('list_number', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mylist.myfolder')),
                ('tj_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mylist_set', to='song.tjsong')),
            ],
        ),
    ]
