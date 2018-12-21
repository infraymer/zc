from rest_framework import viewsets

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from social.models import TypeActivity, User, TypeUserRelationShip, UserRelationship
from social.serializers import TypeActivitySerializer, UserSerializer, TypeUserRelationShipSerializer, \
    UserRelationshipSerializer


class TypeActivityViewSet(viewsets.ModelViewSet):
    queryset = TypeActivity.objects.all()
    serializer_class = TypeActivitySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RelationshipsViewSet(viewsets.ModelViewSet):
    queryset = TypeUserRelationShip.objects.all()
    serializer_class = TypeUserRelationShipSerializer


class UserRelationshipViewSet(viewsets.ModelViewSet):
    queryset = UserRelationship.objects.all()
    serializer_class = UserRelationshipSerializer


class AuthUser(APIView):

    def get(self, requset):
        username = self.request.query_params.get('username', None)
        try:
            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except:
            return Response(data={'detail'}, status=400)

# class FriendsList(APIView):
#
#     def get(self, request):
#
