let digits = document.getElementById("digits");
digits.addEventListener("input", (event) => {
    digits_value.innerHTML = event.target.value;
});

let size = document.getElementById("size");
size.addEventListener("input", (event) => {
    size_value.innerHTML = event.target.value;
});

function fetchData() {
    let digits = document.getElementById("digits").value;
    let size = document.getElementById("size").value;

    fetch("http://127.0.0.1:5000/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ digits: digits, size: size }),
    })
    .then(response => response.json())
    .then(data => {
        plotResults(data);
    })
    .catch(error => {
        console.error("Error fetching data:", error);
    });
}

function initializePlots() {
    let layout_time = {
        title: "Time Comparison (seconds)",
        barmode: "group",
    };

    let layout_memory = {
        title: "Memory Comparison (MB)",
        barmode: "group",
    };

    let plotData_time = [];
    let plotData_memory = [];

    Plotly.newPlot("plotly_chart_time", plotData_time, layout_time);
    Plotly.newPlot("plotly_chart_memory", plotData_memory, layout_memory);
}

function plotResults(data) {
    console.log(data);
    let digits = document.getElementById("digits").value;
    let size = document.getElementById("size").value;

    let trace_time = {
        x: ["Python", "NumPy"],
        y: [data.time_traditional, data.time_numpy],
        name: digits + " digits, " + size + "x" + size,
        type: "bar"
    };

    Plotly.addTraces("plotly_chart_time", trace_time);

    let trace_memory = {
        x: ["Python", "NumPy"],
        y: [data.memory_traditional, data.memory_numpy],
        name: digits + " digits, " + size + "x" + size,
        type: "bar"
    };

    Plotly.addTraces("plotly_chart_memory", trace_memory);
}

initializePlots();