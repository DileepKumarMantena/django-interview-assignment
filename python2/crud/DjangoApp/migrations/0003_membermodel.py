# Generated by Django 4.0.1 on 2022-05-06 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0002_bookmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MemberName', models.CharField(max_length=250)),
                ('MemberId', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('LibraryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LibraryId', to='DjangoApp.librarianmodel')),
            ],
            options={
                'db_table': 'Memeber_Table',
            },
        ),
    ]
