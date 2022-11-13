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

## システムストップ
```
#vueのサーバー停止
ctrl + c

# dockerコンテナの停止
make down
```

## DBシェル起動
```
make dbshell

# ログイン後
\c recruit-management
```

### テストユーザーでのログイン方法
```
# メールアドレス
test@test.test

# パスワード
password1234
```