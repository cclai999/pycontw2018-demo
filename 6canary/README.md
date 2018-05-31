# Pycon Taiwan 2018
### Java-Jersey 到 Python-Flask 服務不中斷重構之旅
### 以Nginx 的 Upstream設定達成金絲雀部署

要執行這個 demo，必須要先安裝 [Docker](https://docs.docker.com/install/)

- 利用 docker-compose 把 nginx, web1 & web2 server 啟動
```shell
$ docker-compose build
$ docker-compose up
``` 
- 連續打 nginx 10 次，觀察 web1 & web2 個別回應的次數
```shell
# 這個 demo 需要 requests 套件
$ pip install requests
$ python request_10_times.py
{"no":1,"server-name":"demo-2"}
{"no":2,"server-name":"demo-2"}
{"no":3,"server-name":"demo-1"}
{"no":4,"server-name":"demo-2"}
{"no":5,"server-name":"demo-2"}
{"no":6,"server-name":"demo-2"}
{"no":7,"server-name":"demo-2"}
{"no":8,"server-name":"demo-1"}
{"no":9,"server-name":"demo-2"}
{"no":10,"server-name":"demo-2"}
```
