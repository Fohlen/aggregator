import datetime
from django.test import TestCase
from django.db.utils import IntegrityError
from django.utils import timezone
from .models import Feed, Item

class FeedTestCase(TestCase):
    def test_creation(self):

        test_feed = Feed.objects.create(name='test', url='https://www.test.de/rss/alles/')
        now_date = timezone.now()
        self.assertAlmostEqual(test_feed.created, now_date, datetime.timedelta(seconds=2))

        with self.assertRaises(IntegrityError):
            Feed.objects.create(name='a', url=None) # no empty feeds

class ItemTestCase(TestCase):
    def setUp(self):
        self.feed = Feed.objects.create(name='test', url='https://www.test.de/rss/alles/')

    def test_creation(self):

        test_item = Item.objects.create(feed=self.feed, url='https://www.test.de/rss/alles/', content=\
        'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.')

        self.assertEqual(test_item.description, 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam') # only 20 words preview

        with self.assertRaises(IntegrityError):
            Item.objects.create(feed=self.feed, url='https://www.test.de/rss/alles/', content= \
            'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.') # URL is unique
