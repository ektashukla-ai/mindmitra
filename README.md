# mindmitra

> **Project Status**: Work in Progress (Auth and Chatbot Service Ready)

---

## 🚀 Project Overview
This project is a scalable, secure, and production-grade **Mental Health Triage Chatbot** built using a microservice architecture. It is designed to simulate how real-world healthcare-grade AI chatbots work — from triage to follow-up, in compliance with privacy standards like HIPAA.

The chatbot:
- Understands mental health-related queries (depression, anxiety, PTSD)
- Offers preliminary triage and severity classification
- Provides next steps (self-help, emergency escalation, or professional referral)
- Maintains private chat history per user
- Is multilingual and safe-by-design

---

## 💡 Intent Behind the Project

I wanted to build something beyond business demos — something that:
- Resembles **real-world scale** (billions of users)
- Uses **modern engineering practices** (clean architecture, security, modularity)
- Could act as a **portfolio centerpiece** for ML/AI/Backend-focused roles

This project serves as a **learning-ground for real production systems**. Every microservice is designed with extensibility, security, and cloud readiness in mind.

---

## ⚙️ Tech Stack

### 🔧 Backend
| Service | Technology |
|--------|------------|
| Auth Service | FastAPI + PostgreSQL + JWT |
| Chatbot Core | FastAPI + LangChain + LLM APIs + Vector DB (ChromaDB) |
| Message Service | FastAPI + MongoDB (Chat History) |
| User Profile Service | FastAPI + PostgreSQL |

### 🗂️ Frontend
- ReactJS (chat interface, user portal)

### 🐳 Infrastructure
- Docker + Docker Compose
- GitHub Actions (CI/CD, auto deployment)
- (Upcoming) Kubernetes YAMLs for scalable cloud deploy

### 📈 Monitoring & Logging
- Prometheus + Grafana

### 🔐 Security
- JWT Auth + RBAC
- `.env`-based config
- AES256 encryption for sensitive fields
- Secrets are never committed

---

## 🧱 Architecture Overview

This project follows a **modular monorepo** design.

```
mindmitra/
├── auth-service/           🔐 Login, JWT, register
├── chatbot-core/           🤖 Intent classification, RAG + LLM
├── message-service/        💬 Chat history DB
├── user-profile-service/   👤 Demographics, preferences
├── frontend/               🌐 React-based UI
├── shared/                 📦 Common models/utils
├── deployment/             🐳 Docker + K8s YAMLs
└── docs/                   📄 Architecture diagrams
```

Each service communicates via REST now, with a plan to adopt **gRPC or event-based queues** (Kafka) later.

We follow **hexagonal architecture** in each service and adhere to patterns like **Factory, Strategy, and Repository** to keep things clean and extensible.

---

## 🌍 Scaling Plan (Enterprise-Grade)

| Concern | Solution |
|--------|----------|
| 2–3 Billion Users | Global load balancer + CDN + multi-region replicas |
| Database | Sharded PostgreSQL / MongoDB Atlas / Spanner |
| Memory Context | Redis + Vector DB (Chroma / Pinecone) |
| LLM Latency | Warmed inference pools + async retry queues |
| Security | End-to-end TLS + RBAC + Zero Trust APIs |
| Monitoring | Grafana + Prometheus logs per service |
| Disaster Recovery | Replication + static fallback intents + offline flow |

---

## 🧩 Services (Work in Progress)

- [x] ✅ **Auth Service** (register/login via JWT, PostgreSQL)
- [ ] 🔄 **Chatbot Core** (LLM + intent/RAG pipeline)
- [ ] 🔄 **Message Service** (chat history, MongoDB)
- [ ] 🔄 **User Profile Service** (user demographics/preferences)
- [ ] 🔄 **Frontend UI** (React-based)

---

## 🙌 Contribution & Feedback

This is a solo project for now, but feel free to suggest features, report bugs, or give me architectural feedback.

## 📜 License
MIT License — Feel free to fork and build upon it!

