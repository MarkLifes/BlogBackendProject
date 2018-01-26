# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-26 02:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('material', '0008_auto_20180112_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_content', models.TextField(help_text='原始内容', verbose_name='原始内容')),
                ('formatted_content', models.TextField(help_text='处理后内容', verbose_name='处理后内容')),
            ],
            options={
                'verbose_name': '图书详情',
                'verbose_name_plural': '图书详情列表',
            },
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('postbaseinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='material.PostBaseInfo')),
                ('douban_id', models.CharField(blank=True, help_text='豆瓣资源类型', max_length=255, null=True, verbose_name='豆瓣资源类型')),
                ('douban_type', models.CharField(blank=True, help_text='豆瓣资源ID', max_length=255, null=True, verbose_name='豆瓣资源ID')),
                ('isbn10', models.CharField(blank=True, help_text='isbn10', max_length=255, null=True, verbose_name='isbn10')),
                ('isbn13', models.CharField(blank=True, help_text='isbn13', max_length=255, null=True, verbose_name='isbn13')),
                ('book_name', models.CharField(blank=True, help_text='书名', max_length=255, null=True, verbose_name='书名')),
                ('book_author', models.CharField(blank=True, help_text='本书作者', max_length=255, null=True, verbose_name='本书作者')),
                ('publisher', models.CharField(blank=True, help_text='出版社', max_length=255, null=True, verbose_name='出版社')),
                ('pages', models.CharField(blank=True, help_text='总页数', max_length=20, null=True, verbose_name='总页数')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书列表',
            },
            bases=('material.postbaseinfo',),
        ),
        migrations.CreateModel(
            name='BookNoteDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_content', models.TextField(help_text='原始内容', verbose_name='原始内容')),
                ('formatted_content', models.TextField(help_text='处理后内容', verbose_name='处理后内容')),
            ],
            options={
                'verbose_name': '图书笔记详情',
                'verbose_name_plural': '图书笔记详情列表',
            },
        ),
        migrations.CreateModel(
            name='BookNoteInfo',
            fields=[
                ('postbaseinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='material.PostBaseInfo')),
            ],
            options={
                'verbose_name': '图书笔记',
                'verbose_name_plural': '图书笔记列表',
            },
            bases=('material.postbaseinfo',),
        ),
        migrations.CreateModel(
            name='BookResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('download', models.FileField(upload_to='course/resource/%Y/%m', verbose_name='资源文件')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookInfo', verbose_name='图书')),
            ],
            options={
                'verbose_name': '图书资源',
                'verbose_name_plural': '图书资源',
            },
        ),
        migrations.CreateModel(
            name='BookChapter',
            fields=[
                ('booknoteinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='book.BookNoteInfo')),
            ],
            options={
                'verbose_name': '章节',
                'verbose_name_plural': '章节',
            },
            bases=('book.booknoteinfo',),
        ),
        migrations.CreateModel(
            name='BookSection',
            fields=[
                ('booknoteinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='book.BookNoteInfo')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookChapter', verbose_name='章节')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
            },
            bases=('book.booknoteinfo',),
        ),
        migrations.AddField(
            model_name='booknotedetail',
            name='book_note_info',
            field=models.OneToOneField(blank=True, help_text='内容', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='book.BookNoteInfo', verbose_name='内容'),
        ),
        migrations.AddField(
            model_name='bookdetail',
            name='book_info',
            field=models.OneToOneField(blank=True, help_text='内容', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='book.BookInfo', verbose_name='内容'),
        ),
    ]
