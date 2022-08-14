from rest_framework import viewsets, status, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
#from rest_condition import Or

from .models import News, User, Comment
from .serializers import CommentsSerializer, NewsSerializer, UserRegistrSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    authentication_classes = [SessionAuthentication,]
    #permissions_classes = (AuthorOrReadOnly,)

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.erros
            return Response(data)
        

class NewsAPIList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)

class NewsAPIRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    
class CommentsAPIList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticated,)

class CommentsAPIRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsOwnerOrReadOnly, )
