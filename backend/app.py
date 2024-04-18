from flask import Flask
from flask_graphql import GraphQLView
import graphene
from flask_cors import CORS
from auth.keycloak import Keycloak  # Assuming you have implemented this correctly
from backend.graphql.resolvers import AddTodo, DeleteTodo, EditTodo  # Update import path as needed

app = Flask(__name__)
CORS(app)

# Initialize Keycloak
keycloak = Keycloak(app)  # Assuming you have implemented this correctly

# Define GraphQL types
class Todo(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    time = graphene.String()
    image = graphene.String()

# Define GraphQL queries and mutations
class Query(graphene.ObjectType):
    todos = graphene.List(Todo)

class Mutation(graphene.ObjectType):
    add_todo = AddTodo.Field()
    delete_todo = DeleteTodo.Field()  # Assuming you have defined this resolver
    edit_todo = EditTodo.Field()  # Assuming you have defined this resolver

# Define GraphQL schema
schema = graphene.Schema(query=Query, mutation=Mutation)

# Route for GraphQL endpoint
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == "__main__":
    app.run(debug=True)
