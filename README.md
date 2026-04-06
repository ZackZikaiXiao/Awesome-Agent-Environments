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

- [Scope](#scope)
- [How This List Is Organized](#how-this-list-is-organized)
- [Agent Environments](#agent-environments)
  - [Web Environments](#web-environments)
  - [Computer-Use Environments](#computer-use-environments)
  - [Coding and Terminal Environments](#coding-and-terminal-environments)
  - [Tool and API Environments](#tool-and-api-environments)
  - [Enterprise and Workflow Environments](#enterprise-and-workflow-environments)
- [Environment Generation and Scaling](#environment-generation-and-scaling)
  - [Programmatic and Synthetic Generation](#programmatic-and-synthetic-generation)
  - [World Models and Learned Simulators](#world-models-and-learned-simulators)
  - [Environment Scaling Methods](#environment-scaling-methods)
- [Sandboxes and Infrastructure](#sandboxes-and-infrastructure)
  - [Sandbox Platforms](#sandbox-platforms)
  - [Runtime and Isolation](#runtime-and-isolation)
  - [Deployment and Orchestration](#deployment-and-orchestration)

## Scope

Included:

- Reusable agent environments and task suites
- Training environments and executable benchmarks
- Environment generation and environment scaling work
- Sandboxes and infrastructure used to host agent environments

Excluded by default:

- Pure agent frameworks with no reusable environment contribution
- Pure model papers with no environment contribution
- Generic infrastructure that is not directly useful for building or running agent environments

## How This List Is Organized

This list is organized around three questions:

- Where do agents act
- How are new environments generated and scaled
- How are these environments hosted safely and operated in practice

## Agent Environments

### Web Environments

- [MiniWoB++](https://github.com/Farama-Foundation/miniwob-plusplus) [![GitHub Repo stars](https://img.shields.io/github/stars/Farama-Foundation/miniwob-plusplus)](https://github.com/Farama-Foundation/miniwob-plusplus) - Canonical lightweight browser tasks for web interaction agents.
- [WebShop](https://github.com/princeton-nlp/WebShop) [![GitHub Repo stars](https://img.shields.io/github/stars/princeton-nlp/WebShop)](https://github.com/princeton-nlp/WebShop) - Shopping environment for instruction following and decision making on realistic storefronts.
- [Mind2Web](https://github.com/OSU-NLP-Group/Mind2Web) [![GitHub Repo stars](https://img.shields.io/github/stars/OSU-NLP-Group/Mind2Web)](https://github.com/OSU-NLP-Group/Mind2Web) - Real-world web task dataset and benchmark grounded in live websites.
- [Online-Mind2Web](https://arxiv.org/abs/2504.01382) - Online extension of Mind2Web for live and dynamic web interaction.
- [WebArena](https://github.com/web-arena-x/webarena) [![GitHub Repo stars](https://img.shields.io/github/stars/web-arena-x/webarena)](https://github.com/web-arena-x/webarena) - Self-hostable benchmark built from cloned web services.
- [VisualWebArena](https://github.com/web-arena-x/visualwebarena) [![GitHub Repo stars](https://img.shields.io/github/stars/web-arena-x/visualwebarena)](https://github.com/web-arena-x/visualwebarena) - Multimodal extension of WebArena with richer visual grounding.
- [WebVoyager](https://github.com/MinorJerry/WebVoyager) [![GitHub Repo stars](https://img.shields.io/github/stars/MinorJerry/WebVoyager)](https://github.com/MinorJerry/WebVoyager) - Open-web browsing benchmark and agent setup for realistic live website interaction.
- [WorkArena](https://github.com/ServiceNow/WorkArena) [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/WorkArena)](https://github.com/ServiceNow/WorkArena) - BrowserGym-compatible enterprise web tasks built on ServiceNow workflows.
- [WorkArena++](https://arxiv.org/abs/2407.05291) - Harder successor benchmark expanding task realism and difficulty for enterprise web agents.
- [AssistantBench](https://arxiv.org/abs/2407.15711) - Web-assisted benchmark for complex, realistic assistant tasks.
- [WebLINX](https://github.com/McGill-NLP/WebLINX) [![GitHub Repo stars](https://img.shields.io/github/stars/McGill-NLP/WebLINX)](https://github.com/McGill-NLP/WebLINX) - Browser interaction benchmark and dataset focused on long, realistic web sessions.
- [FieldWorkArena](https://github.com/FujitsuResearch/FieldWorkArena) [![GitHub Repo stars](https://img.shields.io/github/stars/FujitsuResearch/FieldWorkArena)](https://github.com/FujitsuResearch/FieldWorkArena) - Benchmark for field-service style workflows conducted through enterprise web interfaces.
- [WebChoreArena](https://arxiv.org/abs/2509.13177) - Cross-page and multi-step web chores benchmark designed to break shortcut-heavy web agents.
- [BrowserGym](https://github.com/ServiceNow/BrowserGym) [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/BrowserGym)](https://github.com/ServiceNow/BrowserGym) - Unified Gym-style interface spanning multiple browser and enterprise web environments.
- [AgentLab](https://github.com/ServiceNow/AgentLab) [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/AgentLab)](https://github.com/ServiceNow/AgentLab) - Experiment layer built around BrowserGym environments.
- [DoomArena](https://github.com/ServiceNow/DoomArena) [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/DoomArena)](https://github.com/ServiceNow/DoomArena) - Stress-testing environment for robust and adversarial browser-agent behavior.

### Computer-Use Environments

- [OSWorld](https://github.com/xlang-ai/OSWorld) [![GitHub Repo stars](https://img.shields.io/github/stars/xlang-ai/OSWorld)](https://github.com/xlang-ai/OSWorld) - Full operating-system benchmark with real desktop applications and scripted verification.
- [WindowsAgentArena](https://github.com/microsoft/WindowsAgentArena) [![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/WindowsAgentArena)](https://github.com/microsoft/WindowsAgentArena) - Windows-native desktop benchmark for GUI agents.
- [AndroidWorld](https://github.com/google-research/android_world) [![GitHub Repo stars](https://img.shields.io/github/stars/google-research/android_world)](https://github.com/google-research/android_world) - Android task suite for mobile agent evaluation and training.
- [MobileWorld](https://arxiv.org/abs/2512.19432) - Harder mobile benchmark built to stay ahead of rapidly saturating phone-use agents.
- [OSExpert](https://arxiv.org/abs/2603.07978) - Harder desktop benchmark targeting professional software usage beyond commodity OS tasks.
- [CRAB](https://github.com/camel-ai/crab) [![GitHub Repo stars](https://img.shields.io/github/stars/camel-ai/crab)](https://github.com/camel-ai/crab) - Cross-environment benchmark covering computer-use and agent interaction tasks.
- [GroundCUA](https://github.com/ServiceNow/GroundCUA) [![GitHub Repo stars](https://img.shields.io/github/stars/ServiceNow/GroundCUA)](https://github.com/ServiceNow/GroundCUA) - Grounding and dataset layer for computer-use agents, complementary to GUI environments.
- [OS-Harm](https://github.com/tml-epfl/os-harm) [![GitHub Repo stars](https://img.shields.io/github/stars/tml-epfl/os-harm)](https://github.com/tml-epfl/os-harm) - Harm benchmark for computer-use agents operating over OS-like environments.

### Coding and Terminal Environments

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
- [OpenHands Benchmarks](https://github.com/OpenHands/benchmarks) [![GitHub Repo stars](https://img.shields.io/github/stars/OpenHands/benchmarks)](https://github.com/OpenHands/benchmarks) - Benchmark collections and execution harnesses for coding and software-agent tasks.

### Tool and API Environments

- [tau-bench](https://github.com/sierra-research/tau-bench) [![GitHub Repo stars](https://img.shields.io/github/stars/sierra-research/tau-bench)](https://github.com/sierra-research/tau-bench) - Tool-use benchmark centered on customer-support and business-rule-heavy agent tasks.
- [tau2-bench](https://github.com/sierra-research/tau2-bench) [![GitHub Repo stars](https://img.shields.io/github/stars/sierra-research/tau2-bench)](https://github.com/sierra-research/tau2-bench) - Harder successor benchmark with dual-control and richer environment dynamics.
- [Tau^3-bench](https://github.com/sierra-research/tau2-bench) [![GitHub Repo stars](https://img.shields.io/github/stars/sierra-research/tau2-bench)](https://github.com/sierra-research/tau2-bench) - Harder successor to tau2-bench adding full-duplex voice interaction, retrieval, and refined task design.
- [AppWorld](https://github.com/StonyBrookNLP/appworld) [![GitHub Repo stars](https://img.shields.io/github/stars/StonyBrookNLP/appworld)](https://github.com/StonyBrookNLP/appworld) - App-centric environment for multi-tool and multi-app task completion.
- [Toolathlon](https://github.com/hkust-nlp/Toolathlon) [![GitHub Repo stars](https://img.shields.io/github/stars/hkust-nlp/Toolathlon)](https://github.com/hkust-nlp/Toolathlon) - Benchmark featuring 600+ tools across real-world software applications with execution-based evaluation.
- [ToolSandbox](https://github.com/apple/ToolSandbox) [![GitHub Repo stars](https://img.shields.io/github/stars/apple/ToolSandbox)](https://github.com/apple/ToolSandbox) - Controlled environment for tool-using agents with rich API-level task design.
- [MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe) [![GitHub Repo stars](https://img.shields.io/github/stars/SalesforceAIResearch/MCP-Universe)](https://github.com/SalesforceAIResearch/MCP-Universe) - Benchmarking framework using real-world MCP servers instead of simulated tools.
- [MCPMark](https://github.com/eval-sys/mcpmark) [![GitHub Repo stars](https://img.shields.io/github/stars/eval-sys/mcpmark)](https://github.com/eval-sys/mcpmark) - Evaluation suite that stress-tests tool usage across real MCP services.
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) [![GitHub Repo stars](https://img.shields.io/github/stars/ethz-spylab/agentdojo)](https://github.com/ethz-spylab/agentdojo) - Security benchmark for tool-using agents under adversarial and policy-constrained settings.
- [ToolEmu](https://github.com/ryoungj/ToolEmu) [![GitHub Repo stars](https://img.shields.io/github/stars/ryoungj/ToolEmu)](https://github.com/ryoungj/ToolEmu) - Sandbox for emulating risky tool-use scenarios and evaluating tool-agent safety.
- [ASB](https://github.com/agiresearch/ASB) [![GitHub Repo stars](https://img.shields.io/github/stars/agiresearch/ASB)](https://github.com/agiresearch/ASB) - Agent security benchmark suite for evaluating attack surfaces and unsafe tool behavior.

### Enterprise and Workflow Environments

- [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany) [![GitHub Repo stars](https://img.shields.io/github/stars/TheAgentCompany/TheAgentCompany)](https://github.com/TheAgentCompany/TheAgentCompany) - Enterprise-style benchmark covering long-horizon workplace tasks.
- [OfficeBench](https://github.com/zlwang-cs/OfficeBench) [![GitHub Repo stars](https://img.shields.io/github/stars/zlwang-cs/OfficeBench)](https://github.com/zlwang-cs/OfficeBench) - Office productivity benchmark spanning documents, spreadsheets, slides, and email-style tasks.
- [ScienceBoard](https://github.com/OS-Copilot/ScienceBoard) [![GitHub Repo stars](https://img.shields.io/github/stars/OS-Copilot/ScienceBoard)](https://github.com/OS-Copilot/ScienceBoard) - Scientific workflow environment for research-task agents.
- [DefenderBench](https://github.com/microsoft/DefenderBench) [![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/DefenderBench)](https://github.com/microsoft/DefenderBench) - Defensive benchmark for agents operating inside security-sensitive workflow settings.

## Environment Generation and Scaling

### Programmatic and Synthetic Generation

- [OS-Genesis](https://arxiv.org/abs/2412.19723) - Reverse task synthesis pipeline for generating GUI-agent trajectories.
- [GUI-GENESIS](https://arxiv.org/abs/2602.14093) - Automated synthesis of efficient GUI environments with verifiable rewards.
- [WebArena-Infinity](https://github.com/web-arena-x/webarena-infinity) [![GitHub Repo stars](https://img.shields.io/github/stars/web-arena-x/webarena-infinity)](https://github.com/web-arena-x/webarena-infinity) - Generates browser environments with verifiable tasks at scale using multi-agent automation.
- [SWE-Factory](https://github.com/DeepSoftwareAnalytics/swe-factory) [![GitHub Repo stars](https://img.shields.io/github/stars/DeepSoftwareAnalytics/swe-factory)](https://github.com/DeepSoftwareAnalytics/swe-factory) - Automated factory for issue-resolution training data and benchmark generation.
- [Toucan](https://github.com/TheAgentArk/Toucan) [![GitHub Repo stars](https://img.shields.io/github/stars/TheAgentArk/Toucan)](https://github.com/TheAgentArk/Toucan) - Environment and data generation pipeline around real MCP-style tool ecosystems.
- [LLM-in-Sandbox](https://arxiv.org/abs/2601.16206) - Sandbox-first environment design showing broad gains from letting models explore a virtual computer.

### World Models and Learned Simulators

- [Agent World Model](https://github.com/Snowflake-Labs/agent-world-model) [![GitHub Repo stars](https://img.shields.io/github/stars/Snowflake-Labs/agent-world-model)](https://github.com/Snowflake-Labs/agent-world-model) - Fully synthetic code-driven environments backed by databases and tool APIs.
- [WebWorld](https://arxiv.org/abs/2602.14721) - Large-scale world model for open-web agent training.
- [WebDreamer](https://arxiv.org/abs/2411.06559) - Web world-model direction for simulated web interaction and planning.
- [Dreamer 4](https://arxiv.org/abs/2509.24527) - Scalable world-model training in imagination, including complex Minecraft-style tasks.
- [VirtualEnv](https://arxiv.org/abs/2601.07553) - Open-source simulated platform with procedurally generated tasks and game-inspired mechanics.

### Environment Scaling Methods

- [EnvScaler](https://github.com/RUC-NLPIR/EnvScaler) [![GitHub Repo stars](https://img.shields.io/github/stars/RUC-NLPIR/EnvScaler)](https://github.com/RUC-NLPIR/EnvScaler) - Programmatic scaling of tool-interactive environments and verifiable scenarios.
- [ScaleEnv](https://arxiv.org/abs/2602.06820) - From-scratch scaling of generalist tool-use environments with executable verification.
- [RLVE](https://github.com/Zhiyuan-Zeng/RLVE) [![GitHub Repo stars](https://img.shields.io/github/stars/Zhiyuan-Zeng/RLVE)](https://github.com/Zhiyuan-Zeng/RLVE) - Adaptive verifiable environments for reinforcement learning over language models.
- [AgentScaler](https://arxiv.org/abs/2509.13311) - Environment scaling for function-calling and heterogeneous tool-use agents.
- [Adaptive Environment Generation for Embodied Agents](https://arxiv.org/abs/2602.06366) - Adaptive scene generation driven by current agent competence.

## Sandboxes and Infrastructure

### Sandbox Platforms

- [E2B](https://github.com/e2b-dev/E2B) [![GitHub Repo stars](https://img.shields.io/github/stars/e2b-dev/E2B)](https://github.com/e2b-dev/E2B) - Cloud sandboxes for code-interpreter and agent workloads.
- [E2B Desktop Sandbox](https://github.com/e2b-dev/desktop) [![GitHub Repo stars](https://img.shields.io/github/stars/e2b-dev/desktop)](https://github.com/e2b-dev/desktop) - Browser and desktop sandbox for computer-use style agents.
- [Kubernetes Agent Sandbox](https://developers.googleblog.com/en/announcing-kubernetes-agent-sandbox/) - Google's direction for standardizing sandboxed agent runtimes on Kubernetes.
- [Fault-Tolerant Sandboxing for LLM Agents](https://arxiv.org/abs/2512.12806) - Research on resilient sandbox execution for long-running agent systems.

### Runtime and Isolation

- [OCI Runtime Spec](https://github.com/opencontainers/runtime-spec) [![GitHub Repo stars](https://img.shields.io/github/stars/opencontainers/runtime-spec)](https://github.com/opencontainers/runtime-spec) - Standard for how container runtimes launch and manage container bundles.
- [OCI Image Spec](https://github.com/opencontainers/image-spec) [![GitHub Repo stars](https://img.shields.io/github/stars/opencontainers/image-spec)](https://github.com/opencontainers/image-spec) - Standard image format used across container-based agent environments.
- [runc](https://github.com/opencontainers/runc) [![GitHub Repo stars](https://img.shields.io/github/stars/opencontainers/runc)](https://github.com/opencontainers/runc) - Reference OCI runtime used under much of the modern container stack.
- [containerd](https://github.com/containerd/containerd) [![GitHub Repo stars](https://img.shields.io/github/stars/containerd/containerd)](https://github.com/containerd/containerd) - Core container runtime layer used by many sandboxed and orchestrated agent systems.
- [Docker](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) - Default container abstraction used across many agent benchmarks and training gyms.
- [Firecracker](https://github.com/firecracker-microvm/firecracker) [![GitHub Repo stars](https://img.shields.io/github/stars/firecracker-microvm/firecracker)](https://github.com/firecracker-microvm/firecracker) - MicroVM runtime for stronger isolation than process-level containers.
- [firecracker-containerd](https://github.com/firecracker-microvm/firecracker-containerd) [![GitHub Repo stars](https://img.shields.io/github/stars/firecracker-microvm/firecracker-containerd)](https://github.com/firecracker-microvm/firecracker-containerd) - Containerd integration for launching workloads inside Firecracker microVMs.
- [gVisor](https://github.com/google/gvisor) [![GitHub Repo stars](https://img.shields.io/github/stars/google/gvisor)](https://github.com/google/gvisor) - User-space kernel that hardens container isolation for untrusted workloads.
- [Kata Containers](https://github.com/kata-containers/kata-containers) [![GitHub Repo stars](https://img.shields.io/github/stars/kata-containers/kata-containers)](https://github.com/kata-containers/kata-containers) - Lightweight VMs that look like containers to orchestration systems.
- [Confidential Containers](https://github.com/confidential-containers) [![GitHub Repo stars](https://img.shields.io/github/stars/confidential-containers/trustee)](https://github.com/confidential-containers) - Confidential-computing stack for running workloads inside attested trusted environments.
- [Wasmtime](https://github.com/bytecodealliance/wasmtime) [![GitHub Repo stars](https://img.shields.io/github/stars/bytecodealliance/wasmtime)](https://github.com/bytecodealliance/wasmtime) - WebAssembly runtime for portable and capability-bounded execution.
- [WASI](https://github.com/WebAssembly/WASI) [![GitHub Repo stars](https://img.shields.io/github/stars/WebAssembly/WASI)](https://github.com/WebAssembly/WASI) - Capability-oriented system interface for sandboxed WebAssembly modules.

### Deployment and Orchestration

- [Kubernetes](https://github.com/kubernetes/kubernetes) [![GitHub Repo stars](https://img.shields.io/github/stars/kubernetes/kubernetes)](https://github.com/kubernetes/kubernetes) - Cluster orchestrator for multi-tenant agent runtimes and sandbox scheduling.
- [Knative](https://github.com/knative/serving) [![GitHub Repo stars](https://img.shields.io/github/stars/knative/serving)](https://github.com/knative/serving) - Serverless layer on Kubernetes for elastic agent backends.
- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) - Serverless compute platform with snapshot-backed execution semantics relevant to agent workloads.
- [Cloudflare Workers](https://developers.cloudflare.com/workers/reference/how-workers-works/) - Isolate-based edge execution model relevant to ultra-fast agent serving and sandboxing.
