import django
from django.db.models import Manager
from django.db.models.query import QuerySet


# query
def cached_as(sample, timeout=None, extra=None):
    return lambda func: func

def install_cacheops():
    if django.VERSION < (1, 6):
        Manager.get_queryset = lambda self: self.get_query_set()

    # query
    QuerySet._cache_key = lambda self, extra=None: None
    QuerySet.nocache = lambda self: self
    QuerySet.cache = lambda self: self
    QuerySet.inplace = lambda self: self
    Manager.nocache = lambda self: self.get_queryset().nocache()
    Manager.cache = lambda self: self.get_queryset().cache()
    Manager.inplace = lambda self: self.get_queryset().inplace()


# invalidation
def invalidate_obj(obj):
    pass

def invalidate_model(model):
    pass

def invalidate_all():
    pass


# simple
from cacheops.simple import BaseCache, CacheMiss

class DummyCache(BaseCache):
    def get(self, cache_key):
        raise CacheMiss

    def set(self, cache_key, data, timeout=None):
        pass

    def delete(self, cache_key):
        pass

cache = DummyCache()
cached = cache.cached
file_cache = DummyCache()
