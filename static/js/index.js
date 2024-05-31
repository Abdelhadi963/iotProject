
data = [
    {
        "timestamp": "19:33:07",
        "temperature": 22.0,
        "humidity": 20.0
    },
    {
        "timestamp": "19:38:10",
        "temperature": 22.0,
        "humidity": 20.0
    },
    {
        "timestamp": "19:43:11",
        "temperature": 22.0,
        "humidity": 26.0
    },
    {
        "timestamp": "19:48:14",
        "temperature": 22.0,
        "humidity": 26.0
    },
    {
        "timestamp": "19:53:15",
        "temperature": 22.0,
        "humidity": 20.0
    },
    {
        "timestamp": "19:58:15",
        "temperature": 22.0,
        "humidity": 23.0
    },
    {
        "timestamp": "20:03:16",
        "temperature": 22.0,
        "humidity": 20.0
    },
    {
        "timestamp": "20:08:17",
        "temperature": 22.0,
        "humidity": 23.0
    },
    {
        "timestamp": "20:13:17",
        "temperature": 21.0,
        "humidity": 20.0
    },
    {
        "timestamp": "20:18:18",
        "temperature": 21.0,
        "humidity": 21.0
    },
    {
        "timestamp": "20:23:19",
        "temperature": 21.0,
        "humidity": 20.0
    },
    {
        "timestamp": "20:28:19",
        "temperature": 21.0,
        "humidity": 20.0
    },
    {
        "timestamp": "20:33:20",
        "temperature": 21.0,
        "humidity": 20.0
    },
    {
        "timestamp": "20:38:20",
        "temperature": 21.0,
        "humidity": 20.0
    },
    {
        "timestamp": "20:43:21",
        "temperature": 21.0,
        "humidity": 20.0
    },
    {
        "timestamp": "20:48:22",
        "temperature": 21.0,
        "humidity": 20.0
    },
    {
        "timestamp": "20:53:22",
        "temperature": 21.0,
        "humidity": 21.0
    },
    {
        "timestamp": "20:58:25",
        "temperature": 21.0,
        "humidity": 26.0
    },
    {
        "timestamp": "21:03:26",
        "temperature": 21.0,
        "humidity": 20.0
    },
    {
        "timestamp": "21:08:29",
        "temperature": 21.0,
        "humidity": 21.0
    },
    {
        "timestamp": "21:13:30",
        "temperature": 21.0,
        "humidity": 20.0
    },
    {
        "timestamp": "21:18:30",
        "temperature": 21.0,
        "humidity": 21.0
    },
    {
        "timestamp": "21:23:31",
        "temperature": 21.0,
        "humidity": 22.0
    },
    {
        "timestamp": "21:28:31",
        "temperature": 21.0,
        "humidity": 20.0
    },
    {
        "timestamp": "21:33:32",
        "temperature": 20.0,
        "humidity": 21.0
    },
    {
        "timestamp": "21:38:33",
        "temperature": 21.0,
        "humidity": 20.0
    },
    {
        "timestamp": "21:43:33",
        "temperature": 20.0,
        "humidity": 21.0
    },
    {
        "timestamp": "21:48:34",
        "temperature": 20.0,
        "humidity": 21.0
    },
    {
        "timestamp": "21:53:35",
        "temperature": 20.0,
        "humidity": 21.0
    },
    {
        "timestamp": "21:58:35",
        "temperature": 20.0,
        "humidity": 21.0
    },
    {
        "timestamp": "22:03:36",
        "temperature": 20.0,
        "humidity": 21.0
    }
]

function getTemperatureStatus(temp) {
    if (temp >= 18 && temp <= 24) {
        return 'Normal';
    } else if (temp >= 25 && temp <= 30) {
        return 'High';
    } else if (temp >= 10 && temp <= 17) {
        return 'Low';
    } else if (temp > 30) {
        return 'Critical High';
    } else if (temp < 10) {
        return 'Critical Low';
    }
}

function getHumidityStatus(humidity) {
    if (humidity >= 30 && humidity <= 50) {
        return 'Normal';
    } else if (humidity >= 51 && humidity <= 70) {
        return 'High';
    } else if (humidity >= 20 && humidity <= 29) {
        return 'Low';
    } else if (humidity > 70) {
        return 'Very High';
    } else if (humidity < 20) {
        return 'Very Low';
    }
}

function getAirQualityStatus(aqi) {
    if (aqi >= 0 && aqi <= 50) {
        return 'Good';
    } else if (aqi >= 51 && aqi <= 100) {
        return 'Moderate';
    } else if (aqi >= 101 && aqi <= 150) {
        return 'Unhealthy for Sensitive Groups';
    } else if (aqi >= 151 && aqi <= 200) {
        return 'Unhealthy';
    } else if (aqi >= 201 && aqi <= 300) {
        return 'Very Unhealthy';
    } else if (aqi > 300) {
        return 'Hazardous';
    }
}

function generateNormalDistribution(mean, stdDev) {
    let u = 0, v = 0;
    while (u === 0) u = Math.random(); // Converting [0,1) to (0,1)
    while (v === 0) v = Math.random();
    let num = Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    num = num * stdDev + mean;
    return Math.round(num);
}

function updateData(i){

    const temperature_Act = document.getElementById("room-temp") ;
    const temperature_status = document.getElementById("room-temp-status") ;
    const humidity_act = document.getElementById("room-humidity") ;
    const humiduty_status = document.getElementById("room-humidity-status") ;
    const airquality_act = document.getElementById("air-quality") ;
    const airquality_status = document.getElementById("air-quality-status") ;

    temperature_Act.textContent = `${data[i].temperature} °C`;
    humidity_act.textContent = `${data[i].humidity} %`;

    const meanAQI = 50; 
    const stdDevAQI = 10; 
    const airQuality = generateNormalDistribution(meanAQI, stdDevAQI);
    airquality_act.textContent = `${airQuality}`

    temperature_status.textContent = `${getTemperatureStatus(data[i].temperature)}`;
    humiduty_status.textContent = `${getHumidityStatus(data[i].humidity)} `;
    airquality_status.textContent =`${getAirQualityStatus(airQuality)}`;
}

function update() {
    let i = 0;
    const interval = setInterval(() => {
        updateData(i);
        i++;
        if (i >= data.length) {
            clearInterval(interval);
        }
    }, 50000); 
}

update();

function getCurrentTime() {
    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const seconds = now.getSeconds();

    const formattedHours = hours < 10 ? `0${hours}` : hours;
    const formattedMinutes = minutes < 10 ? `0${minutes}` : minutes;
    const formattedSeconds = seconds < 10 ? `0${seconds}` : seconds;

    return `${formattedHours}:${formattedMinutes}:${formattedSeconds}`;
}

function getDatetime() {
    const date_time = document.getElementById("date-time");
    date_time.textContent = `Friday, ${getCurrentTime()}`;
}

function updateOutside() {
    setInterval(() => {
        getDatetime();
    }, 1000); // Update every 1000 milliseconds (1 second)
}

// Call the function to start updating the date and time
updateOutside();


