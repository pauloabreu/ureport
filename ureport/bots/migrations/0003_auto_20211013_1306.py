# Generated by Django 3.2.6 on 2021-10-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bots", "0002_auto_20211007_1243"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bot",
            name="deeplink",
        ),
        migrations.AddField(
            model_name="bot",
            name="facebook_deeplink",
            field=models.URLField(blank=True, help_text="The Facebook bot deeplink, optional", null=True),
        ),
        migrations.AddField(
            model_name="bot",
            name="telegram_deeplink",
            field=models.URLField(blank=True, help_text="The Telegram bot deeplink, optional", null=True),
        ),
        migrations.AddField(
            model_name="bot",
            name="viber_deeplink",
            field=models.URLField(blank=True, help_text="The Viber bot deeplink, optional", null=True),
        ),
        migrations.AddField(
            model_name="bot",
            name="whatsapp_deeplink",
            field=models.URLField(blank=True, help_text="The WhatsApp bot deeplink, optional", null=True),
        ),
        migrations.AlterField(
            model_name="bot",
            name="featured",
            field=models.BooleanField(
                default=False,
                help_text="Whether this bot is displayed on the homepage, up to 3 only with the highest priorities are displayed",
            ),
        ),
    ]
