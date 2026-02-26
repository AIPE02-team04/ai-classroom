<<<<<<< HEAD
# 🏫 SELf-corner 虛擬教室前端專案

歡迎來到我們的虛擬教室 (Virtual Classroom) 專案！本專案的前端主要是透過 [Lovable AI](https://lovable.dev/) 輔助開發，並結合 n8n 等自動化技術來打造的全新平台。

為了維持專案架構的穩定與 AI 協作的順暢，**目前由特定負責人統一操作 Lovable 進行主體架構的生成與版本同步**。其他團隊成員請透過標準的 Git 流程，直接在地端進行開發、測試與 Code Review。

## 💻 專案使用的技術棧

本專案的前端主要建構於以下技術：
- **Vite** (極速的前端建置工具)
- **TypeScript** (提供強型別的 JavaScript，減少 Bug)
- **React** (前端 UI 框架)
- **shadcn-ui** (高品質的客製化 UI 元件庫)
- **Tailwind CSS** (Utility-first CSS 樣式框架)

---

## 🛠️ 如何參與開發與測試？

請將專案下載到你的電腦上進行本機端的作業。
**(前置作業：請確保你的電腦已安裝 Node.js 與 npm)**

**開發環境建置步驟：**
```bash
# 步驟 1：Clone 這個專案到你的電腦 (僅第一次需要)
git clone -b frontend_jia https://github.com/AIPE02-team04/ai-classroom.git

# 步驟 2：進入專案資料夾
cd SELf-corner

# 步驟 3：安裝所有依賴套件 (很重要！)
npm install

# 步驟 4：啟動本地端開發伺服器
npm run dev
=======
# AI Classroom

> An AI-powered interactive classroom system  
> Built with FastAPI, React, LangGraph, and Docker

---

## 📌 Project Overview

AI Classroom is an intelligent interactive teaching system integrating:

- 🎯 Real-time classroom interaction
- 🤖 LLM-based agent orchestration (LangGraph)
- 🔐 Authentication & session management
- 🎙️ STT / TTS voice interaction
- 🗄️ Postgres + Redis data layer
- 📖 [專案分工對照表 (點此查看)](./docs/WBS.md)
- 📖 [專案開發規則 (點此查看)](./docs/TEAM_RULES.md)

---

## 🏗️ Project Structure

```
project-root/
├── backend/            # FastAPI backend application
├── DB/                 # PostgreSQL
├── frontend/           # React frontend application
├── infrastructure/     # Docker & deployment configuration
├── docs/               # Documentation & development logs
├── prototypes/         # Experimental MVP prototypes
│
├── .env.example        # Environment variable template
├── Makefile            # Project command shortcuts
└── README.md
```

---

## 📂 Folder Description

### 🔹 backend/

Core backend system built with FastAPI.

Contains:

- API routes
- Authentication module
- LangGraph agent orchestration
- Service layer (LLM / STT / TTS integration)
- Database models & migration
- Unit & integration tests

This folder represents the **core business logic layer**.

---

### 🔹 DB/

Database: **PostgreSQL**

This folder contains SQL scripts for database schema definition and management.

#### 📁 Contents

- `create_tables.sql` — table schema definitions
- `init_data.sql` — initial seed data
- `constraints.sql` — foreign keys and constraints

#### 📊 Tables

Total Tables: **5**
- Table 1: User's...
- Table 2: User's...

---

### 🔹 frontend/

React-based client application.

Contains:

- UI components
- Hooks
- API service layer
- Classroom interaction interface

This is the **user interaction layer**.

---

### 🔹 infrastructure/

Infrastructure-as-Code related files.

Contains:

- docker-compose.yml
- Dockerfiles
- Deployment configuration

This ensures the project is:

- Reproducible
- Environment-consistent
- Easy to deploy

---

### 🔹 docs/

Project documentation.

Contains:

- Architecture design
- API specifications
- Development logs
- Meeting notes

This folder represents the **knowledge layer** of the project.

---

### 🔹 prototypes/

Experimental or MVP features.

Used for:

- Streamlit experiments
- Rapid LLM testing
- Temporary research validation

⚠️ Not production code.

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/AIPE02-team04/ai-classroom.git
cd ai-classroom
```

### 2️⃣ Setup Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and configure:

- Database credentials
- OpenAI / LLM API key
- Redis config

---

### 3️⃣ Start with Docker

```bash
docker-compose up --build
```

Frontend:  
```
http://localhost:3000
```

Backend API docs:  
```
http://localhost:8000/docs
```

---

## 🧪 Running Tests

```bash
cd backend
pytest
```

---

## 🔐 Branch Strategy

- `main` → stable version
- `feature/*` → feature branches
- All changes require Pull Request & Code Review

---

## 👥 Team Responsibility

| Area | Responsible Team |
|------|------------------|
| Frontend | frontend-team |
| Backend API | backend-team |
| Database | database-team |
| Infrastructure | backend-team |
| Documentation | project-lead |

---

## 📖 Development Philosophy

- Clear layer separation
- Configuration over hardcoding
- Infrastructure as Code
- Testable service architecture
- Clean Pull Request workflow

---

## 🛠 Tech Stack

**Backend**
- FastAPI
- LangGraph
- SQLAlchemy / SQLModel
- Redis
- Alembic

**Frontend**
- React
- TypeScript

**Infrastructure**
- Docker
- docker-compose

---

## 📌 Future Roadmap

- [ ] Complete authentication flow
- [ ] Integrate voice interaction
- [ ] Improve agent orchestration logic
- [ ] Add CI/CD pipeline

---

## 📜 License

Academic / Internal Use
>>>>>>> 72f6c64bfb0dd8d90ba1c620edbc95e7f5d3f0f3
