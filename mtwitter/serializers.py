from rest_framework import serializers
from . import models
# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types.

class TwitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TwitterData
        fields = ('screen_name', 'tweet', 'date','favCount')

