# Generated by Django 2.0.8 on 2019-04-08 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_auto_20190408_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent_comment',
            name='to_Parent_Comments',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='to_Parent_Commenty', to=settings.AUTH_USER_MODEL, verbose_name='目标用户'),
        ),
    ]
