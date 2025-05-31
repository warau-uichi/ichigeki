# How to Run Pyxel Games

This document explains how to run Pyxel games locally.

## Running Locally (Without Docker)

This section describes how to set up and run the Pyxel game directly on your local machine.

### 1. Prerequisites

*   **Python:** Python 3.9 or higher must be installed on your system.
*   **Package Manager:** `uv` or `pip` should be installed for managing Python packages. `uv` is a newer, faster alternative if available.

### 2. Setup Virtual Environment and Install Dependencies

Using a virtual environment is strongly recommended to isolate project dependencies.

*   **Create a virtual environment:**
    *   If using `uv`:
        ```bash
        uv venv
        ```
    *   If using the standard `venv` module with Python:
        ```bash
        python -m venv .venv
        ```

*   **Activate the virtual environment:**
    *   On macOS and Linux (bash/zsh):
        ```bash
        source .venv/bin/activate
        ```
    *   On Windows (Command Prompt):
        ```bash
        .venv\Scripts\activate.bat
        ```
    *   On Windows (PowerShell):
        ```bash
        .venv\Scripts\Activate.ps1
        ```

*   **Install Dependencies:**

    #### Installing Pyxel on macOS (Recommended)
    For macOS, it's recommended to install Pyxel using `pipx` for a clean global installation:
    1. Install Homebrew (if you don't have it): `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    2. Install pipx: `brew install pipx`
    3. Ensure pipx is in your path: `pipx ensurepath`
    4. Install Pyxel: `pipx install pyxel`

    After this, Pyxel is available system-wide. You can then run the game using `python src/main.py` from the project root. If you use other development tools like `ruff` or `coverage` (which are typically installed in your project's virtual environment), ensure that virtual environment is active when you use those tools. Pyxel itself will be run from the `pipx` environment.

    #### Installing Pyxel into a Virtual Environment (All OS)
    Alternatively, on any OS (including macOS, Linux, Windows), you can install Pyxel directly into your project's virtual environment along with other development tools:
    (Ensure your virtual environment is active before running these commands)
    ```bash
    # Using uv
    uv pip install pyxel ruff coverage

    # Or using pip
    pip install pyxel ruff coverage
    ```
    *   Note: If your project has a `pyproject.toml` with dependencies specified, you might also be able to install them using `uv pip install -e .` (for main dependencies) or `uv pip install -e .[dev]` (if a "dev" extra is defined). For this guide, we'll stick to explicit package installation.

### 3. Running the Game

*   **Execute the main script:**
    Once Pyxel is installed (either via `pipx` or into your active virtual environment) and any other necessary dependencies are installed in your venv, you can run the game application from the project root using:
    ```bash
    python src/main.py
    ```

*   **Graphical Environment Notes:**
    Pyxel is a graphical library and requires a desktop environment to run.
    *   **Linux:** Ensure an X11 display server is running. If you are in a headless environment (like a server without a monitor), X11 forwarding (e.g., via SSH) or a virtual framebuffer like Xvfb will be necessary.
    *   **Windows & macOS:** This is generally handled automatically by the operating system, as they are inherently graphical.

**Note on Asset Generation Scripts:**
You might notice several Python scripts in the project's root directory (e.g., `create_pyxel_resource.py`, `add_player_sprites.py`). These scripts were used by the developers to programmatically create and populate the `assets/game.pyxres` file. You **do not** need to run these scripts to play or run the game. The game (`src/main.py`) directly uses the `assets/game.pyxres` file, which already contains all necessary assets.

---
This is the recommended method for playing the game. The Docker environment is preserved for development and automated testing purposes.
