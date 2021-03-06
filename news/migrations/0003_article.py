# Generated by Django 3.2.10 on 2022-05-25 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('post', models.TextField()),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.editor')),
                ('tags', models.ManyToManyField(to='news.tags')),
            ],
        ),
    ]
