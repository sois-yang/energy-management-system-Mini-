
import React, { useState, useEffect } from 'react';
import { Chart } from 'react-chartjs-2';
import axios from 'axios';

const ManagementApp = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Fetching energy data from the backend
    axios.get('/api/energyData')
      .then(response => {
        setData(response.data);
      })
      .catch(error => console.log(error));
  }, []);

  const chartData = {
    labels: data.map(item => item.timestamp),
    datasets: [{
      label: '电力消耗',
      data: data.map(item => item.electricityUsage),
      borderColor: 'rgba(0, 123, 255, 0.6)',
      fill: false,
    }],
  };

  return (
    <div>
      <h1>管理端 - 宿舍水电使用统计</h1>
      <Chart type="line" data={chartData} />
    </div>
  );
};

export default ManagementApp;
