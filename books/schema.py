from graphene import ObjectType, Schema

# from app.film.graphql.schema import Query as FilmQuery
# from app.film.graphql.schema import Mutation as FilmMutation


class Query(ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = Schema(query=Query, mutation=Mutation)
