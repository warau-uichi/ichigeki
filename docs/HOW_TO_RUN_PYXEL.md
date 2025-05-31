# How to Run Pyxel Games

This document explains how to run Pyxel games, either locally or using Docker.

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

*   **Install dependencies:**
    The main runtime dependency for this project is Pyxel. Development tools like Ruff (for linting) and Coverage (for test coverage) are typically listed in `pyproject.toml`.
    *   To install Pyxel (and common development tools):
        ```bash
        # Using uv
        uv pip install pyxel ruff coverage

        # Or using pip
        pip install pyxel ruff coverage
        ```
    *   Note: If your project has a `pyproject.toml` with dependencies specified, you might also be able to install them using `uv pip install -e .` (for main dependencies) or `uv pip install -e .[dev]` (if a "dev" extra is defined). For this guide, we'll stick to explicit package installation.


### 3. Running the Game

*   **Execute the main script:**
    Once the virtual environment is active and dependencies are installed, you can run the game application using:
    ```bash
    python src/main.py
    ```

*   **Graphical Environment Notes:**
    Pyxel is a graphical library and requires a desktop environment to run.
    *   **Linux:** Ensure an X11 display server is running. If you are in a headless environment (like a server without a monitor), X11 forwarding (e.g., via SSH) or a virtual framebuffer like Xvfb will be necessary.
    *   **Windows & macOS:** This is generally handled automatically by the operating system, as they are inherently graphical.

---

## Dockerコンテナ内でPyxelゲームを実行する方法

このドキュメントでは、ホストマシンからDockerコンテナ内でPyxelゲームを実行する方法を説明します。

## 前提条件

- Dockerがインストールされていること
- プロジェクトのDockerイメージがビルドされていること

## Docker環境のセットアップ

まず、Dockerコンテナを起動します：

```bash
cd /Users/yosukeikei/Projects/ichigeki
docker compose -f docker/docker-compose.yml up -d
```

## 仕組みの説明

Pyxelはグラフィカルな環境を必要としますが、Dockerコンテナにはデフォルトでグラフィカルな環境がありません。ホスト側で表示するためには、X11フォワーディングなどの方法が必要です。

## ホスト側でゲームをプレイする方法

Dockerコンテナ内で実行されるPyxelゲームをホスト側で表示・プレイするには、以下の方法があります。

### X11フォワーディングを使用する方法

macOSでは、XQuartzを使用してX11フォワーディングを設定できます：

1. XQuartzをインストールします：
```bash
brew install --cask xquartz
```

2. XQuartzを起動し、環境設定で「リモート接続を許可」をオンにします。
```bash
open -a XQuartz
```

3. XQuartzを再起動します。

4. Docker環境変数を変更します。docker-compose.ymlファイルの`DISPLAY`環境変数を`host.docker.internal:0`に設定します：
```yaml
environment:
  - DISPLAY=host.docker.internal:0
```

5. Dockerコンテナを再起動します：
```bash
docker compose -f docker/docker-compose.yml down
docker compose -f docker/docker-compose.yml up -d
```

6. プロジェクトに含まれる`run_pyxel_on_host.sh`スクリプトを使用して、ゲームを実行します：
```bash
./run_pyxel_on_host.sh src/main.py
```

この方法では、ゲームの画面がホスト側のXQuartzウィンドウに表示され、キー入力も可能になります。

## トラブルシューティング

### エラー: Failed to create window

このエラーが発生した場合、以下を確認してください：

1. XQuartzが正しく起動しているか
2. XQuartzの環境設定で「リモート接続を許可」がオンになっているか
3. Docker環境変数の`DISPLAY`が正しく設定されているか
4. Dockerコンテナの再起動後にXQuartzも再起動したか

### その他のエラー

他のエラーが発生した場合は、`RUST_BACKTRACE=1`環境変数を設定してより詳細なエラー情報を取得してください：

```bash
docker exec -it ichigekeen-dev-container bash -c "RUST_BACKTRACE=1 python -m pyxel run src/main.py"
```
