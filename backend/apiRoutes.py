# 从Flask框架中导入Blueprint模块
from flask import Blueprint

# 创建一个名为 'api_routes' 的蓝图。蓝图帮助我们把路由分组，方便管理
api_routes = Blueprint('api_routes', __name__)

# 定义一个路由，当用户访问 '/energyData' 时，系统会执行这个函数
# 这个路由只会响应GET请求（用于获取数据）
@api_routes.route('/energyData', methods=['GET'])
def get_energy_data():
    # 返回一个简单的消息，告诉用户这是能量数据接口
    return jsonify({'message': 'Energy data endpoint'})

# 定义另一个路由，当用户访问 '/setEnergyGoal' 时，系统会执行这个函数
# 这个路由只会响应POST请求（用于发送数据）
@api_routes.route('/setEnergyGoal', methods=['POST'])
def set_energy_goal():
    # 返回一个简单的消息，告诉用户这是设置能量目标的接口
    return jsonify({'message': 'Set energy goal endpoint'})
