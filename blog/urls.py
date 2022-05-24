from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('post/api/', include('post.api.urls'))
    path('post/api/', include('post.api.urls'))
]