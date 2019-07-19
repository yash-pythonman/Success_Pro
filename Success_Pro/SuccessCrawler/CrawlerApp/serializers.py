from rest_framework import serializers
from .models import *


class BaseUrlSerializers(serializers.ModelSerializer):
    class Meta:
        model = BaseUrl
        fields = '__all__'


class PageUrlSerializers(serializers.ModelSerializer):
    class Meta:
        model = PageUrl
        fields = '__all__'


class SubPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPage
        fields = '__all__'


class BaseUrlImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUrlImages
        fields = '__all__'


class PageImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageImages
        fields = '__all__'


class UrlDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlDepth
        fields = '__all__'