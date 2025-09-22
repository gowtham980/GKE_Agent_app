# Deploying the Financial Agent to Vertex AI and Integrating with a Flutter Application

This document outlines the plan and checklist for deploying the `financial_agent` to Google Vertex AI and integrating it with a Flutter application.

## 1. Google Cloud & Vertex AI Setup

-   [ ] **Create a Google Cloud Project:**
    -   Go to the [Google Cloud Console](https://console.cloud.google.com/).
    -   Create a new project or select an existing one.
-   [ ] **Enable Vertex AI API:**
    -   In your Google Cloud project, navigate to the "APIs & Services" > "Library".
    -   Search for "Vertex AI API" and enable it.
-   [ ] **Set Up a Service Account:**
    -   Navigate to "IAM & Admin" > "Service Accounts".
    -   Create a new service account with the "Vertex AI User" role.
    -   Download the JSON key file for this service account. This will be used for authentication.
-   [ ] **Authenticate Local Environment:**
    -   Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your service account key file:
        ```bash
        export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/keyfile.json"
        ```

## 2. Deploy Dependent Services (MCP Tool Server)

-   [ ] **Deploy the MCP Tool Server:**
    -   Your agent relies on an `MCPTool` that connects to `http://localhost:8080/mcp/stream`. This will not work in a cloud environment.
    -   Deploy your MCP tool server as a separate, publicly accessible service (e.g., using Google Cloud Run).
    -   Ensure the service is secure and can handle requests from Vertex AI.
-   [ ] **Update Agent Configuration:**
    -   Before building the agent's Docker image, you **must** update the URL in `financial_agent/tools/mcp_tool.py` to point to the public URL of your deployed MCP tool server.

## 3. Agent Deployment to Vertex AI

-   [ ] **Containerize the Agent with Docker:**
    -   Create a `Dockerfile` in the root of your project to define the container image.
    -   Create a `.dockerignore` file to exclude unnecessary files from the container.
-   [ ] **Build and Push the Docker Image to Artifact Registry:**
    -   Enable the Artifact Registry API in your Google Cloud project.
    -   Create a new Docker repository in the Artifact Registry.
    -   Configure Docker to authenticate with the Artifact Registry:
        ```bash
        gcloud auth configure-docker
        ```
    -   Build the Docker image:
        ```bash
        docker build -t us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/financial-agent:latest .
        ```
    -   Push the image to the Artifact Registry:
        ```bash
        docker push us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/financial-agent:latest
        ```
-   [ ] **Deploy to Vertex AI:**
    -   Navigate to the Vertex AI section in the Google Cloud Console.
    -   Go to the "Models" section and click "Import".
    -   Select "Import from Artifact Registry" and choose the Docker image you pushed.
    -   Configure the model settings and deploy it to an endpoint.

## 3. Flutter Application Integration

-   [ ] **Develop the Flutter Application:**
    -   Create a new Flutter project.
    -   Design and build the user interface for the financial agent.
-   [ ] **Integrate with Vertex AI Endpoint:**
    -   Use the `http` package in Flutter to make POST requests to the deployed Vertex AI endpoint.
    -   The request body should contain the user's input in the format expected by your agent.
-   [ ] **Handle API Keys and Authentication:**
    -   Securely store and manage the API key for accessing the Vertex AI endpoint.
    -   Consider using a secure storage solution like `flutter_secure_storage`.
    -   Implement user authentication to personalize the agent's interactions.

## 4. Testing and Validation

-   [ ] **End-to-End Testing:**
    -   Thoroughly test the entire workflow, from the Flutter app to the Vertex AI agent and back.
    -   Verify that the agent's responses are displayed correctly in the app.
-   [ ] **User Acceptance Testing (UAT):**
    -   Conduct UAT to gather feedback from users and ensure a seamless experience.
    -   Iterate on the app and agent based on user feedback.
