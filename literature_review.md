# Literature Review: Opponent Modeling in Multi-Agent LLM Systems

## Research Area Overview

The intersection of Large Language Models (LLMs) and Game Theory has emerged as a critical testing ground for evaluating the reasoning capabilities of AI agents. Social deduction games like Werewolf (or Mafia) are particularly challenging because they require **Theory of Mind (ToM)**—the ability to impute mental states (beliefs, intents, knowledge) to oneself and others. Unlike perfect information games (e.g., Chess), Werewolf involves hidden information, deception, and persuasion.

Early approaches focused on simply prompting LLMs to play roles. Recent research has shifted towards enhancing strategic reasoning through Reinforcement Learning (RL), specialized reasoning modules (e.g., Chain-of-Thought), and explicit opponent modeling frameworks.

## Key Papers

### 1. Exploring Large Language Models for Communication Games: An Empirical Study on Werewolf (Xu et al., 2023)
- **arXiv**: 2309.04658
- **Key Contribution**: One of the first comprehensive empirical studies of LLMs in Werewolf.
- **Methodology**: Evaluated various LLMs (GPT-3.5, GPT-4) with different prompting strategies.
- **Findings**: Found that while LLMs can follow game rules, they struggle with complex logical deduction and consistent deception without specialized prompting or fine-tuning. They established a baseline for "naive" LLM play.
- **Relevance**: Provides the baseline performance and identifies the core challenges (hallucination, inconsistency) that newer methods try to solve.

### 2. MultiMind: Enhancing Werewolf Agents with Multimodal Reasoning and Theory of Mind (2025)
- **arXiv**: 2504.18039
- **Key Contribution**: Explicitly addresses the lack of "mental modeling" in previous agents by introducing a framework that tracks suspicion and beliefs.
- **Methodology**: Integrates multimodal cues (if available) and a structured ToM module that maintains a belief state about every other player's role and knowledge.
- **Findings**: Agents with explicit ToM modules significantly outperform those without, especially in the "Imposter" (Werewolf) role where understanding what others know is crucial for survival.
- **Relevance**: Directly addresses our research hypothesis. It proves that explicit modeling > implicit modeling.

### 3. Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game (2023)
- **arXiv**: 2310.18940
- **Key Contribution**: Applying RL to fine-tune LLMs for winning objectives rather than just language plausibility.
- **Methodology**: Used RLHF-style training where the reward signal is game victory/survival.
- **Findings**: RL agents learned more aggressive and effective voting strategies but sometimes sacrificed conversational naturalness.
- **Relevance**: Suggests that "behavioral" modeling (learning what wins) can mimic "mental" modeling, but may not be true ToM.

### 4. Werewolf Arena: A Case Study in LLM Evaluation via Social Deduction (2024)
- **arXiv**: 2407.13943
- **Key Contribution**: A standardized benchmark framework.
- **Methodology**: Created a robust environment for pitting agents against each other.
- **Relevance**: Provides the *infrastructure* for our experiments (we have cloned this repo).

### 5. Enhance Reasoning for Large Language Models in the Game Werewolf (2024)
- **arXiv**: 2402.02330
- **Key Contribution**: Introduces a dual-process module (intuitive vs. analytical) to improve deduction.
- **Methodology**: Separates the "talking" module from the "thinking" module, allowing the agent to reason about contradictions before speaking.
- **Relevance**: A precursor to full ToM; shows that internal monologue/reasoning improves performance.

## Synthesis: The State of Opponent Modeling

### Common Methodologies
1.  **Prompt Engineering**: The baseline. "You are a villager, who do you suspect?"
2.  **Chain-of-Thought (CoT)**: "Reason step-by-step before voting."
3.  **Reflection/Memory Modules**: Storing past history to find contradictions.
4.  **Explicit Belief State**: (MultiMind) Maintaining a matrix of $P(Role_j | Agent_i)$.

### Gaps and Opportunities
-   **Implicit vs. Explicit**: Most papers show *that* LLMs can play, but few rigorously quantify *if* they form a mental model or just pattern match.
-   **Metric Gap**: We measure "Win Rate" (outcome), but we rarely measure "Model Accuracy" (e.g., "Did the agent correctly predict that Player B knows Player C is a seer?").
-   **Deception Detection**: There is a lack of analysis on how agents detect deception specifically through modeling the *intent* of others.

## Recommendations for Our Experiment

1.  **Experimental Design**: Compare a standard CoT agent against an agent with an injected "Mental Model" step (forcing it to explicitly state what it thinks others believe).
2.  **Datasets**: Use `LLMafia` for analyzing human-human ToM interactions to establish a "gold standard" of reasoning. Use `Werewolf-Among-Us` if we want to analyze multimodal cues (less critical for pure LLM text experiments).
3.  **Codebase**: Use `Werewolf Arena` or `ChatArena-Werewolf` as the base environment. Modify the agent class to log "Internal Beliefs" separately from "Public Utterances."
4.  **Metrics**:
    -   **Win Rate**: Standard.
    -   **Prediction Accuracy**: Can the agent correctly guess roles before the game ends?
    -   **Surprise**: Does the agent act surprised when a role is revealed? (Information theoretic measure).

