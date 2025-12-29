# Software Requirements Specification (SRS)
## AI-Assisted Code Vulnerability Explainer

## 1. Introduction

### 1.1 Purpose
The purpose of this document is to specify the requirements for an AI-assisted tool that helps developers identify and understand common security vulnerabilities in source code.

### 1.2 Scope
The system will analyze small code snippets provided by the user and generate explanations of potential vulnerabilities using a large language model. The tool focuses on educational and supportive use cases rather than full automated security verification.

---

## 2. Overall Description

### 2.1 Product Perspective
The system is a standalone command-line application that uses an external large language model API to analyze code.

### 2.2 Product Functions
- Accept source code as text input
- Detect common vulnerability patterns (e.g., SQL injection)
- Explain detected vulnerabilities in natural language
- Suggest secure coding practices

### 2.3 User Characteristics
Users are software developers or students with basic programming knowledge who want to learn about secure coding.

---

## 3. Specific Requirements

### Functional Requirements
- The system shall allow the user to input a code snippet.
- The system shall analyze the code using a large language model.
- The system shall output an explanation if vulnerabilities are detected.
- The system shall indicate when no vulnerabilities are found.

### Non-Functional Requirements
- The system shall respond within a few seconds.
- The system shall not store user-provided code.

### User Stories
- As a developer, I want to understand why my code is insecure so that I can fix it.
- As a student, I want explanations of vulnerabilities so that I can learn secure coding practices.
