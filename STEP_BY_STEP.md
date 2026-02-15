# Step-by-step instructions

Follow these steps **in order**. Do not skip steps. After each step, do the **Check** before going on.

---

## Part A: Get ready (Terminal + project folder)

### Step 1: Open Terminal

- **On Mac:** Press **Command + Space**, type **Terminal**, press **Enter**.
- **On Windows:** Press the Windows key, type **PowerShell** or **cmd**, press **Enter**.

**Check:** A window opens with a blinking cursor. You are in Terminal.

---

### Step 2: Go to your project folder

In Terminal, type this **exactly** (one line), then press **Enter**:

```bash
cd /Users/Sean/knowledge-assistant-mcp
```

**If your project is somewhere else**, use that path instead. Examples:
- If it’s on your Desktop: `cd ~/Desktop/knowledge-assistant-mcp`
- If it’s in Documents: `cd ~/Documents/knowledge-assistant-mcp`

**Check:** Type this and press **Enter**:

```bash
pwd
```

You should see a line that **ends with** `knowledge-assistant-mcp`.  
If you see something else, run Step 2 again with the correct path.

---

### Step 3: Install dependencies

In Terminal, type this **exactly**, then press **Enter**:

```bash
uv sync
```

**Check:**  
- You should see lines like `Resolved ...` and `Installed ...` and **no red error text**.  
- If you see **`command not found: uv`**, you need to install **uv** first (tell me your OS and I’ll give you the install command).

Then type this and press **Enter**:

```bash
uv run python --version
```

**Check:** You should see **`Python 3.14.x`** (the x can be any number).  
If you see a different version, stop and tell me.

---

## Part B: Add your API key

### Step 4: Create the .env file

In Terminal, type this **exactly**, then press **Enter**:

```bash
cp .env.sample .env
```

**Check:** Usually nothing is printed. The command just finishes.  
(That’s correct. It copied `.env.sample` to a new file named `.env`.)

---

### Step 5: Get a Google API key (if you don’t have one)

1. Open a **web browser**.
2. Go to: **https://aistudio.google.com/app/apikey**
3. **Sign in** with your Google account.
4. Click **“Create API key”** (or “Get API key”).
5. Copy the key (long string starting with `AIza...`).  
   **Keep this key private.** Do not share it or put it on GitHub.

**Check:** You have a long string copied (your API key).  
If you already have a key, you can use it and skip to Step 6.

---

### Step 6: Put the API key into .env

1. Open **Finder** (Mac) or **File Explorer** (Windows).
2. Go to your **project folder**: `knowledge-assistant-mcp`.
3. Find the file named **`.env`**.  
   - If you don’t see it: on **Mac**, press **Command + Shift + .** to show hidden files; on **Windows**, turn on “Hidden items” in the View menu.
4. **Double‑click** `.env` to open it in a text editor (e.g. TextEdit, Notepad).
5. Find this line:  
   `GOOGLE_API_KEY=your-google-api-key-here`
6. **Replace** `your-google-api-key-here` with your **real** API key (the one you copied).  
   The line should look like:  
   `GOOGLE_API_KEY=AIzaSy...` (long string, no spaces).
7. **Save** the file (e.g. **Command + S** on Mac, **Ctrl + S** on Windows).
8. **Close** the file.

**Check:** When you open `.env` again, the line shows your real key (starts with `AIza`), not `your-google-api-key-here`.  
**Important:** Never commit `.env` to GitHub. It must stay only on your computer.

---

## Part C: Test the server

### Step 7: Start the server

In **Terminal** (still in your project folder — run `cd /Users/Sean/knowledge-assistant-mcp` again if needed), type this **exactly**, then press **Enter**:

```bash
uv run python -m src.server --transport stdio
```

**Check:**  
- **Success:** You see a short line of output (maybe with an emoji or “Opik”), then the cursor just sits there with **no new prompt**. The server is running.  
- **Failure:** You see **red text** or the word **Error**. **Do not go to Step 8.** Copy the **entire** error message and tell me.

---

### Step 8: Stop the server

With the server still running (cursor sitting there), press:

**Ctrl + C**

(Hold the **Control** key and press **C** once.)

**Check:** The server stops. You see your normal terminal prompt again (e.g. your path and `%` or `$`).  
**Part C is done.** Your server works. You can go to Part D when you’re ready to put the project on GitHub.

---

## Part D: Put the project on GitHub

Do Part D only after Part C works. Do each step in order.

---

### Step 9: Make sure you’re in the project folder

In Terminal, type:

```bash
cd /Users/Sean/knowledge-assistant-mcp
```

Press **Enter**. Then type:

```bash
ls
```

Press **Enter**.

**Check:** You see a list that includes **`README.md`**, **`src`**, **`pyproject.toml`**, **`.env.sample`**, **`Dockerfile`**.  
If you don’t, run Step 2 again and then Step 9.

---

### Step 10: Turn the folder into a Git repo

Type this **exactly**, then press **Enter**:

```bash
git init
```

**Check:** You see a line like: **`Initialized empty Git repository in .../knowledge-assistant-mcp/.git/`**

---

### Step 11: Stage all files

Type this **exactly**, then press **Enter**:

```bash
git add .
```

**Check:** Usually nothing is printed. That’s correct.

---

### Step 12: Confirm .env is NOT being committed

Type this **exactly**, then press **Enter**:

```bash
git status
```

**Check:** In the list of files, you must **NOT** see **`.env`**.  
- If you **do** see `.env`, **stop.** Do not run Step 13. Tell me and we’ll fix `.gitignore`.  
- If you don’t see `.env`, it’s correct. Continue.

---

### Step 13: Create the first commit

Type this **exactly**, then press **Enter**:

```bash
git commit -m "Initial commit: Knowledge Assistant MCP server"
```

**Check:** You see something like **`X files changed`** and **`create mode ...`** with **no red error**.  
If it says **`*** Please tell me who you are`**, you must set your Git name and email first — tell me and I’ll give you the exact commands.

---

### Step 14: Name the main branch

Type this **exactly**, then press **Enter**:

```bash
git branch -M main
```

**Check:** Usually nothing is printed. That’s correct.

---

### Step 15: Create a new repo on GitHub (in your browser)

1. Open a **web browser**.
2. Go to **https://github.com** and **sign in**.
3. Click the **+** icon (top right) → **“New repository”**.
4. **Repository name:** type **`knowledge-assistant-mcp`** (or another name you prefer).
5. **Description (optional):** e.g. **Multi-agent RAG MCP server with human-in-the-loop**.
6. Leave **Public** selected.
7. **Do not** check “Add a README file,” “Add .gitignore,” or “Choose a license.”
8. Click **“Create repository.”**

**Check:** You see a new page with a URL like **`https://github.com/YOUR_USERNAME/knowledge-assistant-mcp`**.  
Note your **YOUR_USERNAME** (your GitHub username). You’ll need it in Step 16.

---

### Step 16: Connect your folder to GitHub

In **Terminal**, type this **one line** — but **replace `YOUR_USERNAME`** with **your real GitHub username**:

```bash
git remote add origin https://github.com/YOUR_USERNAME/knowledge-assistant-mcp.git
```

Example: if your username is **johndoe**, you type:

```bash
git remote add origin https://github.com/johndoe/knowledge-assistant-mcp.git
```

Press **Enter**.

**Check:** Usually nothing is printed.  
If you see **`fatal: remote origin already exists`**, that’s OK — you can continue.

---

### Step 17: Push to GitHub

Type this **exactly**, then press **Enter**:

```bash
git push -u origin main
```

**Check:**  
- If it asks for **username:** type your **GitHub username** and press Enter.  
- If it asks for **password:** do **not** type your GitHub password. You must use a **Personal Access Token**:  
  1. In the browser, go to GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**.  
  2. **Generate new token (classic)**. Give it a name, check **repo**, then generate.  
  3. **Copy the token** and paste it into Terminal when it asks for the password.  
- **Success:** You see something like **`Writing objects: 100%`** and **`main -> main`**.  
If you see an error, copy the full message and tell me.

---

### Step 18: Verify on GitHub

1. In your browser, go to **`https://github.com/YOUR_USERNAME/knowledge-assistant-mcp`** (use your username).
2. **Refresh** the page.

**Check:** You see **`README.md`**, **`src/`**, **`pyproject.toml`**, **`.env.sample`**, **`Dockerfile`** at the top.  
You do **NOT** see **`.env`**.  
**Part D is done.** Your project is on GitHub.

---

## Part E: Submit for certification

Do Part E only after Part D is done.

---

### Step 19: Copy your repo URL

1. On your GitHub repo page, click the **address bar** (the URL at the top).
2. Select the **entire** URL (e.g. **Command + A** on Mac, **Ctrl + A** on Windows).
3. **Copy** it (e.g. **Command + C**, **Ctrl + C**).  
   It should look like: **`https://github.com/YOUR_USERNAME/knowledge-assistant-mcp`**

**Check:** When you paste somewhere, you see **only** that one line, nothing else.

---

### Step 20: Create the submission file

1. Open **TextEdit** (Mac) or **Notepad** (Windows).  
   - Mac: set format to **Plain Text** (Format → Make Plain Text).
2. **Paste** the URL you copied (nothing else).
3. **Save** the file.  
   - Name it: **`repo-link.txt`**  
   - Save it somewhere easy to find (e.g. Desktop).

**Check:** When you open **`repo-link.txt`**, it contains **exactly one line**: your GitHub repo URL.

---

### Step 21: Submit in the course

1. Go to the **course website**.
2. Open the **lesson where you submit the project**.
3. Find where to **attach** or **upload** a file.
4. Select **`repo-link.txt`**.
5. **Submit.**

**Check:** You get a confirmation that the assignment was submitted.  
You’re done.

---

## Quick checklist

Before you say you’re done, confirm:

- [ ] **Step 3:** `uv sync` worked and `uv run python --version` shows Python 3.14.x.
- [ ] **Step 6:** Your real API key is in `.env` (and you never commit `.env`).
- [ ] **Step 7–8:** Server started and you stopped it with Ctrl+C.
- [ ] **Step 12:** `git status` did **not** list `.env`.
- [ ] **Step 18:** On GitHub you see the project and **no** `.env`.
- [ ] **Step 21:** You submitted `repo-link.txt` with only the repo URL.

If any step fails, **stop** and tell me the **step number** and the **exact message** you see (copy and paste).
