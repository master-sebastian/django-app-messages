# Generated by Django 3.2.3 on 2021-05-22 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager_messages', '0005_alter_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager_messages.role'),
            preserve_default=False,
        ),
    ]