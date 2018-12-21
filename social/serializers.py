from rest_framework import serializers

from social.models import TypeActivity, User, TypeUserRelationShip, UserRelationship


class TypeActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeActivity
        fields = ('name', 'rating', 'icon')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'fullname', 'email', 'updated_at', 'created_at', 'image', 'is_active')


class TypeUserRelationShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeUserRelationShip
        fields = ('id', 'name')


class UserRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRelationship
        fields = ('user_first', 'user_second', 'type', 'timestamp')
