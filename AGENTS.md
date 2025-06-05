# Translation Tasks Coordination

This repository contains multiple language versions of the AI Agents course. The English content lives under `units/en` and the Korean translation under `units/ko`.

## Goal
Translate all `.mdx` files in `units/en` to Korean, keeping the same subfolder structure under `units/ko`.

## Current Status
- Total English `.mdx` files: 74
- Current Korean `.mdx` files: 11
- Files remaining: 63

Run `python3 scripts/check_translation.py` to see an overview of MDX counts per language.

## Missing Files
The following paths (relative to `units/`) still need a Korean translation:

```text
bonus-unit1/conclusion.mdx
bonus-unit1/fine-tuning.mdx
bonus-unit1/introduction.mdx
bonus-unit1/what-is-function-calling.mdx
bonus-unit2/introduction.mdx
bonus-unit2/monitoring-and-evaluating-agents-notebook.mdx
bonus-unit2/quiz.mdx
bonus-unit2/what-is-agent-observability-and-evaluation.mdx
bonus-unit3/building_your_pokemon_agent.mdx
bonus-unit3/conclusion.mdx
bonus-unit3/from-llm-to-agents.mdx
bonus-unit3/introduction.mdx
bonus-unit3/launching_agent_battle.mdx
bonus-unit3/state-of-art.mdx
communication/live1.mdx
unit1/actions.mdx
unit1/agent-steps-and-structure.mdx
unit1/conclusion.mdx
unit1/dummy-agent-library.mdx
unit1/final-quiz.mdx
unit1/introduction.mdx
unit1/messages-and-special-tokens.mdx
unit1/observations.mdx
unit1/quiz1.mdx
unit1/quiz2.mdx
unit1/thoughts.mdx
unit1/tools.mdx
unit1/tutorial.mdx
unit1/what-are-agents.mdx
unit1/what-are-llms.mdx
unit2/langgraph/building_blocks.mdx
unit2/langgraph/conclusion.mdx
unit2/langgraph/document_analysis_agent.mdx
unit2/langgraph/first_graph.mdx
unit2/langgraph/introduction.mdx
unit2/langgraph/quiz1.mdx
unit2/langgraph/when_to_use_langgraph.mdx
unit2/llama-index/agents.mdx
unit2/llama-index/components.mdx
unit2/llama-index/conclusion.mdx
unit2/llama-index/introduction.mdx
unit2/llama-index/llama-hub.mdx
unit2/llama-index/quiz1.mdx
unit2/llama-index/quiz2.mdx
unit2/llama-index/tools.mdx
unit2/llama-index/workflows.mdx
unit2/smolagents/code_agents.mdx
unit2/smolagents/conclusion.mdx
unit2/smolagents/final_quiz.mdx
unit2/smolagents/introduction.mdx
unit2/smolagents/multi_agent_systems.mdx
unit2/smolagents/quiz1.mdx
unit2/smolagents/quiz2.mdx
unit2/smolagents/retrieval_agents.mdx
unit2/smolagents/tool_calling_agents.mdx
unit2/smolagents/tools.mdx
unit2/smolagents/vision_agents.mdx
unit2/smolagents/why_use_smolagents.mdx
unit3/agentic-rag/agent.mdx
unit3/agentic-rag/agentic-rag.mdx
unit3/agentic-rag/conclusion.mdx
unit3/agentic-rag/invitees.mdx
unit3/agentic-rag/tools.mdx
```

## Suggested Assignment
To spread the workload, translators can divide the files by folder:

- **Agent A**: `bonus-unit1/` and `bonus-unit2/`
- **Agent B**: `bonus-unit3/` and `communication/`
- **Agent C**: `unit1/`
- **Agent D**: `unit2/`
- **Agent E**: `unit3/`

When you translate a file:
1. Keep the same filename and relative path under `units/ko`.
2. Add a `[[slug]]` anchor after the main heading so internal links work. Copy this slug from the English version.
3. Commit your translations with concise English commit messages.
4. After adding translations, run `python3 scripts/check_translation.py` to ensure counts are updated.

