# Generated by Django 3.2.3 on 2021-05-23 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager_messages', '0007_remove_message_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager_messages.profile'),
        ),
    ]
