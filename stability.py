import boto3
import json

# Get the string input from the user
user_input = input("Enter a string: ")

# Initialize the Boto3 client or resource as needed (e.g., S3, EC2, etc.)
# Replace 'your_service' with the AWS service you want to use.
# Replace 'your_region' with the AWS region you want to work in.
client = boto3.client('bedrock', region_name='us-east-1')

# Use the user_input in your Boto3 operations
response = client.some_boto3_operation(ParameterName=user_input)

# Create a dictionary with the desired JSON structure
json_data = {
    "text_prompts": [{"text": user_input}],
    "cfg_scale": 10,
    "seed": 0,
    "steps": 50
}

# Save the dictionary to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

# Print the response or perform other actions with it
print("Boto3 Response:", response)
print("JSON data saved to output.json")
