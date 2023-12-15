// public/assets/js/your-custom-page.js

function initializeChart(chartData) {
    var myChart = echarts.init(document.getElementById('myChart'));

    var option = {
        xAxis: {
            type: 'category',
            data: chartData.categories
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: chartData.values,
            type: 'bar'
        }]
    };

    myChart.setOption(option);
}
