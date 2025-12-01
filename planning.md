# Research Plan: Do AI Agents Form Mental Models of Each Other?

## 1. Research Question
Do AI agents in social deduction games (specifically Werewolf) improve their performance (win rate) and deduction accuracy when explicitly prompted to form and update "mental models" (role probabilities and intent) of other players, compared to agents that rely solely on dialogue history?

## 2. Background and Motivation
Current LLM agents often treat dialogue as a sequence of inputs without explicitly modeling the *source* of those inputs as distinct entities with hidden states (roles). Humans play Werewolf by maintaining a mental belief state ("I think Player A is the Wolf because they lied about X").
**Hypothesis:** Agents with an explicit "Opponent Modeling" (OM) step—where they must articulate their beliefs about other players' roles before speaking—will outperform standard agents.

## 3. Hypothesis Decomposition
- **H1 (Performance):** OM-Agents will achieve a higher win rate than Baseline agents.
- **H2 (Deduction):** OM-Agents will identify Werewolves earlier in the game (measured by voting patterns).
- **H3 (Coherence):** OM-Agents will produce more consistent arguments.

## 4. Proposed Methodology

### Approach
We will use the **ChatArena-Werewolf** framework to simulate Werewolf games.
We will compare two conditions:
1.  **Control (Baseline):** Standard LLM agents using the default ChatArena prompts (Context -> Action).
2.  **Treatment (ToM-Agent):** Modified agents that utilize a Chain-of-Thought (CoT) prompting strategy specifically focused on *Opponent Modeling*.
    *   *Mechanism:* Before generating a public message, the agent generates a private "Internal Monologue" assessing the probability of each other player being a Werewolf/Villager/Seer.

### Experimental Steps
1.  **Setup:** Install `ChatArena-Werewolf` dependencies.
2.  **Agent Implementation:**
    *   Inspect `chatarena` code.
    *   Create a new configuration or modify `chatarena/backends/openai.py` (or where prompts are handled) to inject the ToM instruction.
    *   Define the ToM prompt: "Current Beliefs: List each player and your suspicion level (0-100). Reasoning: ... Action: ..."
3.  **Simulation:**
    *   Run a tournament of *N* games (aiming for 10-20 given time/budget).
    *   Configuration: 7 players (2 Werewolves, 1 Seer, 1 Guard, 3 Villagers).
    *   Mix: 
        *   All Baseline (to check balance).
        *   All ToM (to check behavior).
        *   Mixed (e.g., ToM Werewolves vs Baseline Villagers, and vice versa).
4.  **Data Collection:**
    *   Save game logs (JSON).
    *   Parse logs to extract winners and roles.

### Baselines
- **Standard ChatArena Agent:** Represents the "naive" LLM approach.

### Evaluation Metrics
- **Win Rate:** Percentage of games won by the faction containing the ToM agent.
- **Survival Rate:** How long the agent survives.

### Statistical Analysis Plan
- Compare Win Rates using a Chi-Squared test or simple binomial proportion test.

## 5. Timeline
- **Phase 1 (Planning):** Completed.
- **Phase 2 (Setup):** 10 min.
- **Phase 3 (Impl):** 45 min. Modify Agent/Prompt code.
- **Phase 4 (Exp):** 45 min. Run simulations.
- **Phase 5 (Analysis):** 30 min. Parse logs, compute stats.
- **Phase 6 (Docs):** 20 min. Write Report.

## 6. Potential Challenges
- **API Costs/Limits:** Running 7 agents * 10 rounds * 20 games = lots of tokens. I will stick to a smaller number of games if needed or use a cheaper model/mock if absolutely forced (but per instructions, I must use real LLMs). I will use the `openrouter` key provided in the environment variables.
- **Model Capability:** Smaller models might not follow the complex ToM prompt. I will aim for `gpt-4o` or `claude-3.5-sonnet` via OpenRouter.

## 7. Success Criteria
- Successfully running complete game simulations with modified agents.
- Quantifiable difference in win rates (even if not statistically significant due to sample size, a trend is a result).
