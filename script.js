async function startTest() {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Testing your internet speed... Please wait.";

    try {
        const response = await fetch('/api/speedtest');
        const data = await response.json();

        if (data.error) {
            resultDiv.innerHTML = `Error: ${data.error}`;
        } else {
            resultDiv.innerHTML = `
                <p><strong>IP:</strong> ${data.ip_details.ip}</p>
                <p><strong>Region:</strong> ${data.ip_details.region}</p>
                <p><strong>City:</strong> ${data.ip_details.city}</p>
                <p><strong>Country:</strong> ${data.ip_details.country}</p>
                <p><strong>Org:</strong> ${data.ip_details.org}</p>
                <p><strong>Ping:</strong> ${data.speed_results.ping} ms</p>
                <p><strong>Download Speed:</strong> ${data.speed_results.download_speed} Mbps</p>
                <p><strong>Upload Speed:</strong> ${data.speed_results.upload_speed} Mbps</p>
            `;
        }
    } catch (error) {
        resultDiv.innerHTML = `Error: ${error.message}`;
    }
}

  
