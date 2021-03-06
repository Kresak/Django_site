import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 6, 7, 9, 53, 41, 918320, tzinfo=utc),
                                                  verbose_name='Дата публикации')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
