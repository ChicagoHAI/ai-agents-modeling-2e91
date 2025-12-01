# Resources Catalog

## Summary
This document catalogs all resources gathered for the research project "Do AI Agents Form Mental Models of Each Other?".

**Status**: Complete
- Papers: 6
- Datasets: 2
- Code Repositories: 3

---

## Papers
Location: `papers/`

| ID | Title | Year | Key Concept |
|----|-------|------|-------------|
| 2309.04658 | Exploring LLMs for Communication Games | 2023 | Baseline LLM performance in Werewolf. |
| 2504.18039 | MultiMind: Enhancing Werewolf Agents | 2025 | Explicit Theory of Mind and Multimodal reasoning. |
| 2310.18940 | Language Agents with RL | 2023 | Reinforcement Learning for strategy. |
| 2407.13943 | Werewolf Arena | 2024 | Evaluation benchmarking framework. |
| 2402.02330 | Enhance Reasoning for LLMs | 2024 | Improved reasoning modules. |
| 2311.03220 | Alympics | 2023 | Multi-agent strategic competition. |

See `papers/README.md` for details.

---

## Datasets
Location: `datasets/`

### 1. LLMafia
- **Path**: `datasets/LLMafia`
- **Description**: High-quality transcripts of Mafia games. Useful for training/fine-tuning on human strategic dialogue.
- **Status**: Downloaded (Git ignored).

### 2. Werewolf-Among-Us
- **Path**: `datasets/Werewolf-Among-Us`
- **Description**: Large-scale multimodal dataset (video + text). Contains transcripts and vote outcomes.
- **Status**: Downloaded (Git ignored).

See `datasets/README.md` for download/usage instructions.

---

## Code Repositories
Location: `code/`

### 1. Werewolf Arena (`code/werewolf_arena`)
- **Source**: Google Research (implied).
- **Utility**: Best for running standardized benchmarks.

### 2. ChatArena-Werewolf (`code/ChatArena-Werewolf`)
- **Source**: ChatArena ecosystem.
- **Utility**: Flexible, easy to hack for adding new agent types (like ToM agents).

### 3. AIWolf-Python (`code/aiwolf-python`)
- **Source**: AIWolf Project.
- **Utility**: Good if we want to compete in the standard AIWolf protocol, but less "LLM-native" than the others.

---

## Recommendation for Experiment Runner

1.  **Platform**: Use **ChatArena-Werewolf** (`code/ChatArena-Werewolf`) as the primary testbed. It is Pythonic, modular, and designed for LLMs.
2.  **Baseline**: Run the existing agents in ChatArena as the "No-ToM" baseline.
3.  **Intervention**: Implement a "ToM-Agent" that maintains a `BeliefMatrix` (inspired by MultiMind) and uses it to prompt the generation step.
4.  **Evaluation**: Run 50+ games of Baseline vs. Baseline and 50+ of ToM vs. Baseline. Measure win rates and "deduction accuracy" (log who they suspect vs. actual roles).
