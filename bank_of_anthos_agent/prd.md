# Product Requirements Document: Aura Financial Agent on Flutter

## 1. Overview

This document outlines the requirements for deploying the "Aura" financial agent to Google Cloud's Vertex AI and integrating it with a Flutter mobile application.

**Project Goal:** To provide users with a friendly, interactive, and intelligent financial assistant on their mobile devices.

## 2. Agent Deployment Checklist (Vertex AI)

-   [ ] **Containerize the Agent:**
    -   [ ] Create a `Dockerfile` to package the `financial_agent` and its dependencies.
    -   [ ] Ensure all necessary Python packages from `requirements.txt` are included.
    -   [ ] Test the container locally to verify the agent runs correctly.

-   [ ] **Push to Artifact Registry:**
    -   [ ] Create a new Docker repository in Google Artifact Registry.
    -   [ ] Authenticate Docker with gcloud: `gcloud auth configure-docker`.
    -   [ ] Tag the local Docker image with the Artifact Registry path.
    -   [ ] Push the image to the registry.

-   [ ] **Deploy to Vertex AI Endpoint:**
    -   [ ] Create a new Vertex AI Endpoint.
    -   [ ] Deploy the container image from Artifact Registry to the endpoint.
    -   [ ] Configure machine type and scaling parameters (e.g., min/max replicas).
    -   [ ] Set up health checks for the endpoint.

-   [ ] **IAM & Permissions:**
    -   [ ] Create a dedicated service account for the Flutter app to invoke the Vertex AI endpoint.
    -   [ ] Grant the service account the "Vertex AI User" role.
    -   [ ] Ensure the Vertex AI service agent has necessary permissions if it needs to access other Google Cloud services.

## 3. Flutter Application Integration Checklist

-   [ ] **Project Setup:**
    -   [ ] Initialize a new Flutter project.
    -   [ ] Add necessary dependencies to `pubspec.yaml` (e.g., `http` for API calls, `flutter_bloc` for state management).

-   [ ] **API Service Layer:**
    -   [ ] Create a service class (`VertexAIService.dart`) to handle communication with the Vertex AI endpoint.
    -   [ ] Implement a method to send user input to the agent.
    -   [ ] Implement methods to handle authentication (e.g., using API keys or OAuth with the dedicated service account).
    -   [ ] Securely store and manage API keys (e.g., using `flutter_secure_storage` or environment variables).

-   [ ] **User Interface (UI):**
    -   [ ] Design and build a chat-style interface for users to interact with the agent.
    -   [ ] Create UI components for displaying messages (user and agent).
    -   [ ] Add an input field and a send button.
    -   [ ] Implement loading indicators while waiting for the agent's response.

-   [ ] **State Management:**
    -   [ ] Use a state management solution (e.g., BLoC, Provider, Riverpod) to manage the conversation state.
    -   [ ] Handle UI updates when new messages are sent or received.
    -   [ ] Manage loading and error states.

## 4. Testing & Validation

-   [ ] **Unit Tests:**
    -   [ ] Write unit tests for the `VertexAIService` in Flutter to mock API calls.
    -   [ ] Write unit tests for the state management logic.
-   [ ] **Integration Tests:**
    -   [ ] Test the live connection between the Flutter app and the deployed Vertex AI endpoint.
-   - [ ] **End-to-End (E2E) Testing:**
    -   [ ] Simulate a full user conversation flow, from sending a message to receiving and displaying the agent's response.

## 5. Monitoring & Logging

-   [ ] **Vertex AI:**
    -   [ ] Enable and monitor logs for the Vertex AI endpoint in Google Cloud's operations suite (formerly Stackdriver).
    -   [ ] Set up alerts for high error rates or latency.
-   [ ] **Flutter App:**
    -   [ ] Implement analytics (e.g., using Firebase Analytics) to track user engagement and feature usage.
    -   [ ] Set up crash reporting (e.g., using Firebase Crashlytics).
