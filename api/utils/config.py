import datetime

# 署名鍵(対称鍵)
# デフォルトのアルゴリズムはHS256
JWT_SECRET_KEY = "sample"

# デフォルトは15分
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=10)

JWT_TOKEN_LOCATION = ["cookies"]

# CSRF対策 - same siteにのみCookieを送信する。
JWT_COOKIE_SAMESITE = "Strict"

# XSS対策 - デフォルトでhttponly=Trueのため、設定不要

# httpsでのみCookieを送信する。ローカル環境のためFalseの設定。
JWT_COOKIE_SECURE = False
