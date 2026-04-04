# ⚡ Process Forker GUI (Tkinter)
A python-based stress-testing utility designed to evaluate system stability and window manager resilience. It executes high-frequency recursive UI spawning to analyze resources allocation limits and process scheduling under extreme load

## Description

This project is a simple experiment demonstrating rapid GUI window spawning using Python.

It uses:

* `tkinter` for GUI rendering
* `multiprocessing` to generate continuous spawn signals
* a queue system to communicate between processes

Each signal creates a new window with:

* randomized screen position
* custom layout (icon + text)

---

> **A Python-based resource exhaustion tool** that continuously forks processes and spams system notifications to consume CPU, memory, and OS resources.

##

> [!WARNING]
> **System Crash Potential:** This script will consume all available system resources (RAM/CPU) until the OS becomes unresponsive. Use only in a controlled environment (VM/Sandbox).

---

## How It Works

1. A background process (`worker`) continuously sends "spawn" signals into a queue.
2. The main process polls the queue at intervals.
3. For each signal received, a new window (`Toplevel`) is created.
4. Each window is rendered with a fixed size and random position on screen.

---

## Requirements

* Python 3.x
* Tkinter (usually included by default)

---

## Usage

```bash
python main.py
```

Make sure the following file exists:

```
assets/error.png
```

---

## Warning

* This program can spawn a large number of windows in a short time.
* It may cause high CPU usage and system instability.
* It can freeze or crash the environment where it is executed.

**Run this only inside a virtual machine (VM). Do not run on your main system.**

---

## Notes

* This is a behavior simulation project, not intended for real-world use.
* The focus is on understanding process communication and GUI event loops.
* No persistence or system-level modifications are performed.

---
