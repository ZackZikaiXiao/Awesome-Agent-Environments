# Awesome Agent Environments

<div align="center">
  <p align="center">
    <a href="docs/explore.html">🧭 Explorer</a> |
    <a href="docs/taxonomy.md">📝 Taxonomy Notes</a> |
    <a href="https://github.com/ZackZikaiXiao/Awesome-Agent-Environments">🌐 GitHub</a>
  </p>
</div>

<div align="center">

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-red)](https://github.com/ZackZikaiXiao/Awesome-Agent-Environments/pulls)

</div>

This repository collects environments, benchmarks, simulators, sandboxes, and companion infrastructure for training and evaluating AI agents.

It is intentionally broader than a benchmark-only list: besides the worlds agents act in, it also tracks the systems used to synthesize, host, verify, benchmark, and secure those worlds.

⭐ Live GitHub star badges are shown when a public repository exists, so the displayed counts stay current without hard-coding numbers.

🧭 For interactive filtering, open [Explorer](docs/explore.html). It supports interactive filtering, optional click/impression analytics, and per-project CTR tracking.

## Contents

- [Awesome Agent Environments](#awesome-agent-environments)
  - [Contents](#contents)
  - [🧭 Overview](#overview)
    - [Scope](#scope)
  - [🌍 Environment Collections](#environment-collections)
    - [Foundational Environment Systems](#foundational-environment-systems)
    - [Web Environments](#web-environments)
    - [Desktop, GUI, and Mobile Environments](#desktop-gui-and-mobile-environments)
    - [Coding, Terminal, and ML Engineering Environments](#coding-terminal-and-ml-engineering-environments)
    - [Tool, API, and App Environments](#tool-api-and-app-environments)
    - [Enterprise and Workflow Environments](#enterprise-and-workflow-environments)
    - [Embodied, Game, and Social Environments](#embodied-game-and-social-environments)
  - [🏗️ Construction and Infrastructure](#construction-and-infrastructure)
    - [Synthetic Environments and Environment Scaling](#synthetic-environments-and-environment-scaling)
    - [Runtime, Sandbox, and Isolation Infrastructure](#runtime-sandbox-and-isolation-infrastructure)
    - [Orchestration, Serverless, and Platform Engineering](#orchestration-serverless-and-platform-engineering)
    - [Protocols, Standards, and Capability Interfaces](#protocols-standards-and-capability-interfaces)
    - [Observability and Debugging](#observability-and-debugging)
    - [Evaluation Harnesses and Companion Ecosystems](#evaluation-harnesses-and-companion-ecosystems)
    - [Safety, Security, and Robustness](#safety-security-and-robustness)
  - [📚 Supporting Material](#supporting-material)
    - [Surveys and Reading Lists](#surveys-and-reading-lists)
    - [Contributing](#contributing)

## Overview

### Scope

Included:

- Reusable agent environments and benchmarks
- Training gyms and executable task suites
- Environment synthesis and environment scaling systems
- Runtime and sandbox infrastructure used to host agents safely
- Evaluation harnesses tightly coupled to agent environments
- Safety and robustness testbeds for agents

Excluded by default:

- Pure agent frameworks with no reusable environment or benchmark
- Pure model papers with no environment contribution
- Generic tooling unless it is directly used to build, host, or evaluate agent environments

For a longer Chinese write-up on definitions, classification axes, development patterns, and construction methods, see [docs/taxonomy.md](docs/taxonomy.md).

## Environment Collections

### Foundational Environment Systems

- [OpenAI Gym](https://github.com/openai/gym) [![GitHub Repo stars](https://img.shields.io/github/stars/openai/gym)](https://github.com/openai/gym) - The original de facto standard API for reinforcement learning environments.
- [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) [![GitHub Repo stars](https://img.shields.io/github/stars/Farama-Foundation/Gymnasium)](https://github.com/Farama-Foundation/Gymnasium) - Community-maintained continuation of Gym with modernized APIs and compatibility.
- [AEnvironment](https://github.com/inclusionAI/AEnvironment) [![GitHub Repo stars](https://img.shields.io/github/stars/inclusionAI/AEnvironment)](https://github.com/inclusionAI/AEnvironment) - Standardized environment infrastructure for Agentic AI development.
- [AgentBench](https://github.com/THUDM/AgentBench) [![GitHub Repo stars](https://img.shields.io/github/stars/THUDM/AgentBench)](https://github.com/THUDM/AgentBench) - Early broad benchmark suite covering multiple agent settings and task families.
- [VisualAgentBench](https://github.com/THUDM/VisualAgentBench) [![GitHub Repo stars](https://img.shields.io/github/stars/THUDM/VisualAgentBench)](https://github.com/THUDM/VisualAgentBench) - Visual and multimodal benchmark family for environment-grounded agents.
- [CRAB](https://github.com/camel-ai/crab) [![GitHub Repo stars](https://img.shields.io/github/stars/camel-ai/crab)](https://github.com/camel-ai/crab) - A cross-environment benchmark for computer-use and embodied-style agent tasks.
- [Procgen Benchmark](https://github.com/openai/procgen) [![GitHub Repo stars](https://img.shields.io/github/stars/openai/procgen)](https://github.com/openai/procgen) - Procedurally generated RL benchmark emphasizing generalization across environment instances.
- [MiniGrid](https://github.com/Farama-Foundation/Minigrid) [![GitHub Repo stars](https://img.shields.io/github/stars/Farama-Foundation/Minigrid)](https://github.com/Farama-Foundation/Minigrid) - Lightweight gridworld benchmark for instruction following and planning.
- [EnvPool](https://github.com/sail-sg/envpool) [![GitHub Repo stars](https://img.shields.io/github/stars/sail-sg/envpool)](https://github.com/sail-sg/envpool) - High-throughput environment execution engine for large-scale RL training.
- [RLlib](https://github.com/ray-project/ray) [![GitHub Repo stars](https://img.shields.io/github/stars/ray-project/ray)](https://github.com/ray-project/ray) - Distributed RL and agent framework with strong environment-parallelism abstractions.
- [Acme](https://github.com/google-deepmind/acme) [![GitHub Repo stars](https://img.shields.io/github/stars/google-deepmind/acme)](https://github.com/google-deepmind/acme) - DeepMind's RL framework for modular agents, actors, and environments.
- [NVIDIA NeMo Gym](https://github.com/NVIDIA-NeMo/Gym) [![GitHub Repo stars](https://img.shields.io/github/stars/NVIDIA-NeMo/Gym)](https://github.com/NVIDIA-NeMo/Gym) - Gym-style infrastructure for training and evaluating agentic systems.

### Web Environments

- [MiniWoB++](https://github.com/Farama-Foundation/miniwob-plusplus) [![GitHub Repo stars](https://img.shields.io/github/stars/Farama-Foundation/miniwob-plusplus)](https://github.com/Farama-Foundation/miniwob-plusplus) - Canonical lightweight browser tasks for web interaction agents.
- [WebShop](https://github.com/princeton-nlp/WebShop) [![GitHub Repo stars](https://img.shields.io/github/stars/princeton-nlp/WebShop)](https://github.com/princeton-nlp/WebShop) - Shopping environment for instruction following and decision making on realistic storefronts.
- [Mind2Web](https://github.com/OSU-NLP-Group/Mind2Web) [![GitHub Repo stars](https://img.shields.io/github/stars/OSU-NLP-Group/Mind2Web)](https://github.com/OSU-NLP-Group/Mind2Web) - Real-world web task dataset and benchmark grounded in live websites.
- [Online-Mind2Web](https://arxiv.org/abs/2504.01382) - Online extension of Mind2Web for live and dynamic web interaction.
- [WebArena](https://github.com/web-arena-x/webarena) [![GitHub Repo stars](https://img.shields.io/github/stars/web-arena-x/webarena)](https://github.com/web-arena-x/webarena) - Self-hostable benchmark built from cloned web services.
- [WebArena-Infinity](https://github.com/web-arena-x/webarena-infinity) [![GitHub Repo stars](https://img.shields.io/github/stars/web-arena-x/webarena-infinity)](https://github.com/web-arena-x/webarena-infinity) - Generating browser environments with verifiable tasks at scale using multi-agent automation.
- [VisualWebArena](https://github.com/web-arena-x/visualwebarena) [![GitHub Repo stars](https://img.shields.io/github/stars/web-arena-x/visualwebarena)](https://github.com/web-arena-x/visualwebarena) - Multimodal extension of WebArena with richer visual grounding.
- [WebVoyager](https://github.com/MinorJerry/WebVoyager) [![GitHub Repo stars](https://img.shields.io/github/stars/MinorJerry/WebVoyager)](https://github.com/MinorJerry/WebVoyager) - Open-web browsing benchmark and agent setup for realistic live website interaction.
- [WorkArena](https://github.com/ServiceNow/WorkArena) [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/WorkArena)](https://github.com/ServiceNow/WorkArena) - BrowserGym-compatible enterprise web tasks built on ServiceNow workflows.
- [WorkArena++](https://arxiv.org/abs/2407.05291) - Harder successor benchmark expanding task realism and difficulty for enterprise web agents.
- [AssistantBench](https://arxiv.org/abs/2407.15711) - Web-assisted benchmark for complex, realistic assistant tasks.
- [WebLINX](https://github.com/McGill-NLP/WebLINX) [![GitHub Repo stars](https://img.shields.io/github/stars/McGill-NLP/WebLINX)](https://github.com/McGill-NLP/WebLINX) - Browser interaction benchmark and dataset focused on long, realistic web sessions.
- [FieldWorkArena](https://github.com/FujitsuResearch/FieldWorkArena) [![GitHub Repo stars](https://img.shields.io/github/stars/FujitsuResearch/FieldWorkArena)](https://github.com/FujitsuResearch/FieldWorkArena) - Benchmark for field-service style workflows conducted through enterprise web interfaces.
- [WebChoreArena](https://arxiv.org/abs/2509.13177) - Cross-page and multi-step web chores benchmark designed to break shortcut-heavy web agents.

### Desktop, GUI, and Mobile Environments

- [OSWorld](https://github.com/xlang-ai/OSWorld) [![GitHub Repo stars](https://img.shields.io/github/stars/xlang-ai/OSWorld)](https://github.com/xlang-ai/OSWorld) - Full operating-system benchmark with real desktop applications and scripted verification.
- [WindowsAgentArena](https://github.com/microsoft/WindowsAgentArena) [![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/WindowsAgentArena)](https://github.com/microsoft/WindowsAgentArena) - Windows-native desktop benchmark for GUI agents.
- [AndroidWorld](https://github.com/google-research/android_world) [![GitHub Repo stars](https://img.shields.io/github/stars/google-research/android_world)](https://github.com/google-research/android_world) - Android task suite for mobile agent evaluation and training.
- [MobileWorld](https://arxiv.org/abs/2512.19432) - Harder mobile benchmark built to stay ahead of rapidly saturating phone-use agents.
- [OSExpert](https://arxiv.org/abs/2603.07978) - Harder desktop benchmark targeting professional software usage beyond commodity OS tasks.

### Coding, Terminal, and ML Engineering Environments

- [SWE-bench](https://github.com/SWE-bench/SWE-bench) [![GitHub Repo stars](https://img.shields.io/github/stars/SWE-bench/SWE-bench)](https://github.com/SWE-bench/SWE-bench) - Standard issue-resolution benchmark built from real GitHub repositories and tests.
- [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) [![GitHub Repo stars](https://img.shields.io/github/stars/SWE-Gym/SWE-Gym)](https://github.com/SWE-Gym/SWE-Gym) - Public training environment for software engineering agents and verifiers.
- [R2E-Gym](https://github.com/R2E-Gym/R2E-Gym) [![GitHub Repo stars](https://img.shields.io/github/stars/R2E-Gym/R2E-Gym)](https://github.com/R2E-Gym/R2E-Gym) - Procedural environment generation and hybrid verifiers for open-weight SWE agents.
- [Debug-Gym](https://github.com/microsoft/debug-gym) [![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/debug-gym)](https://github.com/microsoft/debug-gym) - Text-based interactive debugging environment with debugger-aware agent loops.
- [Hybrid-Gym](https://github.com/yiqingxyq/Hybrid-Gym) [![GitHub Repo stars](https://img.shields.io/github/stars/yiqingxyq/Hybrid-Gym)](https://github.com/yiqingxyq/Hybrid-Gym) - Coding-agent training environment aimed at cross-task generalization.
- [Terminal-Bench](https://github.com/laude-institute/terminal-bench) [![GitHub Repo stars](https://img.shields.io/github/stars/laude-institute/terminal-bench)](https://github.com/laude-institute/terminal-bench) - Verifiable terminal benchmark for shell-based agents.
- [TerminalTraj](https://github.com/Wusiwei0410/TerminalTraj) [![GitHub Repo stars](https://img.shields.io/github/stars/Wusiwei0410/TerminalTraj)](https://github.com/Wusiwei0410/TerminalTraj) - Large-scale verified terminal trajectories collected from dockerized environments.
- [MLE-bench](https://github.com/openai/mle-bench) [![GitHub Repo stars](https://img.shields.io/github/stars/openai/mle-bench)](https://github.com/openai/mle-bench) - End-to-end machine learning engineering benchmark.
- [MLE-Dojo](https://github.com/MLE-Dojo/MLE-Dojo) [![GitHub Repo stars](https://img.shields.io/github/stars/MLE-Dojo/MLE-Dojo)](https://github.com/MLE-Dojo/MLE-Dojo) - Training and evaluation environment for ML engineering agents.
- [MLGym](https://github.com/facebookresearch/MLGym) [![GitHub Repo stars](https://img.shields.io/github/stars/facebookresearch/MLGym)](https://github.com/facebookresearch/MLGym) - Gym-style benchmark for ML research and engineering tasks.
- [GitTaskBench](https://github.com/QuantaAlpha/GitTaskBench) [![GitHub Repo stars](https://img.shields.io/github/stars/QuantaAlpha/GitTaskBench)](https://github.com/QuantaAlpha/GitTaskBench) - Git-centric task benchmark for repository manipulation agents.
- [SWE-Factory](https://github.com/DeepSoftwareAnalytics/swe-factory) [![GitHub Repo stars](https://img.shields.io/github/stars/DeepSoftwareAnalytics/swe-factory)](https://github.com/DeepSoftwareAnalytics/swe-factory) - Automated factory for issue-resolution training data and benchmark generation.

### Tool, API, and App Environments

- [tau-bench](https://github.com/sierra-research/tau-bench) [![GitHub Repo stars](https://img.shields.io/github/stars/sierra-research/tau-bench)](https://github.com/sierra-research/tau-bench) - Tool-use benchmark centered on customer-support and business-rule-heavy agent tasks.
- [tau2-bench](https://github.com/sierra-research/tau2-bench) [![GitHub Repo stars](https://img.shields.io/github/stars/sierra-research/tau2-bench)](https://github.com/sierra-research/tau2-bench) - Harder successor benchmark with dual-control and richer environment dynamics.
- [Tau^3-bench](https://github.com/sierra-research/tau2-bench) [![GitHub Repo stars](https://img.shields.io/github/stars/sierra-research/tau2-bench)](https://github.com/sierra-research/tau2-bench) - Harder successor benchmark to τ²-bench adding full-duplex voice interaction, knowledge retrieval, and refined task quality.
- [AppWorld](https://github.com/StonyBrookNLP/appworld) [![GitHub Repo stars](https://img.shields.io/github/stars/StonyBrookNLP/appworld)](https://github.com/StonyBrookNLP/appworld) - App-centric benchmark for multi-tool and multi-app task completion.
- [Toolathlon](https://github.com/hkust-nlp/Toolathlon) [![GitHub Repo stars](https://img.shields.io/github/stars/hkust-nlp/Toolathlon)](https://github.com/hkust-nlp/Toolathlon) - A benchmark for language agents featuring 600+ diverse tools across 32 real-world software applications with long-horizon tasks and execution-based evaluation.
- [ToolSandbox](https://github.com/apple/ToolSandbox) [![GitHub Repo stars](https://img.shields.io/github/stars/apple/ToolSandbox)](https://github.com/apple/ToolSandbox) - Controlled environment for tool-using agents with rich API-level task design.
- [MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe) [![GitHub Repo stars](https://img.shields.io/github/stars/SalesforceAIResearch/MCP-Universe)](https://github.com/SalesforceAIResearch/MCP-Universe) - Benchmarking framework using real-world MCP servers instead of simulated tools.
- [MCPMark](https://github.com/eval-sys/mcpmark) [![GitHub Repo stars](https://img.shields.io/github/stars/eval-sys/mcpmark)](https://github.com/eval-sys/mcpmark) - A comprehensive evaluation suite for agentic models that stress-tests tool usage across real MCP services like Notion, GitHub, and Postgres.
- [Toucan](https://github.com/TheAgentArk/Toucan) [![GitHub Repo stars](https://img.shields.io/github/stars/TheAgentArk/Toucan)](https://github.com/TheAgentArk/Toucan) - Environment and data generation pipeline around real MCP-style tool ecosystems.

### Enterprise and Workflow Environments

- [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany) [![GitHub Repo stars](https://img.shields.io/github/stars/TheAgentCompany/TheAgentCompany)](https://github.com/TheAgentCompany/TheAgentCompany) - Enterprise-style benchmark covering long-horizon workplace tasks.
- [OfficeBench](https://github.com/zlwang-cs/OfficeBench) [![GitHub Repo stars](https://img.shields.io/github/stars/zlwang-cs/OfficeBench)](https://github.com/zlwang-cs/OfficeBench) - Office productivity benchmark spanning documents, spreadsheets, slides, and email-style tasks.
- [ScienceBoard](https://github.com/OS-Copilot/ScienceBoard) [![GitHub Repo stars](https://img.shields.io/github/stars/OS-Copilot/ScienceBoard)](https://github.com/OS-Copilot/ScienceBoard) - Scientific workflow environment for research-task agents.

### Embodied, Game, and Social Environments

- [TextWorld](https://github.com/microsoft/TextWorld) [![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/TextWorld)](https://github.com/microsoft/TextWorld) - Text-based reinforcement learning framework for interactive fiction and long-horizon reasoning.
- [ScienceWorld](https://github.com/allenai/ScienceWorld) [![GitHub Repo stars](https://img.shields.io/github/stars/allenai/ScienceWorld)](https://github.com/allenai/ScienceWorld) - Text-based scientific experimentation environment.
- [ALFWorld](https://github.com/alfworld/alfworld) [![GitHub Repo stars](https://img.shields.io/github/stars/alfworld/alfworld)](https://github.com/alfworld/alfworld) - Text + embodied household benchmark bridging language and action.
- [VirtualHome](https://github.com/xavierpuigf/virtualhome) [![GitHub Repo stars](https://img.shields.io/github/stars/xavierpuigf/virtualhome)](https://github.com/xavierpuigf/virtualhome) - Household activity simulator with rich programmatic supervision.
- [AI2-THOR](https://github.com/allenai/ai2thor) [![GitHub Repo stars](https://img.shields.io/github/stars/allenai/ai2thor)](https://github.com/allenai/ai2thor) - Interactive 3D environment for embodied AI tasks.
- [Habitat-Lab](https://github.com/facebookresearch/habitat-lab) [![GitHub Repo stars](https://img.shields.io/github/stars/facebookresearch/habitat-lab)](https://github.com/facebookresearch/habitat-lab) - Research platform for embodied navigation and manipulation.
- [Habitat 2.0](https://aihabitat.org/) - Large-scale embodied benchmark stack integrating simulation, datasets, and tasks.
- [Isaac Gym](https://developer.nvidia.com/isaac-gym) - GPU-native robotics simulation for massively parallel RL.
- [Isaac Lab](https://github.com/isaac-sim/IsaacLab) [![GitHub Repo stars](https://img.shields.io/github/stars/isaac-sim/IsaacLab)](https://github.com/isaac-sim/IsaacLab) - Successor stack for scalable robot learning and simulation on NVIDIA platforms.
- [ManiSkill](https://github.com/haosulab/ManiSkill) [![GitHub Repo stars](https://img.shields.io/github/stars/haosulab/ManiSkill)](https://github.com/haosulab/ManiSkill) - Fast, scalable benchmark suite for manipulation agents.
- [MineRL](https://github.com/minerllabs/minerl) [![GitHub Repo stars](https://img.shields.io/github/stars/minerllabs/minerl)](https://github.com/minerllabs/minerl) - Minecraft benchmark and data ecosystem for long-horizon agents.
- [NetHack Learning Environment](https://github.com/facebookresearch/nle) [![GitHub Repo stars](https://img.shields.io/github/stars/facebookresearch/nle)](https://github.com/facebookresearch/nle) - Roguelike benchmark for long-horizon exploration and planning.
- [DiscoveryWorld](https://github.com/allenai/discoveryworld) [![GitHub Repo stars](https://img.shields.io/github/stars/allenai/discoveryworld)](https://github.com/allenai/discoveryworld) - Open-ended simulated world for scientific and interactive reasoning.
- [Sotopia](https://github.com/sotopia-lab/sotopia) [![GitHub Repo stars](https://img.shields.io/github/stars/sotopia-lab/sotopia)](https://github.com/sotopia-lab/sotopia) - Open-ended social learning environment for language agents.
- [Sotopia-pi](https://github.com/sotopia-lab/sotopia-pi) [![GitHub Repo stars](https://img.shields.io/github/stars/sotopia-lab/sotopia-pi)](https://github.com/sotopia-lab/sotopia-pi) - Preference and interaction stack extending Sotopia-style social evaluation.
- [ChatArena](https://github.com/Farama-Foundation/chatarena) [![GitHub Repo stars](https://img.shields.io/github/stars/Farama-Foundation/chatarena)](https://github.com/Farama-Foundation/chatarena) - Multi-agent language game environments for collaboration and competition.
- [AdaSociety](https://github.com/bigai-ai/AdaSociety) [![GitHub Repo stars](https://img.shields.io/github/stars/bigai-ai/AdaSociety)](https://github.com/bigai-ai/AdaSociety) - Multi-agent environment with expanding state/action spaces and explicit social structure.

## Construction and Infrastructure

### Synthetic Environments and Environment Scaling

- [OS-Genesis](https://arxiv.org/abs/2412.19723) - Reverse task synthesis pipeline for generating GUI-agent trajectories.
- [EnvScaler](https://github.com/RUC-NLPIR/EnvScaler) [![GitHub Repo stars](https://img.shields.io/github/stars/RUC-NLPIR/EnvScaler)](https://github.com/RUC-NLPIR/EnvScaler) - Programmatic synthesis of tool-interactive environments and verifiable scenarios.
- [ScaleEnv](https://arxiv.org/abs/2602.06820) - From-scratch synthesis of generalist tool-use environments with executable verification.
- [Agent World Model](https://github.com/Snowflake-Labs/agent-world-model) [![GitHub Repo stars](https://img.shields.io/github/stars/Snowflake-Labs/agent-world-model)](https://github.com/Snowflake-Labs/agent-world-model) - Fully synthetic code-driven environments backed by databases and tool APIs.
- [WebWorld](https://arxiv.org/abs/2602.14721) - Large-scale world model for open-web agent training.
- [GUI-GENESIS](https://arxiv.org/abs/2602.14093) - Automated synthesis of efficient GUI environments with verifiable rewards.
- [RLVE](https://github.com/Zhiyuan-Zeng/RLVE) [![GitHub Repo stars](https://img.shields.io/github/stars/Zhiyuan-Zeng/RLVE)](https://github.com/Zhiyuan-Zeng/RLVE) - Adaptive verifiable environments for reinforcement learning over language models.
- [AgentScaler](https://arxiv.org/abs/2509.13311) - Environment scaling for function-calling and heterogeneous tool-use agents.
- [WebDreamer](https://arxiv.org/abs/2411.06559) - Web world-model direction for simulated web interaction and planning.
- [VirtualEnv](https://arxiv.org/abs/2601.07553) - Open-source embodied platform with procedurally generated tasks and game-inspired mechanics.
- [Adaptive Environment Generation for Embodied Agents](https://arxiv.org/abs/2602.06366) - Adaptive scene generation driven by current agent competence.
- [Dreamer 4](https://arxiv.org/abs/2509.24527) - Scalable world-model training in imagination, including complex Minecraft-style tasks.
- [LLM-in-Sandbox](https://arxiv.org/abs/2601.16206) - General sandbox-first environment design showing broad gains from letting models explore a virtual computer.

### Runtime, Sandbox, and Isolation Infrastructure

- [OCI Runtime Spec](https://github.com/opencontainers/runtime-spec) [![GitHub Repo stars](https://img.shields.io/github/stars/opencontainers/runtime-spec)](https://github.com/opencontainers/runtime-spec) - Standard for how container runtimes launch and manage container bundles.
- [OCI Image Spec](https://github.com/opencontainers/image-spec) [![GitHub Repo stars](https://img.shields.io/github/stars/opencontainers/image-spec)](https://github.com/opencontainers/image-spec) - Standard image format used across container-based agent environments.
- [runc](https://github.com/opencontainers/runc) [![GitHub Repo stars](https://img.shields.io/github/stars/opencontainers/runc)](https://github.com/opencontainers/runc) - Reference OCI runtime used under much of the modern container stack.
- [containerd](https://github.com/containerd/containerd) [![GitHub Repo stars](https://img.shields.io/github/stars/containerd/containerd)](https://github.com/containerd/containerd) - Core container runtime layer used by many sandboxed and orchestrated agent systems.
- [Docker](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) - The default container abstraction used across many agent benchmarks and training gyms.
- [Firecracker](https://github.com/firecracker-microvm/firecracker) [![GitHub Repo stars](https://img.shields.io/github/stars/firecracker-microvm/firecracker)](https://github.com/firecracker-microvm/firecracker) - MicroVM runtime for stronger isolation than process-level containers.
- [firecracker-containerd](https://github.com/firecracker-microvm/firecracker-containerd) [![GitHub Repo stars](https://img.shields.io/github/stars/firecracker-microvm/firecracker-containerd)](https://github.com/firecracker-microvm/firecracker-containerd) - Containerd integration for launching container workloads inside Firecracker microVMs.
- [gVisor](https://github.com/google/gvisor) [![GitHub Repo stars](https://img.shields.io/github/stars/google/gvisor)](https://github.com/google/gvisor) - User-space kernel that hardens container isolation for untrusted workloads.
- [Kata Containers](https://github.com/kata-containers/kata-containers) [![GitHub Repo stars](https://img.shields.io/github/stars/kata-containers/kata-containers)](https://github.com/kata-containers/kata-containers) - Lightweight VMs that look like containers to orchestration systems.
- [Confidential Containers](https://github.com/confidential-containers) [![GitHub Repo stars](https://img.shields.io/github/stars/confidential-containers/trustee)](https://github.com/confidential-containers) - Confidential-computing stack for running container workloads inside attested trusted environments.
- [E2B](https://github.com/e2b-dev/E2B) [![GitHub Repo stars](https://img.shields.io/github/stars/e2b-dev/E2B)](https://github.com/e2b-dev/E2B) - Managed cloud sandboxes for code-interpreter and agent workloads.
- [E2B Desktop Sandbox](https://github.com/e2b-dev/desktop) [![GitHub Repo stars](https://img.shields.io/github/stars/e2b-dev/desktop)](https://github.com/e2b-dev/desktop) - Browser and desktop sandbox for computer-use style agents.
- [Kubernetes Agent Sandbox](https://developers.googleblog.com/en/announcing-kubernetes-agent-sandbox/) - Google's direction for standardizing sandboxed agent runtimes on Kubernetes.
- [Fault-Tolerant Sandboxing for LLM Agents](https://arxiv.org/abs/2512.12806) - Research on resilient sandbox execution for long-running agent systems.

### Orchestration, Serverless, and Platform Engineering

- [Kubernetes](https://github.com/kubernetes/kubernetes) [![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes/kubernetes)](https://github.com/kubernetes/kubernetes) - The default cluster orchestrator for multi-tenant agent runtimes and sandbox scheduling.
- [Knative](https://github.com/knative/serving) [![GitHub Repo stars](https://img.shields.io/github/stars/knative/serving)](https://github.com/knative/serving) - Serverless layer on Kubernetes for request-driven workloads and elastic agent backends.
- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) - Serverless compute platform that publicly documents microVM-backed execution and snapshotting.
- [Cloudflare Workers](https://developers.cloudflare.com/workers/reference/how-workers-works/) - Isolate-based edge execution model relevant to ultra-fast agent sandboxing.
- [Borg](https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/) - Foundational cluster-management paper shaping later orchestration systems used for large agent fleets.

### Protocols, Standards, and Capability Interfaces

- [Model Context Protocol](https://modelcontextprotocol.io/) - Standardized capability interface for connecting models to tools, data, and external systems.
- [Wasmtime](https://github.com/bytecodealliance/wasmtime) [![GitHub Repo stars](https://img.shields.io/github/stars/bytecodealliance/wasmtime)](https://github.com/bytecodealliance/wasmtime) - WebAssembly runtime that enables portable capability-bounded execution.
- [WASI](https://github.com/WebAssembly/WASI) [![GitHub Repo stars](https://img.shields.io/github/stars/WebAssembly/WASI)](https://github.com/WebAssembly/WASI) - Capability-oriented system interface for WebAssembly modules.
- [Bytecode Alliance](https://github.com/bytecodealliance) - Consortium driving portable and capability-safe Wasm execution ecosystems.
- [Open Container Initiative](https://github.com/opencontainers) - Standards body behind the container formats and runtime interfaces that underpin many agent sandboxes.

### Observability and Debugging

- [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-specification) [![GitHub Repo stars](https://img.shields.io/github/stars/open-telemetry/opentelemetry-specification)](https://github.com/open-telemetry/opentelemetry-specification) - Unified traces, metrics, and logs specification for distributed agent platforms.
- [eBPF](https://ebpf.io/) - Kernel-level programmable observability layer widely used for container and sandbox introspection.
- [Process Monitor](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon) - Windows activity tracing tool useful for understanding GUI-agent side effects and OS interactions.
- [Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) - Broader Windows diagnostic toolkit family for agent-environment debugging.
- [S2E](https://github.com/S2E/s2e) [![GitHub Repo stars](https://img.shields.io/github/stars/S2E/s2e)](https://github.com/S2E/s2e) - Selective symbolic execution platform for deep system analysis and adversarial environment testing.
- [Kubernetes Ephemeral Containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) - Standard pattern for debugging slim or distroless agent runtime pods in place.

### Evaluation Harnesses and Companion Ecosystems

- [BrowserGym](https://github.com/ServiceNow/BrowserGym) [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/BrowserGym)](https://github.com/ServiceNow/BrowserGym) - Unified Gym-style interface spanning multiple browser and enterprise environments.
- [AgentLab](https://github.com/ServiceNow/AgentLab) [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/AgentLab)](https://github.com/ServiceNow/AgentLab) - Experiment and evaluation layer built around BrowserGym environments.
- [OpenHands Benchmarks](https://github.com/OpenHands/benchmarks) [![GitHub Repo stars](https://img.shields.io/github/stars/OpenHands/benchmarks)](https://github.com/OpenHands/benchmarks) - Benchmark collections and execution harnesses for coding and agent tasks.
- [AgentRewardBench](https://github.com/McGill-NLP/agent-reward-bench) [![GitHub Repo stars](https://img.shields.io/github/stars/McGill-NLP/agent-reward-bench)](https://github.com/McGill-NLP/agent-reward-bench) - Reward-model benchmark tailored to agent trajectories and task outcomes.
- [tale-suite](https://github.com/microsoft/tale-suite) [![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/tale-suite)](https://github.com/microsoft/tale-suite) - Task and agent lifecycle evaluation suite for agentic systems.
- [METR Task Standard](https://github.com/METR/task-standard) [![GitHub Repo stars](https://img.shields.io/github/stars/METR/task-standard)](https://github.com/METR/task-standard) - Task specification standard aimed at more reproducible agent evaluation.
- [PettingZoo](https://github.com/Farama-Foundation/PettingZoo) [![GitHub Repo stars](https://img.shields.io/github/stars/Farama-Foundation/PettingZoo)](https://github.com/Farama-Foundation/PettingZoo) - Standard API and reference environments for multi-agent RL research.
- [GroundCUA](https://github.com/ServiceNow/GroundCUA) [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/GroundCUA)](https://github.com/ServiceNow/GroundCUA) - Grounding and dataset layer for computer-use agents, complementary to GUI environments.

### Safety, Security, and Robustness

- [AgentDojo](https://github.com/ethz-spylab/agentdojo) [![GitHub Repo stars](https://img.shields.io/github/stars/ethz-spylab/agentdojo)](https://github.com/ethz-spylab/agentdojo) - Security benchmark for tool-using agents under adversarial and policy-constrained settings.
- [DoomArena](https://github.com/ServiceNow/DoomArena) [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/DoomArena)](https://github.com/ServiceNow/DoomArena) - Stress-testing environment for robust and adversarial browser-agent behavior.
- [ASB](https://github.com/agiresearch/ASB) [![GitHub Repo stars](https://img.shields.io/github/stars/agiresearch/ASB)](https://github.com/agiresearch/ASB) - Agent security benchmark suite for evaluating attack surfaces and unsafe behavior.
- [DefenderBench](https://github.com/microsoft/DefenderBench) [![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/DefenderBench)](https://github.com/microsoft/DefenderBench) - Defensive evaluation benchmark for agent systems operating under security constraints.
- [ToolEmu](https://github.com/ryoungj/ToolEmu) [![GitHub Repo stars](https://img.shields.io/github/stars/ryoungj/ToolEmu)](https://github.com/ryoungj/ToolEmu) - Sandbox for emulating risky tool-use scenarios and evaluating tool-agent safety.
- [OS-Harm](https://github.com/tml-epfl/os-harm) [![GitHub Repo stars](https://img.shields.io/github/stars/tml-epfl/os-harm)](https://github.com/tml-epfl/os-harm) - Harm benchmark for computer-use agents operating over OS-like environments.

## Supporting Material

### Surveys and Reading Lists

- [Taxonomy Notes](docs/taxonomy.md) - Chinese notes on definitions, classification axes, development patterns, and construction methods.
- [Environment Scaling for Interactive Agentic Experience Collection: A Survey](https://arxiv.org/abs/2511.09586) - Survey centered on environment scaling as a training axis.
- [A Compendium of LLM Benchmarks for Agents](https://github.com/philschmid/ai-agent-benchmark-compendium) [![GitHub Repo stars](https://img.shields.io/github/stars/philschmid/ai-agent-benchmark-compendium)](https://github.com/philschmid/ai-agent-benchmark-compendium) - Broad benchmark map with many adjacent agent-evaluation resources.
- [GUI Agents Paper List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) [![GitHub Repo stars](https://img.shields.io/github/stars/OSU-NLP-Group/GUI-Agents-Paper-List)](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) - Curated reading list for GUI-agent research.
- [AgentSafety Paper List](https://github.com/OSU-NLP-Group/AgentSafety) [![GitHub Repo stars](https://img.shields.io/github/stars/OSU-NLP-Group/AgentSafety)](https://github.com/OSU-NLP-Group/AgentSafety) - Reading list focused on agent safety and security.

### Contributing

Contributions are welcome. A good contribution usually includes:

- the official repository, project page, or paper link
- a one-line description of what the environment contributes
- a rationale for why the project belongs here as an environment, environment builder, sandbox, or harness

If a project fits multiple sections, prefer one primary section instead of duplicating it everywhere.
