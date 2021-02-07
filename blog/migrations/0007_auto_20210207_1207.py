# Generated by Django 2.2.1 on 2021-02-07 12:07

import blog.helper
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210207_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='0', upload_to=blog.helper.PathAndRename('post_images/'), verbose_name='Картинка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
