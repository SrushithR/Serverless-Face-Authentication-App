# Serverless Face Authentication App 
A simple serverless app to authenticate/verify user signups using selfies

### Description

The BookYourCab team wants to add a new feature by requiring riders to upload a selfie after signing up. This accomplishes a few things:

1. Prevents the same user from signing up for multiple accounts and prevent from using new-user sign up promotions
2. Allows users to easily identify the rider during pickup to provide a good customer experience. This also enhances security so bad guys can't spoof to be riders

In this workshop, we will build a serverless face authentication/verification system using the following AWS services - Lambda, Rekognition, Step functions, S3, API Gateway and Dynamo DB.

### Implementation Instructions:

1. Create a Rekognition collection:

Sample CLI command to create a collection in Rekognition:

`
  aws rekognition create-collection --region us-west-2 --collection-id rider-photos
`

Make sure you chose a region where is Rekognition is supported.

2. Deploy the CloudFormation template

Use the AWS console or CLI to deploy the CloudFormation template which will create the necessary S3 buckets, lambda functions and IAM roles.

CLI commands to deploy the template:

Create an S3 bucket to upload all the local artifacts:

    aws s3api create-bucket --bucket rekognition-meetup --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2

    aws cloudformation package --s3-bucket srushith-codeops-konfhub --region us-west-2 --template ./setup.yaml --output-template-file setup-sam-transformed-us-west-2.yaml

    aws cloudformation deploy --template-file ./setup-sam-transformed-us-west-1.yaml --stack-name face-authentication-app --capabilities CAPABILITY_IAM --region us-west-1

3. Create step functions

Create step functions using the JSON files in the folder step-functions.

References:
 1. https://github.com/aws-samples/aws-serverless-workshops/tree/master/ImageProcessing
 2. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html
 3. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html
 4. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html
 
 
