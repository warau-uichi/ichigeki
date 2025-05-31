# Dockerコンテナ内でPyxelゲームを実行する方法

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
