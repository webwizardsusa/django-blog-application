"use strict";document.addEventListener("DOMContentLoaded",function(){setTimeout(function(){new ApexCharts(document.querySelector("#support-chart"),{chart:{type:"area",height:95,sparkline:{enabled:!0}},dataLabels:{enabled:!1},colors:["#4099ff"],stroke:{curve:"smooth",width:2},series:[{data:[0,20,10,45,30,55,20,30,0]}],tooltip:{fixed:{enabled:!1},x:{show:!1},y:{title:{formatter:function(e){return"Ticket "}}},marker:{show:!1}}}).render()},500)});