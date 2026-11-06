## React + Nginx + Docker Playground

A minimal, dummy React application created to explore, test, and master how to containerize a Single Page Application (SPA) and serve it efficiently using **Nginx** inside **Docker**.

---

1. Build the React app into static production assets (`HTML`, `CSS`, `JS`).
2. Serve those static files using a high-performance web server like **Nginx**.
3. Containerize the entire setup using **Docker** to ensure consistency across environments.

This repository serves as a sandbox to understand multi-stage Docker builds, Nginx routing configuration for SPAs, and container optimization.

---

## 📂 Project Structure

```text
.
├── Dockerfile          # Multi-stage build (Node build -> Nginx Alpine serve)
├── nginx.conf          # Custom Nginx configuration for React SPA routing
├── package.json        # Standard React project dependencies
├── public/             # Static assets
└── src/                # React components and entry points
