# 导入所需的模块
import shutil  # 用于复制文件
import os      # 用于与操作系统交互（例如文件和目录）
from datetime import datetime  # 用于获取当前时间

# 定义一个函数，用来备份数据库
def backup_database():
    # 获取当前的时间戳，用于生成唯一的备份文件名
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")  # 格式：年-月-日-时-分-秒
    backup_filename = f"backup_{timestamp}.db"  # 生成备份文件名，例：backup_20251107123045.db

    # 使用shutil模块的copy函数将原始数据库文件复制到新文件
    shutil.copy("energy_management.db", backup_filename)  # 备份文件
    print(f"数据库已备份到 {backup_filename}")  # 输出提示信息，告知用户备份完成

# 定时备份
import time  # 用于执行定时任务
while True:
    backup_database()  # 调用备份数据库的函数
    time.sleep(86400)  # 每86400秒（24小时）执行一次备份
