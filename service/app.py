# Layer for MongoDbLayer
from models.user import User

# Layer for DatabaseLayer
from models.client import Client


def lambda_handler(event, context):

    # Call function in models 
    print(User.search_user())

    print('\n-----------------\n')

    # Call function in models
    for item in Client.get_all_clientes():
        print(item)

    return {
        'statusCode': 200,
    }
