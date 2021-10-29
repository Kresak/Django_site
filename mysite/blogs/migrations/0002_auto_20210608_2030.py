import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 8, 17, 30, 38, 19148, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
    ]
