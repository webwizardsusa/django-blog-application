"use strict";document.addEventListener("DOMContentLoaded",function(){setTimeout(function(){new ApexCharts(document.querySelector("#customer-rate-graph"),{chart:{type:"area",height:230,toolbar:{show:!1}},colors:["#0d6efd"],fill:{type:"gradient",gradient:{shadeIntensity:1,type:"vertical",inverseColors:!1,opacityFrom:.5,opacityTo:0}},dataLabels:{enabled:!1},stroke:{width:1},plotOptions:{bar:{columnWidth:"45%",borderRadius:4}},grid:{strokeDashArray:4},series:[{data:[30,60,40,70,50,90,50,55,45,60,50,65]}],xaxis:{categories:["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],labels:{hideOverlappingLabels:!0},axisBorder:{show:!1},axisTicks:{show:!1}}}).render()},500)});