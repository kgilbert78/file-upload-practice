from rest_framework import serializers
from .models import FileWithKeywords, Keyword


class FileWithKeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileWithKeywords
        fields = [
            "id",
            "keyword_doc",
            "keyword",
        ]
        depth = 1  # nests Keyword data in json response, instead of just id


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ["id", "associated_keyword"]