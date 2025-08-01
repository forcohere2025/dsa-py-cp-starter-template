# DSA Python CP Setup

This is a starter template designed to help you quickly set up a competitive programming (CP) and data structures & algorithms (DSA) workflow using Python.

---

## Features

* Pre-configured **devcontainer** environment for consistent development setup
* Simple task runner integration for executing Python code
* Automatic redirection of program output to `output.txt`
* Integrated layout restoration using **Layout Saver** extension

---

## Manual Execution

To run manually from the terminal:

```bash
python3 main.py > output.txt
```

---

## Task Runner (Execute Script)

Use the following shortcut to trigger execution automatically:

* **Windows/Linux**: `Ctrl + Shift + B`
* **macOS**: `Cmd + Shift + B`

This runs `main.py` and redirects the output to `output.txt`.

---

## Devcontainer Support

The included `.devcontainer` folder provides:

* Python installation and extension support
* Pre-configured VS Code workspace with tasks and layout support

Open this folder in **GitHub Codespaces** or locally with the **Dev Containers** extension.

---

## Layout Management

For developers who prefer a consistent editor setup, this project optionally integrates with the **Layout Saver** extension.

### Utility

* Save and restore your preferred VS Code window layout
* Useful for reopening files like `main.py`, `input.txt`, and `output.txt` in a pre-arranged split view
* A **default layout is already pre-configured** and can be restored immediately upon setup
* Trigger with:

  * `Ctrl + Alt + L` on Windows/Linux
  * `Cmd + Alt + L` on macOS

You can also use the Command Palette (`Ctrl + Shift + P`) to save or load layouts.