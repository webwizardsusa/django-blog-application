"use strict";document.addEventListener("DOMContentLoaded",function(){setTimeout(function(){new ApexCharts(document.querySelector("#transactions-chart"),{chart:{type:"bar",height:60,sparkline:{enabled:!0}},colors:["#4099ff"],plotOptions:{bar:{borderRadius:2,columnWidth:"80%"}},series:[{data:[10,30,40,20,60,50,20,15,20,25,30,25]}],xaxis:{crosshairs:{width:1}},tooltip:{fixed:{enabled:!1},x:{show:!1},y:{title:{formatter:function(t){return""}}},marker:{show:!1}}}).render()},500)});