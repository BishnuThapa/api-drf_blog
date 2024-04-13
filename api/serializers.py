from rest_framework.serializers import ModelSerializer
from .models import BlogPost

class BlogPostSerializer(ModelSerializer):
    class Meta:
        model=BlogPost
        fields=['id','title','content','published_date']