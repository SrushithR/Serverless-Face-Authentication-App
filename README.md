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

`aws rekognition create-collection --region us-west-2 --collection-id bookmycab-collection`

Save the collection-id, it will be used in the input of the step function. Make sure you chose a region where is Rekognition is supported.

2. Deploy the Cloud Formation template

Use the AWS console or CLI to deploy the Cloud Formation template which will create the necessary S3 buckets, lambda functions and IAM roles.

CLI commands to deploy the template:

Create an S3 bucket to upload all the local artifacts:

```bash
aws s3api create-bucket --bucket face-authentication --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2

aws cloudformation package --s3-bucket face-authentication --region us-west-2 --template ./setup.yaml --output-template-file setup-sam-transformed-us-west-2.yaml

aws cloudformation deploy --template-file ./setup-sam-transformed-us-west-2.yaml --stack-name face-authentication-app --capabilities CAPABILITY_IAM --region us-west-2
```

3. Create step functions

Use the AWS Console (https://us-west-2.console.aws.amazon.com/states/home?region=us-west-2#/statemachines) to create a step function with the definition defined in the face_detection_step_fn_3.json file inside the step-functions folder.

### Testing the step function

We are all set test our face authentication app! Perform the following steps:

1. Use any of the images under the `sample-images` folder and upload the `BookMyCabS3Bucket` bucket that was created using the cloud formation template.
2. Head over the step functions service in the AWS console and select the newly created step function. Click on the `Start Execution` button with the following as the input:

```json
{
  "file_name": "scarlett.jpg",
  "collection_id": "bookmycab-collection",
  "user_id": "scarlett"
}
```

- The file_name should be the same as the file uploaded in step 1
- The collection id is the id of the rekognition collection created
- user_id is used for indexing the face detected in the image uploaded

### Cleaning Up

Make sure to delete the resources that were created. You can delete the cloud formation stack using the following command:

```bash
aws cloudformation delete-stack --stack-name face-authentication-app --region us-west-2
```

References:

1.  https://github.com/aws-samples/aws-serverless-workshops/tree/master/ImageProcessing
2.  https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html
3.  https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html
4.  https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html
