# Git Workflow: Sharing Publicly & Working Personally

This guide explains how to share your clean project with the world while keeping your personal experiments separate using **Git Branches**.

## Phase 1: Share Publicly (The "Clean" Version)

Perform these steps inside your `chatterbox` folder.

1.  **Initialize Git** (Start tracking files):
    ```bash
    git init
    ```

2.  **Add Files & Commit**:
    This takes a snapshot of your current "clean" state.
    ```bash
    git add .
    git commit -m "Initial release: Chatterbox for Blackwell"
    ```

3.  **Rename Branch to Main**:
    ```bash
    git branch -M main
    ```

4.  **Connect to GitHub** (Replace URL with your own repo):
    ```bash
    git remote add origin https://github.com/codingoai/chatterbox-blackwell.git
    ```

5.  **Push to GitHub**:
    ```bash
    git push -u origin main
    ```

🎉 **Done!** Your code is now live for everyone to see.

---

## Phase 2: Start Personal Work (The "Private" Branch)

Now that the public version is safe, let's create a separate workspace for your personal edits.

1.  **Create a New Branch**:
    This copies the current state into a new parallel timeline called `personal-dev`.
    ```bash
    git checkout -b personal-dev
    ```

2.  **Verify You Are on the New Branch**:
    ```bash
    git branch
    # You should see:
    #   main
    # * personal-dev  <-- The asterisk means you are here
    ```

3.  **Do Your Work**:
    Edit files, change `example_tts_turbo.py`, break things! It won't affect the `main` branch.

4.  **Save Your Personal Work**:
    ```bash
    git add .
    git commit -m "My personal experiments"
    ```

---

## Phase 3: Switching Back & Forth

**Scenario A: You want to update the public code.**
(Maybe you fixed a bug that everyone should have).

1.  Switch to main:
    ```bash
    git checkout main
    ```
    *(Check your files! Changes from `personal-dev` have disappeared. That is magic.)*

2.  Make the fix, commit, and push:
    ```bash
    git add .
    git commit -m "Fixed a bug for everyone"
    git push origin main
    ```

**Scenario B: You want to go back to your experiments.**
1.  Switch back:
    ```bash
    git checkout personal-dev
    ```
    *(Your personal files are back exactly where you left them).*

---

## Summary Cheat Sheet

| Command | Action |
| :--- | :--- |
| `git checkout -b personal-dev` | **Create** & switch to a new branch |
| `git checkout main` | Switch to **Public** version |
| `git checkout personal-dev` | Switch to **Personal** version |
| `git status` | Check which branch you are on |
