from rest_framework.response import Response
from rest_framework.views import APIView
from articles.models import Article
from articles.serializers import ArticleSerializer,ArticlePostSerializer

# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = ArticlePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)