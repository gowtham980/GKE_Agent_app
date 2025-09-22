# Aura: AI Financial Advisor for Bank of Anthos

**A submission for the GKE is Turning 10 Hackathon.**

Aura is a smart, conversational AI financial advisor built to provide an intelligent upgrade to the "Bank of Anthos" microservices application. It acts as a friendly financial companion, allowing users to ask questions about their accounts in natural language and receive personalized, data-driven insights.

This project consists of two main components:
1.  **The Agent:** A Python-based, multi-agent system built with the Google ADK and powered by Gemini. It is containerized with Docker and deployed on a GKE Autopilot cluster.
2.  **The App:** A cross-platform mobile application built with Flutter that provides a clean, conversational UI for users to interact with Aura.

[![Architecture Diagram](bank_of_anthos_agent/architecture.png)](bank_of_anthos_agent/architecture.md)

*Click to view the detailed architecture diagram.*

---

## Features

*   **Conversational Interface:** Ask questions about your finances in plain English.
*   **Secure Authentication:** Logs in using your existing Bank of Anthos credentials to fetch a secure JWT token.
*   **Real-Time Data:** Connects directly to the Bank of Anthos backend services to retrieve your live account balance and transaction history.
*   **Intelligent Insights:** Leverages the Gemini 1.5 Pro model to understand your data and provide helpful summaries and tips.
*   **Cloud-Native & Scalable:** The AI agent is fully containerized and deployed on GKE, demonstrating a modern, scalable architecture.
*   **Non-Invasive Upgrade:** Adds a powerful AI layer to Bank of Anthos *without modifying any of the original application's source code*.

---

## Built With

*   **Languages:** Python, Dart
*   **Frameworks:** Google Agent Development Kit (ADK), FastAPI, Flutter
*   **Platforms & Cloud Services:**
    *   Google Kubernetes Engine (GKE) Autopilot
    *   Google Artifact Registry
    *   Docker
*   **APIs & AI Models:**
    *   Google Gemini 1.5 Pro
    *   Bank of Anthos internal REST APIs

---

## Getting Started

### Prerequisites

*   An active Google Cloud project.
*   A running GKE cluster with the Bank of Anthos application deployed.
*   `gcloud`, `kubectl`, and `docker` CLIs installed and configured.
*   Flutter SDK installed.
*   An editor like VS Code with the Flutter extension.

### 1. Backend Agent Setup (GKE)

The agent runs in a Docker container on your GKE cluster.

**Step 1: Build and Push the Docker Image**

Navigate to the `bank_of_anthos_agent` directory and run the build command. This will build a multi-platform image and push it to your Google Artifact Registry.

```bash
# Configure Docker with gcloud credentials
gcloud auth configure-docker us-central1-docker.pkg.dev

# Build and push the image (replace with your Project ID)
docker buildx build --platform linux/amd64,linux/arm64 \
  -t us-central1-docker.pkg.dev/YOUR_PROJECT_ID/bank-of-anthos-agent/financial-agent:v6 \
  --push .
```

**Step 2: Create a Kubernetes Secret for your API Key**

Replace `your-google-api-key` with your actual Gemini API key.

```bash
kubectl create secret generic gemini-api-key --from-literal=api_key='your-google-api-key'
```

**Step 3: Deploy the Agent**

Apply the Kubernetes manifests to deploy the agent and expose it via a LoadBalancer service.

```bash
kubectl apply -f kubernetes/
```

**Step 4: Get the External IP**

Find the external IP address of your agent. You will need this for the Flutter app.

```bash
kubectl get service bank-of-anthos-agent
```

### 2. Frontend App Setup (Flutter)

**Step 1: Update the API Endpoints**

Open the `aura_flutter_app/lib/main.dart` file and replace the placeholder IP addresses with the external IPs of your Bank of Anthos `frontend` service and your newly deployed `bank-of-anthos-agent` service.

**Step 2: Build and Run the App**

You can run the app on a mobile device (Android/iOS) or as a desktop application.

**To build an Android APK:**
```bash
cd aura_flutter_app
flutter build apk
```
The APK will be located at `build/app/outputs/flutter-apk/app-release.apk`.

**To run as a macOS desktop app:**
```bash
cd aura_flutter_app
flutter run -d macos
```

## Try It Out

*   **Public Code Repo:** [https://github.com/gowtham980/GKE_Agent_app](https://github.com/gowtham980/GKE_Agent_app)
*   **Live App (Android APK):** *https://drive.google.com/file/d/1UQh3lqBbeqglj-ERpnH7FETlUnuhMf56/view?usp=share_link*