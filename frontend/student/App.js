
import React, { useState, useEffect } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

export default function StudentApp() {
  const [electricity, setElectricity] = useState(0);
  const [hotWater, setHotWater] = useState(0);
  const [goal, setGoal] = useState(50); // 初始节能目标

  useEffect(() => {
    // 模拟获取实时数据
    setInterval(() => {
      setElectricity(Math.random() * 100); // 随机生成电力消耗
      setHotWater(Math.random() * 50); // 随机生成热水消耗
    }, 5000); // 每5秒更新一次
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.header}>宿舍水电使用统计与提醒系统 - 学生端</Text>
      <Text style={styles.data}>电力消耗: {electricity.toFixed(2)} kWh</Text>
      <Text style={styles.data}>热水消耗: {hotWater.toFixed(2)} L</Text>
      <Text style={styles.data}>节能目标: {goal} kWh</Text>
      <Button title="设置节能目标" onPress={() => setGoal(goal + 5)} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f1f1f1',
  },
  header: {
    fontSize: 24,
    color: '#007bff',
    fontWeight: 'bold',
  },
  data: {
    fontSize: 18,
    color: '#333',
  },
});
