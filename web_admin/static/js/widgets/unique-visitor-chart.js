"use strict";document.addEventListener("DOMContentLoaded",function(){setTimeout(function(){new ApexCharts(document.querySelector("#unique-visitor-chart"),{chart:{type:"bar",height:220,zoom:{enabled:!1},toolbar:{show:!1}},dataLabels:{enabled:!1},colors:["#fff"],plotOptions:{bar:{color:"#fff",columnWidth:"80%"}},fill:{type:"gradient",gradient:{shade:"light",type:"vertical",shadeIntensity:.25,gradientToColors:["#fff"],inverseColors:!0,opacityFrom:.99,opacityTo:.65,stops:[0,100]}},series:[{data:[25,66,41,89,63,25,44,12,36,9,54,25,66,41,89,63,54,25,66,41,89,63,25,44,12,36,9,54,25,66,41,89,63,25,44,12,36,9,25,44,12,36,9,54]}],xaxis:{labels:{show:!1},axisBorder:{show:!1},axisTicks:{show:!1}},yaxis:{labels:{style:{colors:"#fff"}}},grid:{borderColor:"#ffffff3b"},tooltip:{fixed:{enabled:!1},x:{show:!1},y:{title:{formatter:function(e){return"Click "}}},marker:{show:!1}}}).render()},500)});