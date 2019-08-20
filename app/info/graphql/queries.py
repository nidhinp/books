import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from ..models import Author, Book


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(ObjectType):
    author = graphene.Field(AuthorType, id=graphene.Int())
    book = graphene.Field(BookType, id=graphene.Int())
    authors = graphene.List(AuthorType)
    books = graphene.List(BookType)
    author_search = graphene.List(AuthorType, string=graphene.String())

    def resolve_author(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Author.objects.get(pk=id)

        return None

    def resolve_book(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Book.objects.get(pk=id)

        return None

    def resolve_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_author_search(self, info, **kwargs):
        string = kwargs.get("string", "")
        return Author.objects.filter(name__icontains=string)
