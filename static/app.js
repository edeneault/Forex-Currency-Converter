//// JS for Line plot ////
// chart colors //
const COLORS = ['#007bff', '#28a745', '#333333', '#c3e6cb', '#dc3545', '#6c757d'];
const btnDetails = document.querySelector("#btnFetch")

const dataArr = Object.values(data);
const mappedData= dataArr.map(function (x) { 
return parseFloat(x);
});

// /* large line chart */
const chLine = document.getElementById("chLine");
const chartData = {
  labels: ["10yrs", "5yrs", "1yrs", "1m", "now"],
  datasets: [{
    data: mappedData,
    backgroundColor: COLORS[3],
    borderColor: COLORS[1],
    borderWidth: 4,
    pointBackgroundColor: COLORS[1]
  }]
};

if (chLine) {
  new Chart(chLine, {
  type: 'line',
  data: chartData,
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: false
        }
      }]
    },
    legend: {
      display: false
    }
  }
  });
}



