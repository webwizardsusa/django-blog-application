"use strict";!function(){document.getElementsByTagName("body")[0].setAttribute("data-pc-layout","compact"),document.querySelector(".navbar-content")&&new SimpleBar(document.querySelector(".navbar-content"));for(var e=document.querySelectorAll(".pc-navbar li .pc-submenu"),t=0;t<e.length;t++)e[t].style.display="none";for(var c=document.querySelector("#sidebar-hide"),r=(c&&c.addEventListener("click",function(){document.querySelector("body").classList.contains("pc-sidebar-hide")?document.querySelector("body").classList.remove("pc-sidebar-hide"):document.querySelector("body").classList.add("pc-sidebar-hide")}),document.querySelectorAll(".pc-navbar > li:not(.pc-caption)")),o=0;o<r.length;o++)new bootstrap.Tooltip(r[o],{trigger:"hover",placement:"right",title:r[o].children[0].children[1].innerHTML}),r[o].addEventListener("click",function(e){e.stopPropagation();e=e.target;if((e="I"==(e="SPAN"==e.tagName?e.parentNode:e).tagName?e.parentNode.parentNode:e).parentNode.classList.contains("pc-hasmenu"))if(e.parentNode.classList.contains("pc-trigger"))e.parentNode.classList.remove("pc-trigger"),document.querySelector(".pc-compact-submenu > .pc-compact-list .simplebar-content")&&(document.querySelector(".pc-compact-submenu > .pc-compact-list .simplebar-content").innerHTML=""),document.querySelector(".pc-sidebar").classList.remove("pc-compact-submenu-active"),document.querySelector("body").classList.remove("pc-compact-submenu-active");else{document.querySelector(".pc-compact-submenu > .pc-compact-title h5").innerHTML=e.children[1].innerHTML,document.querySelector(".pc-compact-submenu > .pc-compact-title .avtar").innerHTML=e.children[0].children[0].outerHTML,document.querySelector(".pc-sidebar").classList.add("pc-compact-submenu-active"),document.querySelector("body").classList.add("pc-compact-submenu-active");for(var t=e.parentNode.children[1].outerHTML,c=(document.querySelector(".pc-compact-submenu > .pc-compact-list")&&new SimpleBar(document.querySelector(".pc-compact-submenu > .pc-compact-list")),document.querySelector(".pc-compact-submenu > .pc-compact-list .simplebar-content").innerHTML=t,document.querySelectorAll("li.pc-trigger")),r=0;r<c.length;r++)c[r].classList.remove("pc-trigger");e.parentNode.classList.add("pc-trigger");for(var o=document.querySelectorAll(".pc-compact-list .simplebar-content>ul > li:not(.pc-caption)"),n=0;n<o.length;n++)o[n].addEventListener("click",function(e){e.stopPropagation();e=e.target;if((e="SPAN"==e.tagName?e.parentNode:e).parentNode.classList.contains("pc-trigger"))e.parentNode.classList.remove("pc-trigger"),slideUp(e.parentNode.children[1],200);else{for(var t=document.querySelectorAll(".pc-compact-list .simplebar-content>ul li.pc-trigger"),c=0;c<t.length;c++){var r=t[c];r.classList.remove("pc-trigger"),slideUp(r.children[1],200)}e.parentNode.classList.add("pc-trigger");e=e.parentNode.children[1];e&&slideDown(e,200)}});for(var a=document.querySelectorAll(".pc-compact-list .simplebar-content>ul > li:not(.pc-caption) li"),n=0;n<a.length;n++)a[n].addEventListener("click",function(e){var t=e.target;if("SPAN"==t.tagName&&(t=t.parentNode),e.stopPropagation(),t.parentNode.classList.contains("pc-trigger"))t.parentNode.classList.remove("pc-trigger"),slideUp(t.parentNode.children[1],200);else{for(var c=t.parentNode.parentNode.children,r=0;r<c.length;r++){var o=c[r];o.classList.remove("pc-trigger"),(o="LI"==o.tagName?o.children[0]:o).parentNode.classList.contains("pc-hasmenu")&&slideUp(o.parentNode.children[1],200)}t.parentNode.classList.add("pc-trigger");e=t.parentNode.children[1];e&&(e.removeAttribute("style"),slideDown(e,200))}})}else document.querySelector(".pc-sidebar").classList.remove("pc-compact-submenu-active"),document.querySelector("body").classList.remove("pc-compact-submenu-active")})}();