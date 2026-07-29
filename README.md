<!-- ===================================================== -->
<!-- JUNG JAEHUN · GitHub Profile README                  -->
<!-- AI · Mobility · Product Builder                      -->
<!-- ===================================================== -->

<div align="center">

<img
  src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,100:2952FF&height=240&section=header&text=JUNG%20JAEHUN&fontSize=54&fontColor=FFFFFF&fontAlignY=39&desc=AI%20%C2%B7%20MOBILITY%20%C2%B7%20PRODUCT%20BUILDER&descSize=17&descAlignY=61&animation=fadeIn"
  width="100%"
  alt="JUNG JAEHUN"
/>

<br/>

### 안녕하세요, 문제를 AI 시스템과 제품으로 연결하는 JUNG JAEHUN입니다.

현실의 모호한 문제를 구조화하고 데이터를 연결하여,  
**AI가 실제 사용자 행동과 제품 가치로 이어지는 시스템**을 만듭니다.

<br/>

<a href="https://deephoon.github.io/portfolio/">
  <img
    src="https://img.shields.io/badge/PORTFOLIO-2952FF?style=for-the-badge&logo=googlechrome&logoColor=white"
    alt="Portfolio"
  />
</a>
&nbsp;
<a href="https://github.com/deephoon">
  <img
    src="https://img.shields.io/badge/GITHUB-111827?style=for-the-badge&logo=github&logoColor=white"
    alt="GitHub"
  />
</a>

<br/><br/>

<img
  src="https://img.shields.io/badge/EV%20DIAGNOSTICS-111827?style=flat-square"
  alt="EV Diagnostics"
/>
<img
  src="https://img.shields.io/badge/V2X-111827?style=flat-square"
  alt="V2X"
/>
<img
  src="https://img.shields.io/badge/TRUSTWORTHY%20AI-111827?style=flat-square"
  alt="Trustworthy AI"
/>
<img
  src="https://img.shields.io/badge/AI%20PRODUCT-111827?style=flat-square"
  alt="AI Product"
/>
<img
  src="https://img.shields.io/badge/SYSTEM%20ENGINEERING-111827?style=flat-square"
  alt="System Engineering"
/>

</div>

<br/>

---

## 01. About Me

저는 단순히 모델을 학습시키는 것보다  
**문제 정의부터 데이터, AI, 시스템, 사용자 경험까지 연결하는 과정**에 관심이 있습니다.

- EV 구동계 이상 진단과 신뢰도 높은 AI 시스템
- V2X 기반 실시간 차량 안전 분석
- Calibration, XAI, Safety Rule을 활용한 Trustworthy AI
- Multimodal AI와 LLM Agent 기반 제품
- Data Pipeline, API, TCP/IP, State Management 설계
- 실제로 실행하고 검증할 수 있는 웹·모바일 프로덕트

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

<table>
  <tr>
    <td width="20%" align="center">
      <b>🔍 DEFINE</b>
    </td>
    <td>
      모호한 현상을 사용자, 데이터, 제약조건을 기준으로 검증 가능한 문제로 정의합니다.
    </td>
  </tr>
  <tr>
    <td width="20%" align="center">
      <b>🧩 DESIGN</b>
    </td>
    <td>
      데이터 흐름, 상태 변화, API 경계와 사용자 행동을 먼저 설계합니다.
    </td>
  </tr>
  <tr>
    <td width="20%" align="center">
      <b>⚙️ BUILD</b>
    </td>
    <td>
      모델, 백엔드, 통신, 저장소와 인터페이스를 하나의 시스템으로 연결합니다.
    </td>
  </tr>
  <tr>
    <td width="20%" align="center">
      <b>🛡️ VALIDATE</b>
    </td>
    <td>
      정확도뿐 아니라 신뢰도, 예외 상황, 실패 대응과 안전성을 함께 검증합니다.
    </td>
  </tr>
  <tr>
    <td width="20%" align="center">
      <b>🚀 SHIP</b>
    </td>
    <td>
      분석 결과를 실제 사용 가능한 제품과 사용자 경험으로 완성합니다.
    </td>
  </tr>
</table>

<br/>

---

## 02. Selected Works

<!-- ===================================================== -->
<!-- EV FAULT GPT                                          -->
<!-- ===================================================== -->

<table>
  <tr>
    <td width="110" align="center">
      <h1>⚡</h1>
      <b>PROJECT 01</b>
    </td>
    <td>
      <h2>EV Fault GPT</h2>
      <p><b>Explainable & Reliable EV Fault Diagnosis</b></p>
      <p>
        PMSM 10Hz 시계열 데이터를 기반으로
        <b>이상 진단 → 신뢰도 보정 → 설명 가능성 → 운전자 행동 안내</b>까지
        연결한 엔드투엔드 EV 구동계 이상 진단 시스템입니다.
      </p>
      <p>
        <code>Accuracy 97.65%</code>
        <code>Macro F1 96.06%</code>
        <code>ECE 0.1973 → 0.0417</code>
      </p>
      <p>
        <code>Python</code>
        <code>PyTorch</code>
        <code>1D-CNN</code>
        <code>Calibration</code>
        <code>Grad-CAM</code>
        <code>Streamlit</code>
      </p>
      <a href="https://github.com/deephoon/EV-fault-GPT">
        <img
          src="https://img.shields.io/badge/VIEW%20REPOSITORY-111827?style=for-the-badge&logo=github&logoColor=white"
          alt="EV Fault GPT Repository"
        />
      </a>
    </td>
  </tr>
</table>

<details>
  <summary><b>🔎 Project Details</b></summary>
  <br/>

### Problem

일반적인 이상 진단 모델은 분류 결과만 제공하기 때문에 다음과 같은 한계가 있습니다.

- 예측 확률을 실제 신뢰도로 해석하기 어려움
- 모델이 특정 이상으로 판단한 근거가 불명확함
- 운전자가 현재 취해야 할 행동을 알기 어려움
- 고위험 상황에서 LLM의 자유로운 응답이 안전 문제를 만들 수 있음

### Key Engineering

- CSV 스키마 차이를 흡수하는 데이터 매핑
- 시간축 정렬과 10Hz 리샘플링
- Sliding Window 기반 학습 데이터 생성
- 1D-CNN + Residual Block 기반 분류
- Temperature Scaling 기반 확률 보정
- Grad-CAM 및 Channel Saliency 기반 XAI
- LLM 설명과 Rule 기반 안전 경고 결합
- 운전자용 화면과 연구자용 화면 분리
- Streamlit 기반 진단 시뮬레이터 구현

### System Flow

```text
PMSM Time-series Data
        ↓
Preprocessing & Windowing
        ↓
1D-CNN Fault Classification
        ↓
Probability Calibration
        ↓
Grad-CAM & Channel Saliency
        ↓
LLM Explanation / Safety Rule
        ↓
Driver & Researcher Interface
```

</details>

<br/>

<!-- ===================================================== -->
<!-- V2X SAFETY AGENT                                      -->
<!-- ===================================================== -->

<table>
  <tr>
    <td width="110" align="center">
      <h1>🛰️</h1>
      <b>PROJECT 02</b>
    </td>
    <td>
      <h2>V2X Safety Agent</h2>
      <p><b>TCP/IP-based Intelligent V2X Safety System</b></p>
      <p>
        V2X 환경의 위험 데이터를 실시간으로 분석하고,
        운전자에게 <b>위험도·판단 근거·행동 지침</b>을 제공하는
        차량용 지능형 안전 에이전트입니다.
      </p>
      <p>
        <code>React Cockpit</code>
        <code>FastAPI</code>
        <code>TCP/IP</code>
        <code>MCP Tool Chain</code>
        <code>Gemini</code>
      </p>
      <a href="https://github.com/deephoon/V2X_Agent">
        <img
          src="https://img.shields.io/badge/VIEW%20REPOSITORY-111827?style=for-the-badge&logo=github&logoColor=white"
          alt="V2X Safety Agent Repository"
        />
      </a>
    </td>
  </tr>
</table>

<details>
  <summary><b>🔎 Project Details</b></summary>
  <br/>

### System Architecture

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

### Key Engineering

- React 기반 차량 Cockpit UI
- FastAPI 기반 HTTP-to-TCP Bridge
- Python TCP Client·Server 통신
- JSON + `<END>` Marker 기반 메시지 경계 처리
- Agent Controller 기반 Tool 실행 순서 관리
- 차량·날씨·교통·위험도·QoS Tool Chain
- TTC와 거리 기반 위험도 분석
- Gemini 기반 운전자 XAI 브리핑
- Web Speech API 기반 TTS
- 외부 API, LLM, 통신 장애 Fallback

### Layer Responsibility

| Layer | Responsibility |
|---|---|
| React UI | 시나리오 선택 및 위험 분석 결과 표시 |
| FastAPI Bridge | HTTP 요청을 TCP 요청으로 변환 |
| TCP Client | TCP 연결 및 데이터 송수신 |
| TCP Server | Agent 실행 및 응답 반환 |
| Agent Controller | MCP Tool 호출 순서 관리 |
| MCP Tools | 차량·환경·위험도·네트워크 분석 |
| Gemini Agent | 운전자가 이해할 수 있는 브리핑 생성 |

</details>

<br/>

<!-- ===================================================== -->
<!-- GOCHIDA                                               -->
<!-- ===================================================== -->

<table>
  <tr>
    <td width="110" align="center">
      <h1>🛠️</h1>
      <b>PROJECT 03</b>
    </td>
    <td>
      <h2>고치다 · Gochida</h2>
      <p><b>AI Home-Repair Request Product</b></p>
      <p>
        수리가 필요한 부위의 사진과 증상을 AI가 분석해
        <b>공종·위험도·비용 감각·전문가용 요청서</b>로 구조화하는
        생활시공 요청 모바일 제품입니다.
      </p>
      <p>
        <code>Founder</code>
        <code>Product Lead</code>
        <code>React Native</code>
        <code>Expo</code>
        <code>Gemini</code>
      </p>
      <a href="https://github.com/DO-DAA/gochida">
        <img
          src="https://img.shields.io/badge/VIEW%20REPOSITORY-111827?style=for-the-badge&logo=github&logoColor=white"
          alt="Gochida Repository"
        />
      </a>
    </td>
  </tr>
</table>

<details>
  <summary><b>🔎 Project Details</b></summary>
  <br/>

### Problem

생활시공이 필요한 사용자는 다음과 같은 어려움을 겪습니다.

- 문제 부위의 정확한 명칭을 모름
- 어떤 분야의 전문가가 필요한지 판단하기 어려움
- 합리적인 비용 범위를 알기 어려움
- 위험한 문제를 직접 해결하려고 할 수 있음
- 전문가에게 동일한 설명을 반복해야 함

### Product Flow

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
상담 준비
```

### Key Engineering

- 카메라·갤러리 기반 다중 이미지 입력
- Gemini 2.5 Flash 멀티모달 분석
- 공종 자동 분류와 위험도 평가
- 비용 감각과 자가 점검 가이드 제공
- 전문가용 구조화 요청서 생성
- 전문가 응답을 동일 기준으로 비교
- AI 응답 정규화와 Mock Fallback
- React Context 기반 상태 관리
- 모바일 중심 디자인 시스템

</details>

<br/>

<!-- ===================================================== -->
<!-- TOMATO                                                -->
<!-- ===================================================== -->

<table>
  <tr>
    <td width="110" align="center">
      <h1>🍅</h1>
      <b>PROJECT 04</b>
    </td>
    <td>
      <h2>Tomato Focus Ritual</h2>
      <p><b>Immersive Focus Management Product</b></p>
      <p>
        계획, 집중, 휴식, 기록과 회고를 하나의 흐름으로 연결하고,
        3D 인터랙션과 AI 작업 분해를 결합한
        <b>개인화 집중 관리 웹 제품</b>입니다.
      </p>
      <p>
        <code>JavaScript</code>
        <code>Vite</code>
        <code>Three.js</code>
        <code>GSAP</code>
        <code>Gemini</code>
        <code>PWA</code>
      </p>
      <a href="https://github.com/deephoon/Tomato">
        <img
          src="https://img.shields.io/badge/VIEW%20REPOSITORY-111827?style=for-the-badge&logo=github&logoColor=white"
          alt="Tomato Repository"
        />
      </a>
      &nbsp;
      <a href="https://deephoon.github.io/Tomato/">
        <img
          src="https://img.shields.io/badge/LIVE%20DEMO-2952FF?style=for-the-badge&logo=googlechrome&logoColor=white"
          alt="Tomato Live Demo"
        />
      </a>
    </td>
  </tr>
</table>

<details>
  <summary><b>🔎 Project Details</b></summary>
  <br/>

### Product Flow

```text
작업 계획
    ↓
집중 타이머
    ↓
휴식
    ↓
완료 기록
    ↓
아카이브 회고
```

### Key Engineering

- `Date.now()` 기반 타이머 드리프트 최소화
- 작업 생성·수정·삭제 기능
- 작업별 집중 시간과 테마 설정
- Three.js 기반 3D Glass Tomato
- 세션 상태와 3D 시각 피드백 연결
- GSAP 기반 모션 인터랙션
- Gemini 기반 AI Task Slicing
- 한국어·영어 다국어 지원
- PWA 및 Service Worker 구성
- 모듈 기반 SPA 구조

</details>

<br/>

<!-- ===================================================== -->
<!-- OTHER PROJECT                                         -->
<!-- ===================================================== -->

<table>
  <tr>
    <td width="110" align="center">
      <h1>🧪</h1>
      <b>MORE</b>
    </td>
    <td>
      <h2>Fig</h2>
      <p><b>Experimental Project Repository</b></p>
      <p>
        추가적인 실험과 프로토타이핑 결과를 관리하는 프로젝트 저장소입니다.
      </p>
      <a href="https://github.com/deephoon/Fig">
        <img
          src="https://img.shields.io/badge/VIEW%20REPOSITORY-111827?style=for-the-badge&logo=github&logoColor=white"
          alt="Fig Repository"
        />
      </a>
    </td>
  </tr>
</table>

<br/>

<div align="center">

<a href="https://deephoon.github.io/portfolio/">
  <img
    src="https://img.shields.io/badge/VIEW%20FULL%20PORTFOLIO-2952FF?style=for-the-badge&logo=googlechrome&logoColor=white"
    alt="View Full Portfolio"
  />
</a>

</div>

<br/>

---

## 03. Tech Stack

### Languages

<div align="center">

<img src="https://img.shields.io/badge/Python-111827?style=flat-square&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/JavaScript-111827?style=flat-square&logo=javascript&logoColor=white" alt="JavaScript"/>
<img src="https://img.shields.io/badge/TypeScript-111827?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"/>
<img src="https://img.shields.io/badge/C%2B%2B-111827?style=flat-square&logo=cplusplus&logoColor=white" alt="C++"/>
<img src="https://img.shields.io/badge/Java-111827?style=flat-square&logo=openjdk&logoColor=white" alt="Java"/>
<img src="https://img.shields.io/badge/Kotlin-111827?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin"/>

</div>

<br/>

### AI · Data

<div align="center">

<img src="https://img.shields.io/badge/PyTorch-111827?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch"/>
<img src="https://img.shields.io/badge/TensorFlow-111827?style=flat-square&logo=tensorflow&logoColor=white" alt="TensorFlow"/>
<img src="https://img.shields.io/badge/scikit--learn-111827?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn"/>
<img src="https://img.shields.io/badge/pandas-111827?style=flat-square&logo=pandas&logoColor=white" alt="pandas"/>
<img src="https://img.shields.io/badge/NumPy-111827?style=flat-square&logo=numpy&logoColor=white" alt="NumPy"/>
<img src="https://img.shields.io/badge/OpenCV-111827?style=flat-square&logo=opencv&logoColor=white" alt="OpenCV"/>
<img src="https://img.shields.io/badge/Gemini-111827?style=flat-square&logo=googlegemini&logoColor=white" alt="Gemini"/>
<img src="https://img.shields.io/badge/XAI-111827?style=flat-square" alt="XAI"/>

</div>

<br/>

### Product · Frontend

<div align="center">

<img src="https://img.shields.io/badge/React-111827?style=flat-square&logo=react&logoColor=white" alt="React"/>
<img src="https://img.shields.io/badge/React%20Native-111827?style=flat-square&logo=react&logoColor=white" alt="React Native"/>
<img src="https://img.shields.io/badge/Expo-111827?style=flat-square&logo=expo&logoColor=white" alt="Expo"/>
<img src="https://img.shields.io/badge/Vite-111827?style=flat-square&logo=vite&logoColor=white" alt="Vite"/>
<img src="https://img.shields.io/badge/Three.js-111827?style=flat-square&logo=threedotjs&logoColor=white" alt="Three.js"/>
<img src="https://img.shields.io/badge/Streamlit-111827?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit"/>
<img src="https://img.shields.io/badge/HTML5-111827?style=flat-square&logo=html5&logoColor=white" alt="HTML5"/>
<img src="https://img.shields.io/badge/CSS3-111827?style=flat-square&logo=css&logoColor=white" alt="CSS3"/>

</div>

<br/>

### Backend · Infrastructure

<div align="center">

<img src="https://img.shields.io/badge/FastAPI-111827?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI"/>
<img src="https://img.shields.io/badge/Supabase-111827?style=flat-square&logo=supabase&logoColor=white" alt="Supabase"/>
<img src="https://img.shields.io/badge/PostgreSQL-111827?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
<img src="https://img.shields.io/badge/TCP%2FIP-111827?style=flat-square" alt="TCP/IP"/>
<img src="https://img.shields.io/badge/MCP-111827?style=flat-square" alt="MCP"/>
<img src="https://img.shields.io/badge/GitHub%20Actions-111827?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions"/>
<img src="https://img.shields.io/badge/AWS-111827?style=flat-square&logo=amazonwebservices&logoColor=white" alt="AWS"/>

</div>

<br/>

### Tools · Design

<div align="center">

<img src="https://img.shields.io/badge/Git-111827?style=flat-square&logo=git&logoColor=white" alt="Git"/>
<img src="https://img.shields.io/badge/GitHub-111827?style=flat-square&logo=github&logoColor=white" alt="GitHub"/>
<img src="https://img.shields.io/badge/VS%20Code-111827?style=flat-square&logo=visualstudiocode&logoColor=white" alt="VS Code"/>
<img src="https://img.shields.io/badge/Jupyter-111827?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"/>
<img src="https://img.shields.io/badge/Android%20Studio-111827?style=flat-square&logo=androidstudio&logoColor=white" alt="Android Studio"/>
<img src="https://img.shields.io/badge/Figma-111827?style=flat-square&logo=figma&logoColor=white" alt="Figma"/>
<img src="https://img.shields.io/badge/Notion-111827?style=flat-square&logo=notion&logoColor=white" alt="Notion"/>

</div>

<br/>

---

## 04. Current Focus

| Area | Building & Exploring |
|---|---|
| **🛡️ Trustworthy AI** | Calibration, XAI, Safety Rule, Failure Fallback |
| **🚘 Mobility Intelligence** | EV Diagnostics, V2X, Vehicle Safety Agent |
| **🤖 AI Product** | Multimodal AI, LLM UX, Agent Workflow |
| **📊 Machine Learning** | Time-series Analysis, Classification, Anomaly Detection |
| **⚙️ System Engineering** | Data Pipeline, API Orchestration, TCP/IP, State Management |
| **🧩 Product Experience** | Problem Definition, UX Flow, Prototype, Validation Metrics |

<br/>

### Current Direction

```text
Mobility & Product Data
          ↓
Context Modeling
          ↓
AI / ML / Agent
          ↓
Reliability & Explainability
          ↓
User Decision & Action
```

<br/>

---

## 05. Engineering Principles

> **A model prediction is not the final product.**  
> 결과는 사용자가 이해할 수 있어야 하며, 신뢰할 수 있고, 실제 행동으로 연결되어야 합니다.

### Problem First

기술을 먼저 선택하지 않고  
사용자, 데이터, 환경에서 발생하는 문제를 먼저 정의합니다.

### Data & State Flow First

구현 전에 데이터가 어디에서 생성되고,  
어떻게 이동하며, 어떤 상태로 저장되는지 설계합니다.

### Reliability Before Automation

정상 동작뿐 아니라 다음 조건도 함께 검토합니다.

- 데이터 누락과 스키마 오류
- 외부 API 실패와 응답 지연
- 네트워크 연결 실패
- LLM 응답 오류와 Hallucination
- 모델의 과도한 확신
- 고위험 상황의 안전 통제

### Build End-to-End

```text
Problem
   ↓
Data
   ↓
Model
   ↓
API & System
   ↓
Interface
   ↓
Validation
```

<br/>

---

## 06. Repository Map

| Project | Domain | Core Capability | Link |
|---|---|---|---|
| ⚡ **EV Fault GPT** | EV · Trustworthy AI | Diagnosis, Calibration, XAI, Safety UX | [Repository](https://github.com/deephoon/EV-fault-GPT) |
| 🛰️ **V2X Safety Agent** | Mobility · AI Agent | TCP/IP, MCP Tool Chain, XAI Briefing | [Repository](https://github.com/deephoon/V2X_Agent) |
| 🛠️ **Gochida** | Multimodal AI Product | Image Analysis, Request Structuring, Product UX | [Repository](https://github.com/DO-DAA/gochida) |
| 🍅 **Tomato** | Productivity Product | Focus UX, 3D Interaction, AI Task Slicing | [Repository](https://github.com/deephoon/Tomato) |
| 🧪 **Fig** | Experimental Project | Prototype and Technical Experiment | [Repository](https://github.com/deephoon/Fig) |
| 🌐 **Portfolio** | Portfolio | Project Storytelling and Case Study | [Website](https://deephoon.github.io/portfolio/) |

<br/>

---

## 07. Connect

<div align="center">

프로젝트의 자세한 문제 정의,  
설계 의사결정과 구현 결과는 포트폴리오에서 확인할 수 있습니다.

<br/>

<a href="https://deephoon.github.io/portfolio/">
  <img
    src="https://img.shields.io/badge/PORTFOLIO-2952FF?style=for-the-badge&logo=googlechrome&logoColor=white"
    alt="Portfolio"
  />
</a>
&nbsp;
<a href="https://github.com/deephoon">
  <img
    src="https://img.shields.io/badge/GITHUB-111827?style=for-the-badge&logo=github&logoColor=white"
    alt="GitHub"
  />
</a>

<br/><br/>

### Define clearly · Engineer reliably · Ship thoughtfully

</div>

<br/>

<div align="center">

<img
  src="https://capsule-render.vercel.app/api?type=waving&color=0:2952FF,100:0D1117&height=110&section=footer"
  width="100%"
  alt="Footer"
/>

</div>
