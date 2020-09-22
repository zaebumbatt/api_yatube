from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, api_all_comments, api_specific_comment

router = DefaultRouter()

router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/posts/<int:post_id>/comments/<int:comment_id>/',
         api_specific_comment
         ),
    path('api/v1/posts/<int:post_id>/comments/', api_all_comments),
    path('api/v1/', include(router.urls)),
]
