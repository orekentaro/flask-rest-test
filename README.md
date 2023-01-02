# ~採用管理をするためのシステム~
## 色々試していたら処理がクッソ遅くなったのでボツ

dockerとMakeFileを使って誰でも同じ環境で楽にAPIを実装できたらと言う思想で作成。

Django風に作ろうとして失敗しました。

あと、Flask-SQLAlchemy等Flask用にラッパーされたライブラリを敢えて使用しなかったが失敗だった。

大人しくDjangoで作り直す。



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
