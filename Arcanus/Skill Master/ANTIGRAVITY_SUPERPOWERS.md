# 🚀 Antigravity Superpowers & Ecosystem Guide

Welcome to your Antigravity Agent Ecosystem! This guide details all the active rules, workflows, and skills currently installed on your system. Because these are configured globally in your `~/.agent` directory and system prompts, they are active **across all projects** without needing manual copying!

---

## 🏛️ 1. Global Rules ("The House Way")

These are the fundamental laws that govern how Antigravity operates. They are **always active** on every interaction.

| Core Rule | What it does | Why it's useful |
| :--- | :--- | :--- |
| **Persona (Senior Product Engineer)** | Antigravity acts as a senior engineer at a top startup, prioritizing speed-to-market and clean, maintainable code. | Prevents generic, "robotic" advice and provides opinionated, high-quality architectural decisions. |
| **Tech Stack & Defaults** | Forces default technologies: **Next.js App Router**, **Lucide React** for icons, and prioritizes **JSON data structures** over complex DBs unless explicitly asked otherwise. | Saves hours of back-and-forth by creating code in "The House Way" immediately without guesswork. |
| **Style & Communication** | Requires the agent to explain the "Why" before the "How", and mandates verifying UI changes via browser screenshots before finishing tasks. | Ensures you understand the design decisions and guarantees that the UI actually looks correct before the agent claims it is done. |
| **Squad Project Setup** | When you ask to "Initialise a Squad Project", the agent automatically generates a `PLAN.md` Master Ledger containing the Master Roadmap, Current Trajectory, and Squad Status table. | Creates immediate, organized project management and visibility for complex multi-agent objectives. |

---

## ⚡ 2. Global Workflows (Slash Commands)

Workflows are specific, multi-step procedures designed to accomplish targeted goals. 

**How to trigger:** You trigger these manually by typing the exact slash command in your chat prompt (e.g., *"Let's run /audit on the new dashboard"*).

| Command | Description & Usefulness |
| :--- | :--- |
| `/audit` | Runs an audit to ensure the application is functional, accessible, and looks great aesthetically. |
| `/the-builder` | Activates a specialized workflow focused purely on implementing core functionality, logic, and architecture. |
| `/the-design-lead` | Activates a specialized workflow focusing on UI, UX, and Visual Excellence (premium, modern, dynamic designs). |
| `/the-nerd` | Activates a strict Quality Control and Testing workflow to bulletproof the codebase. |
| `/the-researcher` | Focuses the agent on deep research, data gathering, and strategic planning before writing code. |
| `/workflow-debugging` | Runs a systematic, structured debugging flow to trace and resolve complex application errors. |

---

## 🧠 3. Global Agent Skills

Skills are highly specific techniques, mental models, and documentation guides that Antigravity utilizes.

**How to trigger:** You **do not** need to trigger these manually. Antigravity continuously monitors your prompts and context. It reads the hidden `description` tags inside each skill. When the situation matches a skill's trigger (e.g., you mention "tests are flaky", or "write an implementation plan"), Antigravity will **autonomously** load and follow the skill's specific instructions.

### 📝 Planning & Architecture
* **`brainstorming`**: Activates before creative work. Explores user intent, requirements, and edge cases *before* any code is written. Prevents building the wrong thing.
* **`planning` / `writing-plans`**: Triggers when dealing with multi-step tasks. Forces the agent to write a bite-sized, Test-Driven implementation plan assumming zero prior context.
* **`executing-plans`**: Batches task execution from a written plan, checking in with you periodically rather than trying to do everything at once and failing.
* **`subagent-driven-development`**: A hyper-efficient workflow where Antigravity dispatches fresh, dedicated subagents for independent tasks to prevent context pollution and maximize parallel speed.

### 🛠️ Core Engineering
* **`test-driven-development` (TDD)**: Forces the rigid discipline of writing failing tests first, implementing minimal code, and refactoring.
* **`error-handling-patterns`**: Triggers when designing APIs or dealing with faults. Enforces mastery of exceptions, Result types, and graceful degradation.
* **`systematic-debugging`**: Activates when fixing bugs. Prevents the agent from endlessly guessing; forces it to form hypotheses, isolate variables, and find root causes.
* **`verification-before-completion`**: Ensures the agent physically tests and validates code changes before telling you the task is "done".

### 🎨 Design & Ecosystem
* **`brand-identity`**: The single source of truth for your brand guidelines, active whenever generating UI components. Ensures all generated code respects your specific color tokens, typography, and voice/tone.
* **`using-git-worktrees`**: Automates the management of isolated Git worktrees, allowing the agent to experiment safely without breaking your main branch.
* **`finishing-a-development-branch`**: Triggers at the end of a feature lifecycle to ensure tests pass, code is pristine, and the branch is safely merged or handed off.

### 🤖 Meta-Agent Skills (Operating the Agent)
* **`using-superpowers`**: The master directive that forces the AI to check for and apply relevant skills before answering any of your questions.
* **`dispatching-parallel-agents`**: Activates when multiple independent bugs occur, allowing Antigravity to solve 3 separate problems concurrently instead of sequentially.
* **`receiving-code-review` & `requesting-code-review`**: Defines strict rules for how the agent should review your code, and how it should accept your feedback (no performative apologies, just fixes).
* **`gemini-skill-creator`**: Triggers when you say "Create a new skill for X." Opens a structured workflow to generate bulletproof new skills for the `.agent` folder.
* **`writing-skills`**: Advanced meta-skill on how to write *process documentation* using TDD principles, ensuring new skills are loophole-free.

---

### 💡 Why this Ecosystem is Powerful
Because everything is modular and global, you have essentially built yourself a **Junior Engineering Team, QA Department, and Design Lead** all rolled into one. Antigravity knows to check its toolbox *before* writing code, meaning the more you utilize this setup, the more predictable, high-quality, and autonomous the agent's output becomes across every project you touch!
