# Task Tracker CLI

A lightweight, dependency-free Command Line Interface (CLI) application built with Python to track and manage your tasks. This project was built to satisfy the core requirements of the [roadmap.sh Task Tracker challenge](https://roadmap.sh/projects/task-tracker).

## Features

- **Zero External Dependencies**: Built entirely using Python's standard library (`json`, `time`, `os`).
- **Modern Control Flow**: Utilizes Python 3.10+ Structural Pattern Matching (`match-case`) for clean CLI routing.
- **Persistent Storage**: Automatically creates and updates a local `data.json` file to store your tasks.
- **Full CRUD Support**: Add, update, display, and delete tasks dynamically.

---

## Getting Started

### Prerequisites

- **Python 3.10** or higher is required due to the use of modern structural pattern matching (`match-case`).

### Installation

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt and navigate to the folder containing the script:
   ```bash
   cd path/to/your/project/folder