from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveUpdateAPIView
from post.models import Post
from post.api.seriliazers import PostSerializers, PostUpdateCreateSerializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated


#! CRUD views
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetailAPIView(RetrieveAPIView):  # ekrana yazı getirme
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    # slug a göre detaya git
    lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = 'slug'

#  güncelleme bilgileri ekrana önceki değerleri gelmeyebilir
# class PostUpdateAPIView(UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostUpdateCreateSerializers
#     lookup_field = 'slug'

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializers
    lookup_field = 'slug'
    # kullanıcı kendi kaydı ise buaraya girebilimeli
    def perform_update(self, serializer): # hangi user'ın id si onu bil 
        serializer.save(modified_by_user = self.request.user)

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateCreateSerializers
    permission_classes = [IsAuthenticated] # üye girişi yapan kişi create yapsın 
    def perform_create(self, serializer): # hangi user'ın id si onu bil 
        serializer.save(user = self.request.user)


#! permission views

