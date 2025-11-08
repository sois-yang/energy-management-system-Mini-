let electricityConsumption = 5;
let hotWaterConsumption = 3;
let energyGoal = 50;
let energyData = {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    datasets: [{
        label: '电力消耗 (kWh)',
        data: [10, 20, 30, 40, 50],
        borderColor: 'rgba(0, 123, 255, 0.6)',
        fill: false
    }]
};

// Initialize chart
const ctx = document.getElementById('energyChart').getContext('2d');
const energyChart = new Chart(ctx, {
    type: 'line',
    data: energyData
});

function updateUsage() {
    // Simulating random updates for electricity and water usage
    electricityConsumption = (Math.random() * 100).toFixed(2);
    hotWaterConsumption = (Math.random() * 50).toFixed(2);

    document.getElementById('electricity-usage').innerText = electricityConsumption + " kWh";
    document.getElementById('water-usage').innerText = hotWaterConsumption + " L";

    // Update chart with new data
    energyData.datasets[0].data.push(electricityConsumption);
    energyData.labels.push(new Date().toLocaleDateString());
    energyChart.update();
}

function setGoal() {
    let goal = document.getElementById('goal').value;
    if (goal && goal > 0) {
        alert("已设置节能目标：" + goal + " kWh");
    } else {
        alert("请输入有效的节能目标！");
    }
}
