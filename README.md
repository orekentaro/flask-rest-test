# 採用管理をするためのシステム
## 色々試していたら処理がクッソ遅くなったのでボツ

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
make init
```

## 起動

```
make run
```

## データリセットと再起動

```
make reset
```
