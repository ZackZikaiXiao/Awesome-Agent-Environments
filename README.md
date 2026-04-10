# Awesome Agent Environments

<div align="center">
  <p align="center">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License: Apache 2.0"></a>
    <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
    <a href="https://github.com/ZackZikaiXiao/Awesome-Agent-Environments/pulls"><img src="https://img.shields.io/badge/PRs-welcome-red" alt="PRs Welcome"></a>
    <a href="https://drive.google.com/file/d/1njGVDPSVtDA4m2tsYDgNbYHOpRYst3Vc/view?usp=drive_link"><img src="https://img.shields.io/badge/Slides-Google%20Drive-4285F4?logo=googledrive&logoColor=white" alt="Slides"></a>
  </p>
</div>

> From LLMs to agents, environments are becoming essential infrastructure: no environment, no training, no evaluation.

In the supervised learning era, progress scaled with data, algorithms, and compute. In the agent era, environments increasingly take the role of datasets, reward design and verification become core algorithmic bottlenecks, and compute expands beyond GPUs to the full execution stack: runtimes, sandboxes, and orchestration.

This repository tracks research and engineering work across three layers:

- Task layer: agent environments and benchmarks across web, vision, computer use, code, tools, personal agents, and enterprise workflows
- Construction layer: real-world environments, programmatically synthesized environments, and model-based simulators
- Execution layer: sandbox platforms, runtime isolation, and deployment infrastructure

A Chinese slide deck is included, covering definitions, taxonomy, properties, and open questions around agent environments.

⭐ Live GitHub star badges are shown when a public repository exists, so the displayed counts stay current without hard-coding numbers.

## Contents

- [Agent Environments and Benchmarks](#agent-environments-and-benchmarks)
  - [Web](#web)
  - [Vision](#vision)
  - [Computer Use](#computer-use)
  - [Coding and Terminal](#coding-and-terminal)
  - [Tool and API](#tool-and-api)
  - [Personal Agents](#personal-agents)
  - [Enterprise and Workflow](#enterprise-and-workflow)
- [Environment Generation and Scaling](#environment-generation-and-scaling)
  - [Programmatic Synthesis](#programmatic-synthesis)
  - [Model-Based Simulation](#model-based-simulation)
  - [Environment Scaling Methods](#environment-scaling-methods)
- [Sandboxes and Infrastructure](#sandboxes-and-infrastructure)
  - [Sandbox Platforms](#sandbox-platforms)
  - [Runtime and Isolation](#runtime-and-isolation)
  - [Deployment and Orchestration](#deployment-and-orchestration)

## Agent Environments and Benchmarks

### Web

- [Ego2Web: A Web Agent Benchmark Grounded in Egocentric Videos](https://arxiv.org/abs/2603.22529). CVPR 2026. Web-agent benchmark that links egocentric video perception with live web execution and automatic evaluation. [![GitHub Repo stars](https://img.shields.io/github/stars/Yui010206/Ego2Web)](https://github.com/Yui010206/Ego2Web)
- [Online-Mind2Web](https://openreview.net/forum?id=6jZi4HSs6o). COLM 2025. Online extension of Mind2Web for live and dynamic web interaction. [![GitHub Repo stars](https://img.shields.io/github/stars/OSU-NLP-Group/Online-Mind2Web)](https://github.com/OSU-NLP-Group/Online-Mind2Web)
- [FieldWorkArena](https://arxiv.org/abs/2505.19662). ArXiv 2025. Benchmark for field-service style workflows conducted through enterprise web interfaces. [![GitHub Repo stars](https://img.shields.io/github/stars/FujitsuResearch/FieldWorkArena)](https://github.com/FujitsuResearch/FieldWorkArena)
- [WebChoreArena](https://arxiv.org/abs/2506.01952). ArXiv 2025. Cross-page and multi-step web chores benchmark designed to break shortcut-heavy web agents. [![GitHub Repo stars](https://img.shields.io/github/stars/WebChoreArena/WebChoreArena)](https://github.com/WebChoreArena/WebChoreArena)
- [DoomArena](https://arxiv.org/abs/2504.14064). ArXiv 2025. Stress-testing environment for robust and adversarial browser-agent behavior. [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/DoomArena)](https://github.com/ServiceNow/DoomArena)
- [VisualWebArena](https://aclanthology.org/2024.acl-long.50/). ACL 2024. Multimodal extension of WebArena with richer visual grounding. [![GitHub Repo stars](https://img.shields.io/github/stars/web-arena-x/visualwebarena)](https://github.com/web-arena-x/visualwebarena)
- [WebVoyager](https://aclanthology.org/2024.acl-long.371/). ACL 2024. Open-web browsing benchmark and agent setup for realistic live website interaction. [![GitHub Repo stars](https://img.shields.io/github/stars/MinorJerry/WebVoyager)](https://github.com/MinorJerry/WebVoyager)
- [WorkArena](https://openreview.net/forum?id=BRfqYrikdo). ICML 2024. BrowserGym-compatible enterprise web tasks built on ServiceNow workflows. [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/WorkArena)](https://github.com/ServiceNow/WorkArena)
- [WorkArena++](https://openreview.net/forum?id=i2dkwLA0DK). NeurIPS 2024. Harder successor benchmark expanding task realism and difficulty for enterprise web agents.
- [AssistantBench](https://aclanthology.org/2024.emnlp-main.505/). EMNLP 2024. Web-assisted benchmark for complex, realistic assistant tasks. [![GitHub Repo stars](https://img.shields.io/github/stars/oriyor/assistantbench)](https://github.com/oriyor/assistantbench)
- [WebLINX](https://proceedings.mlr.press/v235/lu24e.html). ICML 2024. Browser interaction benchmark and dataset focused on long, realistic web sessions. [![GitHub Repo stars](https://img.shields.io/github/stars/McGill-NLP/WebLINX)](https://github.com/McGill-NLP/WebLINX)
- [BrowserGym](https://openreview.net/forum?id=5298fKGmv3). TMLR 2025. Unified Gym-style interface spanning multiple browser and enterprise web environments. [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/BrowserGym)](https://github.com/ServiceNow/BrowserGym)
- [AgentLab](https://openreview.net/forum?id=5298fKGmv3). TMLR 2025. Experiment layer built around BrowserGym environments. [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/AgentLab)](https://github.com/ServiceNow/AgentLab)
- [Mind2Web](https://openreview.net/forum?id=696d82pNeA). NeurIPS 2023. Real-world web task dataset and benchmark grounded in live websites. [![GitHub Repo stars](https://img.shields.io/github/stars/OSU-NLP-Group/Mind2Web)](https://github.com/OSU-NLP-Group/Mind2Web)
- [WebArena](https://openreview.net/forum?id=oKn9c6ytLx). ICLR 2024. Self-hostable benchmark built from cloned web services. [![GitHub Repo stars](https://img.shields.io/github/stars/web-arena-x/webarena)](https://github.com/web-arena-x/webarena)
- [WebShop](https://proceedings.neurips.cc/paper_files/paper/2022/hash/82ad13ec01f9fe44c01cb91814fd7b8c-Abstract-Conference.html). NeurIPS 2022. Shopping environment for instruction following and decision making on realistic storefronts. [![GitHub Repo stars](https://img.shields.io/github/stars/princeton-nlp/WebShop)](https://github.com/princeton-nlp/WebShop)
- [MiniWoB++](https://openreview.net/forum?id=ryTp3f-0-). ICLR 2018. Canonical lightweight browser tasks for web interaction agents. [![GitHub Repo stars](https://img.shields.io/github/stars/Farama-Foundation/miniwob-plusplus)](https://github.com/Farama-Foundation/miniwob-plusplus)

### Vision

- [Vision-DeepResearch Benchmark: Rethinking Visual and Textual Search for Multimodal Large Language Models](https://arxiv.org/abs/2602.02185). ArXiv 2026. VDR-Bench is a vision-centric benchmark for multimodal deep-research systems, designed to require genuine visual search rather than relying on textual leakage or model priors. [![GitHub Repo stars](https://img.shields.io/github/stars/Osilly/Vision-DeepResearch)](https://github.com/Osilly/Vision-DeepResearch)
- [Gym-V: A Unified Vision Environment System for Agentic Vision Research](https://arxiv.org/abs/2603.15432). ArXiv 2026. Unified platform of 179 procedurally generated visual environments across 10 domains with controllable difficulty for agentic vision training and evaluation.

### Computer Use

- [OSExpert](https://arxiv.org/abs/2603.07978). ArXiv 2026. Harder desktop benchmark targeting professional software usage beyond commodity OS tasks.
- [OSWorld](https://openreview.net/forum?id=tN61DTr4Ed). NeurIPS 2024. Full operating-system benchmark with real desktop applications and scripted verification. [![GitHub Repo stars](https://img.shields.io/github/stars/xlang-ai/OSWorld)](https://github.com/xlang-ai/OSWorld)
- [MobileWorld](https://arxiv.org/abs/2512.19432). ArXiv 2025. Harder mobile benchmark built to stay ahead of rapidly saturating phone-use agents.
- [GroundCUA](https://arxiv.org/abs/2511.07332). ArXiv 2025. Grounding and dataset layer for computer-use agents, complementary to GUI environments. [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/GroundCUA)](https://github.com/ServiceNow/GroundCUA)
- [OS-Harm](https://arxiv.org/abs/2506.14866). ArXiv 2025. Harm benchmark for computer-use agents operating over OS-like environments. [![GitHub Repo stars](https://img.shields.io/github/stars/tml-epfl/os-harm)](https://github.com/tml-epfl/os-harm)
- [OSUniverse](https://arxiv.org/abs/2505.03570). NeSy 2025. Docker-based desktop benchmark with 160 vision-only tasks across five difficulty levels for multimodal GUI-navigation agents. [![GitHub Repo stars](https://img.shields.io/github/stars/agentsea/osuniverse)](https://github.com/agentsea/osuniverse)
- [AndroidLab](https://aclanthology.org/2025.acl-long.107/). ACL 2025. Systematic Android agent training and benchmarking framework with 138 tasks across nine apps. [![GitHub Repo stars](https://img.shields.io/github/stars/THUDM/Android-Lab)](https://github.com/THUDM/Android-Lab)
- [WindowsAgentArena](https://openreview.net/forum?id=W9s817KqYf). ICML 2025. Windows-native desktop benchmark for GUI agents. [![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/WindowsAgentArena)](https://github.com/microsoft/WindowsAgentArena)
- [AndroidWorld](https://openreview.net/forum?id=il5yUQsrjC). ICLR 2025. Android task suite for mobile agent evaluation and training. [![GitHub Repo stars](https://img.shields.io/github/stars/google-research/android_world)](https://github.com/google-research/android_world)
- [CRAB](https://aclanthology.org/2025.findings-acl.1113/). ACL Findings 2025. Cross-environment benchmark covering computer-use and agent interaction tasks. [![GitHub Repo stars](https://img.shields.io/github/stars/camel-ai/crab)](https://github.com/camel-ai/crab)

### Coding and Terminal

- [SWE-World: Building Software Engineering Agents in Docker-Free Environments](https://arxiv.org/abs/2602.03419). ArXiv 2026. Docker-free learned surrogate environment for software engineering agents, with code available in RUCAIBox/SWE-World. [![GitHub Repo stars](https://img.shields.io/github/stars/RUCAIBox/SWE-World)](https://github.com/RUCAIBox/SWE-World)
- [SWE-Universe](https://arxiv.org/abs/2602.02361). ArXiv 2026. Scales real-world verifiable software engineering environments to millions of instances via automated pipeline.
- [DevOps-Gym](https://arxiv.org/abs/2601.20882). ArXiv 2026. Full DevOps lifecycle benchmark covering build, monitoring, issue resolution, test generation, and end-to-end pipeline tasks.
- [Hybrid-Gym](https://arxiv.org/abs/2602.16819). ArXiv 2026. Coding-agent training environment aimed at cross-task generalization. [![GitHub Repo stars](https://img.shields.io/github/stars/Hybrid-Gym/Hybrid-Gym)](https://github.com/Hybrid-Gym/Hybrid-Gym)
- [Large-Scale Terminal Agentic Trajectory Generation from Dockerized Environments](https://arxiv.org/abs/2602.01244). ArXiv 2026. Introduces TerminalTraj and the TerminalTraj-5k-instances dataset for verified terminal-agent training in Dockerized environments. [![GitHub Repo stars](https://img.shields.io/github/stars/Wusiwei0410/TerminalTraj)](https://github.com/Wusiwei0410/TerminalTraj)
- [MLE-bench](https://openreview.net/forum?id=6s5uXNWGIh). ICLR 2025. End-to-end machine learning engineering benchmark. [![GitHub Repo stars](https://img.shields.io/github/stars/openai/mle-bench)](https://github.com/openai/mle-bench)
- [SETA](https://github.com/camel-ai/seta). 2026. Scaling Environments for Terminal Agents with 400 Terminal-Bench-compatible RL environments, dataset releases, and an RL pipeline. [![GitHub Repo stars](https://img.shields.io/github/stars/camel-ai/seta)](https://github.com/camel-ai/seta)
- [R2E-Gym](https://openreview.net/forum?id=7evvwwdo3z). COLM 2025. Procedural environment generation and hybrid verifiers for open-weight SWE agents. [![GitHub Repo stars](https://img.shields.io/github/stars/R2E-Gym/R2E-Gym)](https://github.com/R2E-Gym/R2E-Gym)
- [Multi-SWE-bench](https://openreview.net/forum?id=MhBZzkz4h9). NeurIPS 2025. Multilingual SWE-bench extension covering eight languages with 2,132 instances curated by 68 expert annotators.
- [SWE-smith](https://openreview.net/forum?id=63iVrXc8cC). NeurIPS 2025. Pipeline that turns any Python repository into a SWE-gym, generating 50K task instances from 128 GitHub repos for agent training. [![GitHub Repo stars](https://img.shields.io/github/stars/SWE-bench/SWE-smith)](https://github.com/SWE-bench/SWE-smith)
- [CyberGym](https://arxiv.org/abs/2506.02548). ArXiv 2025. 1,507 real-world vulnerabilities across 188 open-source projects for cybersecurity agent evaluation.
- [Terminal-Bench](https://openreview.net/forum?id=a7Qa4CcHak). ICLR 2026. Verifiable terminal benchmark for shell-based agents. [![GitHub Repo stars](https://img.shields.io/github/stars/laude-institute/terminal-bench)](https://github.com/laude-institute/terminal-bench)
- [MLE-Dojo](https://openreview.net/forum?id=5W5mFU4oMO). NeurIPS 2025. Training and evaluation environment for ML engineering agents. [![GitHub Repo stars](https://img.shields.io/github/stars/MLE-Dojo/MLE-Dojo)](https://github.com/MLE-Dojo/MLE-Dojo)
- [MLGym](https://openreview.net/forum?id=ryTr83DxRq). COLM 2025. Gym-style benchmark for ML research and engineering tasks. [![GitHub Repo stars](https://img.shields.io/github/stars/facebookresearch/MLGym)](https://github.com/facebookresearch/MLGym)
- [GitTaskBench](https://arxiv.org/abs/2508.18993). ArXiv 2025. Git-centric task benchmark for repository manipulation agents. [![GitHub Repo stars](https://img.shields.io/github/stars/QuantaAlpha/GitTaskBench)](https://github.com/QuantaAlpha/GitTaskBench)
- [OpenHands Benchmarks](https://openreview.net/forum?id=OJd3ayDDoF). ICLR 2025. Benchmark collections and execution harnesses for coding and software-agent tasks. [![GitHub Repo stars](https://img.shields.io/github/stars/OpenHands/benchmarks)](https://github.com/OpenHands/benchmarks)
- [SWE-Gym](https://proceedings.mlr.press/v267/pan25g.html). ICML 2025. Public training environment for software engineering agents and verifiers. [![GitHub Repo stars](https://img.shields.io/github/stars/SWE-Gym/SWE-Gym)](https://github.com/SWE-Gym/SWE-Gym)
- [Debug-Gym](https://arxiv.org/abs/2503.21557). ArXiv 2025. Text-based interactive debugging environment with debugger-aware agent loops. [![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/debug-gym)](https://github.com/microsoft/debug-gym)
- [SWE-bench](https://openreview.net/forum?id=VTF8yNQM66). ICLR 2024. Standard issue-resolution benchmark built from real GitHub repositories and tests. [![GitHub Repo stars](https://img.shields.io/github/stars/SWE-bench/SWE-bench)](https://github.com/SWE-bench/SWE-bench)

### Tool and API

- [MCP-Atlas: A Large-Scale Benchmark for Tool-Use Competency with Real MCP Servers](https://arxiv.org/abs/2602.00933). ArXiv 2026. Large-scale benchmark for real MCP-based tool use across 36 servers and 220 tools.
- [Tau^3-bench](https://github.com/sierra-research/tau2-bench). 2025. Harder successor to tau2-bench adding full-duplex voice interaction, retrieval, and refined task design. [![GitHub Repo stars](https://img.shields.io/github/stars/sierra-research/tau2-bench)](https://github.com/sierra-research/tau2-bench)
- [tau2-bench](https://arxiv.org/abs/2506.07982). ArXiv 2025. Harder successor benchmark with dual-control and richer environment dynamics. [![GitHub Repo stars](https://img.shields.io/github/stars/sierra-research/tau2-bench)](https://github.com/sierra-research/tau2-bench)
- [AppWorld](https://aclanthology.org/2024.acl-long.850/). ACL 2024. App-centric environment for multi-tool and multi-app task completion. [![GitHub Repo stars](https://img.shields.io/github/stars/StonyBrookNLP/appworld)](https://github.com/StonyBrookNLP/appworld)
- [Toolathlon](https://openreview.net/forum?id=z53s5p0qhf). ICLR 2026. Benchmark featuring 600+ tools across real-world software applications with execution-based evaluation. [![GitHub Repo stars](https://img.shields.io/github/stars/hkust-nlp/Toolathlon)](https://github.com/hkust-nlp/Toolathlon)
- [MCP-Universe](https://arxiv.org/abs/2508.14704). ArXiv 2025. Benchmarking framework using real-world MCP servers instead of simulated tools. [![GitHub Repo stars](https://img.shields.io/github/stars/SalesforceAIResearch/MCP-Universe)](https://github.com/SalesforceAIResearch/MCP-Universe)
- [MCPMark](https://openreview.net/forum?id=uobROwBsJm). ICLR 2026. Evaluation suite that stress-tests tool usage across real MCP services. [![GitHub Repo stars](https://img.shields.io/github/stars/eval-sys/mcpmark)](https://github.com/eval-sys/mcpmark)
- [tau-bench](https://arxiv.org/abs/2406.12045). ArXiv 2024. Tool-use benchmark centered on customer-support and business-rule-heavy agent tasks. [![GitHub Repo stars](https://img.shields.io/github/stars/sierra-research/tau-bench)](https://github.com/sierra-research/tau-bench)
- [ToolSandbox](https://aclanthology.org/2025.findings-naacl.65/). NAACL Findings 2025. Controlled environment for tool-using agents with rich API-level task design. [![GitHub Repo stars](https://img.shields.io/github/stars/apple/ToolSandbox)](https://github.com/apple/ToolSandbox)
- [AgentDojo](https://openreview.net/forum?id=m1YYAQjO3w). NeurIPS 2024. Security benchmark for tool-using agents under adversarial and policy-constrained settings. [![GitHub Repo stars](https://img.shields.io/github/stars/ethz-spylab/agentdojo)](https://github.com/ethz-spylab/agentdojo)
- [ASB](https://openreview.net/forum?id=V4y0CpX4hK). ICLR 2025. Agent security benchmark suite for evaluating attack surfaces and unsafe tool behavior. [![GitHub Repo stars](https://img.shields.io/github/stars/agiresearch/ASB)](https://github.com/agiresearch/ASB)
- [ToolEmu](https://openreview.net/forum?id=GEcwtMk1uA). ICLR 2024. Sandbox for emulating risky tool-use scenarios and evaluating tool-agent safety. [![GitHub Repo stars](https://img.shields.io/github/stars/ryoungj/ToolEmu)](https://github.com/ryoungj/ToolEmu)

### Personal Agents

- [Proactive Agent Research Environment: Simulating Active Users to Evaluate Proactive Assistants](https://arxiv.org/abs/2604.00842). ArXiv 2026. PARE and Pare-Bench model proactive assistants in digital environments spanning communication, productivity, scheduling, and lifestyle apps. [![GitHub Repo stars](https://img.shields.io/github/stars/deepakn97/pare)](https://github.com/deepakn97/pare)
- [OpenClaw Arena](https://openclaw-arena.github.io/). 2026. Benchmark for personal AI agents that measures task competence and personality consistency across 100 real-world tasks.
- [OpenClaw](https://github.com/openclaw/openclaw). 2026. Local-first personal AI agent and workflow system with multi-channel interfaces, tool use, and controlled execution boundaries. [![GitHub Repo stars](https://img.shields.io/github/stars/openclaw/openclaw)](https://github.com/openclaw/openclaw)
- [PIRA-Bench: A Transition from Reactive GUI Agents to GUI-based Proactive Intent Recommendation Agents](https://arxiv.org/abs/2603.08013). ArXiv 2026. Benchmark for proactive GUI assistants over long, noisy, multi-intent screen trajectories.
- [ASTRA-bench: Evaluating Tool-Use Agent Reasoning and Action Planning with Personal User Context](https://arxiv.org/abs/2603.01357). ArXiv 2026. Execution-based benchmark for assistants that reason over time-evolving personal context and interactive tools.
- [ProactiveMobile: A Comprehensive Benchmark for Boosting Proactive Intelligence on Mobile Devices](https://arxiv.org/abs/2602.21858). ArXiv 2026. Mobile benchmark for proactive assistants that infer user intent from on-device context and generate executable API sequences.
- [ProAgentBench](https://arxiv.org/abs/2602.04482). ArXiv 2026. Benchmark for proactive assistants in working scenarios built from long-term real user sessions.
- [ContextAgent: Context-Aware Proactive LLM Agents with Open-World Sensory Perceptions](https://openreview.net/forum?id=tRXt10xKc5). NeurIPS 2025. ContextAgentBench evaluates proactive assistants that combine sensory context, persona signals, and tool use.
- [EverMemBench: A Benchmark for Evaluating Long-Term Interactive Memory in LLMs](https://arxiv.org/abs/2602.01313). ArXiv 2026. Evaluates long-term memory across multi-party collaborative dialogues with 1M+ token histories, temporal reasoning, and persona-consistent recall. [![GitHub Repo stars](https://img.shields.io/github/stars/EverMind-AI/EverMemBench)](https://github.com/EverMind-AI/EverMemBench)
- [PersonaMem](https://openreview.net/forum?id=6ox8XZGOqP). COLM 2025. Dynamic user profiling benchmark for evaluating how LLMs internalize user traits and track evolving preferences across multiple sessions (~1M tokens). [![GitHub Repo stars](https://img.shields.io/github/stars/bowen-upenn/PersonaMem)](https://github.com/bowen-upenn/PersonaMem)
- [PersonaMem-v2: Towards Personalized Intelligence via Learning Implicit User Personas and Agentic Memory](https://arxiv.org/abs/2512.06688). ArXiv 2025. Advanced personalization benchmark and training framework for learning implicit user personas and agentic memory via reinforcement fine-tuning. [![GitHub Repo stars](https://img.shields.io/github/stars/bowen-upenn/PersonaMem-v2)](https://github.com/bowen-upenn/PersonaMem-v2)

### Enterprise and Workflow

- [MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research](https://openreview.net/forum?id=JX9DE6colf). NeurIPS 2025. Benchmark for scientific research agents with 201 open-ended ML research tasks, staged evaluation from ideation to paper writing, and automated judging via MLR-Judge. [![GitHub Repo stars](https://img.shields.io/github/stars/chchenhui/mlrbench)](https://github.com/chchenhui/mlrbench)
- [ScienceBoard](https://arxiv.org/abs/2505.19897). ArXiv 2025. Scientific workflow environment for research-task agents. [![GitHub Repo stars](https://img.shields.io/github/stars/OS-Copilot/ScienceBoard)](https://github.com/OS-Copilot/ScienceBoard)
- [DefenderBench](https://openreview.net/forum?id=BtZBwwjO5d). SEA @ NeurIPS 2025. Defensive benchmark for agents operating inside security-sensitive workflow settings. [![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/DefenderBench)](https://github.com/microsoft/DefenderBench)
- [TheAgentCompany](https://openreview.net/forum?id=LZnKNApvhG). NeurIPS 2025. Enterprise-style benchmark covering long-horizon workplace tasks. [![GitHub Repo stars](https://img.shields.io/github/stars/TheAgentCompany/TheAgentCompany)](https://github.com/TheAgentCompany/TheAgentCompany)
- [OfficeBench](https://arxiv.org/abs/2407.19056). ArXiv 2024. Office productivity benchmark spanning documents, spreadsheets, slides, and email-style tasks. [![GitHub Repo stars](https://img.shields.io/github/stars/zlwang-cs/OfficeBench)](https://github.com/zlwang-cs/OfficeBench)

## Environment Generation and Scaling

### Programmatic Synthesis

- [GUI-GENESIS](https://arxiv.org/abs/2602.14093). ArXiv 2026. Automated synthesis of efficient GUI environments with verifiable rewards.
- [WebArena-Infinity](https://github.com/web-arena-x/webarena-infinity). 2026. Generates browser environments with verifiable tasks at scale using multi-agent automation. [![GitHub Repo stars](https://img.shields.io/github/stars/web-arena-x/webarena-infinity)](https://github.com/web-arena-x/webarena-infinity)
- [LLM-in-Sandbox](https://arxiv.org/abs/2601.16206). ArXiv 2026. Sandbox-first environment design showing broad gains from letting models explore a virtual computer.
- [Safe and Scalable Web Agent Learning via Recreated Websites](https://arxiv.org/abs/2603.10505). DEFI 2025. VeriEnv recreates real websites into executable, verifiable training environments for safe web-agent learning.
- [Simulating Environments with Reasoning Models for Agent Training](https://arxiv.org/abs/2511.01824). ArXiv 2025. Uses reasoning models to simulate environment feedback for scalable SFT and RL agent training without hand-written environment code.
- [SWE-Factory](https://arxiv.org/abs/2506.10954). ArXiv 2025. Automated factory for issue-resolution training data and benchmark generation. [![GitHub Repo stars](https://img.shields.io/github/stars/DeepSoftwareAnalytics/swe-factory)](https://github.com/DeepSoftwareAnalytics/swe-factory)
- [Toucan](https://arxiv.org/abs/2510.01179). ArXiv 2025. Environment and data generation pipeline around real MCP-style tool ecosystems. [![GitHub Repo stars](https://img.shields.io/github/stars/TheAgentArk/Toucan)](https://github.com/TheAgentArk/Toucan)
- [OS-Genesis](https://aclanthology.org/2025.acl-long.277/). ACL 2025. Reverse task synthesis pipeline for generating GUI-agent trajectories.

### Model-Based Simulation

- [Code2World: A GUI World Model via Renderable Code Generation](https://arxiv.org/abs/2602.09856). CVPR 2026. GUI world model that predicts next UI states through renderable code generation, with code available from AMAP-ML. [![GitHub Repo stars](https://img.shields.io/github/stars/AMAP-ML/Code2World)](https://github.com/AMAP-ML/Code2World)
- [Agent World Model](https://arxiv.org/abs/2602.10090). ArXiv 2026. Fully synthetic code-driven environments backed by databases and tool APIs. [![GitHub Repo stars](https://img.shields.io/github/stars/Snowflake-Labs/agent-world-model)](https://github.com/Snowflake-Labs/agent-world-model)
- [WebWorld](https://arxiv.org/abs/2602.14721). ArXiv 2026. Large-scale world model for open-web agent training.
- [Reinforcement World Model Learning for LLM-based Agents](https://arxiv.org/abs/2602.05842). ArXiv 2026. Self-supervised world-model learning method that aligns simulated next states with real environment transitions.
- [VirtualEnv](https://arxiv.org/abs/2601.07553). ArXiv 2026. Open-source simulated platform with procedurally generated tasks and game-inspired mechanics.
- [ViMo: A Generative Visual GUI World Model for App Agent](https://arxiv.org/abs/2504.13936). ArXiv 2025. Visual GUI world model for app agents that generates future GUI observations as images and text. [![GitHub Repo stars](https://img.shields.io/github/stars/ai-agents-2030/ViMo)](https://github.com/ai-agents-2030/ViMo)
- [LLMs as Scalable, General-Purpose Simulators For Evolving Digital Agent Training](https://arxiv.org/abs/2510.14969). ArXiv 2025. Uses LLM-based simulators as scalable digital training worlds for evolving agent capabilities across changing environments.
- [Internalizing World Models via Self-Play Finetuning for Agentic RL](https://arxiv.org/abs/2510.15047). ArXiv 2025. Improves agentic RL by internalizing latent world models through self-play fine-tuning.
- [Dyna-Mind: Learning to Simulate from Experience for Better AI Agents](https://arxiv.org/abs/2510.09577). ArXiv 2025. Teaches agents to internalize simulation traces from experience and improve long-horizon decision making.
- [WebDreamer](https://arxiv.org/abs/2411.06559). ArXiv 2024. Web world-model direction for simulated web interaction and planning.

### Environment Scaling Methods

- [Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data](https://arxiv.org/abs/2602.21320). ArXiv 2026. Self-play framework that co-evolves a task generator and solver to bootstrap tool-use training without external task data.
- [EnvScaler](https://arxiv.org/abs/2601.05808). ArXiv 2026. Programmatic scaling of tool-interactive environments and verifiable scenarios. [![GitHub Repo stars](https://img.shields.io/github/stars/RUC-NLPIR/EnvScaler)](https://github.com/RUC-NLPIR/EnvScaler)
- [ScaleEnv](https://arxiv.org/abs/2602.06820). ArXiv 2026. From-scratch scaling of generalist tool-use environments with executable verification.
- [Adaptive Environment Generation for Embodied Agents](https://arxiv.org/abs/2602.06366). ArXiv 2026. Adaptive scene generation driven by current agent competence.
- [GenEnv: Difficulty-Aligned Co-Evolution Between LLM Agents and Environment Simulators](https://arxiv.org/abs/2512.19682). ArXiv 2025. Co-trains agents with a generative environment simulator that adaptively proposes tasks near the agent's current capability boundary. [![GitHub Repo stars](https://img.shields.io/github/stars/Gen-Verse/GenEnv)](https://github.com/Gen-Verse/GenEnv)
- [Towards General Agentic Intelligence via Environment Scaling](https://arxiv.org/abs/2509.13311). ArXiv 2025. Studies how expanding environment diversity and agent experience can improve generalist tool-use agents.
- [Scaling Agent Learning via Experience Synthesis](https://arxiv.org/abs/2511.03773). ArXiv 2025. Introduces DreamGym, a framework that synthesizes scalable agent experiences for online RL training.
- [Agent Learning via Early Experience](https://arxiv.org/abs/2510.08558). ArXiv 2025. Learns from future states generated by the agent's own actions, bridging imitation learning and full RL.
- [RLVE](https://arxiv.org/abs/2511.07317). ArXiv 2025. Adaptive verifiable environments for reinforcement learning over language models. [![GitHub Repo stars](https://img.shields.io/github/stars/Zhiyuan-Zeng/RLVE)](https://github.com/Zhiyuan-Zeng/RLVE)

## Sandboxes and Infrastructure

### Sandbox Platforms

- [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview). 2026. Anthropic's managed agent runtime with configurable cloud environments, hosted execution, built-in tools, and persistent sessions. Docs: [Environment setup](https://platform.claude.com/docs/en/managed-agents/environments), [Container reference](https://platform.claude.com/docs/en/managed-agents/cloud-containers), [Start a session](https://platform.claude.com/docs/en/managed-agents/sessions).
- [AEnvironment](https://github.com/inclusionAI/AEnvironment). 2026. Production-grade environment platform built around "Everything as Environment", unifying benchmark integration, agentic RL training, and agent deployment behind a standardized interface. [![GitHub Repo stars](https://img.shields.io/github/stars/inclusionAI/AEnvironment)](https://github.com/inclusionAI/AEnvironment)
- [ROCK](https://github.com/alibaba/ROCK). 2026. Environment and sandbox management framework with a client-server architecture, unified SDKs, and scalable runtime orchestration for agent training workloads. [![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/ROCK)](https://github.com/alibaba/ROCK)
- [OpenSandbox](https://github.com/alibaba/OpenSandbox). 2026. General-purpose sandbox platform for AI applications with unified sandbox APIs, Docker/Kubernetes runtimes, and built-in coding and GUI environments. [![GitHub Repo stars](https://img.shields.io/github/stars/alibaba/OpenSandbox)](https://github.com/alibaba/OpenSandbox)
- [AIO Sandbox](https://github.com/agent-infra/sandbox). 2025. All-in-one sandbox combining browser, shell, file, MCP, and VSCode Server in a single Docker container with MCP-compatible APIs. [![GitHub Repo stars](https://img.shields.io/github/stars/agent-infra/sandbox)](https://github.com/agent-infra/sandbox)
- [Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox). 2025. Kubernetes SIGs project for managing isolated, stateful, singleton workloads through a Sandbox CRD and controller, designed for AI agent runtimes. [![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes-sigs/agent-sandbox)](https://github.com/kubernetes-sigs/agent-sandbox)
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

- [OSGym: Scalable OS Infrastructure for Computer Use Agents](https://arxiv.org/abs/2511.11672). ArXiv 2025. Large-scale OS training infrastructure for computer-use agents with 1024 parallel sandboxes, aggressive disk deduplication, and RAM-bound orchestration.
- [Knative](https://github.com/knative/serving). 2018. Serverless layer on Kubernetes for elastic agent backends. [![GitHub Repo stars](https://img.shields.io/github/stars/knative/serving)](https://github.com/knative/serving)
- [Cloudflare Workers](https://developers.cloudflare.com/workers/reference/how-workers-works/). 2018. Isolate-based edge execution model relevant to ultra-fast agent serving and sandboxing.
- [Kubernetes](https://github.com/kubernetes/kubernetes). 2014. Cluster orchestrator for multi-tenant agent runtimes and sandbox scheduling. [![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes/kubernetes)](https://github.com/kubernetes/kubernetes)
- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html). 2014. Serverless compute platform with snapshot-backed execution semantics relevant to agent workloads.
