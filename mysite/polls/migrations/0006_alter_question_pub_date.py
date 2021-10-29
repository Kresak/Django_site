import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210608_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 8, 17, 46, 40, 977571, tzinfo=utc),
                                       verbose_name='Дата публикации'),
        ),
    ]
