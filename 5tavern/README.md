# Pycon Taiwan 2018
### Java-Jersey 到 Python-Flask 服務不中斷重構之旅
### Tavern RESTful API 自動化測試
這個demo 的程式是 Tavern 的範例程式:

https://github.com/taverntesting/tavern/tree/master/example/simple

- 安裝並執行 server
```shell
# 安裝相依套件
pip install -r requirements.txt

# 啟動 server
python server.py
```
- 執行測試的三種方法
#### a. 直接在 Python code 用 library 執行 yaml file
```python
from tavern.core import run

success = run("test_server.tavern.yaml", {})

if not success:
    print("Error running tests")
```

#### b. 在命令列利用 Use tavern-ci tool 跑測試
```shell
$ tavern-ci test_server.tavern.yaml
$ echo $?
0
```

#### c. 透過 pytest
```shell
$ py.test test_server.tavern.yaml
=============================================== test session starts ===============================================
platform darwin -- Python 3.6.5, pytest-3.6.0, py-1.5.3, pluggy-0.6.0
rootdir: /Users/maxlai/PycharmProjects/pycontw2018/pycontw2018-demo/5tavern, inifile:
plugins: tavern-0.9.8
collected 3 items

test_server.tavern.yaml ...                                                                                 [100%]

============================================ 3 passed in 0.25 seconds =============================================
```
