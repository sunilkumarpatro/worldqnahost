# Generated by Django 5.0.1 on 2024-02-09 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('msg', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qna',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('showhide', models.CharField(choices=[('hide', 'hide'), ('show', 'show')], default='hide', max_length=20)),
                ('question_image', models.FileField(blank=True, max_length=250, null=True, upload_to='question/')),
                ('facebook_image', models.FileField(blank=True, max_length=250, null=True, upload_to='facebook/')),
                ('twitter_image', models.FileField(blank=True, max_length=250, null=True, upload_to='twitter/')),
                ('slug', models.TextField()),
                ('english_title_question', models.TextField()),
                ('hindi_title_question', models.TextField()),
                ('spanish_title_question', models.TextField()),
                ('chinese_title_question', models.TextField()),
                ('arabic_title_question', models.TextField()),
                ('portuguese_title_question', models.TextField()),
                ('russian_title_question', models.TextField()),
                ('french_title_question', models.TextField()),
                ('japanese_title_question', models.TextField()),
                ('german_title_question', models.TextField()),
                ('english_descripton', models.TextField()),
                ('hindi_descripton', models.TextField()),
                ('spanish_descripton', models.TextField()),
                ('chinese_descripton', models.TextField()),
                ('arabic_descripton', models.TextField()),
                ('portuguese_descripton', models.TextField()),
                ('russian_descripton', models.TextField()),
                ('french_descripton', models.TextField()),
                ('japanese_descripton', models.TextField()),
                ('german_descripton', models.TextField()),
                ('english_keyword', models.TextField()),
                ('english_answer', models.TextField()),
                ('hindi_answer', models.TextField()),
                ('spanish_answer', models.TextField()),
                ('chinese_answer', models.TextField()),
                ('arabic_answer', models.TextField()),
                ('portuguese_answer', models.TextField()),
                ('russian_answer', models.TextField()),
                ('french_answer', models.TextField()),
                ('japanese_answer', models.TextField()),
                ('german_answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('showhide', models.CharField(choices=[('hide', 'hide'), ('show', 'show')], default='hide', max_length=20)),
                ('english_comment', models.TextField()),
                ('hindi_comment', models.TextField()),
                ('spanish_comment', models.TextField()),
                ('chinese_comment', models.TextField()),
                ('arabic_comment', models.TextField()),
                ('portuguese_comment', models.TextField()),
                ('russian_comment', models.TextField()),
                ('french_comment', models.TextField()),
                ('japanese_comment', models.TextField()),
                ('german_comment', models.TextField()),
                ('qna_catagary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.qna')),
            ],
        ),
        migrations.CreateModel(
            name='Related',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('english_question', models.TextField()),
                ('hindi_question', models.TextField()),
                ('spanish_question', models.TextField()),
                ('chinese_question', models.TextField()),
                ('arabic_question', models.TextField()),
                ('portuguese_question', models.TextField()),
                ('russian_question', models.TextField()),
                ('french_question', models.TextField()),
                ('japanese_question', models.TextField()),
                ('german_question', models.TextField()),
                ('english_answer', models.TextField()),
                ('hindi_answer', models.TextField()),
                ('spanish_answer', models.TextField()),
                ('chinese_answer', models.TextField()),
                ('arabic_answer', models.TextField()),
                ('portuguese_answer', models.TextField()),
                ('russian_answer', models.TextField()),
                ('french_answer', models.TextField()),
                ('japanese_answer', models.TextField()),
                ('german_answer', models.TextField()),
                ('url', models.TextField()),
                ('qna_catagary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.qna')),
            ],
        ),
    ]
