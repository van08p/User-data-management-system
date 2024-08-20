# API Gateway setup

## Prerequisite
- AWS account 
- Required permission for lambda and dynamodb

## Steps for API gateway setup

### 1. Create API
- Go to AWS Management Console and navigate to API Gateway
- Click on "Create API" button
- Choose "REST API" and click on "Build" button
- Enter API name: UserDataManagementAPI and API endpoint type: Regional
- Click on Create API

### 2. Create resources and methods
1. **Add Resources:**
- Select API you created and Select "Create Resource"
- Enter resource path (eg. addUser, searchUser)
- Click on "Create Resource"

2. **Add Methods:**
- Select resource you created and click on "Create Method"
- Choose HTTP method (eg. POST)
- Configure integration type
- Integration Type: Lambda Function
- Lambda Function: Enter the name of the Lambda function (e.g., `AddUserFunction`).
- Click on "Save" button
- Repeat this step for other resources and methods (e.g., searchUser)

### 3. Deploy API
- Click on "Actions" and select "Deploy API".
- Create a new Stage, Stage Name: `prod` (or another name as desired)
- Click "Deploy".


## Example

### POST `/addUser`
- Request Body:
  ```json
  {
    "UserID": "12345",
    "Name": "John Doe",
    "Skills": ["Python", "AWS"],
    "Company": "CrackCode",
    "Domain": "Backend"
  }


- ## Response
  ```json
  {
  "statusCode": 200,
  "body": "\"User added successfully!\""
  }


### GET `/searchUser`
- Request Body:
  ```json
  {
    "queryStringParameters": {
        "Skills": "Python"
    }
  }

- ## Response
  ```json
  {
    "statusCode": 200,
    "body": "[{\"UserID\": \"12345\", \"Domain\": \"Backend\", \"Company\": \"CrackCode\", \"Skills\": [\"Python\", \"AWS\"], \"Name\": \"John Doe\"}]"
  }
