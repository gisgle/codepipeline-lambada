import json

def lambda_handler(event, context):
    # Parse the request body as JSON
    request_body = json.loads(event['body'])
    
    # Extract the name and age from the request body
    name = request_body['name']
    age = request_body['age']
    
    # Construct the response body as a JSON object
    response_body = {
        'message': f'Hello, {name}! You are {age} years old.'
    }
    
    # Return the response as a JSON object
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response_body)
    }
