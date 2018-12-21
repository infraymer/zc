from django.conf.urls import url, include
from rest_framework import routers

from social import views

router = routers.DefaultRouter()
router.register(r'activities', views.TypeActivityViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'type-relationships', views.RelationshipsViewSet)
router.register(r'relationships', views.UserRelationshipViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^check', views.AuthUser.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
