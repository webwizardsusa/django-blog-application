"use strict";document.addEventListener("DOMContentLoaded",function(){setTimeout(function(){new ApexCharts(document.querySelector("#amunt-card2"),{chart:{type:"area",height:90,sparkline:{enabled:!0}},dataLabels:{enabled:!1},colors:["#FFF"],fill:{type:"solid",opacity:1},stroke:{curve:"smooth",width:2},series:[{name:"series1",data:[80,40,60,45,65]}],yaxis:{min:0,max:80},tooltip:{theme:"dark",fixed:{enabled:!1},x:{show:!1},y:{title:{formatter:function(e){return"$"}}},marker:{show:!1}}}).render()},500)});