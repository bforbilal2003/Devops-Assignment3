#!/bin/bash

echo "Initializing Terraform..."
terraform init

echo "Applying Terraform Configuration..."
terraform apply -auto-approve

echo "Building Docker Image..."
docker build -t bilalaslam/Devops-Assignment4:latest ./app

echo "Pushing Docker Image to Docker Hub..."
dcoker push bilalaslam/Devops-Assignment4:latest

echo "Deployment Complete!"
