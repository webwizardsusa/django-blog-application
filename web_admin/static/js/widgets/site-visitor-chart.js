"use strict";document.addEventListener("DOMContentLoaded",function(){setTimeout(function(){var t=0,n=[];for(var e=new Date("11 Feb 2017 GMT").getTime(),a=10,i={min:10,max:90},o=0;o<a;){var r=e,s=Math.floor(Math.random()*(i.max-i.min+1))+i.min;n.push({x:r,y:s}),t=e,e+=864e5,o++}var d={chart:{height:300,type:"area",animations:{enabled:!0,easing:"linear",dynamicAnimation:{speed:2e3}},toolbar:{show:!1},zoom:{enabled:!1}},dataLabels:{enabled:!1},stroke:{curve:"smooth"},series:[{name:"active Users :",data:n}],colors:["#FF5370"],fill:{type:"gradient",gradient:{shadeIntensity:1,type:"horizontal",opacityFrom:.8,opacityTo:0,stops:[0,100]}},markers:{size:0},xaxis:{type:"datetime",range:7776e5},yaxis:{max:100},legend:{show:!1}},m=new ApexCharts(document.querySelector("#site-visitor-chart"),d);m.render();window.setInterval(function(){var e,a;e=t,a={min:10,max:90},t=e+=864e5,n.push({x:e,y:Math.floor(Math.random()*(a.max-a.min+1))+a.min}),m.updateSeries([{data:n}])},2e3),window.setInterval(function(){n=n.slice(n.length-10,n.length),m.updateSeries([{data:n}],!1,!0)},6e4)},500)});