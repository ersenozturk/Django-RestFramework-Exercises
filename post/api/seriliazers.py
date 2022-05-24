from rest_framework import serializers
from post.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =[
            'user', 'title', 'content','image', 'slug', 'created', 'modified_by_user'
        ]
        
# slug ve created models.py içinde editable=false olduğu için updateve create işlemleri için yeni bir serializers tanımlandı
class PostUpdateCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =[
            'title', 'content', 'image', 
        ]