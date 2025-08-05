# 📌 Predictive Maintenance Pipeline

## 📖 Project Overview

This project demonstrates a **real-world MLOps + DevOps solution** for predictive maintenance. It focuses on predicting whether an industrial machine will fail soon based on its operating conditions. The solution uses **machine learning for failure prediction**, **FastAPI for serving predictions**, and a **secure CI/CD pipeline using GitHub Actions** with **Docker** and **Trivy**.

### ✅ Real-World Relevance

Unplanned machine failures in data centers, manufacturing plants, and industrial systems lead to costly downtime. Predictive maintenance aims to **forecast failures before they occur**, allowing timely maintenance and reducing operational disruptions.

Vertiv specializes in **data center infrastructure, power systems, and cooling solutions**, where machine reliability is critical. This project simulates a **predictive maintenance system** relevant to Vertiv's domain.

---

## 🗂 Dataset Details

The dataset used is the **Predictive Maintenance Dataset** (from Kaggle). It represents **sensor readings and operational conditions** of industrial machines.

### **Features**

- **air_temperature** (°C) – Ambient temperature around the machine.
- **process_temperature** (°C) – Internal temperature during operation.
- **rotational_speed** (rpm) – Speed of machine’s rotating components.
- **torque** (Nm) – Torque applied on the shaft.
- **tool_wear** (minutes) – Usage wear of machine tool.
- **type** – Machine category (L = Light, M = Medium, H = Heavy).
- **target** – Binary label: **1 = Machine will fail soon**, **0 = Normal**.

### **What Does "Soon" Mean?**

In predictive maintenance terms, **soon** means **before the next maintenance cycle** (hours or a few days). The model predicts whether a machine is at high risk of failure in the near future based on its current operating conditions.

---

## 🛠 Tech Stack

- **Machine Learning:** Python, Scikit-learn, Pandas, Joblib
- **API Framework:** FastAPI
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Security:** Trivy (Image Scanning), GitLeaks (Secret Scanning)
- **Testing:** Pytest

---

## 📂 Project Structure

```
|-- app/
|   |-- main.py          # FastAPI app entry point
|   |-- inference.py     # Loads model & predicts
|   |-- schemas.py       # Input validation
|-- models/
|   |-- predictive_maintenance_model.pkl  # Trained model
|   |-- train_model.py   # Model training script
|-- tests/
|   |-- test_api.py      # API endpoint tests
|   |-- test_inference.py# ML prediction tests
|-- data/
|   |-- predictive_maintenance.csv        # Dataset
|-- .github/workflows/
|   |-- ci-cd-pipeline.yaml  # CI/CD workflow
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
|-- README.md
```

---

## ⚙️ Workflow

### **1. Model Training**

- Dataset: Predictive Maintenance Dataset (Machine conditions & failure labels)
- Target: **Predict if a machine will fail soon**
- Algorithm: Logistic Regression (or RandomForest)
- Output: `predictive_maintenance_model.pkl`

### **2. API Deployment**

- FastAPI app exposes:
  - `/predict` → Predict machine failure
  - `/health` → Check API health

### **3. Containerization**

- API is packaged into a Docker image.
- Image is pushed to Docker Hub via CI/CD pipeline.

### **4. CI/CD Pipeline**

- Runs on **GitHub Actions**:
  - ✅ Run tests (`pytest`)
  - ✅ Build Docker image
  - ✅ Scan image with **Trivy**
  - ✅ Push image to Docker Hub

---

## 🔐 Security Measures

- **Image Vulnerability Scan:** Trivy integrated into CI/CD pipeline.
- **Secret Scanning:** GitLeaks / GitHub Advanced Security.
- **Dependency Check:** pip-audit (optional if added).

---

## 🚀 How to Run

### **Run Locally**

```bash
# Clone the repo
git clone https://github.com/<your-username>/Predictive-Maintenance-Pipeline.git
cd Predictive-Maintenance-Pipeline

# Install dependencies
pip install -r requirements.txt

# Run FastAPI app
uvicorn app.main:app --reload
```

### **Run with Docker**

```bash
docker build -t predictive-maintenance:latest .
docker run -d -p 8000:8000 predictive-maintenance:latest
```

---

## ✅ CI/CD Pipeline

**Pipeline Steps:**

1. Checkout Code
2. Install Dependencies
3. Run Tests
4. Build Docker Image
5. Scan Image with Trivy
6. Push Image to Docker Hub

**Pipeline Status:** ![Build Status](https://github.com/<your-username>/Predictive-Maintenance-Pipeline/actions/workflows/ci-cd-pipeline.yaml/badge.svg)

---

## 📸 Screenshots

_(Add these when ready)_  
✅ **CI/CD Pipeline Run**  
✅ **Docker Image on Docker Hub**  
✅ **FastAPI Swagger UI (http://localhost:8000/docs)**

---

## 📊 Architecture Diagram

![Architecture](predictive_maintenance_architecture.png)

---

### ✅ Future Enhancements

- Integrate database for storing predictions.
- Add monitoring & alerting (Prometheus & Grafana).
- Implement role-based API security.

---

### 👨‍💻 Author

**Gowtham Sriram Arepalli**
