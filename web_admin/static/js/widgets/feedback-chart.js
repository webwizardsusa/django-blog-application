"use strict";document.addEventListener("DOMContentLoaded",function(){setTimeout(function(){new ApexCharts(document.querySelector("#feedback-chart"),{chart:{height:135,type:"donut"},dataLabels:{enabled:!1},colors:["#2ed8b6","#ff5370"],series:[83,17],labels:["Positive","Negative"],grid:{padding:{top:20,right:0,bottom:-10,left:0}},legend:{show:!1}}).render()},500)});