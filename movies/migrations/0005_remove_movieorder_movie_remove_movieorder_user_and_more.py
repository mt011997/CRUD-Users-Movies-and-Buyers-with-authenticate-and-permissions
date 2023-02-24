# Generated by Django 4.1.7 on 2023-02-21 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0004_movieorder"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movieorder",
            name="movie",
        ),
        migrations.RemoveField(
            model_name="movieorder",
            name="user",
        ),
        migrations.AddField(
            model_name="movieorder",
            name="movie",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_movie",
                to="movies.movie",
            ),
        ),
        migrations.AddField(
            model_name="movieorder",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_movie",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]