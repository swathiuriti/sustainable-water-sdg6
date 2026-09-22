new Chart(document.getElementById("myChart"), {
    type: "bar",
    data: {
        labels: ["Hygiene", "Sanitation"],
        datasets: [{
            label: "Average Score",
            data:[85,90]
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});