from django.conf.urls import url, include
from rest_framework import routers

from social import views

router = routers.DefaultRouter()
router.register(r'activities', views.TypeActivityViewSet)
router.register(r'all-users', views.UserViewSet)
router.register(r'type-relationships', views.RelationshipsViewSet)
router.register(r'relationships', views.UserRelationshipViewSet)
router.register(r'all-posts', views.PostViewSet)
router.register(r'locations', views.LocationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^check', views.AuthUser.as_view()),
    url(r'^friends', views.FriendsList.as_view()),
    url(r'^users', views.UserList.as_view()),
    url(r'^posts', views.PostList.as_view()),
    url(r'^follow', views.Follow.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
