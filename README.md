# Awesome Agent Environments

> A curated list of environments, benchmarks, simulators, sandboxes, and companion infrastructure for training and evaluating AI agents.

This repository treats "agent environment" broadly: not only the interactive worlds that agents act in, but also the systems that synthesize, host, verify, benchmark, and secure those worlds.

Live GitHub star badges are used where a public repository exists, so the displayed star counts stay current without hard-coding numbers.

For interactive filtering, open [docs/explore.html](docs/explore.html). It supports multi-tag selection, both `match any` and `match all` filtering modes, and optional click/impression analytics for per-project CTR tracking.

## Contents

- [Scope](#scope)
- [Taxonomy](#taxonomy)
- [Foundational Environment Systems](#foundational-environment-systems)
- [Web Environments](#web-environments)
- [Desktop, GUI, and Mobile Environments](#desktop-gui-and-mobile-environments)
- [Coding, Terminal, and ML Engineering Environments](#coding-terminal-and-ml-engineering-environments)
- [Tool, API, and App Environments](#tool-api-and-app-environments)
- [Enterprise and Workflow Environments](#enterprise-and-workflow-environments)
- [Embodied, Game, and Social Environments](#embodied-game-and-social-environments)
- [Synthetic Environments and Environment Scaling](#synthetic-environments-and-environment-scaling)
- [Runtime, Sandbox, and Isolation Infrastructure](#runtime-sandbox-and-isolation-infrastructure)
- [Orchestration, Serverless, and Platform Engineering](#orchestration-serverless-and-platform-engineering)
- [Protocols, Standards, and Capability Interfaces](#protocols-standards-and-capability-interfaces)
- [Observability and Debugging](#observability-and-debugging)
- [Evaluation Harnesses and Companion Ecosystems](#evaluation-harnesses-and-companion-ecosystems)
- [Safety, Security, and Robustness](#safety-security-and-robustness)
- [Surveys and Reading Lists](#surveys-and-reading-lists)
- [Contributing](#contributing)

## Scope

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

## Taxonomy

This list uses one primary section per project plus lightweight tags. The tags encode the orthogonal views that are harder to express with a single table-of-contents tree.

- Fidelity: `real` `self-hosted` `llm-sim` `synthetic` `world-model`
- Domain: `web` `gui` `mobile` `coding` `terminal` `tool-use` `enterprise` `workflow` `embodied` `game` `social` `science` `multi-domain`
- Purpose: `eval` `train` `train+eval`
- Verification: `fully-verifiable` `partially-verifiable` `llm-judge` `human`
- Infra: `platform` `sandbox` `runtime` `orchestration` `serverless` `protocol` `observability` `harness` `security` `standard`

For a longer Chinese write-up on definitions, trends, and construction patterns, see [docs/taxonomy.md](docs/taxonomy.md).

## Foundational Environment Systems

- [OpenAI Gym](https://github.com/openai/gym) ![stars](https://img.shields.io/github/stars/openai/gym?style=flat-square) - The original de facto standard API for reinforcement learning environments. Tags: `platform` `multi-domain` `train+eval` `standard`
- [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) ![stars](https://img.shields.io/github/stars/Farama-Foundation/Gymnasium?style=flat-square) - Community-maintained continuation of Gym with modernized APIs and compatibility. Tags: `platform` `multi-domain` `train+eval` `standard`
- [AEnvironment](https://github.com/inclusionAI/AEnvironment) ![stars](https://img.shields.io/github/stars/inclusionAI/AEnvironment?style=flat-square) - Standardized environment infrastructure for Agentic AI development. Tags: `platform` `multi-domain` `train+eval`
- [AgentBench](https://github.com/THUDM/AgentBench) ![stars](https://img.shields.io/github/stars/THUDM/AgentBench?style=flat-square) - Early broad benchmark suite covering multiple agent settings and task families. Tags: `platform` `multi-domain` `eval`
- [VisualAgentBench](https://github.com/THUDM/VisualAgentBench) ![stars](https://img.shields.io/github/stars/THUDM/VisualAgentBench?style=flat-square) - Visual and multimodal benchmark family for environment-grounded agents. Tags: `platform` `gui` `web` `eval`
- [CRAB](https://github.com/camel-ai/crab) ![stars](https://img.shields.io/github/stars/camel-ai/crab?style=flat-square) - A cross-environment benchmark for computer-use and embodied-style agent tasks. Tags: `platform` `multi-domain` `eval`
- [Procgen Benchmark](https://github.com/openai/procgen) ![stars](https://img.shields.io/github/stars/openai/procgen?style=flat-square) - Procedurally generated RL benchmark emphasizing generalization across environment instances. Tags: `platform` `game` `synthetic` `train+eval`
- [MiniGrid](https://github.com/Farama-Foundation/Minigrid) ![stars](https://img.shields.io/github/stars/Farama-Foundation/Minigrid?style=flat-square) - Lightweight gridworld benchmark for instruction following and planning. Tags: `platform` `game` `synthetic` `train+eval`
- [EnvPool](https://github.com/sail-sg/envpool) ![stars](https://img.shields.io/github/stars/sail-sg/envpool?style=flat-square) - High-throughput environment execution engine for large-scale RL training. Tags: `platform` `runtime` `train`
- [RLlib](https://github.com/ray-project/ray) ![stars](https://img.shields.io/github/stars/ray-project/ray?style=flat-square) - Distributed RL and agent framework with strong environment-parallelism abstractions. Tags: `platform` `multi-domain` `train`
- [Acme](https://github.com/google-deepmind/acme) ![stars](https://img.shields.io/github/stars/google-deepmind/acme?style=flat-square) - DeepMind's RL framework for modular agents, actors, and environments. Tags: `platform` `multi-domain` `train`
- [NVIDIA NeMo Gym](https://github.com/NVIDIA-NeMo/Gym) ![stars](https://img.shields.io/github/stars/NVIDIA-NeMo/Gym?style=flat-square) - Gym-style infrastructure for training and evaluating agentic systems. Tags: `platform` `train+eval` `harness`

## Web Environments

- [MiniWoB++](https://github.com/Farama-Foundation/miniwob-plusplus) ![stars](https://img.shields.io/github/stars/Farama-Foundation/miniwob-plusplus?style=flat-square) - Canonical lightweight browser tasks for web interaction agents. Tags: `web` `self-hosted` `eval` `fully-verifiable`
- [WebShop](https://github.com/princeton-nlp/WebShop) ![stars](https://img.shields.io/github/stars/princeton-nlp/WebShop?style=flat-square) - Shopping environment for instruction following and decision making on realistic storefronts. Tags: `web` `self-hosted` `train+eval` `partially-verifiable`
- [Mind2Web](https://github.com/OSU-NLP-Group/Mind2Web) ![stars](https://img.shields.io/github/stars/OSU-NLP-Group/Mind2Web?style=flat-square) - Real-world web task dataset and benchmark grounded in live websites. Tags: `web` `real` `eval`
- [Online-Mind2Web](https://arxiv.org/abs/2504.01382) - Online extension of Mind2Web for live and dynamic web interaction. Tags: `web` `real` `eval`
- [WebArena](https://github.com/web-arena-x/webarena) ![stars](https://img.shields.io/github/stars/web-arena-x/webarena?style=flat-square) - Self-hostable benchmark built from cloned web services. Tags: `web` `self-hosted` `eval` `partially-verifiable`
- [WebArena-Infinity](https://github.com/web-arena-x/webarena-infinity) ![stars](https://img.shields.io/github/stars/web-arena-x/webarena-infinity?style=flat-square) - Generating browser environments with verifiable tasks at scale using multi-agent automation. Tags: `web` `synthetic` `train+eval` `fully-verifiable`
- [VisualWebArena](https://github.com/web-arena-x/visualwebarena) ![stars](https://img.shields.io/github/stars/web-arena-x/visualwebarena?style=flat-square) - Multimodal extension of WebArena with richer visual grounding. Tags: `web` `self-hosted` `eval`
- [WebVoyager](https://github.com/MinorJerry/WebVoyager) ![stars](https://img.shields.io/github/stars/MinorJerry/WebVoyager?style=flat-square) - Open-web browsing benchmark and agent setup for realistic live website interaction. Tags: `web` `real` `eval` `llm-judge`
- [WorkArena](https://github.com/ServiceNow/WorkArena) ![stars](https://img.shields.io/github/stars/ServiceNow/WorkArena?style=flat-square) - BrowserGym-compatible enterprise web tasks built on ServiceNow workflows. Tags: `web` `self-hosted` `enterprise` `eval`
- [WorkArena++](https://arxiv.org/abs/2407.05291) - Harder successor benchmark expanding task realism and difficulty for enterprise web agents. Tags: `web` `enterprise` `eval`
- [AssistantBench](https://arxiv.org/abs/2407.15711) - Web-assisted benchmark for complex, realistic assistant tasks. Tags: `web` `real` `eval`
- [WebLINX](https://github.com/McGill-NLP/WebLINX) ![stars](https://img.shields.io/github/stars/McGill-NLP/WebLINX?style=flat-square) - Browser interaction benchmark and dataset focused on long, realistic web sessions. Tags: `web` `eval`
- [FieldWorkArena](https://github.com/FujitsuResearch/FieldWorkArena) ![stars](https://img.shields.io/github/stars/FujitsuResearch/FieldWorkArena?style=flat-square) - Benchmark for field-service style workflows conducted through enterprise web interfaces. Tags: `web` `enterprise` `eval`
- [WebChoreArena](https://arxiv.org/abs/2509.13177) - Cross-page and multi-step web chores benchmark designed to break shortcut-heavy web agents. Tags: `web` `eval`

## Desktop, GUI, and Mobile Environments

- [OSWorld](https://github.com/xlang-ai/OSWorld) ![stars](https://img.shields.io/github/stars/xlang-ai/OSWorld?style=flat-square) - Full operating-system benchmark with real desktop applications and scripted verification. Tags: `gui` `real` `eval` `partially-verifiable`
- [WindowsAgentArena](https://github.com/microsoft/WindowsAgentArena) ![stars](https://img.shields.io/github/stars/microsoft/WindowsAgentArena?style=flat-square) - Windows-native desktop benchmark for GUI agents. Tags: `gui` `real` `eval`
- [AndroidWorld](https://github.com/google-research/android_world) ![stars](https://img.shields.io/github/stars/google-research/android_world?style=flat-square) - Android task suite for mobile agent evaluation and training. Tags: `mobile` `real` `train+eval`
- [MobileWorld](https://arxiv.org/abs/2512.19432) - Harder mobile benchmark built to stay ahead of rapidly saturating phone-use agents. Tags: `mobile` `eval`
- [OSExpert](https://arxiv.org/abs/2603.07978) - Harder desktop benchmark targeting professional software usage beyond commodity OS tasks. Tags: `gui` `eval`

## Coding, Terminal, and ML Engineering Environments

- [SWE-bench](https://github.com/SWE-bench/SWE-bench) ![stars](https://img.shields.io/github/stars/SWE-bench/SWE-bench?style=flat-square) - Standard issue-resolution benchmark built from real GitHub repositories and tests. Tags: `coding` `terminal` `eval` `fully-verifiable`
- [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) ![stars](https://img.shields.io/github/stars/SWE-Gym/SWE-Gym?style=flat-square) - Public training environment for software engineering agents and verifiers. Tags: `coding` `train` `fully-verifiable`
- [R2E-Gym](https://github.com/R2E-Gym/R2E-Gym) ![stars](https://img.shields.io/github/stars/R2E-Gym/R2E-Gym?style=flat-square) - Procedural environment generation and hybrid verifiers for open-weight SWE agents. Tags: `coding` `train` `fully-verifiable` `synthetic`
- [Debug-Gym](https://github.com/microsoft/debug-gym) ![stars](https://img.shields.io/github/stars/microsoft/debug-gym?style=flat-square) - Text-based interactive debugging environment with debugger-aware agent loops. Tags: `coding` `terminal` `train+eval`
- [Hybrid-Gym](https://github.com/yiqingxyq/Hybrid-Gym) ![stars](https://img.shields.io/github/stars/yiqingxyq/Hybrid-Gym?style=flat-square) - Coding-agent training environment aimed at cross-task generalization. Tags: `coding` `train`
- [Terminal-Bench](https://github.com/laude-institute/terminal-bench) ![stars](https://img.shields.io/github/stars/laude-institute/terminal-bench?style=flat-square) - Verifiable terminal benchmark for shell-based agents. Tags: `terminal` `eval` `fully-verifiable`
- [TerminalTraj](https://github.com/Wusiwei0410/TerminalTraj) ![stars](https://img.shields.io/github/stars/Wusiwei0410/TerminalTraj?style=flat-square) - Large-scale verified terminal trajectories collected from dockerized environments. Tags: `terminal` `train` `fully-verifiable`
- [MLE-bench](https://github.com/openai/mle-bench) ![stars](https://img.shields.io/github/stars/openai/mle-bench?style=flat-square) - End-to-end machine learning engineering benchmark. Tags: `coding` `science` `eval`
- [MLE-Dojo](https://github.com/MLE-Dojo/MLE-Dojo) ![stars](https://img.shields.io/github/stars/MLE-Dojo/MLE-Dojo?style=flat-square) - Training and evaluation environment for ML engineering agents. Tags: `coding` `science` `train+eval`
- [MLGym](https://github.com/facebookresearch/MLGym) ![stars](https://img.shields.io/github/stars/facebookresearch/MLGym?style=flat-square) - Gym-style benchmark for ML research and engineering tasks. Tags: `coding` `science` `train+eval`
- [GitTaskBench](https://github.com/QuantaAlpha/GitTaskBench) ![stars](https://img.shields.io/github/stars/QuantaAlpha/GitTaskBench?style=flat-square) - Git-centric task benchmark for repository manipulation agents. Tags: `coding` `terminal` `eval`
- [SWE-Factory](https://github.com/DeepSoftwareAnalytics/swe-factory) ![stars](https://img.shields.io/github/stars/DeepSoftwareAnalytics/swe-factory?style=flat-square) - Automated factory for issue-resolution training data and benchmark generation. Tags: `coding` `synthetic` `train`

## Tool, API, and App Environments

- [tau-bench](https://github.com/sierra-research/tau-bench) ![stars](https://img.shields.io/github/stars/sierra-research/tau-bench?style=flat-square) - Tool-use benchmark centered on customer-support and business-rule-heavy agent tasks. Tags: `tool-use` `eval` `partially-verifiable`
- [tau2-bench](https://github.com/sierra-research/tau2-bench) ![stars](https://img.shields.io/github/stars/sierra-research/tau2-bench?style=flat-square) - Harder successor benchmark with dual-control and richer environment dynamics. Tags: `tool-use` `eval`
- [Tau^3-bench](https://github.com/sierra-research/tau2-bench) ![stars](https://img.shields.io/github/stars/sierra-research/tau2-bench?style=flat-square) - Harder successor benchmark to τ²-bench adding full-duplex voice interaction, knowledge retrieval, and refined task quality. Tags: `tool-use` `eval` 
- [AppWorld](https://github.com/StonyBrookNLP/appworld) ![stars](https://img.shields.io/github/stars/StonyBrookNLP/appworld?style=flat-square) - App-centric benchmark for multi-tool and multi-app task completion. Tags: `tool-use` `eval`
- [Toolathlon](https://github.com/hkust-nlp/Toolathlon) ![stars](https://img.shields.io/github/stars/hkust-nlp/Toolathlon?style=flat-square) - A benchmark for language agents featuring 600+ diverse tools across 32 real-world software applications with long-horizon tasks and execution-based evaluation. Tags: `tool-use` `real` `eval` 
- [ToolSandbox](https://github.com/apple/ToolSandbox) ![stars](https://img.shields.io/github/stars/apple/ToolSandbox?style=flat-square) - Controlled environment for tool-using agents with rich API-level task design. Tags: `tool-use` `train+eval`
- [MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe) ![stars](https://img.shields.io/github/stars/SalesforceAIResearch/MCP-Universe?style=flat-square) - Benchmarking framework using real-world MCP servers instead of simulated tools. Tags: `tool-use` `eval` `real`
- [MCPMark](https://github.com/eval-sys/mcpmark) ![stars](https://img.shields.io/github/stars/eval-sys/mcpmark?style=flat-square) - A comprehensive evaluation suite for agentic models that stress-tests tool usage across real MCP services like Notion, GitHub, and Postgres. Tags: `tool-use` `eval` `real`
- [Toucan](https://github.com/TheAgentArk/Toucan) ![stars](https://img.shields.io/github/stars/TheAgentArk/Toucan?style=flat-square) - Environment and data generation pipeline around real MCP-style tool ecosystems. Tags: `tool-use` `synthetic` `train`

## Enterprise and Workflow Environments

- [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany) ![stars](https://img.shields.io/github/stars/TheAgentCompany/TheAgentCompany?style=flat-square) - Enterprise-style benchmark covering long-horizon workplace tasks. Tags: `enterprise` `eval`
- [OfficeBench](https://github.com/zlwang-cs/OfficeBench) ![stars](https://img.shields.io/github/stars/zlwang-cs/OfficeBench?style=flat-square) - Office productivity benchmark spanning documents, spreadsheets, slides, and email-style tasks. Tags: `enterprise` `eval`
- [ScienceBoard](https://github.com/OS-Copilot/ScienceBoard) ![stars](https://img.shields.io/github/stars/OS-Copilot/ScienceBoard?style=flat-square) - Scientific workflow environment for research-task agents. Tags: `science` `workflow` `eval`

## Embodied, Game, and Social Environments

- [TextWorld](https://github.com/microsoft/TextWorld) ![stars](https://img.shields.io/github/stars/microsoft/TextWorld?style=flat-square) - Text-based reinforcement learning framework for interactive fiction and long-horizon reasoning. Tags: `game` `train+eval`
- [ScienceWorld](https://github.com/allenai/ScienceWorld) ![stars](https://img.shields.io/github/stars/allenai/ScienceWorld?style=flat-square) - Text-based scientific experimentation environment. Tags: `science` `game` `train+eval`
- [ALFWorld](https://github.com/alfworld/alfworld) ![stars](https://img.shields.io/github/stars/alfworld/alfworld?style=flat-square) - Text + embodied household benchmark bridging language and action. Tags: `embodied` `train+eval`
- [VirtualHome](https://github.com/xavierpuigf/virtualhome) ![stars](https://img.shields.io/github/stars/xavierpuigf/virtualhome?style=flat-square) - Household activity simulator with rich programmatic supervision. Tags: `embodied` `train+eval`
- [AI2-THOR](https://github.com/allenai/ai2thor) ![stars](https://img.shields.io/github/stars/allenai/ai2thor?style=flat-square) - Interactive 3D environment for embodied AI tasks. Tags: `embodied` `train+eval`
- [Habitat-Lab](https://github.com/facebookresearch/habitat-lab) ![stars](https://img.shields.io/github/stars/facebookresearch/habitat-lab?style=flat-square) - Research platform for embodied navigation and manipulation. Tags: `embodied` `train+eval`
- [Habitat 2.0](https://aihabitat.org/) - Large-scale embodied benchmark stack integrating simulation, datasets, and tasks. Tags: `embodied` `train+eval`
- [Isaac Gym](https://developer.nvidia.com/isaac-gym) - GPU-native robotics simulation for massively parallel RL. Tags: `embodied` `train`
- [Isaac Lab](https://github.com/isaac-sim/IsaacLab) ![stars](https://img.shields.io/github/stars/isaac-sim/IsaacLab?style=flat-square) - Successor stack for scalable robot learning and simulation on NVIDIA platforms. Tags: `embodied` `train`
- [ManiSkill](https://github.com/haosulab/ManiSkill) ![stars](https://img.shields.io/github/stars/haosulab/ManiSkill?style=flat-square) - Fast, scalable benchmark suite for manipulation agents. Tags: `embodied` `train+eval`
- [MineRL](https://github.com/minerllabs/minerl) ![stars](https://img.shields.io/github/stars/minerllabs/minerl?style=flat-square) - Minecraft benchmark and data ecosystem for long-horizon agents. Tags: `game` `train+eval`
- [NetHack Learning Environment](https://github.com/facebookresearch/nle) ![stars](https://img.shields.io/github/stars/facebookresearch/nle?style=flat-square) - Roguelike benchmark for long-horizon exploration and planning. Tags: `game` `train+eval`
- [DiscoveryWorld](https://github.com/allenai/discoveryworld) ![stars](https://img.shields.io/github/stars/allenai/discoveryworld?style=flat-square) - Open-ended simulated world for scientific and interactive reasoning. Tags: `science` `game` `train+eval`
- [Sotopia](https://github.com/sotopia-lab/sotopia) ![stars](https://img.shields.io/github/stars/sotopia-lab/sotopia?style=flat-square) - Open-ended social learning environment for language agents. Tags: `social` `train+eval`
- [Sotopia-pi](https://github.com/sotopia-lab/sotopia-pi) ![stars](https://img.shields.io/github/stars/sotopia-lab/sotopia-pi?style=flat-square) - Preference and interaction stack extending Sotopia-style social evaluation. Tags: `social` `eval`
- [ChatArena](https://github.com/Farama-Foundation/chatarena) ![stars](https://img.shields.io/github/stars/Farama-Foundation/chatarena?style=flat-square) - Multi-agent language game environments for collaboration and competition. Tags: `social` `train+eval`
- [AdaSociety](https://github.com/bigai-ai/AdaSociety) ![stars](https://img.shields.io/github/stars/bigai-ai/AdaSociety?style=flat-square) - Multi-agent environment with expanding state/action spaces and explicit social structure. Tags: `social` `train+eval`

## Synthetic Environments and Environment Scaling

- [OS-Genesis](https://arxiv.org/abs/2412.19723) - Reverse task synthesis pipeline for generating GUI-agent trajectories. Tags: `gui` `synthetic` `train`
- [EnvScaler](https://github.com/RUC-NLPIR/EnvScaler) ![stars](https://img.shields.io/github/stars/RUC-NLPIR/EnvScaler?style=flat-square) - Programmatic synthesis of tool-interactive environments and verifiable scenarios. Tags: `tool-use` `synthetic` `train`
- [ScaleEnv](https://arxiv.org/abs/2602.06820) - From-scratch synthesis of generalist tool-use environments with executable verification. Tags: `tool-use` `synthetic` `train`
- [Agent World Model](https://github.com/Snowflake-Labs/agent-world-model) ![stars](https://img.shields.io/github/stars/Snowflake-Labs/agent-world-model?style=flat-square) - Fully synthetic code-driven environments backed by databases and tool APIs. Tags: `tool-use` `synthetic` `train`
- [WebWorld](https://arxiv.org/abs/2602.14721) - Large-scale world model for open-web agent training. Tags: `web` `world-model` `train`
- [GUI-GENESIS](https://arxiv.org/abs/2602.14093) - Automated synthesis of efficient GUI environments with verifiable rewards. Tags: `gui` `synthetic` `train`
- [RLVE](https://github.com/Zhiyuan-Zeng/RLVE) ![stars](https://img.shields.io/github/stars/Zhiyuan-Zeng/RLVE?style=flat-square) - Adaptive verifiable environments for reinforcement learning over language models. Tags: `synthetic` `train` `fully-verifiable`
- [AgentScaler](https://arxiv.org/abs/2509.13311) - Environment scaling for function-calling and heterogeneous tool-use agents. Tags: `tool-use` `synthetic` `train`
- [WebDreamer](https://arxiv.org/abs/2411.06559) - Web world-model direction for simulated web interaction and planning. Tags: `web` `world-model` `train`
- [VirtualEnv](https://arxiv.org/abs/2601.07553) - Open-source embodied platform with procedurally generated tasks and game-inspired mechanics. Tags: `embodied` `synthetic` `train+eval`
- [Adaptive Environment Generation for Embodied Agents](https://arxiv.org/abs/2602.06366) - Adaptive scene generation driven by current agent competence. Tags: `embodied` `synthetic` `train`
- [Dreamer 4](https://arxiv.org/abs/2509.24527) - Scalable world-model training in imagination, including complex Minecraft-style tasks. Tags: `world-model` `embodied` `train`
- [LLM-in-Sandbox](https://arxiv.org/abs/2601.16206) - General sandbox-first environment design showing broad gains from letting models explore a virtual computer. Tags: `sandbox` `synthetic` `train`

## Runtime, Sandbox, and Isolation Infrastructure

- [OCI Runtime Spec](https://github.com/opencontainers/runtime-spec) ![stars](https://img.shields.io/github/stars/opencontainers/runtime-spec?style=flat-square) - Standard for how container runtimes launch and manage container bundles. Tags: `runtime` `standard`
- [OCI Image Spec](https://github.com/opencontainers/image-spec) ![stars](https://img.shields.io/github/stars/opencontainers/image-spec?style=flat-square) - Standard image format used across container-based agent environments. Tags: `runtime` `standard`
- [runc](https://github.com/opencontainers/runc) ![stars](https://img.shields.io/github/stars/opencontainers/runc?style=flat-square) - Reference OCI runtime used under much of the modern container stack. Tags: `runtime`
- [containerd](https://github.com/containerd/containerd) ![stars](https://img.shields.io/github/stars/containerd/containerd?style=flat-square) - Core container runtime layer used by many sandboxed and orchestrated agent systems. Tags: `runtime` `platform`
- [Docker](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) - The default container abstraction used across many agent benchmarks and training gyms. Tags: `sandbox` `runtime`
- [Firecracker](https://github.com/firecracker-microvm/firecracker) ![stars](https://img.shields.io/github/stars/firecracker-microvm/firecracker?style=flat-square) - MicroVM runtime for stronger isolation than process-level containers. Tags: `sandbox` `runtime` `security`
- [firecracker-containerd](https://github.com/firecracker-microvm/firecracker-containerd) ![stars](https://img.shields.io/github/stars/firecracker-microvm/firecracker-containerd?style=flat-square) - Containerd integration for launching container workloads inside Firecracker microVMs. Tags: `sandbox` `runtime`
- [gVisor](https://github.com/google/gvisor) ![stars](https://img.shields.io/github/stars/google/gvisor?style=flat-square) - User-space kernel that hardens container isolation for untrusted workloads. Tags: `sandbox` `security`
- [Kata Containers](https://github.com/kata-containers/kata-containers) ![stars](https://img.shields.io/github/stars/kata-containers/kata-containers?style=flat-square) - Lightweight VMs that look like containers to orchestration systems. Tags: `sandbox` `runtime`
- [Confidential Containers](https://github.com/confidential-containers) ![stars](https://img.shields.io/github/stars/confidential-containers/trustee?style=flat-square) - Confidential-computing stack for running container workloads inside attested trusted environments. Tags: `sandbox` `security`
- [E2B](https://github.com/e2b-dev/E2B) ![stars](https://img.shields.io/github/stars/e2b-dev/E2B?style=flat-square) - Managed cloud sandboxes for code-interpreter and agent workloads. Tags: `sandbox` `platform`
- [E2B Desktop Sandbox](https://github.com/e2b-dev/desktop) ![stars](https://img.shields.io/github/stars/e2b-dev/desktop?style=flat-square) - Browser and desktop sandbox for computer-use style agents. Tags: `sandbox` `gui`
- [Kubernetes Agent Sandbox](https://developers.googleblog.com/en/announcing-kubernetes-agent-sandbox/) - Google's direction for standardizing sandboxed agent runtimes on Kubernetes. Tags: `sandbox` `platform`
- [Fault-Tolerant Sandboxing for LLM Agents](https://arxiv.org/abs/2512.12806) - Research on resilient sandbox execution for long-running agent systems. Tags: `sandbox` `security`

## Orchestration, Serverless, and Platform Engineering

- [Kubernetes](https://github.com/kubernetes/kubernetes) ![stars](https://img.shields.io/github/stars/kubernetes/kubernetes?style=flat-square) - The default cluster orchestrator for multi-tenant agent runtimes and sandbox scheduling. Tags: `platform` `orchestration`
- [Knative](https://github.com/knative/serving) ![stars](https://img.shields.io/github/stars/knative/serving?style=flat-square) - Serverless layer on Kubernetes for request-driven workloads and elastic agent backends. Tags: `platform` `orchestration` `serverless`
- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) - Serverless compute platform that publicly documents microVM-backed execution and snapshotting. Tags: `platform` `serverless`
- [Cloudflare Workers](https://developers.cloudflare.com/workers/reference/how-workers-works/) - Isolate-based edge execution model relevant to ultra-fast agent sandboxing. Tags: `platform` `serverless`
- [Borg](https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/) - Foundational cluster-management paper shaping later orchestration systems used for large agent fleets. Tags: `platform` `orchestration`

## Protocols, Standards, and Capability Interfaces

- [Model Context Protocol](https://modelcontextprotocol.io/) - Standardized capability interface for connecting models to tools, data, and external systems. Tags: `protocol` `standard`
- [Wasmtime](https://github.com/bytecodealliance/wasmtime) ![stars](https://img.shields.io/github/stars/bytecodealliance/wasmtime?style=flat-square) - WebAssembly runtime that enables portable capability-bounded execution. Tags: `protocol` `runtime`
- [WASI](https://github.com/WebAssembly/WASI) ![stars](https://img.shields.io/github/stars/WebAssembly/WASI?style=flat-square) - Capability-oriented system interface for WebAssembly modules. Tags: `protocol` `standard`
- [Bytecode Alliance](https://github.com/bytecodealliance) - Consortium driving portable and capability-safe Wasm execution ecosystems. Tags: `protocol` `standard`
- [Open Container Initiative](https://github.com/opencontainers) - Standards body behind the container formats and runtime interfaces that underpin many agent sandboxes. Tags: `protocol` `standard`

## Observability and Debugging

- [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-specification) ![stars](https://img.shields.io/github/stars/open-telemetry/opentelemetry-specification?style=flat-square) - Unified traces, metrics, and logs specification for distributed agent platforms. Tags: `observability` `standard`
- [eBPF](https://ebpf.io/) - Kernel-level programmable observability layer widely used for container and sandbox introspection. Tags: `observability`
- [Process Monitor](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon) - Windows activity tracing tool useful for understanding GUI-agent side effects and OS interactions. Tags: `observability` `gui`
- [Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) - Broader Windows diagnostic toolkit family for agent-environment debugging. Tags: `observability` `gui`
- [S2E](https://github.com/S2E/s2e) ![stars](https://img.shields.io/github/stars/S2E/s2e?style=flat-square) - Selective symbolic execution platform for deep system analysis and adversarial environment testing. Tags: `observability` `security`
- [Kubernetes Ephemeral Containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) - Standard pattern for debugging slim or distroless agent runtime pods in place. Tags: `observability` `orchestration`

## Evaluation Harnesses and Companion Ecosystems

- [BrowserGym](https://github.com/ServiceNow/BrowserGym) ![stars](https://img.shields.io/github/stars/ServiceNow/BrowserGym?style=flat-square) - Unified Gym-style interface spanning multiple browser and enterprise environments. Tags: `harness` `web` `train+eval`
- [AgentLab](https://github.com/ServiceNow/AgentLab) ![stars](https://img.shields.io/github/stars/ServiceNow/AgentLab?style=flat-square) - Experiment and evaluation layer built around BrowserGym environments. Tags: `harness` `web` `eval`
- [OpenHands Benchmarks](https://github.com/OpenHands/benchmarks) ![stars](https://img.shields.io/github/stars/OpenHands/benchmarks?style=flat-square) - Benchmark collections and execution harnesses for coding and agent tasks. Tags: `harness` `coding` `eval`
- [AgentRewardBench](https://github.com/McGill-NLP/agent-reward-bench) ![stars](https://img.shields.io/github/stars/McGill-NLP/agent-reward-bench?style=flat-square) - Reward-model benchmark tailored to agent trajectories and task outcomes. Tags: `harness` `eval`
- [tale-suite](https://github.com/microsoft/tale-suite) ![stars](https://img.shields.io/github/stars/microsoft/tale-suite?style=flat-square) - Task and agent lifecycle evaluation suite for agentic systems. Tags: `harness` `eval`
- [METR Task Standard](https://github.com/METR/task-standard) ![stars](https://img.shields.io/github/stars/METR/task-standard?style=flat-square) - Task specification standard aimed at more reproducible agent evaluation. Tags: `harness` `standard`
- [PettingZoo](https://github.com/Farama-Foundation/PettingZoo) ![stars](https://img.shields.io/github/stars/Farama-Foundation/PettingZoo?style=flat-square) - Standard API and reference environments for multi-agent RL research. Tags: `harness` `social`
- [GroundCUA](https://github.com/ServiceNow/GroundCUA) ![stars](https://img.shields.io/github/stars/ServiceNow/GroundCUA?style=flat-square) - Grounding and dataset layer for computer-use agents, complementary to GUI environments. Tags: `harness` `gui`

## Safety, Security, and Robustness

- [AgentDojo](https://github.com/ethz-spylab/agentdojo) ![stars](https://img.shields.io/github/stars/ethz-spylab/agentdojo?style=flat-square) - Security benchmark for tool-using agents under adversarial and policy-constrained settings. Tags: `security` `tool-use` `eval`
- [DoomArena](https://github.com/ServiceNow/DoomArena) ![stars](https://img.shields.io/github/stars/ServiceNow/DoomArena?style=flat-square) - Stress-testing environment for robust and adversarial browser-agent behavior. Tags: `security` `web` `eval`
- [ASB](https://github.com/agiresearch/ASB) ![stars](https://img.shields.io/github/stars/agiresearch/ASB?style=flat-square) - Agent security benchmark suite for evaluating attack surfaces and unsafe behavior. Tags: `security` `eval`
- [DefenderBench](https://github.com/microsoft/DefenderBench) ![stars](https://img.shields.io/github/stars/microsoft/DefenderBench?style=flat-square) - Defensive evaluation benchmark for agent systems operating under security constraints. Tags: `security` `eval`
- [ToolEmu](https://github.com/ryoungj/ToolEmu) ![stars](https://img.shields.io/github/stars/ryoungj/ToolEmu?style=flat-square) - Sandbox for emulating risky tool-use scenarios and evaluating tool-agent safety. Tags: `security` `tool-use` `llm-sim`
- [OS-Harm](https://github.com/tml-epfl/os-harm) ![stars](https://img.shields.io/github/stars/tml-epfl/os-harm?style=flat-square) - Harm benchmark for computer-use agents operating over OS-like environments. Tags: `security` `gui` `eval`

## Surveys and Reading Lists

- [Taxonomy Notes](docs/taxonomy.md) - Chinese notes on definitions, classification axes, development patterns, and construction methods.
- [Environment Scaling for Interactive Agentic Experience Collection: A Survey](https://arxiv.org/abs/2511.09586) - Survey centered on environment scaling as a training axis.
- [A Compendium of LLM Benchmarks for Agents](https://github.com/philschmid/ai-agent-benchmark-compendium) ![stars](https://img.shields.io/github/stars/philschmid/ai-agent-benchmark-compendium?style=flat-square) - Broad benchmark map with many adjacent agent-evaluation resources.
- [GUI Agents Paper List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) ![stars](https://img.shields.io/github/stars/OSU-NLP-Group/GUI-Agents-Paper-List?style=flat-square) - Curated reading list for GUI-agent research.
- [AgentSafety Paper List](https://github.com/OSU-NLP-Group/AgentSafety_Papers) ![stars](https://img.shields.io/github/stars/OSU-NLP-Group/AgentSafety_Papers?style=flat-square) - Reading list focused on agent safety and security.

## Contributing

Contributions are welcome. A good contribution usually includes:

- the official repository, project page, or paper link
- a one-line description of what the environment contributes
- primary tags for fidelity, domain, purpose, and verifiability
- a rationale for why the project belongs here as an environment, environment builder, sandbox, or harness

If a project fits multiple sections, prefer one primary section and use tags instead of duplicating it everywhere.
