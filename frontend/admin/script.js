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

// Simulate new data periodically (for demonstration purposes)
function updateEnergyData() {
    energyData.datasets[0].data.push(Math.random() * 100);
    energyData.labels.push(new Date().toLocaleDateString());
    energyChart.update();
}

// Update energy data every 5 seconds
setInterval(updateEnergyData, 5000);
