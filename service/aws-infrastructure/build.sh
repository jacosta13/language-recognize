#!/bin/bash

# Import environment variables
source .env
source ../../.env

# Copy template to S3
export S3_TEMPLATE_LOC=infrastructure/ecs-deploy.yml
aws s3 cp ecs-deploy.yml s3://$S3_BUCKET/$S3_TEMPLATE_LOC

# Launch stack
aws cloudformation create-stack --stack-name language-recognize-stack \
    --template-url https://s3.amazonaws.com/$S3_BUCKET/$S3_TEMPLATE_LOC \
    --capabilities "CAPABILITY_NAMED_IAM" \
    --parameters ParameterKey=DockerImage,ParameterValue=$DOCKER_IMG ParameterKey=SubnetID,ParameterValue=$SUBNET_ID
