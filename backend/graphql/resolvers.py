import graphene
from auth.keycloak import Keycloak
from backend.app import Todo

class AddTodo(graphene.Mutation):
    # Define mutation input fields
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        time = graphene.String(required=True)

    # Define mutation output fields
    todo = graphene.Field(Todo)

    # Mutation resolver function
    def mutate(self, info, title, description, time):
        keycloak_instance = Keycloak()  # Assuming Keycloak class needs no instance initialization
        keycloak_instance.require_keycloak_token()
        
        # Implement todo creation logic here and replace created_todo with the actual result
        created_todo = {}  # Placeholder for the created todo
        
        # Return the created todo
        return AddTodo(todo=created_todo)
