# Generated by Django 3.0.6 on 2020-05-21 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0003_form_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('comment', models.TextField(null=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='Quizz.User')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='Quizz.User')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(through='Quizz.Friends', to='Quizz.User'),
        ),
    ]