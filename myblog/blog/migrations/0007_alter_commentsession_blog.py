# Generated by Django 3.2.8 on 2021-10-31 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20211028_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsession',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog'),
        ),
    ]