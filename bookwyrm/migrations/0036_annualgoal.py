# Generated by Django 3.0.7 on 2021-01-16 18:43

import bookwyrm.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0035_edition_edition_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('remote_id', bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id])),
                ('goal', models.IntegerField()),
                ('year', models.IntegerField(default=2021)),
                ('privacy', models.CharField(choices=[('public', 'Public'), ('unlisted', 'Unlisted'), ('followers', 'Followers'), ('direct', 'Direct')], default='public', max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'year')},
            },
        ),
    ]
