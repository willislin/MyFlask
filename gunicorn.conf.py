# 用本機的 8081 port
bind = "0.0.0.0:8081"
# gunicorn 的 pid file，和前面 runit 設定檔內相同
pidfile = "/tmp/flask_project.pid"
# 設定要用幾個 worker 來執行
workers = 2
timeout = 90