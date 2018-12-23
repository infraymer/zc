from django.db.models import Q
from rest_framework import viewsets

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from social.models import TypeActivity, User, TypeUserRelationShip, UserRelationship, Post, Location
from social.serializers import TypeActivitySerializer, UserSerializer, TypeUserRelationShipSerializer, \
    UserRelationshipSerializer, PostSerializer, LocationSerializer


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


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class AuthUser(APIView):

    def get(self, requset):
        username = self.request.query_params.get('user', None)
        try:
            user = User.objects.get(user=username)
            serializer = UserSerializer(user)
            return Response({'created': True, 'data': serializer.data})
        except:
            return Response({'created': False, 'data': None})


class FriendsList(APIView):

    def get(self, request):
        username = self.request.query_params.get('user', None)
        user = User.objects.get(username=username)
        rel = user.owner.all()
        friends = [r.user_second for r in rel]
        return Response(UserSerializer(friends, many=True).data)


class UserList(APIView):

    def get(self, _):
        user = self.request.query_params.get('user', None)
        query = self.request.query_params.get('query', None)

        user_queryset = User.objects.get(username=user)

        queryset = User.objects.exclude(username=user).filter(username__contains=query)
        users = UserSerializer(queryset, many=True).data

        q = [r.user_second for r in user_queryset.owner.all()]
        friends = UserSerializer(q, many=True).data

        friends_ids = [f['id'] for f in friends]

        for user in users:
            if user['id'] in friends_ids:
                user['is_follow'] = True
            else:
                user['is_follow'] = False

        return Response(users)


class Follow(APIView):

    def post(self, _):
        id = self.request.query_params.get('id', None)
        data = self.request.data

        follow = data['follow']
        user_id = data['user_id']

        if follow:
            UserRelationship.objects.create(
                user_first_id=id,
                user_second_id=user_id,
                type_id=1)
        else:
            rel = UserRelationship.objects.get(
                user_first_id=id,
                user_second_id=user_id)
            rel.delete()
        return Response()


class PostList(APIView):

    def get(self, _):
        pk = self.request.query_params.get('id', None)

        user = User.objects.get(pk=pk)
        posts = Post.objects.filter(Q(owner__dependent__in=user.owner.all()) | Q(owner=user))

        return Response(PostSerializer(posts, many=True).data)
