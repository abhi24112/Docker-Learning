# 🐳 Docker Learning - Mastering Containerization 🌟

📌 **Overview**
Welcome to the Docker Learning repository! 🚀 This project is a hands-on guide to mastering Docker concepts through practical examples and workflows. Whether you're a beginner or looking to refine your skills, this repository has something for everyone. 🌍

🔹 **Main Focus:** Dockerization & Workflow Automation 🐳⚙️  
🔹 **Not Focused on:** Advanced ML Model Optimization ❌📊  
🔹 **Python Version:** 3.11 🐍  
🔹 **Repository Status:** Public 🌟

---

## 🎯 **What This Project Covers**

✅ Containerizing Python Applications 🌐  
✅ Managing Multi-Container Applications with Docker Compose 📂  
✅ Building and Running Machine Learning Workflows in Containers 📊  
✅ Experimenting with MLflow for Tracking and Logging 🔄  
✅ Exploring MLOps Best Practices for Model Deployment 🚀

---

## 🔥 **Technologies & Tools Used**

| **🛠️ Technology** | **🚀 Purpose**                      |
| ----------------- | ----------------------------------- |
| Docker 🐳         | Containerizing Applications         |
| Docker Compose ⚙️ | Managing Multi-Container Apps       |
| MLflow 📊         | Experiment Tracking & Model Logging |
| Streamlit 🎨      | Interactive UI for ML Predictions   |
| Python 3.11 🐍    | Main Programming Language           |
| Scikit-learn 📚   | Model Training                      |
| Git & GitHub 🔗   | Version Control                     |

---

## 🏗️ **Docker Setup & Configuration**

### 1️⃣ **Docker Compose File (docker-compose.yml)**

🔹 Volumes persist data, models, and logs between container runs.  
🔹 Restart Policy ensures containers restart automatically if they fail. 🔄  
🔹 Port Mapping exposes services like Streamlit on specific ports. 🌐

### 2️⃣ **Dockerfile - Building the Container**

🔹 **Base Image:** Python 3.11 🐍  
🔹 Installing dependencies from `requirements.txt` 📦  
🔹 Copying application code into the container 📂  
🔹 Running the application inside the container 🎨

---

## 🚀 **Running the Project with Docker**

1️⃣ **Build & Start Containers:**

```bash
docker-compose up --build
```

2️⃣ **Stop Running Containers:**

```bash
docker-compose down
```

3️⃣ **Check Running Containers:**

```bash
docker ps
```

4️⃣ **Clean Up Unused Resources:**

```bash
docker system prune -a
```

---

## 📊 **MLflow Integration - Experiment Tracking**

MLflow is used to track experiments, log metrics, and manage model versions. 📝

### **How MLflow Helps in This Project**

✅ Logging Model Performance 📊  
✅ Tracking Different Experiments 🔄  
✅ Versioning ML Models 📂  
✅ Comparing Experiment Runs 📈

### **Start MLflow UI**

```bash
mlflow ui --host 0.0.0.0 --port 5000
```

📍 Open in Browser: [http://localhost:5000](http://localhost:5000) 🌐

---

## 🎯 **Machine Learning Workflow Overview**

This project includes a regression model for predicting sleep efficiency based on:

- Age
- Sleep Duration ⏳
- REM Sleep (%) 😴
- Deep Sleep (%) 🌙
- Light Sleep (%) 💡
- Number of Awakenings ⚡

> **Note:** The focus is on demonstrating Docker and MLOps concepts, not achieving the highest model accuracy. 🚀

---

## 🔗 **Useful Links & Resources**

- **GitHub Repository:** [Click Here](#) 🖥️
- **Docker Documentation:** [Click Here](https://docs.docker.com/) 📘

---

## 🎯 **Next Steps: MLOps Pipeline** 🔄

🚀 **Future Enhancements:**

- Integrate GitHub Actions for CI/CD 🤖
- Implement Model Versioning with MLflow 📂
- Automate Deployment with Kubernetes ☸️
- Enhance Data Pipeline Automation 🔄

---

## 📢 **Conclusion** 🎉

This repository is a comprehensive guide to Dockerizing applications and exploring MLOps principles. From containerizing ML workflows to integrating MLflow, this project is a stepping stone for anyone diving into Docker and MLOps. 🚀💡

