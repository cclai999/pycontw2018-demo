# Pycon Taiwan 2018
### Java-Jersey 到 Python-Flask 服務不中斷重構之旅
### Flask+SQLAlchemy with  existing MySQL DB

要執行這個 demo，必須要先安裝 [Docker](https://docs.docker.com/install/)

- 使用 Docker 安裝 MySQL
假設專案原始碼放在 /works/www 之下
```shell
# 先在 /works/www 之下建立 'db' 目錄
mkdir db

# 啟動MySQL
docker run --restart=always --name mysql \
    -p 3306:3306 \
    -v /works/www/docker-mysqld.cnf:/etc/mysql/conf.d/mysqld.cnf \
    -v /works/www/db:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=pycontw2018 \
    -e MYSQL_DATABASE=demodb \
    -e MYSQL_USER=maxlai \
    -e MYSQL_PASSWORD=pycontw2018 \
    -d mysql/mysql-server:5.7
```
- 安裝並執行 server
```shell
# 安裝相依套件
pip install -r requirements.txt

# 在 MySQL 建立 DB 'demodb' 並插入測試資料 
python db_create.py

# 啟動 RESTful API server
python server_mysql.py

# 查詢todo list 中所有task的內容
curl -i http://localhost:5000/todo/api/v1.0/tasks
``` 
