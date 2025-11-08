# 导入 sqlite3 模块，这个模块用来操作 SQLite 数据库
import sqlite3

# 定义一个函数，用于插入电力和热水使用数据到数据库表格中
def insert_energy_data(electricity_usage, hot_water_usage):
    # 连接到 SQLite 数据库，'energy_management.db' 是我们使用的数据库文件
    conn = sqlite3.connect('energy_management.db')

    # 创建一个游标对象，游标用于执行数据库的操作
    cursor = conn.cursor()

    # 执行 SQL 语句，将电力和热水使用数据插入到 'energy_data' 表中
    # ? 是占位符，用来安全地传入数据
    cursor.execute("INSERT INTO energy_data (electricityUsage, hotWaterUsage) VALUES (?, ?)", (electricity_usage, hot_water_usage))

    # 提交事务，保存插入的数据
    conn.commit()

    # 关闭数据库连接
    conn.close()
