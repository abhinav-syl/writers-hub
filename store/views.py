from django.shortcuts import render

# Create your views here.

from .models import Author, Article
from .serializers import AuthorSerializer, ArticleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from django.template import loader  
# Create your views here.  
from django.http import HttpResponse  
import os


def pages(request, title):
    template = loader.get_template(title + '.html')
    return HttpResponse(template.render())


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


class ArticleApiView(APIView):
    # add permission to check if user is authenticated
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'Title': request.data.get('Title'),
            'Heading': request.data.get('Heading'),
            # 'user': request.user.id
            'para': request.data.get('para'),
            'author': request.data.get('author'),
        }

        print(data)

        html = '''
            <html>
            <head>
            <title>''' + data['Title'] + '''
            </title>
            </head>
            <body> ''' + data['para'] + '''
            </body>
            </html>
            '''
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        # f = open('templates/' + data['Title'] + '.html', "w")
        f = open(os.path.join(__location__, 'templates/' + data['Title'] + '.html'), 'w')
        f.write(html)
        f.close()

        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorApiView(APIView):
    # add permission to check if user is authenticated
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        authors = Author.objects.all()
        serializer = ArticleSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'last_name': request.data.get('last_name'),
            'first_name': request.data.get('first_name'),
        }

        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleSpecificApiView(APIView):
    # add permission to check if user is authenticated
    # 1. List all
    def get(self, request, title, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        print('title---------------- =  ', title)
        articles = Article.objects.filter(Title=title)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorSpecificApiView(APIView):
    # add permission to check if user is authenticated
    # 1. List all
    def get(self, request, first_name, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        authors = Author.objects.filter(first_name=first_name)
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)