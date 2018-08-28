from rest_framework import serializers
from .models import *

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class ArticleSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Inventory objects."""
    content = serializers.CharField()
    author_name = serializers.CharField()
    upvote = serializers.IntegerField()

    class Meta:
        model = Article
        fields = ('content','author_name','upvote')
    