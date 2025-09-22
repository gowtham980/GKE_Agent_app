# Product Requirements Document: Aura Flutter App

## 1. Overview

Aura is a mobile financial advisor application for Bank of Anthos customers. It provides a conversational interface for users to get insights into their finances, ask questions, and receive personalized recommendations.

## 2. Goals

- Provide a simple, intuitive, and beautiful mobile interface for interacting with the Aura financial agent.
- Securely authenticate users against the Bank of Anthos backend.
- Enable users to ask financial questions in natural language.
- Display financial data (balance, transactions) retrieved by the agent.
- Offer a single, actionable financial tip to the user.

## 3. Features & Implementation Checklist

- [ ] **Feature 1: Foundational Setup**
    - [ ] Add necessary dependencies (`http` for network requests).
    - [ ] Create a clean, modern folder structure for UI components, models, and services.

- [ ] **Feature 2: Login Screen**
    - [ ] Build a simple, elegant UI for username and password entry.
    - [ ] Implement the logic to call the Bank of Anthos `userservice` to authenticate and retrieve a JWT token.
    - [ ] Implement secure storage for the JWT token on the device.

- [ ] **Feature 3: Chat Interface**
    - [ ] Build the main chat screen UI.
    - [ ] Include a message list to display the conversation history.
    - [ ] Add a text input field and a "Send" button.

- [ ] **Feature 4: Agent Communication**
    - [ ] Implement a service to send POST requests to the deployed agent's external IP (`http://34.135.12.119`).
    - [ ] Ensure the user's message and the stored JWT token are correctly formatted in the request body.
    - [ ] Implement logic to handle and display the agent's JSON response in the chat UI.
    - [ ] Manage loading states while waiting for the agent's response.
