from rest_framework import serializers


class studentserializer(serializers.Serializer):
    id= serializers.IntegerField()
    name=serializers.CharField(max_length=50)
    Class=serializers.IntegerField()
    age= serializers.IntegerField()
    city=serializers.CharField(max_length=50)