document.getElementById('update-btn').addEventListener('click', async () => {
    const response = await fetch('/api/weather/update');
    const data = await response.json();
    alert(data.status);
    fetchWeatherSummaries();
});

async function fetchWeatherSummaries() {
    const response = await fetch('/api/weather/summaries');
    const summaries = await response.json();
    const summaryDiv = document.getElementById('summary');
    summaryDiv.innerHTML = ''; // Clear previous summaries

    summaries.forEach(summary => {
        const div = document.createElement('div');
        div.innerHTML = `
            <h3>${summary.date}</h3>
            <p>Avg Temp: ${summary.avg_temp}°C</p>
            <p>Max Temp: ${summary.max_temp}°C</p>
            <p>Min Temp: ${summary.min_temp}°C</p>
            <p>Dominant Weather: ${summary.dominant_weather}</p>
        `;
        summaryDiv.appendChild(div);
    });
}

// Fetch summaries on initial load
fetchWeatherSummaries();
