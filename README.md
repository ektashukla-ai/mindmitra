# mindmitra

> **Project Status**: Work in Progress (⚙️ Auth Service Ready)

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

This project serves as a **learning-ground for real production systems**, not copy-paste AI toy examples. Every microservice is designed with extensibility, security, and cloud readiness in mind.

---

## ⚙️ Tech Stack

### 🔧 Backend
| Service | Technology |
|--------|------------|
| Auth Service | FastAPI + PostgreSQL + JWT |
| Chatbot Core | FastAPI + LangChain + LLM APIs + Vector DB (Weaviate) |
| Message Service | FastAPI + MongoDB (Chat History) |
| User Profile Service | FastAPI + PostgreSQL |

### 🗂️ Frontend
- ReactJS (chat interface, user portal)

### 🐳 Infrastructure
- Docker + Docker Compose
- GitHub Actions (CI/CD, auto deployment)
- (Upcoming) Kubernetes YAMLs for scalable cloud deploy

### 📈 Monitoring & Logging
- Prometheus + Grafana + Loki

### 🔐 Security
- JWT Auth + RBAC
- `.env`-based config
- AES256 encryption for sensitive fields
- Secrets are never committed

---

## 🧱 Architecture Overview

This project follows a **modular monorepo** design.

```
mental-health-chatbot/
├── auth-service/           🔐 Login, JWT, register
├── chatbot-core/           🤖 Intent classification, RAG + LLM
├── message-service/        💬 Chat history DB
├── user-profile-service/   👤 Demographics, preferences
├── frontend/               🌐 React-based UI
├── shared/                 📦 Common models/utils
├── deployment/             🐳 Docker + K8s YAMLs
└── docs/                   📄 Architecture diagrams
```

Each service communicates via REST now, with a plan to adopt **gRPC or event-based queues** (Kafka or NATS) later.

We follow **hexagonal architecture** in each service and adhere to patterns like **Factory, Strategy, and Repository** to keep things clean and extensible.

---

## 🌍 Scaling Plan (Enterprise-Grade)

| Concern | Solution |
|--------|----------|
| 2–3 Billion Users | Global load balancer + CDN + multi-region replicas |
| Database | Sharded PostgreSQL / MongoDB Atlas / Spanner |
| Memory Context | Redis + Vector DB (Weaviate / Pinecone) |
| LLM Latency | Warmed inference pools + async retry queues |
| Security | End-to-end TLS + RBAC + Zero Trust APIs |
| Monitoring | Grafana + Prometheus + Loki logs per service |
| Disaster Recovery | Replication + static fallback intents + offline flow |

---

## 🧩 Services (Work in Progress)

- [x] ✅ **Auth Service** (register/login via JWT, PostgreSQL)
- [ ] 🔄 **Chatbot Core** (LLM + intent/RAG pipeline)
- [ ] 🔄 **Message Service** (chat history, MongoDB)
- [ ] 🔄 **User Profile Service** (user demographics/preferences)
- [ ] 🔄 **Frontend UI** (React-based)

---

## 📅 What’s Next (Next 4-5 Hours Plan)

1. Push `chatbot-core`, `message-service`, and `user-profile-service`
2. Add shared Docker Compose file for local development
3. Create README files inside each service folder
4. Build the basic chatbot-core with FastAPI + OpenAI API + intent router
5. Add CI/CD via GitHub Actions for service-level testing

---

## 🙌 Contribution & Feedback

This is a solo project for now, but feel free to suggest features, report bugs, or give me architectural feedback.

> **If you're a recruiter or engineer reviewing this**, this project reflects my real hands-on backend/ML experience and my obsession with production-grade quality. ❤️

---

## 📜 License
MIT License — Feel free to fork and build upon it!

