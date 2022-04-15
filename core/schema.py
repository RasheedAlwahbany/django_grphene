import graphene

import app.schema

class Query(
    app.schema.Query, # Add your Query objects here
    graphene.ObjectType
):
    pass

class Mutation(
    app.schema.Mutation, # Add your Mutation objects here
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)