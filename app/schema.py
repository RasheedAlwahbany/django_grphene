from typing import Type
from venv import create
import graphene
from graphene_django import DjangoObjectType
from .models import Books

class BooksType(DjangoObjectType):
    
    class Meta:
        model = Books
        fields=('id','title','desc','created_at')
            
class Query(graphene.ObjectType):
    all_books=graphene.List(BooksType,name='all_books')
    by_name=graphene.Field(BooksType)
    
    def resolve_all_books(self, info,**args):
        return Books.objects.get(pk=args.get('id'))
    
    def resolve_by_name(self, info):
        return Books.objects.get(title='Book 1')




class createBooks(graphene.Mutation):
    class arguments:
        title=graphene.String()
        desc=graphene.String()
    book=graphene.Field(BooksType)
    
    def mutate(self,info,**args):
        book=BooksType(title=args.get('title'),desc=args.get('desc'))
        return createBooks(BooksType=book)
    class Meta:
        fields=('id','title','desc','created_at')


class Mutation(graphene.ObjectType):
    create_book=createBooks.Field()
    update_book=createBooks.Field()
    delete_book=createBooks.Field()
   
    create_book=graphene.Field(BooksType,title=graphene.String(),desc=graphene.String())
    update_book=graphene.Field(BooksType,id=graphene.Int(),title=graphene.String(),desc=graphene.String())
    delete_book=graphene.Field(BooksType,id=graphene.Int())
    
    def resolve_create_book(self,info,**kwargs):
        title=kwargs.get('title')
        desc=kwargs.get('desc')
        book=Books(title=title,desc=desc)
        book.save()
        return book
    
    def resolve_update_book(self,info,**kwargs):
        id=kwargs.get('id')
        title=kwargs.get('title')
        desc=kwargs.get('desc')
        book=Books.objects.get(id=id)
        book.title=title
        book.desc=desc
        book.save()
        return book
    
    def resolve_delete_book(self,info,**kwargs):
        id=kwargs.get('id')
        book=Books.objects.get(id=id)
        book.delete()
        return book    

schema = graphene.Schema(query=Query,mutation=Mutation)