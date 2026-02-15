# Test, Publish, Submit

Do **Part 1** (test). Then **Part 2** (publish to GitHub). Then **Part 3** (submit). Do not skip ahead.

This project requires **Python 3.14**. Run all steps from **this project folder** (the repo root). Use `uv sync` to install dependencies; uv will use the Python version specified in `.python-version`.

---

# PART 1: Test the project

Run the server from this project folder to make sure it works.

---

## Step 1: Open Terminal

- **Mac:** **Terminal** app (Command+Space, type `Terminal`, Enter).
- **Windows:** **Command Prompt** or **PowerShell** (search for `cmd` or `PowerShell`).

**Check:** A window with a blinking cursor.

---

## Step 2: Go to this project folder

Type this (replace with **your** path if different):

```bash
cd ~/Desktop/knowledge-assistant-mcp
```

If the folder is in **Documents**:

```bash
cd ~/Documents/knowledge-assistant-mcp
```

**Check:** Run `pwd` and press Enter. The path should end with your project folder name (e.g. `knowledge-assistant-mcp`).

---

## Step 3: Install dependencies

Type:

```bash
uv sync
```

Press Enter.

**Check:** You see something like "Resolved" and "Installed" and no red error. If you see "command not found: uv," you need to install uv—tell me your OS and I'll give you the command.

**Check Python version:** Type `uv run python --version` and press Enter. You should see **Python 3.14.x**.

---

## Step 4: Create your .env file

Type:

```bash
cp .env.sample .env
```

Press Enter.

**Check:** Nothing usually prints. You now have a file named `.env` in your project folder.

---

## Step 5: Add your Google API key to .env

1. Open **this project folder** in Finder (Mac) or File Explorer (Windows).
2. Find the file **`.env`** (you may need to show hidden files: Mac = Command+Shift+.).
3. Open `.env` in a text editor.
4. Find: `GOOGLE_API_KEY=your-google-api-key-here`
5. Replace `your-google-api-key-here` with your **real** Google API key.
   - Get one: [Google AI Studio](https://aistudio.google.com/app/apikey) → sign in → Create API key → copy.
6. Save and close the file.

**Check:** The line looks like `GOOGLE_API_KEY=AIza...` (long string). Do **not** put this file or key on GitHub.

---

## Step 6: Start the server

In Terminal (still in your project folder), type:

```bash
uv run python -m src.server --transport stdio
```

Press Enter.

**Check:**
- **Success:** A short line of output, then the cursor sits there (server is running).
- **Error:** Red text or "Error" — copy the full message and tell me. Do not go to Part 2 until this works.

---

## Step 7: Stop the server

Press **Ctrl+C** (hold Control, press C).

**Check:** Server stops and you see your normal terminal prompt.

---

## Step 8 (optional): Test in Cursor

If you want to try the MCP server in Cursor:

1. **Settings** → **MCP** (or edit `.cursor/mcp.json`).
2. Add a server:
   - **Command:** `uv`
   - **Args:** `--directory`, `FULL_PATH_TO_THIS_PROJECT_FOLDER`, `run`, `python`, `-m`, `src.server`, `--transport`, `stdio`
   - (Replace `FULL_PATH_TO_THIS_PROJECT_FOLDER` with the real path, e.g. `/Users/Sean/Desktop/knowledge-assistant-mcp`.)
   - **Env:** `GOOGLE_API_KEY` = your key (or leave blank if Cursor reads `.env`).
3. Restart or reload MCP, then try a tool or the `knowledge_assistant_workflow` prompt.

You can skip this. Part 1 is done when Step 6 runs without errors and Step 7 stops the server.

---

# PART 2: Put the project on GitHub

Do this only after Part 1 works. You will turn **this project folder** into a Git repo and push it to a new GitHub repo.

---

## Step 9: Go to this project folder in Terminal

If Terminal is not already in your project folder, type (use your path):

```bash
cd ~/Desktop/knowledge-assistant-mcp
```

**Check:** Run `ls`. You see `README.md`, `src`, `pyproject.toml`, etc.

---

## Step 10: Initialize Git

Type:

```bash
git init
```

Press Enter.

**Check:** A line like "Initialized empty Git repository in .../knowledge-assistant-mcp/.git/"

---

## Step 11: Stage all files

Type:

```bash
git add .
```

Press Enter.

**Check:** Nothing usually prints.

---

## Step 12: Confirm .env is not included

Type:

```bash
git status
```

Press Enter.

**Check:** In the list, you must **not** see `.env`. If you see `.env`, **stop** and fix `.gitignore` so `.env` is ignored.

---

## Step 13: Create the first commit

Type:

```bash
git commit -m "Initial commit: Knowledge Assistant MCP server"
```

Press Enter.

**Check:** Something like "X files changed" and "create mode ..." with no red error.

---

## Step 14: Name the branch

Type:

```bash
git branch -M main
```

Press Enter.

**Check:** Nothing usually prints.

---

## Step 15: Create the repo on GitHub (in the browser)

1. Go to [github.com](https://github.com) and **sign in**.
2. Click the **+** icon (top right) → **New repository**.
3. **Repository name:** e.g. `knowledge-assistant-mcp`.
4. **Description (optional):** e.g. `Multi-agent RAG MCP server with human-in-the-loop`.
5. Leave **Public** selected.
6. **Do not** check "Add a README file," "Add .gitignore," or "Choose a license."
7. Click **Create repository**.

**Check:** You see a new page with a URL like `https://github.com/YOUR_USERNAME/knowledge-assistant-mcp.git`. Have that URL or YOUR_USERNAME and repo name ready.

---

## Step 16: Connect this folder to GitHub

In Terminal (still in your project folder), type this **one line** (replace `YOUR_USERNAME` and repo name with yours):

```bash
git remote add origin https://github.com/YOUR_USERNAME/knowledge-assistant-mcp.git
```

Example: username `johndoe`, repo `knowledge-assistant-mcp`:

```bash
git remote add origin https://github.com/johndoe/knowledge-assistant-mcp.git
```

Press Enter.

**Check:** Nothing usually prints. If you see "fatal: remote origin already exists," that's OK.

---

## Step 17: Push to GitHub

Type:

```bash
git push -u origin main
```

Press Enter.

**Check:**
- If it asks for **username** and **password:** username = your GitHub username; password = a **Personal Access Token** (GitHub → Settings → Developer settings → Personal access tokens → Generate new token). Use the token as the password.
- Success: something like "Writing objects: 100%" and "main -> main".

---

## Step 18: Verify on GitHub

1. In the browser, go to `https://github.com/YOUR_USERNAME/knowledge-assistant-mcp`.
2. Refresh.

**Check:** You see `README.md`, `src/`, `pyproject.toml`, `.env.sample`, `Dockerfile`, etc. at the top. You do **not** see `.env`.

---

# PART 3: Submit the assignment

Do this only after Part 2 is done and Step 18 looks correct.

---

## Step 19: Copy your repo URL

On your GitHub repo page, click the address bar and copy the URL. It should look like:

```
https://github.com/YOUR_USERNAME/knowledge-assistant-mcp
```

**Check:** You have that one line copied (no extra text).

---

## Step 20: Create the .txt file for submission

1. Open **Notepad** (Windows) or **TextEdit** (Mac; Plain Text mode).
2. Paste **only** the repo URL. Nothing else.
3. Save as e.g. `repo-link.txt` somewhere easy to find (e.g. Desktop).

**Check:** Opening the file shows exactly one line: your GitHub repo URL.

---

## Step 21: Submit

1. Go to the **course website** and the **lesson where you submit the project**.
2. Find where to **attach** or **upload** a file.
3. Select the `.txt` file from Step 20.
4. Submit.

**Check:** You get a confirmation that the assignment was submitted.

---

# Final checklist (before you submit)

- [ ] Part 1: Server ran without error (Step 6) and you stopped it (Step 7). Python 3.14.x (Step 3).
- [ ] Part 2: On GitHub you see `README.md`, `src/`, `pyproject.toml` at the top (Step 18). No `.env` on GitHub.
- [ ] Part 3: The `.txt` file contains **only** the repo URL (Step 20). You attached it and submitted (Step 21).

If any box is unchecked, fix that step before submitting.

---

# If something goes wrong

- **"uv: command not found"** – Install uv. Tell me your OS (Mac/Windows) for the exact command.
- **"git: command not found"** – Install Git from [git-scm.com](https://git-scm.com/).
- **Wrong Python version** – Make sure you're in this project folder and run `uv sync`; uv uses `.python-version` (3.14).
- **Server error in Step 6** – Copy the full error and tell me. Don't continue to Part 2 until the server runs.
- **".env" in git status (Step 12)** – Do not commit. Ensure `.env` is listed in `.gitignore`.
- **Git password rejected** – Use a GitHub Personal Access Token as the password (Step 17).

When something fails, say the **step number** and paste the **exact message** you see.
