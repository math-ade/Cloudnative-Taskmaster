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
| Logging | Loki · Promtail · LogQL |
