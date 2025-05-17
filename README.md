# 🚀 Iris Classifier API on Kubernetes

This is a simple machine learning project that serves an Iris classifier using **FastAPI**, containerized with **Docker**, and deployed to **Kubernetes** using **Kind (Kubernetes in Docker)**.

---

## ✅ What This Project Shows

- Building an ML API with FastAPI
- Containerizing the app using Docker
- Deploying to Kubernetes with Kind
- Exposing the service using NodePort
- Testing the API via Swagger UI

---

## ⚙️ How to Run

1. **Build Docker Image**
   ```bash
   docker build -t iris-api:local .

2. **Start Kind Cluster**
    ```bash
    kind create cluster
    kind load docker-image iris-api:local

3. **Deploy to Kubernetes**
    ```bash
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
4. **Access the API**
    ```bash
    kubectl port-forward svc/iris-api-service 8000:80

    Open: http://localhost:8000/docs for the FastAPI Swagger UI.


## 📦 Files in This Repo

- main.py – FastAPI app with ML model

- train_model.py – ML model Training

- requirements.txt – Python dependencies

- Dockerfile – For building the Docker image

- deployment.yaml – Kubernetes deployment config

- service.yaml – Kubernetes service config


#### 🙌 Thanks for Visiting!

Feel free to clone, test, or build upon this project.