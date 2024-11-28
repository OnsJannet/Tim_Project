from flask import Blueprint, redirect, jsonify, session, request
from pymongo.errors import CollectionInvalid, OperationFailure
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from itertools import chain
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

# Define db_name or set it to 'TIM_Demo' as default
db_name = "TIM_Demo"

db = client[db_name]



db_bp = Blueprint('db', __name__)


'''@db_bp.route('/current_db', methods=['GET'])
def current_db():
    """Retrieve the currently selected database."""
    db_name = session.get('db_name', 'TIM_Demo')  
    print('inside GET request db_name', db_name)
    return jsonify({'current_db': db_name})'''

current_db_name = 'TIM_Demo'

def get_current_db():
    print("current_db_name", current_db_name)
    return client[current_db_name]


@db_bp.route('/switch_db/<db>', methods=['POST'])
def switch_db(db):
    """Switch to a different database."""
    global current_db_name
    current_db_name = 'TIM_Demo_' + db
    session['db_name'] = current_db_name
    print('Switched to database:', current_db_name)
    return jsonify({'message': f'Switched to database {db} successfully'})



@db_bp.route('/create_db', methods=['POST'])
def create_db():
    print("entered")
    # Extract JSON data from the request body
    request_data = request.get_json()
    db_name = request_data.get('db_name') 
    print('Created database:', db_name)

    print("dbName", db_name)

    """Create a new database."""
    existing_databases = [name.lower() for name in client.list_database_names()]  # Convert to lowercase
    counter = 1

    # If dbName is provided, use it directly
    if db_name:
        new_db_name = 'TIM_Demo_' + db_name.lower()# Convert to lowercase
        print("new_db_name", new_db_name)
    else:
        new_db_name = "TIM_Demo"

    # If the name already exists, generate a new name
    while new_db_name in existing_databases:
        if db_name:  # If a custom db_name was provided, append counter to it
            new_db_name = f"{db_name.lower()}"
        else:  # Otherwise, generate a default name with counter appended
            new_db_name = f"TIM_Demo_{counter}"
        counter += 1

    # Attempt to create a collection in the new database
    try:
        db = client[new_db_name]
        db.create_collection('placeholder_collection')
        
        # Loop through all collections in 'new' database and copy them directly to the new database
        for collection_name in client['new'].list_collection_names():
            new_collection = db[collection_name]
            new_collection.insert_many(client['new'][collection_name].find())
        
    except CollectionInvalid:
        # Collection creation failed, indicating the database already exists
        pass
    return jsonify({'message': f'New database {new_db_name} created successfully'})






@db_bp.route('/delete_db/<db_name>', methods=['DELETE'])
def delete_db(db_name):
    """Delete a database."""
    try:
        client.drop_database(db_name)
        return jsonify({'message': f'Database {db_name} deleted successfully'})
    except OperationFailure as e:
        return jsonify({'error': str(e)}), 400 
    

'''@db_bp.route('/list_databases', methods=['GET'])
def list_databases():
    """List all databases containing 'TIM_Demo'."""
    try:
        all_databases = client.list_database_names()
        matching_databases = [db for db in all_databases if 'TIM_Demo' in db]
        return jsonify({'databases': matching_databases})
    except OperationFailure as e:
        return jsonify({'error': str(e)}), 400  '''




@db_bp.route('/list_databases', methods=['GET'])
def list_databases():
    """List databases containing 'TIM_Demo', 'TIM_Demo_1', and 'TIM_Demo_2', but not 'TIM_Demo_new'."""
    try:
        all_databases = client.list_database_names()
        matching_databases = [db.split('TIM_Demo_')[-1] for db in all_databases if db.startswith('TIM_Demo') and db != 'TIM_Demo_new']
        
        # Add 'new' at the top if 'TIM_Demo_new' exists
        if 'TIM_Demo_new' in all_databases:
            matching_databases = list(chain(['new'], matching_databases))
        
        return jsonify({'databases': matching_databases})
    except OperationFailure as e:
        return jsonify({'error': str(e)}), 400


