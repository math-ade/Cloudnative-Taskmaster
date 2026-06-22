# CloudNative Taskmaster

A production-grade, cloud-native task management platform built with modern DevOps practices.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Infrastructure | Terraform |
| Configuration | Ansible |
| Container Runtime | Docker |
| Orchestration | Kubernetes (kubeadm) |
| CI/CD | GitHub Actions |
| Registry | Docker Hub |
| Monitoring | Prometheus + Grafana |
| Logging | Loki |
| Ingress | NGINX |

## Architecture

- **app/** - Microservices (Frontend, API, Worker)
- **terraform/** - Infrastructure as Code
- **ansible/** - Configuration management
- **k8s/** - Kubernetes manifests
- **observability/** - Monitoring stack
- **.github/workflows/** - CI/CD pipelines

## Getting Started

```bash
# Clone the repository
git clone git@github.com:math-ade/Cloudnative-Taskmaster.git
cd Cloudnative-Taskmaster

# Initialize infrastructure
make init

# Deploy application
make deploy
```

## Author

**Adetunji Mathew Babatunde**
Cloud & DevOps Engineer | Lagos, Nigeria
