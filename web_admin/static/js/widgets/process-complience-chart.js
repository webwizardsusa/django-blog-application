"use strict";document.addEventListener("DOMContentLoaded",function(){setTimeout(function(){new ApexCharts(document.querySelector("#process-complience-chart"),{chart:{height:200,type:"bar",sparkline:{enabled:!0}},colors:["#4099ff","#2ed8b6","#ff5370"],plotOptions:{bar:{columnWidth:"55%",distributed:!0}},dataLabels:{enabled:!1},stroke:{width:0},series:[{name:"Requests",data:[66.6,29.7,32.8]}],xaxis:{categories:["Desktop","Tablet","Mobile"]},fill:{type:"gradient",gradient:{shade:"light",type:"vertical",shadeIntensity:.25,gradientToColors:["#4099ff","#2ed8b6","#ff5370"],inverseColors:!0,opacityFrom:.99,opacityTo:.65,stops:[0,100]}}}).render()},500)});