# 採用管理をするためのシステム

## ファイル構成

```
./recruit-management
├── api  # Flaskで作成されたAPI
├── client  # Vue/TypeScriptで作成されたUI
├── docker-compose.yml
├── Makefile
├── README
```

## 初回起動

```
make start
```

## 起動

```
make run
```

## データリセットと再起動

```
make restart
```

## API テスト実行

```
docker exec -it api pytest
```

## カバレッジレポート出力

```
docker exec -it api pytest --cov=./api --cov-report=xml
```
