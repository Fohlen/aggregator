from graphene_django import DjangoObjectType
import graphene
from graphene.types import datetime
import feed

class Feed(DjangoObjectType):
    last_updated = datetime.DateTime(source='last_updated')

    class Meta:
        model = feed.models.Feed

class Item(DjangoObjectType):
    description = graphene.String(source='description')

    class Meta:
        model = feed.models.Item

class Query(graphene.ObjectType):
    feed = graphene.Field(Feed, name=graphene.String())
    item = graphene.Field(Item, url=graphene.String())

    feeds = graphene.List(Feed)
    items = graphene.List(Item)



    def resolve_feed(self, *args, **kwargs):
        name = kwargs.pop('name')
        return feed.models.Feed.objects.get(name=name)

    def resolve_item(self, *args, **kwargs):
        url = kwargs.pop('url')
        return feed.models.Item.objects.get(url=url)

    def resolve_feeds(self, *args, **kwargs):
        return feed.models.Feed.objects.all()

    def resolve_items(self, *args, **kwargs):
        return feed.models.Item.objects.all()

schema = graphene.Schema(query=Query)