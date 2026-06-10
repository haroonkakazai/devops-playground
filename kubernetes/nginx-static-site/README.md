# Kubernetes Static Website Deployment

This project demonstrates how to containerize and deploy a simple static website using Docker and Kubernetes.

## Project Overview

The application consists of:

- HTML page
- CSS styling
- Docker container
- Kubernetes Deployment
- Kubernetes Service

The website is served using Nginx inside a Docker container.

---

## Project Structure
nginx-static-site/
├── Dockerfile
├── index.html
├── style.css
├── deployment.yaml
├── service.yaml
└── README.md

## Docker Build
Build the Docker image: docker build -t my-app .
Verify image: docker images
Run locally: docker run -p 8080:80 my-app
Access: http://localhost:8080

## Kubernetes Deployment
Create Deployment: kubectl apply -f deployment.yaml
Verify Pods: kubectl get pods
Verify Deployment: kubectl get deployments

## Kubernetes Service
Create Service: kubectl apply -f service.yaml
Verify Service: kubectl get services

## Useful Commands
View Pods: kubectl get pods
Describe Pod: kubectl describe pod <pod-name>
View Logs: kubectl logs <pod-name>

## Delete Deployment:
kubectl delete deployment my-app-deployment

Delete Service: kubectl delete service my-app-service
Delete Everything: kubectl delete -f deployment.yaml
kubectl delete -f service.yaml

## Concepts Learned
Docker image creation
Containerizing static websites
Kubernetes Deployments
Kubernetes Services
Pod management
Container orchestration basics
Application exposure through Services
Future Improvements
Use Docker Hub image repository
Add Ingress Controller
Deploy on a cloud Kubernetes cluster
Configure CI/CD pipeline
Add monitoring and logging

Author
Haroon Malik