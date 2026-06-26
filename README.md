# CloudNative-Taskmaster

> A production-grade, cloud-native task management platform built end-to-end with modern DevOps practices — from infrastructure provisioning to live observability.

[![CI Pipeline](https://github.com/math-ade/Cloudnative-Taskmaster/actions/workflows/ci.yml/badge.svg)](https://github.com/math-ade/Cloudnative-Taskmaster/actions)
[![CD Pipeline](https://github.com/math-ade/Cloudnative-Taskmaster/actions/workflows/cd.yml/badge.svg)](https://github.com/math-ade/Cloudnative-Taskmaster/actions)
[![Stack](https://img.shields.io/badge/stack-Flask%20%7C%20Prometheus%20%7C%20Grafana%20%7C%20Loki-informational?style=flat-square)](/)
[![IaC](https://img.shields.io/badge/IaC-Terraform-7B42BC?style=flat-square&logo=terraform)](terraform/)
[![Orchestration](https://img.shields.io/badge/orchestration-Kubernetes-326CE5?style=flat-square&logo=kubernetes)](k8s/)
[![Platform](https://img.shields.io/badge/platform-CentOS%20Stream%2010-blue?style=flat-square)](/)
[![Containers](https://img.shields.io/badge/containers-7%20UP-brightgreen?style=flat-square)](/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)](LICENSE)

---

## What This Is

CloudNative-Taskmaster is a Flask REST API deployed on a self-hosted Linux stack with a complete production-grade DevOps pipeline built around it — from infrastructure as code and container orchestration through to CI/CD automation, Kubernetes with autoscaling, and a full Prometheus + Grafana + Loki observability layer.

Everything here was built and operated by hand: no managed Kubernetes services, no click-ops, no pre-baked cloud environments. The intent is to demonstrate the skills that matter in production — understanding what breaks, why, and how to build systems that tell you before users notice.

---

## Architecture

![Architecture Diagram](docs/images/architecture.png)

---

## Full Tech Stack

| Layer | Technology | Location |
|-------|-----------|----------|
| Application | Python · Flask · REST API | `app/` |
| Containerisation | Docker · Docker Compose | `docker-compose.yml` |
| Infrastructure as Code | Terraform (HCL) | `terraform/` |
| Orchestration | Kubernetes (kubeadm) · HPA | `k8s/` |
| CI/CD | GitHub Actions (self-hosted runner) | `.github/workflows/` |
| Metrics | Prometheus · PromQL · custom instrumentation | `observability/` |
| Dashboards | Grafana · import-ready JSON | `observability/grafana/` |
| Logging | Loki · Promtail · LogQL | `observability/` |
| Ingress | NGINX | `k8s/` |
| Registry | Docker Hub | — |

---

## Containers (7, all UP)

| Service | Image | Port | Role |
|---------|-------|------|------|
| `taskmaster-api` | Custom Flask | 5000 | REST API + `/metrics` endpoint |
| `prometheus` | prom/prometheus | 9091 | Metrics scraper & time-series DB |
| `grafana` | grafana/grafana | 3000 | Dashboards & alerting |
| `loki` | grafana/loki | 3100 | Log aggregation backend |
| `promtail` | grafana/promtail | — | Docker log shipper → Loki |
| `cadvisor` | gcr.io/cadvisor | 8080 | Container resource metrics |
| `node-exporter` | prom/node-exporter | 9100 | Host OS metrics |

---

## CI/CD Pipeline

Fully automated pipeline on GitHub Actions using a **self-hosted runner** on the CentOS VM. Pipeline runs complete in **~1 minute CI + ~40 seconds CD** — visible in the [Actions tab](https://github.com/math-ade/Cloudnative-Taskmaster/actions).

---

## Kubernetes (kubeadm)

Manifests in `k8s/` deploy the API with:

- **Namespace isolation** — dedicated `taskmaster` namespace
- **Deployment** — rolling update strategy, readiness/liveness probes
- **Service** — ClusterIP + NGINX Ingress for external access
- **HPA** — scales pods based on CPU utilisation

```bash
kubectl apply -f k8s/
kubectl get pods -n taskmaster
kubectl get hpa -n taskmaster
```

---

## Observability

### Metrics (Prometheus)

| Metric | Type | Labels | What it measures |
|--------|------|--------|-----------------|
| `taskmaster_requests_total` | Counter | `endpoint`, `method`, `status` | All HTTP traffic |
| `taskmaster_request_latency_seconds` | Histogram | `endpoint` | Response time distribution |
| `taskmaster_tasks_total` | Counter | `status` | Task throughput by state |

---

## Skills Demonstrated

| Skill | Evidence |
|-------|---------|
| CI/CD automation | Self-hosted GitHub Actions runner · 6 successful pipeline runs |
| Kubernetes operations | kubeadm cluster · HPA autoscaling · namespace isolation |
| Infrastructure as Code | Terraform provisioning of underlying compute |
| Observability engineering | Custom Prometheus metrics · PromQL · Grafana dashboard |
| Log pipeline design | Promtail → Loki → Grafana with LogQL filtering |
| Container networking | Docker Compose service discovery · no hardcoded IPs |
| Linux operations | CentOS Stream 10 · SELinux · firewalld · Docker daemon config |
| Python / API development | Flask REST API with Prometheus instrumentation |

---

## Roadmap

- [ ] Alertmanager — Slack/email alerts on P99 > 1s or error rate > 5%
- [ ] Helm chart — package K8s manifests for reusable deployments
- [ ] Multi-environment Terraform — dev / staging / prod workspaces
- [ ] SLO dashboard — burn rate alerts using Grafana 10 SLO panel

---

## Author

**Adetunji Mathew Babatunde** — Cloud & DevOps Engineer
Lagos, Nigeria · Open to Remote & Relocation 🌍

[![LinkedIn](https://img.shields.io/badge/LinkedIn-mathew--adetunji-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/mathew-adetunji-37a907259)
[![GitHub](https://img.shields.io/badge/GitHub-math--ade-black?style=flat-square&logo=github)](https://github.com/math-ade)

---

*CentOS Stream 10 · Docker · Terraform · Kubernetes · GitHub Actions · Flask · Prometheus · Grafana · Loki*
