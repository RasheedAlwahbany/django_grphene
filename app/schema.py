from typing import Type
import graphene
from graphene_django import DjangoObjectType
from .models import Books

class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields=('id','title','desc','created_at')
            
class Query(graphene.ObjectType):
    all_books=graphene.List(BooksType)

schema = graphene.Schema(query=Query)