"use strict";document.addEventListener("DOMContentLoaded",function(){setTimeout(function(){new ApexCharts(document.querySelector("#seo-card2"),{chart:{type:"area",height:120,sparkline:{enabled:!0}},dataLabels:{enabled:!1},colors:["#4099ff"],fill:{type:"gradient",gradient:{shade:"dark",gradientToColors:["#4099ff"],shadeIntensity:1,type:"horizontal",opacityFrom:.9,opacityTo:.5,stops:[0,100,100,100]}},stroke:{curve:"smooth",width:2},series:[{data:[40,25,60,50,75,60]}],tooltip:{fixed:{enabled:!1},x:{show:!1},y:{title:{formatter:function(e){return"Ticket "}}},marker:{show:!1}}}).render()},500)});