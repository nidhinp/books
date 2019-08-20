import graphene

from .queries import AuthorType, BookType
from ..models import Author, Book


class AuthorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class BookInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    synopsis = graphene.String()
    author = graphene.Field(AuthorInput)
    published_date = graphene.Date()


class CreateAuthor(graphene.Mutation):
    class Arguments:
        input = AuthorInput(required=True)

    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, input=None):
        author_instance = Author(name=input.name)
        author_instance.save()
        return CreateAuthor(author=author_instance)


class UpdateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = AuthorInput(required=True)

    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, id, input=None):
        author_instance = Author.objects.get(pk=id)
        if author_instance:
            author_instance.name = input.name
            author_instance.save()
            return UpdateAuthor(author=author_instance)
        return UpdateAuthor(author=None)


class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, input=None):
        author = Author.objects.get(pk=input.author.id)
        book_instance = Book(
            title=input.title,
            synopsis=input.synopsis,
            author=author,
            published_date=input.published_date
        )
        book_instance.save()
        return CreateBook(book=book_instance)


class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, id, input=None):
        book_instance = Book.objects.get(pk=id)
        if book_instance:
            book_instance.title = input.title
            book_instance.synopsis = input.synopsis
            book_instance.published_date = input.published_date
            return UpdateBook(book=book_instance)
        return UpdateBook(book=None)


class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
