from dateutil import parser
from django.core.management.base import BaseCommand, CommandError
from feed.models import Feed, Item
from django.utils import timezone
from django.utils.html import escape
import feedparser

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Crawl through all the feeds and collect new items'

    def handle(self, *args, **options):
        for feed in Feed.objects.all():
            try:
                source = feedparser.parse(feed.url)
            except Exception as e:
                logger.debug('Failed to fetch feed {} because'.format(feed.name, str(e)))

            for entry in source.entries:
                try:
                    created_date = entry.published if entry.published else entry.created # if none of these criteria applies what the fuck fix your invalid garbage rss feed
                    created_date = parser(created_date)
                except Exception:
                    created_date = timezone.now()

                item, created = Item.objects.get_or_create(feed=feed, url=entry.link, created=created_date, last_updated=timezone.now(), content=escape(entry.summary_detail.value))
                logger.debug('{} item with link {} on {}'.format('Created' if created else 'Updated', item.url, item.last_updated))
