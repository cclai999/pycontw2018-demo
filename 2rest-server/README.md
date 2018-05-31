# Pycon Taiwan 2018
### Java-Jersey 到 Python-Flask 服務不中斷重構之旅
### RESTful API in Flask

這個demo 的程式主要參考 https://gist.github.com/miguelgrinberg/5614326 這部程式碼，原作者 Miguel Grinberg 的 blog [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) 有深入的說明，對Flask有興趣的朋友建議去看這 blog，有非常棒的教學文

執行方法
```shell
# 安裝相依套件
pip install -r requirements.txt

# 啟動 RESTful API server
python rest-server.py

# 查詢todo list 中所有task的內容
curl -i http://localhost:5000/todo/api/v1.0/tasks

# 查詢todo list 中 task #1 的內容
curl -i http://localhost:5000/todo/api/v1.0/tasks/1

# 新增一個 task
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks


# 候改 task #2 中 'done' 的值為 'true'
curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/2

# 刪除 task #3 
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/todo/api/v1.0/tasks/3
``` 
