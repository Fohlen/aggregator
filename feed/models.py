from django.db import models

class Feed(models.Model):
    name = models.CharField(max_length=200, blank=True)
    url = models.URLField(unique=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    @property
    def last_updated(self):
        """
        When was the last item in this feed updated
        :return: DateTime
        """
        return self.item_set.latest().last_updated if self.item_set.exists() else self.created

class Item(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    url = models.URLField(unique=True)

    created = models.DateTimeField()
    last_updated = models.DateTimeField()

    content = models.TextField()

    @property
    def description(self):
        """
        :return: returns the first 20 words of the content
        """
        fifty_words = self.content.split()[:20]
        return u' '.join(fifty_words)

    class Meta:
        ordering = ['-last_updated', 'created']
        get_latest_by = 'last_updated'
