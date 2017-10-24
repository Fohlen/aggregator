from django.core.management import BaseCommand, CommandError
from django.conf import settings
from feed.models import Feed
import requests

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Loads all feeds from the feeds definition file"

    def handle(self, *args, **options):
        try:
            r = requests.get(settings.FEED_URL)
            feeds_config = r.json()
        except Exception as e:
            pass

        for key in feeds_config:
            feed, created = Feed.objects.get_or_create(name=key, url=feeds_config[key])

            logger.debug('{} feed with link {} on {}'.format('Created' if created else 'Updated', feed.url, feed.created))
