<!-- ===================================================== -->
<!-- JAEHOON JEONG · GitHub Profile README                -->
<!-- Stable version: No external images or dynamic cards  -->
<!-- ===================================================== -->

<div align="center">

# JAEHUN JUNG

### Product-minded AI Builder

**AI Systems · Mobility Intelligence · Product Building**

<br/>

현실의 문제를 구조화하고 데이터를 연결하여,  
**AI가 실제 사용자 행동과 제품 가치로 이어지는 시스템**을 만듭니다.

<br/>

[**🌐 Portfolio**](https://deephoon.github.io/portfolio/)
&nbsp;&nbsp;·&nbsp;&nbsp;
[**🐙 GitHub**](https://github.com/deephoon)

</div>

<br/>

---

## 01. About Me

저는 단순히 모델을 학습시키는 것보다,  
**문제 정의부터 데이터·AI·시스템·사용자 경험까지 연결하는 과정**에 관심이 있습니다.

특히 다음 영역을 중심으로 프로젝트를 설계하고 구현하고 있습니다.

- EV 구동계 이상 진단 및 예지정비
- V2X 기반 차량 안전 분석 시스템
- 설명 가능하고 신뢰할 수 있는 AI
- 멀티모달 AI와 LLM 기반 제품
- 데이터 파이프라인과 시스템 아키텍처
- 실제 사용 가능한 웹·모바일 프로덕트

<br/>

### How I Build

```text
Real-world Problem
        ↓
Problem Definition
        ↓
Data & Context Modeling
        ↓
AI / ML / Rule System
        ↓
Reliability & Explainability
        ↓
Usable Product Experience
```

| 단계 | 핵심 역할 |
|---|---|
| **🔍 Define** | 모호한 현상을 검증 가능한 문제로 구조화합니다. |
| **🧩 Model** | 데이터·상태·사용자·시스템의 관계를 설계합니다. |
| **⚙️ Engineer** | 모델, API, 통신, 저장소와 UI를 하나의 시스템으로 연결합니다. |
| **🛡️ Validate** | 성능뿐 아니라 신뢰도, 오류, 예외와 안전성을 검증합니다. |
| **🚀 Ship** | 분석에서 멈추지 않고 실제 작동하는 제품으로 구현합니다. |

<br/>

---

## 02. Selected Works

### ⚡ EV Fault GPT

> **Explainable & Reliable EV Fault Diagnosis**

PMSM 10Hz 시계열 데이터를 기반으로  
**이상 진단 → 신뢰도 보정 → 설명 가능성 → 운전자 행동 안내**까지 연결한  
엔드투엔드 EV 구동계 이상 진단 시스템입니다.

#### Problem

기존 이상 진단 모델은 분류 결과를 제공하지만, 다음과 같은 한계가 있습니다.

- 예측 확률을 실제 신뢰도로 해석하기 어려움
- 모델이 특정 이상으로 판단한 근거가 불명확함
- 운전자가 현재 무엇을 해야 하는지 알기 어려움
- 고위험 상황에서 LLM의 자유로운 응답이 안전 문제를 만들 수 있음

#### Key Engineering

- CSV 스키마 정규화 및 시계열 전처리
- 10Hz 리샘플링과 Sliding Window 생성
- 1D-CNN + Residual Block 기반 분류
- Temperature Scaling 기반 확률 보정
- Grad-CAM 및 Channel Saliency 기반 XAI
- LLM 자연어 안내와 Rule 기반 안전 경고 결합
- 운전자용 화면과 연구자용 화면 분리
- Streamlit 기반 시나리오 실행 및 결과 시각화

#### Result

| Metric | Result |
|---|---:|
| Accuracy | **97.65%** |
| Macro F1 | **96.06%** |
| Weighted F1 | **97.64%** |
| Test ECE | **0.1973 → 0.0417** |

#### Stack

`Python` `PyTorch` `scikit-learn` `pandas`  
`1D-CNN` `Calibration` `Grad-CAM` `XAI` `Streamlit`

[**Repository →**](https://github.com/deephoon/EV-fault-GPT)

<br/>

---

### 🛰️ V2X Safety Agent

> **TCP/IP-based Intelligent V2X Safety System**

V2X 환경에서 감지된 위험 데이터를 실시간으로 분석하고,  
운전자에게 위험도·판단 근거·행동 지침을 제공하는  
**차량용 지능형 안전 에이전트 시스템**입니다.

#### System Flow

```text
Scenario Selection
        ↓
React Cockpit UI
        ↓ HTTP
FastAPI HTTP-to-TCP Bridge
        ↓ TCP/IP
Python TCP Server
        ↓
Agent Controller
        ↓
MCP Tool Chain
        ↓
Gemini XAI Briefing
        ↓
Driver Cockpit Rendering
```

#### Key Engineering

- React 기반 차량 Cockpit UI
- FastAPI 기반 HTTP-to-TCP Bridge
- Python TCP Client·Server 통신
- JSON + `<END>` Marker 기반 메시지 경계 처리
- Agent Controller 기반 Tool 실행 순서 관리
- 차량·날씨·교통·위험도·QoS Tool Chain
- TTC, 거리, 객체 유형 기반 위험도 계산
- Gemini 기반 운전자 XAI 브리핑
- Web Speech API 기반 음성 안내
- 외부 API·LLM·TCP 통신 장애 Fallback

#### Architecture

| Layer | Responsibility |
|---|---|
| React UI | 시나리오 선택, 위험 정보 및 브리핑 표시 |
| FastAPI Bridge | HTTP 요청을 TCP 요청으로 변환 |
| TCP Client | TCP 서버 연결 및 메시지 송수신 |
| TCP Server | 요청 수신 및 Agent 실행 |
| Agent Controller | MCP Tool 호출 순서 오케스트레이션 |
| MCP Tools | 차량·환경·위험도·네트워크 정보 분석 |
| Gemini Agent | 분석 결과 기반 운전자 브리핑 생성 |

#### Stack

`React` `TypeScript` `Vite` `FastAPI`  
`Python Socket` `TCP/IP` `MCP` `Gemini` `pytest`

[**Repository →**](https://github.com/deephoon/V2X_Agent)

<br/>

---

### 🛠️ 고치다 · Gochida

> **AI Home-Repair Request Product**

사용자가 수리할 부위의 사진과 간단한 증상을 입력하면,  
AI가 이를 분석해 **공종·위험도·비용 감각·전문가용 요청서**로 구조화하는  
생활시공 요청 모바일 제품입니다.

#### Problem

생활시공이 필요한 사용자는 다음과 같은 문제를 겪습니다.

- 문제 부위의 정확한 명칭을 모름
- 어떤 분야의 전문가가 필요한지 판단하기 어려움
- 합리적인 비용 범위를 알기 어려움
- 위험한 문제를 직접 해결하려고 할 수 있음
- 전문가에게 동일한 설명을 반복해야 함

#### Product Flow

```text
사진 촬영 또는 업로드
        ↓
위치·증상 선택
        ↓
Gemini Multimodal Analysis
        ↓
공종·위험도·비용 감각 구조화
        ↓
전문가용 요청서 생성
        ↓
사용자 검토 및 수정
        ↓
전문가 비교
        ↓
상담 준비 및 채팅
```

#### Key Engineering

- 카메라·갤러리 기반 최대 3장 이미지 입력
- Gemini 2.5 Flash 멀티모달 분석
- 공종 자동 분류
- 위험도 기반 우선순위 판단
- 자가 점검 및 주의사항 제공
- 전문가용 구조화 요청서 생성
- 여러 전문가 응답의 동일 기준 비교
- AI 응답 정규화 및 길이 제한
- API 실패 시 Mock Fallback
- React Context 기반 요청 상태 관리
- 모바일 중심 디자인 시스템 설계

#### Role

`Founder` `Product Lead` `Development Lead`

#### Stack

`React Native` `Expo` `Expo Router` `TypeScript`  
`Gemini 2.5 Flash` `React Context` `Multimodal AI` `Product UX`

[**Repository →**](https://github.com/DO-DAA/gochida)

<br/>

---

### 🍅 Tomato Focus Ritual

> **Personal Focus Management Product**

오늘 수행할 작업을 계획하고 실제 집중 시간을 측정하며,  
완료 기록을 아카이브에서 회고할 수 있도록 설계한  
**개인화 집중 관리 웹 제품**입니다.

#### Product Flow

```text
로그인
   ↓
오늘의 집중 작업 생성
   ↓
집중 타이머 시작
   ↓
일시정지 · 재개 · 완료
   ↓
휴식
   ↓
집중 기록 저장
   ↓
아카이브 회고
```

#### Key Engineering

- 계획 시간과 실제 집중 시간 분리
- `Date.now()` 기반 실제 경과 시간 계산
- 새로고침·재접속 이후 세션 복원
- Supabase Auth 기반 이메일 인증
- PostgreSQL 및 Row Level Security 적용
- Supabase Realtime 기반 데이터 동기화
- Polling Fallback
- BroadcastChannel 기반 탭·창 동기화
- 오프라인 명령 큐 및 저장 재시도
- 저장 상태 `OFFLINE`, `SYNCING`, `SAVE FAILED` 표시
- Document Picture-in-Picture 플로팅 타이머
- Three.js·GSAP 기반 인터랙션
- 한국어·영어 다국어 지원
- 모바일 우선 반응형 UI
- Vitest·Playwright 기반 테스트

#### Stack

`JavaScript` `Vite` `Supabase` `PostgreSQL`  
`Three.js` `GSAP` `Picture-in-Picture` `Vitest` `Playwright`

[**Repository →**](https://github.com/deephoon/Tomato)
&nbsp;·&nbsp;
[**Live Demo →**](https://deephoon.github.io/Tomato/)

<br/>

---

### 🎨 Fig

> **Experimental Project Repository**

인터페이스, 시각화 또는 프로토타이핑 관련 실험을 관리하는 저장소입니다.

[**Repository →**](https://github.com/deephoon/Fig)

<br/>

---

<div align="center">

### 더 많은 프로젝트와 상세한 의사결정 과정

[**🌐 VIEW FULL PORTFOLIO →**](https://deephoon.github.io/portfolio/)

</div>

<br/>

---

## 03. Current Focus

| Area | Building & Exploring |
|---|---|
| **🛡️ Trustworthy AI** | Calibration, XAI, Safety Rule, Failure Fallback |
| **🚘 Mobility Intelligence** | EV Diagnostics, V2X, Vehicle Safety Agent |
| **🤖 AI Product** | Multimodal AI, LLM UX, Agent Workflow |
| **🧠 Machine Learning** | Time-series Analysis, Anomaly Detection, Classification |
| **⚙️ System Engineering** | Data Pipeline, API Orchestration, TCP/IP, State Management |
| **🧩 Product Experience** | Problem Definition, UX Flow, Prototype, Validation Metrics |
| **🔬 Experimentation** | Reproducible Experiments, Evaluation, Error Analysis |

<br/>

### Current Direction

```text
Mobility Data
      ↓
Context & Reliability
      ↓
AI / ML / Agent
      ↓
Explainable Decision
      ↓
User Action
```

<br/>

---

## 04. Demonstrated Stack

### AI · Machine Learning

`Python` `PyTorch` `TensorFlow` `scikit-learn`  
`pandas` `NumPy` `OpenCV` `Matplotlib`  
`Time-series Analysis` `Anomaly Detection` `XAI` `Calibration`

### LLM · Agent

`Gemini` `Multimodal AI` `Prompt Engineering`  
`MCP Tool Chain` `Agent Orchestration` `Rule-LLM Hybrid`

### Product · Frontend

`React` `React Native` `TypeScript` `JavaScript`  
`Vite` `Three.js` `GSAP` `Streamlit`  
`HTML` `CSS` `Android`

### Backend · Data

`FastAPI` `Supabase` `PostgreSQL`  
`REST API` `TCP/IP` `Realtime Sync` `State Management`

### Validation · Infrastructure

`pytest` `Vitest` `Playwright`  
`Git` `GitHub` `GitHub Actions`  
`Experiment Tracking` `Fallback Design`

### Design · Productivity

`Figma` `Notion` `Jupyter` `VS Code`  
`Android Studio` `MATLAB` `Logic Pro`

<br/>

---

## 05. Repository Map

| Project | Domain | Core Capability | Link |
|---|---|---|---|
| ⚡ **EV Fault GPT** | EV · Trustworthy AI | Diagnosis, Calibration, XAI, Safety UX | [Repository](https://github.com/deephoon/EV-fault-GPT) |
| 🛰️ **V2X Safety Agent** | Mobility · AI Agent | TCP/IP, MCP Tool Chain, XAI Briefing | [Repository](https://github.com/deephoon/V2X_Agent) |
| 🛠️ **Gochida** | Multimodal AI Product | Image Analysis, Request Structuring, Product UX | [Repository](https://github.com/DO-DAA/gochida) |
| 🍅 **Tomato** | Productivity Product | State Sync, Offline Queue, PiP Widget | [Repository](https://github.com/deephoon/Tomato) |
| 🎨 **Fig** | Experimental Project | Interface and Prototype Experiment | [Repository](https://github.com/deephoon/Fig) |
| 🌐 **Portfolio** | Personal Portfolio | Project Storytelling, Case Study | [Website](https://deephoon.github.io/portfolio/) |

<br/>

---

## 06. Engineering Principles

### 1. Problem First

기술을 먼저 선택하지 않고,  
사용자·현장·데이터에서 발생하는 문제를 먼저 정의합니다.

### 2. Data and State Flow First

구현 전에 데이터가 어디서 생성되고,  
어떻게 이동하며, 어떤 상태로 저장되는지 설계합니다.

### 3. Reliability Before Automation

AI 모델의 정상 동작뿐 아니라 다음 조건을 함께 고려합니다.

- 데이터 누락
- 외부 API 실패
- 네트워크 지연
- LLM 응답 실패
- 잘못된 신뢰도
- 사용자 입력 오류
- 고위험 상황

### 4. Explain Before Asking Users to Act

AI가 결론만 전달하는 것이 아니라,  
사용자가 결과를 이해하고 다음 행동을 선택할 수 있어야 합니다.

### 5. Build End-to-End

분석 노트북에서 끝내지 않고 다음 단계까지 연결합니다.

```text
Problem
  ↓
Data
  ↓
Model
  ↓
API
  ↓
Interface
  ↓
Validation
```

<br/>

---

## 07. What I Value

> **A model prediction is not the final product.**  
> The result must be understandable, trustworthy, and connected to a real user action.

- 문제를 명확한 문장으로 정의합니다.
- 데이터와 상태 흐름을 먼저 설계합니다.
- 성능뿐 아니라 실패 상황과 안전성을 검토합니다.
- 사용자가 이해할 수 있는 설명 구조를 만듭니다.
- 구현 결과를 실제 동작하는 제품으로 연결합니다.
- 프로젝트의 판단 과정과 결과를 문서화합니다.

<br/>

---

## 08. Project Evaluation Framework

프로젝트를 다음 기준으로 평가합니다.

| Dimension | Question |
|---|---|
| **Problem** | 실제로 해결해야 하는 문제가 명확한가? |
| **Data** | 필요한 데이터와 품질 조건이 정의되어 있는가? |
| **Model** | 선택한 모델이 문제와 데이터에 적합한가? |
| **Reliability** | 실패·예외·과신 문제를 고려했는가? |
| **Explainability** | 사용자가 결과의 근거를 이해할 수 있는가? |
| **UX** | 결과가 사용자의 다음 행동으로 이어지는가? |
| **Validation** | 성공을 판단할 정량·정성 지표가 존재하는가? |
| **Reproducibility** | 동일한 실험과 결과를 다시 재현할 수 있는가? |

<br/>

---

## 09. Connect

<div align="center">

프로젝트의 자세한 문제 정의, 설계 의사결정과 결과는  
포트폴리오에서 확인할 수 있습니다.

<br/>

[**🌐 Portfolio**](https://deephoon.github.io/portfolio/)
&nbsp;&nbsp;·&nbsp;&nbsp;
[**🐙 GitHub**](https://github.com/deephoon)

<!--
LinkedIn이나 이메일을 공개하려면 아래 형식으로 추가하세요.

&nbsp;&nbsp;·&nbsp;&nbsp;
[**💼 LinkedIn**](YOUR_LINKEDIN_URL)

&nbsp;&nbsp;·&nbsp;&nbsp;
[**✉️ Email**](mailto:YOUR_EMAIL)
-->

<br/><br/>

**Define clearly · Engineer reliably · Ship thoughtfully**

</div>
