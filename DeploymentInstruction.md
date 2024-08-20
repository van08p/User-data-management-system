# Deployment Instructions

## Prerequisites
- AWS IAM permissions for Lambda, DynamoDB, and API Gateway.

## Deploy Lambda Functions
1. Go to the AWS Lambda Console.
2. Create a new Lambda function for each of the following:
   - Add User
   - Search User

## Set Up API Gateway
1. Go to the API Gateway Console.
2. Create a new API.
3. Add resources and methods (POST for Add User, GET for Search User, etc.).
4. Integrate each method with the corresponding Lambda function.
5. Deploy the API to a stage (e.g., `prod`).

## Testing
- Use Postman or CURL to test the endpoints.
- Verify that responses are as expected and troubleshoot any issues.
