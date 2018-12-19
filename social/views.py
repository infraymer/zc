from rest_framework import viewsets

# Create your views here.
from social.models import TypeActivity, User
from social.serializers import TypeActivitySerializer, UserSerializer


class TypeActivityViewSet(viewsets.ModelViewSet):
    queryset = TypeActivity.objects.all()
    serializer_class = TypeActivitySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
