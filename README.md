#  Text-to-SQL Agent with Clarification Engine & Self-Healing

An enterprise-grade, stateful Text-to-SQL agent built using **LangGraph**, **Google Gemini**, and **SQLite**. Features human-in-the-loop clarification interrupts, self-healing SQL execution loops, and dynamic schema retrieval.

---

##  Sprint 0: Database Setup & Infrastructure
- Set up project structure and package management via `uv`.
- Automated retrieval and schema verification of the **Chinook SQLite Sample Database** (`11` tables, relational e-commerce metadata).

### Quickstart Setup

1. **Install Dependencies:**
   ```bash
   uv sync
Initialize Sample Database:

Bash
uv run python scripts/setup_db.py

---

### Step 3: Run Git Commands in Terminal

Run these commands in your Antigravity / Cursor terminal to make your **Sprint 0** commit and push it to GitHub:

```bash
# 1. Initialize git (if not already initialized)
git init

# 2. Stage all files created so far
git add .

# 3. Check what's staged (make sure sample.db is NOT listed)
git status

# 4. Commit Sprint 0
git commit -m "feat(infra): setup sprint 0 project structure and sqlite database verification script"

# 5. Connect to your GitHub repo (replace URL with your actual repo link)
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/text-to-sql-agent.git

# 6. Push to GitHub
git push -u origin main