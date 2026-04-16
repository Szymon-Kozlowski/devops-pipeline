## Overview
This project is implementation of CI/CD pipeline for a Python Flask web application. It automates the process of building a Docker image, running unit tests, and performing security audits before any deployment occurs.

## Tech Stack
* **App Framework:** Python / Flask
* **CI/CD:** Azure Pipelines
* **Containerization:** Docker
* **Security:** Trivy (CVE scanning)
* **Testing:** Unittest (Python)

## Key Features & DevOps Principles
* **Automated Quality Gate:** Implemented unit testing as the first stage of the pipeline to prevent "broken" code from reaching the build stage.
* **Shift-Left Security:** Integrated **Trivy** to scan Docker images for HIGH and CRITICAL vulnerabilities before they are marked as ready for deployment.
* **Optimized Image Management:** Developed a tagging strategy using both `BuildID` for traceability and `latest` for deployment convenience.
* **Infrastructure Maintenance:** Automated build agent cleanup using `docker image prune` to manage disk space and maintain agent health.
* **Problem Solving:** Successfully configured a **Self-Hosted Agent** to bypass Azure limitations. 

## Pipeline Workflow
1. **Install Dependencies:** Standardizes the Python 3.13 environment.
2. **Test:** Runs `unittest` to verify application logic.
3. **Build:** Creates a Docker image with dual-tagging.
4. **Scan:** Analyzes the image for security vulnerabilities.
5. **Clean:** Removes dangling layers to optimize storage.
