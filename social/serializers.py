from rest_framework import serializers

from social.models import TypeActivity, User, TypeUserRelationShip, UserRelationship, Post, Location


class TypeActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeActivity
        fields = ('id', 'name', 'rating', 'icon')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'fullname', 'email', 'updated_at', 'created_at', 'image', 'is_active', 'oauth')


class TypeUserRelationShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeUserRelationShip
        fields = ('id', 'name')


class UserRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRelationship
        fields = ('user_first', 'user_second', 'type', 'timestamp')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'latitude', 'longitude')


class PostSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    type = TypeActivitySerializer()
    owner = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'type', 'owner', 'description', 'location', 'image', 'timestamp')
