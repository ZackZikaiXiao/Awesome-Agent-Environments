# Awesome Agent Environments

<div align="center">
  <p align="center">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License: Apache 2.0"></a>
    <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
    <a href="https://github.com/ZackZikaiXiao/Awesome-Agent-Environments/pulls"><img src="https://img.shields.io/badge/PRs-welcome-red" alt="PRs Welcome"></a>
  </p>
</div>

This repository collects reusable environments for AI agents, along with the systems used to generate, host, and scale those environments.

It focuses on environments where agents can act, be trained, or be evaluated in realistic digital settings such as the web, operating systems, codebases, tools, and enterprise workflows.

⭐ Live GitHub star badges are shown when a public repository exists, so the displayed counts stay current without hard-coding numbers.

## Contents

- [Agent Environments and Benchmarks](#agent-environments-and-benchmarks)
  - [Web](#web)
  - [Computer Use](#computer-use)
  - [Coding and Terminal](#coding-and-terminal)
  - [Tool and API](#tool-and-api)
  - [Enterprise and Workflow](#enterprise-and-workflow)
- [Environment Generation and Scaling](#environment-generation-and-scaling)
  - [Programmatic and Synthetic Generation](#programmatic-and-synthetic-generation)
  - [World Models and Learned Simulators](#world-models-and-learned-simulators)
  - [Environment Scaling Methods](#environment-scaling-methods)
- [Sandboxes and Infrastructure](#sandboxes-and-infrastructure)
  - [Sandbox Platforms](#sandbox-platforms)
  - [Runtime and Isolation](#runtime-and-isolation)
  - [Deployment and Orchestration](#deployment-and-orchestration)

## Agent Environments and Benchmarks

### Web

- [Ego2Web: A Web Agent Benchmark Grounded in Egocentric Videos](https://arxiv.org/abs/2603.22529). ArXiv 2026. Web-agent benchmark that links egocentric video perception with live web execution and automatic evaluation.
- [Online-Mind2Web](https://arxiv.org/abs/2504.01382). ArXiv 2025. Online extension of Mind2Web for live and dynamic web interaction.
- [FieldWorkArena](https://github.com/FujitsuResearch/FieldWorkArena). 2025. Benchmark for field-service style workflows conducted through enterprise web interfaces. [![GitHub Repo stars](https://img.shields.io/github/stars/FujitsuResearch/FieldWorkArena)](https://github.com/FujitsuResearch/FieldWorkArena)
- [WebChoreArena](https://arxiv.org/abs/2509.13177). ArXiv 2025. Cross-page and multi-step web chores benchmark designed to break shortcut-heavy web agents.
- [DoomArena](https://github.com/ServiceNow/DoomArena). 2025. Stress-testing environment for robust and adversarial browser-agent behavior. [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/DoomArena)](https://github.com/ServiceNow/DoomArena)
- [VisualWebArena](https://github.com/web-arena-x/visualwebarena). 2024. Multimodal extension of WebArena with richer visual grounding. [![GitHub Repo stars](https://img.shields.io/github/stars/web-arena-x/visualwebarena)](https://github.com/web-arena-x/visualwebarena)
- [WebVoyager](https://github.com/MinorJerry/WebVoyager). 2024. Open-web browsing benchmark and agent setup for realistic live website interaction. [![GitHub Repo stars](https://img.shields.io/github/stars/MinorJerry/WebVoyager)](https://github.com/MinorJerry/WebVoyager)
- [WorkArena](https://github.com/ServiceNow/WorkArena). 2024. BrowserGym-compatible enterprise web tasks built on ServiceNow workflows. [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/WorkArena)](https://github.com/ServiceNow/WorkArena)
- [WorkArena++](https://arxiv.org/abs/2407.05291). ArXiv 2024. Harder successor benchmark expanding task realism and difficulty for enterprise web agents.
- [AssistantBench](https://arxiv.org/abs/2407.15711). ArXiv 2024. Web-assisted benchmark for complex, realistic assistant tasks.
- [WebLINX](https://github.com/McGill-NLP/WebLINX). 2024. Browser interaction benchmark and dataset focused on long, realistic web sessions. [![GitHub Repo stars](https://img.shields.io/github/stars/McGill-NLP/WebLINX)](https://github.com/McGill-NLP/WebLINX)
- [BrowserGym](https://github.com/ServiceNow/BrowserGym). 2024. Unified Gym-style interface spanning multiple browser and enterprise web environments. [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/BrowserGym)](https://github.com/ServiceNow/BrowserGym)
- [AgentLab](https://github.com/ServiceNow/AgentLab). 2024. Experiment layer built around BrowserGym environments. [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/AgentLab)](https://github.com/ServiceNow/AgentLab)
- [Mind2Web](https://github.com/OSU-NLP-Group/Mind2Web). 2023. Real-world web task dataset and benchmark grounded in live websites. [![GitHub Repo stars](https://img.shields.io/github/stars/OSU-NLP-Group/Mind2Web)](https://github.com/OSU-NLP-Group/Mind2Web)
- [WebArena](https://github.com/web-arena-x/webarena). 2023. Self-hostable benchmark built from cloned web services. [![GitHub Repo stars](https://img.shields.io/github/stars/web-arena-x/webarena)](https://github.com/web-arena-x/webarena)
- [WebShop](https://github.com/princeton-nlp/WebShop). 2022. Shopping environment for instruction following and decision making on realistic storefronts. [![GitHub Repo stars](https://img.shields.io/github/stars/princeton-nlp/WebShop)](https://github.com/princeton-nlp/WebShop)
- [MiniWoB++](https://github.com/Farama-Foundation/miniwob-plusplus). 2018. Canonical lightweight browser tasks for web interaction agents. [![GitHub Repo stars](https://img.shields.io/github/stars/Farama-Foundation/miniwob-plusplus)](https://github.com/Farama-Foundation/miniwob-plusplus)

### Computer Use

- [OSExpert](https://arxiv.org/abs/2603.07978). ArXiv 2026. Harder desktop benchmark targeting professional software usage beyond commodity OS tasks.
- [OSWorld](https://github.com/xlang-ai/OSWorld). 2025. Full operating-system benchmark with real desktop applications and scripted verification. [![GitHub Repo stars](https://img.shields.io/github/stars/xlang-ai/OSWorld)](https://github.com/xlang-ai/OSWorld)
- [MobileWorld](https://arxiv.org/abs/2512.19432). ArXiv 2025. Harder mobile benchmark built to stay ahead of rapidly saturating phone-use agents.
- [GroundCUA](https://github.com/ServiceNow/GroundCUA). 2025. Grounding and dataset layer for computer-use agents, complementary to GUI environments. [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/GroundCUA)](https://github.com/ServiceNow/GroundCUA)
- [OS-Harm](https://github.com/tml-epfl/os-harm). 2025. Harm benchmark for computer-use agents operating over OS-like environments. [![GitHub Repo stars](https://img.shields.io/github/stars/tml-epfl/os-harm)](https://github.com/tml-epfl/os-harm)
- [WindowsAgentArena](https://github.com/microsoft/WindowsAgentArena). 2024. Windows-native desktop benchmark for GUI agents. [![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/WindowsAgentArena)](https://github.com/microsoft/WindowsAgentArena)
- [AndroidWorld](https://github.com/google-research/android_world). 2024. Android task suite for mobile agent evaluation and training. [![GitHub Repo stars](https://img.shields.io/github/stars/google-research/android_world)](https://github.com/google-research/android_world)
- [CRAB](https://github.com/camel-ai/crab). 2024. Cross-environment benchmark covering computer-use and agent interaction tasks. [![GitHub Repo stars](https://img.shields.io/github/stars/camel-ai/crab)](https://github.com/camel-ai/crab)

### Coding and Terminal

- [SWE-World: Building Software Engineering Agents in Docker-Free Environments](https://arxiv.org/abs/2602.03419). ArXiv 2026. Docker-free learned surrogate environment for software engineering agents, with code available in RUCAIBox/SWE-World. [![GitHub Repo stars](https://img.shields.io/github/stars/RUCAIBox/SWE-World)](https://github.com/RUCAIBox/SWE-World)
- [Hybrid-Gym](https://github.com/yiqingxyq/Hybrid-Gym). 2026. Coding-agent training environment aimed at cross-task generalization. [![GitHub Repo stars](https://img.shields.io/github/stars/yiqingxyq/Hybrid-Gym)](https://github.com/yiqingxyq/Hybrid-Gym)
- [Large-Scale Terminal Agentic Trajectory Generation from Dockerized Environments](https://arxiv.org/abs/2602.01244). ArXiv 2026. Introduces TerminalTraj and the TerminalTraj-5k-instances dataset for verified terminal-agent training in Dockerized environments. [![GitHub Repo stars](https://img.shields.io/github/stars/Wusiwei0410/TerminalTraj)](https://github.com/Wusiwei0410/TerminalTraj)
- [MLE-bench](https://github.com/openai/mle-bench). 2026. End-to-end machine learning engineering benchmark. [![GitHub Repo stars](https://img.shields.io/github/stars/openai/mle-bench)](https://github.com/openai/mle-bench)
- [SETA](https://github.com/camel-ai/seta). 2026. Scaling Environments for Terminal Agents with 400 Terminal-Bench-compatible RL environments, dataset releases, and an RL pipeline. [![GitHub Repo stars](https://img.shields.io/github/stars/camel-ai/seta)](https://github.com/camel-ai/seta)
- [R2E-Gym](https://github.com/R2E-Gym/R2E-Gym). 2025. Procedural environment generation and hybrid verifiers for open-weight SWE agents. [![GitHub Repo stars](https://img.shields.io/github/stars/R2E-Gym/R2E-Gym)](https://github.com/R2E-Gym/R2E-Gym)
- [Terminal-Bench](https://github.com/laude-institute/terminal-bench). 2025. Verifiable terminal benchmark for shell-based agents. [![GitHub Repo stars](https://img.shields.io/github/stars/laude-institute/terminal-bench)](https://github.com/laude-institute/terminal-bench)
- [MLE-Dojo](https://github.com/MLE-Dojo/MLE-Dojo). 2025. Training and evaluation environment for ML engineering agents. [![GitHub Repo stars](https://img.shields.io/github/stars/MLE-Dojo/MLE-Dojo)](https://github.com/MLE-Dojo/MLE-Dojo)
- [MLGym](https://github.com/facebookresearch/MLGym). 2025. Gym-style benchmark for ML research and engineering tasks. [![GitHub Repo stars](https://img.shields.io/github/stars/facebookresearch/MLGym)](https://github.com/facebookresearch/MLGym)
- [GitTaskBench](https://github.com/QuantaAlpha/GitTaskBench). 2025. Git-centric task benchmark for repository manipulation agents. [![GitHub Repo stars](https://img.shields.io/github/stars/QuantaAlpha/GitTaskBench)](https://github.com/QuantaAlpha/GitTaskBench)
- [OpenHands Benchmarks](https://github.com/OpenHands/benchmarks). 2025. Benchmark collections and execution harnesses for coding and software-agent tasks. [![GitHub Repo stars](https://img.shields.io/github/stars/OpenHands/benchmarks)](https://github.com/OpenHands/benchmarks)
- [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym). 2024. Public training environment for software engineering agents and verifiers. [![GitHub Repo stars](https://img.shields.io/github/stars/SWE-Gym/SWE-Gym)](https://github.com/SWE-Gym/SWE-Gym)
- [Debug-Gym](https://github.com/microsoft/debug-gym). 2024. Text-based interactive debugging environment with debugger-aware agent loops. [![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/debug-gym)](https://github.com/microsoft/debug-gym)
- [SWE-bench](https://github.com/SWE-bench/SWE-bench). 2023. Standard issue-resolution benchmark built from real GitHub repositories and tests. [![GitHub Repo stars](https://img.shields.io/github/stars/SWE-bench/SWE-bench)](https://github.com/SWE-bench/SWE-bench)

### Tool and API

- [MCP-Atlas: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers](https://arxiv.org/abs/2602.00933). ArXiv 2026. Large-scale benchmark for real MCP-based tool use across 36 servers and 220 tools.
- [tau2-bench](https://github.com/sierra-research/tau2-bench). 2025. Harder successor benchmark with dual-control and richer environment dynamics. [![GitHub Repo stars](https://img.shields.io/github/stars/sierra-research/tau2-bench)](https://github.com/sierra-research/tau2-bench)
- [Tau^3-bench](https://github.com/sierra-research/tau2-bench). 2025. Harder successor to tau2-bench adding full-duplex voice interaction, retrieval, and refined task design. [![GitHub Repo stars](https://img.shields.io/github/stars/sierra-research/tau2-bench)](https://github.com/sierra-research/tau2-bench)
- [AppWorld](https://github.com/StonyBrookNLP/appworld). 2025. App-centric environment for multi-tool and multi-app task completion. [![GitHub Repo stars](https://img.shields.io/github/stars/StonyBrookNLP/appworld)](https://github.com/StonyBrookNLP/appworld)
- [Toolathlon](https://github.com/hkust-nlp/Toolathlon). 2025. Benchmark featuring 600+ tools across real-world software applications with execution-based evaluation. [![GitHub Repo stars](https://img.shields.io/github/stars/hkust-nlp/Toolathlon)](https://github.com/hkust-nlp/Toolathlon)
- [MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe). 2025. Benchmarking framework using real-world MCP servers instead of simulated tools. [![GitHub Repo stars](https://img.shields.io/github/stars/SalesforceAIResearch/MCP-Universe)](https://github.com/SalesforceAIResearch/MCP-Universe)
- [MCPMark](https://github.com/eval-sys/mcpmark). 2025. Evaluation suite that stress-tests tool usage across real MCP services. [![GitHub Repo stars](https://img.shields.io/github/stars/eval-sys/mcpmark)](https://github.com/eval-sys/mcpmark)
- [tau-bench](https://github.com/sierra-research/tau-bench). 2024. Tool-use benchmark centered on customer-support and business-rule-heavy agent tasks. [![GitHub Repo stars](https://img.shields.io/github/stars/sierra-research/tau-bench)](https://github.com/sierra-research/tau-bench)
- [ToolSandbox](https://github.com/apple/ToolSandbox). 2024. Controlled environment for tool-using agents with rich API-level task design. [![GitHub Repo stars](https://img.shields.io/github/stars/apple/ToolSandbox)](https://github.com/apple/ToolSandbox)
- [AgentDojo](https://github.com/ethz-spylab/agentdojo). 2024. Security benchmark for tool-using agents under adversarial and policy-constrained settings. [![GitHub Repo stars](https://img.shields.io/github/stars/ethz-spylab/agentdojo)](https://github.com/ethz-spylab/agentdojo)
- [ASB](https://github.com/agiresearch/ASB). 2024. Agent security benchmark suite for evaluating attack surfaces and unsafe tool behavior. [![GitHub Repo stars](https://img.shields.io/github/stars/agiresearch/ASB)](https://github.com/agiresearch/ASB)
- [ToolEmu](https://github.com/ryoungj/ToolEmu). 2023. Sandbox for emulating risky tool-use scenarios and evaluating tool-agent safety. [![GitHub Repo stars](https://img.shields.io/github/stars/ryoungj/ToolEmu)](https://github.com/ryoungj/ToolEmu)

### Enterprise and Workflow

- [ScienceBoard](https://github.com/OS-Copilot/ScienceBoard). 2026. Scientific workflow environment for research-task agents. [![GitHub Repo stars](https://img.shields.io/github/stars/OS-Copilot/ScienceBoard)](https://github.com/OS-Copilot/ScienceBoard)
- [DefenderBench](https://github.com/microsoft/DefenderBench). 2025. Defensive benchmark for agents operating inside security-sensitive workflow settings. [![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/DefenderBench)](https://github.com/microsoft/DefenderBench)
- [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany). 2024. Enterprise-style benchmark covering long-horizon workplace tasks. [![GitHub Repo stars](https://img.shields.io/github/stars/TheAgentCompany/TheAgentCompany)](https://github.com/TheAgentCompany/TheAgentCompany)
- [OfficeBench](https://github.com/zlwang-cs/OfficeBench). 2024. Office productivity benchmark spanning documents, spreadsheets, slides, and email-style tasks. [![GitHub Repo stars](https://img.shields.io/github/stars/zlwang-cs/OfficeBench)](https://github.com/zlwang-cs/OfficeBench)

## Environment Generation and Scaling

### Programmatic and Synthetic Generation

- [GUI-GENESIS](https://arxiv.org/abs/2602.14093). ArXiv 2026. Automated synthesis of efficient GUI environments with verifiable rewards.
- [WebArena-Infinity](https://github.com/web-arena-x/webarena-infinity). 2026. Generates browser environments with verifiable tasks at scale using multi-agent automation. [![GitHub Repo stars](https://img.shields.io/github/stars/web-arena-x/webarena-infinity)](https://github.com/web-arena-x/webarena-infinity)
- [LLM-in-Sandbox](https://arxiv.org/abs/2601.16206). ArXiv 2026. Sandbox-first environment design showing broad gains from letting models explore a virtual computer.
- [Safe and Scalable Web Agent Learning via Recreated Websites](https://arxiv.org/abs/2603.10505). ArXiv 2026. VeriEnv recreates real websites into executable, verifiable training environments for safe web-agent learning.
- [Simulating Environments with Reasoning Models for Agent Training](https://arxiv.org/abs/2511.01824). ArXiv 2025. Uses reasoning models to simulate environment feedback for scalable SFT and RL agent training without hand-written environment code.
- [SWE-Factory](https://github.com/DeepSoftwareAnalytics/swe-factory). 2025. Automated factory for issue-resolution training data and benchmark generation. [![GitHub Repo stars](https://img.shields.io/github/stars/DeepSoftwareAnalytics/swe-factory)](https://github.com/DeepSoftwareAnalytics/swe-factory)
- [Toucan](https://github.com/TheAgentArk/Toucan). 2025. Environment and data generation pipeline around real MCP-style tool ecosystems. [![GitHub Repo stars](https://img.shields.io/github/stars/TheAgentArk/Toucan)](https://github.com/TheAgentArk/Toucan)
- [OS-Genesis](https://arxiv.org/abs/2412.19723). ArXiv 2024. Reverse task synthesis pipeline for generating GUI-agent trajectories.

### World Models and Learned Simulators

- [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/abs/2602.09856). ArXiv 2026. GUI world model that predicts next UI states through renderable code generation, with code available from AMAP-ML. [![GitHub Repo stars](https://img.shields.io/github/stars/AMAP-ML/Code2World)](https://github.com/AMAP-ML/Code2World)
- [Agent World Model](https://github.com/Snowflake-Labs/agent-world-model). 2026. Fully synthetic code-driven environments backed by databases and tool APIs. [![GitHub Repo stars](https://img.shields.io/github/stars/Snowflake-Labs/agent-world-model)](https://github.com/Snowflake-Labs/agent-world-model)
- [WebWorld](https://arxiv.org/abs/2602.14721). ArXiv 2026. Large-scale world model for open-web agent training.
- [Reinforcement World Model Learning for LLM-based Agents](https://arxiv.org/abs/2602.05842). ArXiv 2026. Self-supervised world-model learning method that aligns simulated next states with real environment transitions.
- [VirtualEnv](https://arxiv.org/abs/2601.07553). ArXiv 2026. Open-source simulated platform with procedurally generated tasks and game-inspired mechanics.
- [ViMo: A Generative Visual GUI World Model for App Agent](https://arxiv.org/abs/2504.13936). ArXiv 2025. Visual GUI world model for app agents that generates future GUI observations as images and text. [![GitHub Repo stars](https://img.shields.io/github/stars/ai-agents-2030/ViMo)](https://github.com/ai-agents-2030/ViMo)
- [LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training](https://arxiv.org/abs/2510.14969). ArXiv 2025. Uses LLM-based simulators as scalable digital training worlds for evolving agent capabilities across changing environments.
- [Internalizing World Models via Self-Play Finetuning for Agentic RL](https://arxiv.org/abs/2510.15047). ArXiv 2025. Improves agentic RL by internalizing latent world models through self-play fine-tuning.
- [Dreamer 4](https://arxiv.org/abs/2509.24527). ArXiv 2025. Scalable world-model training in imagination, including complex Minecraft-style tasks.
- [Dyna-Mind: Learning to Simulate from Experience for Better AI Agents](https://arxiv.org/abs/2510.09577). ArXiv 2025. Teaches agents to internalize simulation traces from experience and improve long-horizon decision making.
- [WebDreamer](https://arxiv.org/abs/2411.06559). ArXiv 2024. Web world-model direction for simulated web interaction and planning.

### Environment Scaling Methods

- [EnvScaler](https://github.com/RUC-NLPIR/EnvScaler). 2026. Programmatic scaling of tool-interactive environments and verifiable scenarios. [![GitHub Repo stars](https://img.shields.io/github/stars/RUC-NLPIR/EnvScaler)](https://github.com/RUC-NLPIR/EnvScaler)
- [ScaleEnv](https://arxiv.org/abs/2602.06820). ArXiv 2026. From-scratch scaling of generalist tool-use environments with executable verification.
- [Adaptive Environment Generation for Embodied Agents](https://arxiv.org/abs/2602.06366). ArXiv 2026. Adaptive scene generation driven by current agent competence.
- [GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators](https://arxiv.org/abs/2512.19682). ArXiv 2025. Co-trains agents with a generative environment simulator that adaptively proposes tasks near the agent's current capability boundary. [![GitHub Repo stars](https://img.shields.io/github/stars/Gen-Verse/GenEnv)](https://github.com/Gen-Verse/GenEnv)
- [Towards General Agentic Intelligence via Environment Scaling](https://arxiv.org/abs/2509.13311). ArXiv 2025. Studies how expanding environment diversity and agent experience can improve generalist tool-use agents.
- [Scaling Agent Learning via Experience Synthesis](https://arxiv.org/abs/2511.03773). ArXiv 2025. Introduces DreamGym, a framework that synthesizes scalable agent experiences for online RL training.
- [Agent Learning via Early Experience](https://arxiv.org/abs/2510.08558). ArXiv 2025. Learns from future states generated by the agent's own actions, bridging imitation learning and full RL.
- [RLVE](https://github.com/Zhiyuan-Zeng/RLVE). 2025. Adaptive verifiable environments for reinforcement learning over language models. [![GitHub Repo stars](https://img.shields.io/github/stars/Zhiyuan-Zeng/RLVE)](https://github.com/Zhiyuan-Zeng/RLVE)

## Sandboxes and Infrastructure

### Sandbox Platforms

- [ROCK](https://github.com/alibaba/ROCK). 2026. Environment and sandbox management framework with a client-server architecture, unified SDKs, and scalable runtime orchestration for agent training workloads. [![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/ROCK)](https://github.com/alibaba/ROCK)
- [OpenSandbox](https://github.com/alibaba/OpenSandbox). 2026. General-purpose sandbox platform for AI applications with unified sandbox APIs, Docker/Kubernetes runtimes, and built-in coding and GUI environments. [![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/OpenSandbox)](https://github.com/alibaba/OpenSandbox)
- [Kubernetes Agent Sandbox](https://developers.googleblog.com/en/announcing-kubernetes-agent-sandbox/). 2025. Google's direction for standardizing sandboxed agent runtimes on Kubernetes.
- [Fault-Tolerant Sandboxing for LLM Agents](https://arxiv.org/abs/2512.12806). ArXiv 2025. Research on resilient sandbox execution for long-running agent systems.
- [E2B Desktop Sandbox](https://github.com/e2b-dev/desktop). 2024. Browser and desktop sandbox for computer-use style agents. [![GitHub Repo stars](https://img.shields.io/github/stars/e2b-dev/desktop)](https://github.com/e2b-dev/desktop)
- [E2B](https://github.com/e2b-dev/E2B). 2023. Cloud sandboxes for code-interpreter and agent workloads. [![GitHub Repo stars](https://img.shields.io/github/stars/e2b-dev/E2B)](https://github.com/e2b-dev/E2B)

### Runtime and Isolation

- [Confidential Containers](https://github.com/confidential-containers). 2022. Confidential-computing stack for running workloads inside attested trusted environments. [![GitHub Repo stars](https://img.shields.io/github/stars/confidential-containers/trustee)](https://github.com/confidential-containers)
- [WASI](https://github.com/WebAssembly/WASI). 2019. Capability-oriented system interface for sandboxed WebAssembly modules. [![GitHub Repo stars](https://img.shields.io/github/stars/WebAssembly/WASI)](https://github.com/WebAssembly/WASI)
- [firecracker-containerd](https://github.com/firecracker-microvm/firecracker-containerd). 2018. Containerd integration for launching workloads inside Firecracker microVMs. [![GitHub Repo stars](https://img.shields.io/github/stars/firecracker-microvm/firecracker-containerd)](https://github.com/firecracker-microvm/firecracker-containerd)
- [gVisor](https://github.com/google/gvisor). 2018. User-space kernel that hardens container isolation for untrusted workloads. [![GitHub Repo stars](https://img.shields.io/github/stars/google/gvisor)](https://github.com/google/gvisor)
- [Firecracker](https://github.com/firecracker-microvm/firecracker). 2017. MicroVM runtime for stronger isolation than process-level containers. [![GitHub Repo stars](https://img.shields.io/github/stars/firecracker-microvm/firecracker)](https://github.com/firecracker-microvm/firecracker)
- [Kata Containers](https://github.com/kata-containers/kata-containers). 2017. Lightweight VMs that look like containers to orchestration systems. [![GitHub Repo stars](https://img.shields.io/github/stars/kata-containers/kata-containers)](https://github.com/kata-containers/kata-containers)
- [Wasmtime](https://github.com/bytecodealliance/wasmtime). 2017. WebAssembly runtime for portable and capability-bounded execution. [![GitHub Repo stars](https://img.shields.io/github/stars/bytecodealliance/wasmtime)](https://github.com/bytecodealliance/wasmtime)
- [OCI Image Spec](https://github.com/opencontainers/image-spec). 2016. Standard image format used across container-based agent environments. [![GitHub Repo stars](https://img.shields.io/github/stars/opencontainers/image-spec)](https://github.com/opencontainers/image-spec)
- [OCI Runtime Spec](https://github.com/opencontainers/runtime-spec). 2015. Standard for how container runtimes launch and manage container bundles. [![GitHub Repo stars](https://img.shields.io/github/stars/opencontainers/runtime-spec)](https://github.com/opencontainers/runtime-spec)
- [runc](https://github.com/opencontainers/runc). 2015. Reference OCI runtime used under much of the modern container stack. [![GitHub Repo stars](https://img.shields.io/github/stars/opencontainers/runc)](https://github.com/opencontainers/runc)
- [containerd](https://github.com/containerd/containerd). 2015. Core container runtime layer used by many sandboxed and orchestrated agent systems. [![GitHub Repo stars](https://img.shields.io/github/stars/containerd/containerd)](https://github.com/containerd/containerd)
- [Docker](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/). 2013. Default container abstraction used across many agent benchmarks and training gyms.

### Deployment and Orchestration

- [Knative](https://github.com/knative/serving). 2018. Serverless layer on Kubernetes for elastic agent backends. [![GitHub Repo stars](https://img.shields.io/github/stars/knative/serving)](https://github.com/knative/serving)
- [Cloudflare Workers](https://developers.cloudflare.com/workers/reference/how-workers-works/). 2018. Isolate-based edge execution model relevant to ultra-fast agent serving and sandboxing.
- [Kubernetes](https://github.com/kubernetes/kubernetes). 2014. Cluster orchestrator for multi-tenant agent runtimes and sandbox scheduling. [![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes/kubernetes)](https://github.com/kubernetes/kubernetes)
- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html). 2014. Serverless compute platform with snapshot-backed execution semantics relevant to agent workloads.
