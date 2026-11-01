# Monorepo CI/CD Pipeline with GitHub Actions

## Purpose
This project is a hands-on practice playground built to master advanced **GitHub Actions** concepts. Specifically, it demonstrates how to design a scalable **CI/CD pipeline for a monorepo** using a centralized reusable workflow architecture rather than duplicating build steps across multiple project files.

---

## What This Project Does

1. **Monorepo Structure:** Houses multiple independent projects (`PROJECT1` and `PROJECT2`) inside a single repository under the `REUSABLE_WORKFLOW_CALL/` directory.
2. **Centralized Reusable Workflow:** Contains a master template (`.github/workflows/docker-reusable.yml`) that handles repetitive CI tasks:
   - Checking out code.
   - Securely logging into Docker Hub using repository secrets.
   - Dynamically building and pushing Docker images based on incoming parameters.
3. **Independent Project Triggers:** Uses small, lightweight caller workflows (`docker-reusable-build-project1.yml` and `docker-reusable-build-project2.yml`) that watch for code changes in their respective folders. 
4. **Smart Path Filtering:** Ensures that pushing a change to `PROJECT1` *only* triggers the build for `PROJECT1`, saving time and compute resources.

---

## Architecture Overview

```text
.github/workflows/
├── docker-reusable.yml                  # The core template (engine)
├── docker-reusable-build-project1.yml   # Remote-control for Project 1
└── docker-reusable-build-project2.yml   # Remote-control for Project 2

REUSABLE_WORKFLOW_CALL/
├── PROJECT1/                            # Project 1 source & Dockerfile
└── PROJECT2/                            # Project 2 source & Dockerfile
