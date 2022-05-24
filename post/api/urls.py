from django.urls import path

from post.api.views import PostListAPIView, PostDetailAPIView, PostUpdateAPIView, PostDeleteAPIView, PostCreateAPIView

urlpatterns = [
    # path('post/api/', include('post.api.urls'))
    path('list', PostListAPIView.as_view(), name='list'),
    path('detail/<slug>', PostDetailAPIView.as_view(), name='detail'),
    path('update/<slug>', PostUpdateAPIView.as_view(), name='update'),
    path('delete/<slug>', PostDeleteAPIView.as_view(), name='delete'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
]