# 导入Flask框架中的一些功能模块
from flask import Flask, jsonify, request
import sqlite3  # 导入SQLite模块，用于操作SQLite数据库

# 创建Flask应用对象
app = Flask(__name__)

# 数据库连接函数：用于连接SQLite数据库
def get_db():
    # 连接到名为 'energy_management.db' 的数据库文件
    conn = sqlite3.connect('energy_management.db')
    return conn  # 返回数据库连接对象

# 定义一个路由，响应GET请求，用于获取最新的能量数据
@app.route('/api/energyData', methods=['GET'])
def get_energy_data():
    # 获取数据库连接
    conn = get_db()
    # 创建一个游标对象，用于执行数据库查询
    cursor = conn.cursor()
    # 执行SQL查询，按时间戳降序获取最新的10条能量数据
    cursor.execute("SELECT * FROM energy_data ORDER BY timestamp DESC LIMIT 10")
    # 获取查询结果
    data = cursor.fetchall()
    # 关闭数据库连接
    conn.close()
    # 将查询结果以JSON格式返回给客户端
    return jsonify(data)

# 定义一个路由，响应POST请求，用于设置能量目标
@app.route('/api/setEnergyGoal', methods=['POST'])
def set_energy_goal():
    # 获取客户端请求中的JSON数据，提取 'goal' 字段的值（默认为0）
    goal = request.json.get('goal', 0)
    # 假设我们设置了一个全局的能量目标
    # 返回一个JSON响应，告诉客户端能量目标已经设置
    return jsonify({"status": "success", "message": f"Energy goal set to {goal} kWh"}), 201

# 如果这个脚本是直接运行的（而不是被导入到其他脚本中），就启动Flask应用
if __name__ == '__main__':
    app.run(debug=True)  # 启动Flask应用并开启调试模式，便于开发时查看错误信息
