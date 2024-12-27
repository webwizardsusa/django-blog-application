var rtl_flag=!1,dark_flag=!1;function layout_change_default(){var e=window.matchMedia("(prefers-color-scheme: dark)");let t=e.matches?"dark":"light";layout_change(t);var a=document.querySelector('.theme-layout .btn[data-value="default"]');a&&a.classList.add("active"),e.addEventListener("change",e=>{layout_change(t=e.matches?"dark":"light")})}function dark_mode(){var e=document.getElementById("dark-mode");e&&layout_change(e.checked?"dark":"light")}function layout_sidebar_change(e){var t;"dark"==e?(document.getElementsByTagName("body")[0].setAttribute("data-pc-sidebar-theme","dark"),(t=document.querySelector(".theme-sidebar-color .btn.active"))&&t.classList.remove("active"),(e=document.querySelector(".theme-sidebar-color .btn[data-value='true']"))&&e.classList.add("active")):(document.getElementsByTagName("body")[0].setAttribute("data-pc-sidebar-theme","light"),(t=document.querySelector(".theme-sidebar-color .btn.active"))&&t.classList.remove("active"),(e=document.querySelector(".theme-sidebar-color .btn[data-value='false']"))&&e.classList.add("active"))}function header_change(e){var t;document.body.setAttribute("data-pc-header",e),document.querySelector(".pct-offcanvas")&&((t=document.querySelector(".header-color > a.active"))&&t.classList.remove("active"),t=document.querySelector(`.header-color > a[data-value='${e}']`))&&t.classList.add("active")}function layout_caption_change(e){document.body.setAttribute("data-pc-sidebar-caption",e);var t=document.querySelector(".theme-nav-caption .btn.active"),t=(t&&t.classList.remove("active"),document.querySelector(`.theme-nav-caption .btn[data-value='${e}']`));t&&t.classList.add("active")}function preset_change(e){var t=document.querySelector("body"),a=document.querySelector(".pct-offcanvas");t.setAttribute("data-pc-preset",e),a&&(t=document.querySelector(".preset-color > a.active"),a=document.querySelector(`.preset-color > a[data-value='${e}']`),t&&t.classList.remove("active"),a)&&a.classList.add("active")}function layout_rtl_change(e){var t=document.querySelector("body"),a=document.querySelector("html"),c=document.querySelector(".theme-direction .btn.active"),r=document.querySelector(".theme-direction .btn[data-value='true']"),o=document.querySelector(".theme-direction .btn[data-value='false']");"true"===e?(rtl_flag=!0,t.setAttribute("data-pc-direction","rtl"),a.setAttribute("dir","rtl"),a.setAttribute("lang","ar"),c&&c.classList.remove("active"),r&&r.classList.add("active")):(rtl_flag=!1,t.setAttribute("data-pc-direction","ltr"),a.removeAttribute("dir"),a.removeAttribute("lang"),c&&c.classList.remove("active"),o&&o.classList.add("active"))}function layout_change(e){document.body.setAttribute("data-pc-theme",e);var t=document.querySelector('.theme-layout .btn[data-value="default"]');t&&t.classList.remove("active"),"dark"===e?(dark_flag=!0,(t=document.querySelector(".auth-main.v1 .auth-sidefooter img"))&&t.setAttribute("src","../assets/images/logo-white.html"),(e=document.querySelector(".footer-top .footer-logo"))&&e.setAttribute("src","../assets/images/logo-white.html"),(t=document.querySelector(".theme-layout .btn.active"))&&t.classList.remove("active"),(e=document.querySelector(".theme-layout .btn[data-value='false']"))&&e.classList.add("active")):(dark_flag=!1,(t=document.querySelector(".auth-main.v1 .auth-sidefooter img"))&&t.setAttribute("src","../assets/images/logo-dark.html"),(e=document.querySelector(".footer-top .footer-logo"))&&e.setAttribute("src","../assets/images/logo-dark.html"),(t=document.querySelector(".theme-layout .btn.active"))&&t.classList.remove("active"),(e=document.querySelector(".theme-layout .btn[data-value='true']"))&&e.classList.add("active"))}function change_box_container(e){var t;document.querySelector(".pc-content")&&("true"==e?(document.querySelector(".pc-content").classList.add("container"),document.querySelector(".footer-wrapper").classList.add("container"),document.querySelector(".footer-wrapper").classList.remove("container-fluid"),(t=document.querySelector(".theme-container .btn.active"))&&(t.classList.remove("active"),document.querySelector(".theme-container .btn[data-value='true']").classList.add("active"))):(document.querySelector(".pc-content").classList.remove("container"),document.querySelector(".footer-wrapper").classList.remove("container"),document.querySelector(".footer-wrapper").classList.add("container-fluid"),(t=document.querySelector(".theme-container .btn.active"))&&(t.classList.remove("active"),document.querySelector(".theme-container .btn[data-value='false']").classList.add("active"))))}document.addEventListener("DOMContentLoaded",function(){var e=document.querySelectorAll(".preset-color > a");if(e.length&&e.forEach(e=>{e.addEventListener("click",function(e){let t=e.target;"SPAN"===t.tagName?t=t.parentNode:"IMG"===t.tagName&&(t=t.closest("a")),preset_change(t.getAttribute("data-value"))})}),0<document.querySelectorAll(".header-color").length)for(var t=document.querySelectorAll(".header-color > a"),a=0;a<t.length;a++)t[a].addEventListener("click",function(e){e=e.target;header_change((e="SPAN"==e.tagName?e.parentNode:e).getAttribute("data-value"))});e=document.querySelector(".pct-body"),e&&new SimpleBar(e),e=document.querySelector("#layoutreset");e&&e.addEventListener("click",()=>location.reload());const c=document.querySelector("#layoutmodertl");c&&c.addEventListener("click",()=>{layout_rtl_change(c.checked?"true":"false")})});