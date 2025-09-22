# Steps to Deploy the Financial Agent to GKE

This document outlines the steps to build, configure, and deploy the financial agent to your GKE cluster.

**Project ID:** `gcpdevelopment-464720`
**Region:** `us-central1` (You can change this if you prefer another region)

---

### Step 1: Configure Environment for In-Cluster Communication

This step is complete. Your `.env` file is configured for in-cluster communication.

---

### Step 2: Build and Push the Docker Image

These commands will build your agent's Docker image for multiple platforms and push it to a private Google Artifact Registry repository.

1.  **Enable the Artifact Registry API:**
    ```bash
    gcloud services enable artifactregistry.googleapis.com --project=gcpdevelopment-464720
    ```

2.  **Create an Artifact Registry repository (if it doesn't exist):**
    ```bash
    gcloud artifacts repositories create bank-of-anthos-agent --repository-format=docker --location=us-central1 --description="Docker repository for Bank of Anthos Agent" --project=gcpdevelopment-464720
    ```
    *(You can ignore the `ALREADY_EXISTS` error if you've run this before.)*

3.  **Configure Docker authentication:**
    ```bash
    gcloud auth configure-docker us-central1-docker.pkg.dev --project=gcpdevelopment-464720
    ```

4.  **Create and switch to a multi-platform capable Docker builder:**
    ```bash
    docker buildx create --name mybuilder --use
    docker buildx inspect --bootstrap
    ```

5.  **Build and push the multi-platform Docker image:**
    *Navigate to the `/Users/gowtham/Documents/Hackathon/GKE_Hackathon/bank_finance_adk/bank_of_anthos_agent/` directory before running this command.*
    ```bash
    docker buildx build --platform linux/amd64,linux/arm64 -t us-central1-docker.pkg.dev/gcpdevelopment-464720/bank-of-anthos-agent/financial-agent:latest --push .
    ```

---

### Step 3: Create the Kubernetes Secret for Your API Key

**IMPORTANT:** Replace `your-google-api-key` with your actual Google API key.

```bash
kubectl create secret generic gemini-api-key --from-literal=api_key='your-google-api-key'
```

---

### Step 4: Update the Deployment Manifest

This step is complete. The `kubernetes/deployment.yaml` is configured to use the correct image path.

---

### Step 5: Deploy the Agent

```bash
kubectl apply -f kubernetes/
```

---

### Step 6: Verify the Deployment

1.  **Check deployment status:**
    ```bash
    kubectl get deployments
    ```

2.  **Check pod status:**
    ```bash
    kubectl get pods
    ```

3.  **Get the external IP address:**
    ```bash
    kubectl get service bank-of-anthos-agent
    ```
