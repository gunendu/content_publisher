# Create your views here.
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from models import Article
from serilizers import ArticleSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the PBPLUS index")

class ArticleList(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ArticleSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                data = request.data
                print("data is==",data)
                Article.objects.create(
                    content=data['content'],
                    author_name=data['author_name'],
                    upvote=data['upvote']
                )
            return Response({"message": "Success Creating Article"})

        except Exception as e:            
            return Response({ 'errors': str(e) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                data = request.data
                article_id = data['article_id']
                article = Article.objects.get(pk=article_id)
                article.upvote += 1
                article.save()

            return Response({"message": "Success Updating Vote"})

        except Exception as e:
            return Response({ 'errors': str(e) }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_queryset(self):
        final_list = list()
        articles_qs = Article.objects.filter().order_by('-upvote')
        for article in articles_qs:
            final_list.append({"content": article.content,"author_name": article.author_name, "upvote": article.upvote})

        return final_list