## 以 Nginx 的 Upstream 設定達成金絲雀部署修正版

### Prerequirement
要執行這個 demo，必須要先安裝 [Docker](https://docs.docker.com/install/)

### 緣由
之前 demo 目錄中 [6canry](./6canary) 的 nginx.conf 若是 upstream 中的 host 是指定 docker-compose file 的 service name (ex. web1, web2)

如果今天我覺得 service load 沒有那麼重而暫時不想啟動 web3 這個 service, 那 [nginx/nignx.conf](./nginx/nginx.conf) 的設定會讓 [docker-compose-disable-web3.yml](./docker-compose-disable-web3.yml) 的 nginx server crash.

在網上找到一個解決方法：是將 [docker-compose file](./docker-compose-fix-ip.yml) 將每個 service 都設為固定ip, 
然後在 nginx 的 [config file](./nginx/nginx-ip.conf) upstream 也寫成固定 ip, 這樣就可以避免 nginx 在 web3 沒有啟動時會 crash.

參考資料：[IThome 2019 鐵人賽:用js成為老闆心中的全端工程師, Day30-Docker network 暨完賽回顧](https://ithelp.ithome.com.tw/m/articles/10206725)

### nginx crash 的重現
- 利用 docker-compose 把 nginx, web1 & web2 server 啟動
```shell
$ docker-compose -f docker-compose-disable-web3.yml build
$ docker-compose -f docker-compose-disable-web3.yml up
``` 

### 修正後的 docker-compose-fix-ip.yml
- 利用 docker-compose 把 nginx, web1 & web2 server 啟動
```shell
$ docker-compose -f docker-compose-fix-ip.yml build
$ docker-compose -f docker-compose-fix-ip.yml up
``` 
- 連續打 nginx 10 次，觀察 web1 & web2 個別回應的次數
```shell
# 這個 demo 需要 requests 套件
$ pip install requests
$ python request_10_times.py
{"no":1,"server-name":"demo-1"}
{"no":2,"server-name":"demo-2"}
{"no":3,"server-name":"demo-2"}
{"no":4,"server-name":"demo-2"}
{"no":5,"server-name":"demo-1"}
{"no":6,"server-name":"demo-2"}
{"no":7,"server-name":"demo-2"}
{"no":8,"server-name":"demo-2"}
{"no":9,"server-name":"demo-1"}
{"no":10,"server-name":"demo-2"}
```
