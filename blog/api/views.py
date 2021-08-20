from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from blog.models import Blog
from .serializers import BlogSerializer


class BlogList(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class BlogDetail(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
