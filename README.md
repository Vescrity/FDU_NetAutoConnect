使用 selenium 解决宿舍断网重登。  

#### 为什么不直接 curl

问就是试过了，不管用  
改到 .36 后还没试过（

## 使用

- 类 Unix 系统执行 `setup.sh` 。Windows `setup.bat` 。仅测试了 Linux 环境。
- 创建 `config.py` ，根据实际情况更改。

```python
user='123456'
paswd='123456'
url='http://10.102.250.36/'
domain_name='中国联通'
```
- venv 下执行 `main.py`

### 配合 cronie 定时任务自动化执行

编写启动脚本。例如：
```bash
#!/bin/bash
cd /path/to/FDU_NetAutoConnect
source ./.venv/bin/activate
python main.py
```
并添加执行权限。  

添加任务，例如：

```bash
crontab -e
```

```
0 6 * * * /path/to/your/script
```
确保已安装 cronie.

