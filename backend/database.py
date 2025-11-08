# 导入 sqlite3 模块，这个模块用来操作 SQLite 数据库
import sqlite3

# 定义一个函数来创建数据库及表格
def create_db():
    # 连接到 SQLite 数据库。如果数据库不存在，会自动创建一个新的数据库
    conn = sqlite3.connect('energy_management.db')

    # 创建一个游标对象（cursor）。游标是用来执行 SQL 语句的
    cursor = conn.cursor()

    # 执行 SQL 语句：创建一个名为 energy_data 的表
    # 这个表有四个字段：id, electricityUsage, hotWaterUsage, timestamp
    cursor.execute('''CREATE TABLE IF NOT EXISTS energy_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- id 自动增加并作为主键
        electricityUsage INTEGER,              -- 存储电力使用量
        hotWaterUsage INTEGER,                 -- 存储热水使用量
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP  -- 存储时间，默认值为当前时间
    )''')

    # 提交事务（commit），保存对数据库的修改
    conn.commit()

    # 关闭数据库连接
    conn.close()

# 调用 create_db 函数，创建数据库和表格
create_db()
