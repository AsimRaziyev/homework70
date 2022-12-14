
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

# Create your views here.
from webapp.models import Article
from api_v2.serializers import ArticleSerializer


class ArticleView(APIView):
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        articles_data = self.serializer_class(articles, many=True).data
        return Response(articles_data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def put(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=article)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response({
            "message": "Статья `{}` была удалена.".format(pk)
        }, status=204)


class ArticleDetail(APIView):
    serializer_class = ArticleSerializer

    def get(self, request, *args, pk, **kwargs):
        try:
            article = Article.objects.get(pk=pk)
            article_data = self.serializer_class(article).data
            return Response(article_data)
        except:
            return Response({
                "message": "Статья не найдена."
            }, status=404)
