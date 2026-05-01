# 🚀 Credit Risk MLOps: Production-Grade Loan Default Pipeline

[![MLOps CI/CD](https://github.com)](https://github.com)
[![FastAPI](https://shields.io)](https://tiangolo.com)
[![Docker](https://shields.io)](https://docker.com)

> **Live Demo:** [https://fly.dev](https://fly.dev)

## 🏦 Project Overview
Most ML projects die in Jupyter Notebooks. This project implements a **complete production lifecycle** for predicting loan defaults. It handles everything from data versioning and experiment tracking to containerized deployment and automated CI/CD.

### 🏗 System Architecture
`Raw Data -> DVC (Versioning) -> MLflow (Experiment Tracking) -> FastAPI (Serving) -> Docker (Containerization) -> Fly.io (Cloud Deployment)`

## 🛠 Tech Stack
*   **Engine:** Python 3.11, Scikit-Learn
*   **Data Ops:** DVC (Data Version Control)
*   **Experiment Tracking:** MLflow (Model Registry)
*   **API Layer:** FastAPI, Pydantic (Data Validation)
*   **DevOps:** Docker, GitHub Actions (CI/CD)
*   **Deployment:** Fly.io

## 🚦 Key MLOps Features
*   **Reproducible Pipeline:** One command `dvc repro` reconstructs the entire feature engineering and training process.
*   **Automated CI/CD:** GitHub Actions triggers a 25-step validation suite on every push, ensuring only verified models reach production.
*   **API Robustness:** Implemented defensive programming for `predict_proba` edge cases and strict Pydantic schema validation.
*   **Containerization:** Full Docker build allows the model to run identically on local machines and high-scale cloud servers.

## 🚀 How to Run Locally
1. **Clone & Setup:**
   ```bash
   git clone https://github.com
   python -m venv venv
   source venv/Scripts/activate
   pip install .
   ```
2. **Reproduce Pipeline:**
   ```bash
   dvc repro
   ```
3. **Run API (Docker):**
   ```bash
   docker build -t credit-risk-api .
   docker run -p 8080:8080 credit-risk-api
   ```

---
*Created by [Your Name] — Bridging the gap between Data Science and Production Engineering.*
