!function(o){var n={};function i(e){var t;return(n[e]||(t=n[e]={i:e,l:!1,exports:{}},o[e].call(t.exports,t,t.exports,i),t.l=!0,t)).exports}i.m=o,i.c=n,i.d=function(e,t,o){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:o})},i.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var o=Object.create(null);if(i.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)i.d(o,n,function(e){return t[e]}.bind(null,n));return o},i.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="",i(i.s=11)}([,,function(e,t,o){"use strict";e.exports=function(e){"complete"===document.readyState||"interactive"===document.readyState?e.call():document.attachEvent?document.attachEvent("onreadystatechange",function(){"interactive"===document.readyState&&e.call()}):document.addEventListener&&document.addEventListener("DOMContentLoaded",e)}},,function(t,e,o){"use strict";!function(e){e="undefined"!=typeof window?window:void 0!==e?e:"undefined"!=typeof self?self:{};t.exports=e}.call(this,o(5))},function(e,t,o){"use strict";var n="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},i=function(){return this}();try{i=i||Function("return this")()||(0,eval)("this")}catch(e){"object"===("undefined"==typeof window?"undefined":n(window))&&(i=window)}e.exports=i},,,,,,function(e,t,o){e.exports=o(12)},function(e,t,o){"use strict";var n="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},i=l(o(2)),a=o(4),r=l(o(13));function l(e){return e&&e.__esModule?e:{default:e}}var s,c=a.window.jarallax;a.window.jarallax=r.default,a.window.jarallax.noConflict=function(){return a.window.jarallax=c,this},void 0!==a.jQuery&&((o=function(){var e=arguments||[],e=(Array.prototype.unshift.call(e,this),r.default.apply(a.window,e));return"object"!==(void 0===e?"undefined":n(e))?e:this}).constructor=r.default.constructor,s=a.jQuery.fn.jarallax,a.jQuery.fn.jarallax=o,a.jQuery.fn.jarallax.noConflict=function(){return a.jQuery.fn.jarallax=s,this}),(0,i.default)(function(){(0,r.default)(document.querySelectorAll("[data-jarallax]"))})},function(e,$,P){"use strict";!function(e){Object.defineProperty($,"__esModule",{value:!0});var t=function(e,t,o){return t&&a(e.prototype,t),o&&a(e,o),e},s="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},o=r(P(2)),n=r(P(14)),i=P(4);function a(e,t){for(var o=0;o<t.length;o++){var n=t[o];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}function r(e){return e&&e.__esModule?e:{default:e}}var l=-1<navigator.userAgent.indexOf("MSIE ")||-1<navigator.userAgent.indexOf("Trident/index.html")||-1<navigator.userAgent.indexOf("Edge/index.html"),c=function(){for(var e="transform WebkitTransform MozTransform".split(" "),t=document.createElement("div"),o=0;o<e.length;o++)if(t&&void 0!==t.style[e[o]])return e[o];return!1}(),m=void 0,f=void 0,u=void 0,d=!1,p=!1;function y(e){m=i.window.innerWidth||document.documentElement.clientWidth,f=i.window.innerHeight||document.documentElement.clientHeight,"object"!==(void 0===e?"undefined":s(e))||"load"!==e.type&&"dom-loaded"!==e.type||(d=!0)}y(),i.window.addEventListener("resize",y),i.window.addEventListener("orientationchange",y),i.window.addEventListener("load",y),(0,o.default)(function(){y({type:"dom-loaded"})});var g=[],b=!1;function h(){var t,o;g.length&&(u=void 0!==i.window.pageYOffset?i.window.pageYOffset:(document.documentElement||document.body.parentNode||document.body).scrollTop,t=d||!b||b.width!==m||b.height!==f,o=p||t||!b||b.y!==u,p=d=!1,(t||o)&&(g.forEach(function(e){t&&e.onResize(),o&&e.onScroll()}),b={width:m,height:f,y:u}),(0,n.default)(h))}function v(e){("object"===("undefined"==typeof HTMLElement?"undefined":s(HTMLElement))?e instanceof HTMLElement:e&&"object"===(void 0===e?"undefined":s(e))&&null!==e&&1===e.nodeType&&"string"==typeof e.nodeName)&&(e=[e]);for(var t=arguments[1],o=Array.prototype.slice.call(arguments,2),n=e.length,i=0,a=void 0;i<n;i++)if("object"===(void 0===t?"undefined":s(t))||void 0===t?e[i].jarallax||(e[i].jarallax=new S(e[i],t)):e[i].jarallax&&(a=e[i].jarallax[t].apply(e[i].jarallax,o)),void 0!==a)return a;return e}var x=!!e.ResizeObserver&&new e.ResizeObserver(function(e){e&&e.length&&(0,n.default)(function(){e.forEach(function(e){e.target&&e.target.jarallax&&(d||e.target.jarallax.onResize(),p=!0)})})}),w=0,S=(t(j,[{key:"css",value:function(t,o){return"string"==typeof o?i.window.getComputedStyle(t).getPropertyValue(o):(o.transform&&c&&(o[c]=o.transform),Object.keys(o).forEach(function(e){t.style[e]=o[e]}),t)}},{key:"extend",value:function(o){var n=arguments;return o=o||{},Object.keys(arguments).forEach(function(t){n[t]&&Object.keys(n[t]).forEach(function(e){o[e]=n[t][e]})}),o}},{key:"getWindowData",value:function(){return{width:m,height:f,y:u}}},{key:"initImg",value:function(){var e=this,t=e.options.imgElement;return(t=(t=t&&"string"==typeof t?e.$item.querySelector(t):t)instanceof Element?t:null)&&(e.options.keepImg?e.image.$item=t.cloneNode(!0):(e.image.$item=t,e.image.$itemParent=t.parentNode),e.image.useImgTag=!0),!(!e.image.$item&&(null===e.image.src&&(e.image.src=e.css(e.$item,"background-image").replace(/^url\(['"]?/g,"").replace(/['"]?\)$/g,"")),!e.image.src||"none"===e.image.src))}},{key:"canInitParallax",value:function(){return c&&!this.options.disableParallax()}},{key:"init",value:function(){var e,t=this,o={position:"absolute",top:0,left:0,width:"100%",height:"100%",overflow:"hidden",pointerEvents:"none"},n={};if(t.options.keepImg||((e=t.$item.getAttribute("style"))&&t.$item.setAttribute("data-jarallax-original-styles",e),t.image.useImgTag&&(e=t.image.$item.getAttribute("style"))&&t.image.$item.setAttribute("data-jarallax-original-styles",e)),"static"===t.css(t.$item,"position")&&t.css(t.$item,{position:"relative"}),"auto"===t.css(t.$item,"z-index")&&t.css(t.$item,{zIndex:0}),t.image.$container=document.createElement("div"),t.css(t.image.$container,o),t.css(t.image.$container,{"z-index":t.options.zIndex}),l&&t.css(t.image.$container,{opacity:.9999}),t.image.$container.setAttribute("id","jarallax-container-"+t.instanceID),t.$item.appendChild(t.image.$container),t.image.useImgTag?n=t.extend({"object-fit":t.options.imgSize,"object-position":t.options.imgPosition,"font-family":"object-fit: "+t.options.imgSize+"; object-position: "+t.options.imgPosition+";","max-width":"none"},o,n):(t.image.$item=document.createElement("div"),t.image.src&&(n=t.extend({"background-position":t.options.imgPosition,"background-size":t.options.imgSize,"background-repeat":t.options.imgRepeat,"background-image":'url("'+t.image.src+'")'},o,n))),"opacity"!==t.options.type&&"scale"!==t.options.type&&"scale-opacity"!==t.options.type&&1!==t.options.speed||(t.image.position="absolute"),"fixed"===t.image.position)for(var i=0,a=t.$item;null!==a&&a!==document&&0===i;){var r=t.css(a,"-webkit-transform")||t.css(a,"-moz-transform")||t.css(a,"transform");r&&"none"!==r&&(i=1,t.image.position="absolute"),a=a.parentNode}n.position=t.image.position,t.css(t.image.$item,n),t.image.$container.appendChild(t.image.$item),t.onResize(),t.onScroll(!0),t.options.automaticResize&&x&&x.observe(t.$item),t.options.onInit&&t.options.onInit.call(t),"none"!==t.css(t.$item,"background-image")&&t.css(t.$item,{"background-image":"none"}),t.addToParallaxList()}},{key:"addToParallaxList",value:function(){g.push(this),1===g.length&&h()}},{key:"removeFromParallaxList",value:function(){var o=this;g.forEach(function(e,t){e.instanceID===o.instanceID&&g.splice(t,1)})}},{key:"destroy",value:function(){var e,t=this,o=(t.removeFromParallaxList(),t.$item.getAttribute("data-jarallax-original-styles"));t.$item.removeAttribute("data-jarallax-original-styles"),o?t.$item.setAttribute("style",o):t.$item.removeAttribute("style"),t.image.useImgTag&&(e=t.image.$item.getAttribute("data-jarallax-original-styles"),t.image.$item.removeAttribute("data-jarallax-original-styles"),e?t.image.$item.setAttribute("style",o):t.image.$item.removeAttribute("style"),t.image.$itemParent)&&t.image.$itemParent.appendChild(t.image.$item),t.$clipStyles&&t.$clipStyles.parentNode.removeChild(t.$clipStyles),t.image.$container&&t.image.$container.parentNode.removeChild(t.image.$container),t.options.onDestroy&&t.options.onDestroy.call(t),delete t.$item.jarallax}},{key:"clipContainer",value:function(){var e,t,o;"fixed"===this.image.position&&(o=(t=(e=this).image.$container.getBoundingClientRect()).width,t=t.height,e.$clipStyles||(e.$clipStyles=document.createElement("style"),e.$clipStyles.setAttribute("type","text/css"),e.$clipStyles.setAttribute("id","jarallax-clip-"+e.instanceID),(document.head||document.getElementsByTagName("head")[0]).appendChild(e.$clipStyles)),o="#jarallax-container-"+e.instanceID+" {\n           clip: rect(0 "+o+"px "+t+"px 0);\n           clip: rect(0, "+o+"px, "+t+"px, 0);\n        }",e.$clipStyles.styleSheet?e.$clipStyles.styleSheet.cssText=o:e.$clipStyles.innerHTML=o)}},{key:"coverImage",value:function(){var e=this,t=e.image.$container.getBoundingClientRect(),o=t.height,n=e.options.speed,i="scroll"===e.options.type||"scroll-opacity"===e.options.type,a=0,r=o;return i&&(n<0?(a=n*Math.max(o,f),f<o&&(a-=n*(o-f))):a=n*(o+f),1<n?r=Math.abs(a-f):n<0?r=a/n+Math.abs(a):r+=(f-o)*(1-n),a/=2),e.parallaxScrollDistance=a,n=i?(f-r)/2:(o-r)/2,e.css(e.image.$item,{height:r+"px",marginTop:n+"px",left:"fixed"===e.image.position?t.left+"px":"0",width:t.width+"px"}),e.options.onCoverImage&&e.options.onCoverImage.call(e),{image:{height:r,marginTop:n},container:t}}},{key:"isVisible",value:function(){return this.isElementInViewport||!1}},{key:"onScroll",value:function(e){var t,o,n,i,a,r,l=this,s=l.$item.getBoundingClientRect(),c=s.top,u=s.height,d={},p=s;l.options.elementInViewport&&(p=l.options.elementInViewport.getBoundingClientRect()),l.isElementInViewport=0<=p.bottom&&0<=p.right&&p.top<=f&&p.left<=m,(e||l.isElementInViewport)&&(p=Math.max(0,c),e=Math.max(0,u+c),t=Math.max(0,-c),o=Math.max(0,c+u-f),n=Math.max(0,u-(c+u-f)),i=Math.max(0,-c+f-u),a=1-2*(f-c)/(f+u),r=1,u<f?r=1-(t||o)/u:e<=f?r=e/f:n<=f&&(r=n/f),"opacity"!==l.options.type&&"scale-opacity"!==l.options.type&&"scroll-opacity"!==l.options.type||(d.transform="translate3d(0,0,0)",d.opacity=r),"scale"!==l.options.type&&"scale-opacity"!==l.options.type||(u=1,l.options.speed<0?u-=l.options.speed*r:u+=l.options.speed*(1-r),d.transform="scale("+u+") translate3d(0,0,0)"),"scroll"!==l.options.type&&"scroll-opacity"!==l.options.type||(u=l.parallaxScrollDistance*a,"absolute"===l.image.position&&(u-=c),d.transform="translate3d(0,"+u+"px,0)"),l.css(l.image.$item,d),l.options.onScroll)&&l.options.onScroll.call(l,{section:s,beforeTop:p,beforeTopEnd:e,afterTop:t,beforeBottom:o,beforeBottomEnd:n,afterBottom:i,visiblePercent:r,fromViewportCenter:a})}},{key:"onResize",value:function(){this.coverImage(),this.clipContainer()}}]),j);function j(e,t){if(!(this instanceof j))throw new TypeError("Cannot call a class as a function");var o,n,i=this,e=(i.instanceID=w++,i.$item=e,i.defaults={type:"scroll",speed:.5,imgSrc:null,imgElement:".jarallax-img",imgSize:"cover",imgPosition:"50% 50%",imgRepeat:"no-repeat",keepImg:!1,elementInViewport:null,zIndex:-100,disableParallax:!1,disableVideo:!1,automaticResize:!0,videoSrc:null,videoStartTime:0,videoEndTime:0,videoVolume:0,videoLoop:!0,videoPlayOnlyVisible:!0,onScroll:null,onInit:null,onDestroy:null,onCoverImage:null},i.$item.getAttribute("data-jarallax")),a=JSON.parse(e||"{}"),r=(e&&console.warn("Detected usage of deprecated data-jarallax JSON options, you should use pure data-attribute options. See info here - https://github.com/nk-o/jarallax/issues/53"),i.$item.dataset||{}),l={},e=(Object.keys(r).forEach(function(e){var t=e.substr(0,1).toLowerCase()+e.substr(1);t&&void 0!==i.defaults[t]&&(l[t]=r[e])}),i.options=i.extend({},i.defaults,a,l,t),i.pureOptions=i.extend({},i.options),Object.keys(i.options).forEach(function(e){"true"===i.options[e]?i.options[e]=!0:"false"===i.options[e]&&(i.options[e]=!1)}),i.options.speed=Math.min(2,Math.max(-1,parseFloat(i.options.speed))),(i.options.noAndroid||i.options.noIos)&&(console.warn("Detected usage of deprecated noAndroid or noIos options, you should use disableParallax option. See info here - https://github.com/nk-o/jarallax/#disable-on-mobile-devices"),i.options.disableParallax||(i.options.noIos&&i.options.noAndroid?i.options.disableParallax=/iPad|iPhone|iPod|Android/:i.options.noIos?i.options.disableParallax=/iPad|iPhone|iPod/:i.options.noAndroid&&(i.options.disableParallax=/Android/))),"string"==typeof i.options.disableParallax&&(i.options.disableParallax=new RegExp(i.options.disableParallax)),i.options.disableParallax instanceof RegExp&&(o=i.options.disableParallax,i.options.disableParallax=function(){return o.test(navigator.userAgent)}),"function"!=typeof i.options.disableParallax&&(i.options.disableParallax=function(){return!1}),"string"==typeof i.options.disableVideo&&(i.options.disableVideo=new RegExp(i.options.disableVideo)),i.options.disableVideo instanceof RegExp&&(n=i.options.disableVideo,i.options.disableVideo=function(){return n.test(navigator.userAgent)}),"function"!=typeof i.options.disableVideo&&(i.options.disableVideo=function(){return!1}),i.options.elementInViewport);(e=e&&"object"===(void 0===e?"undefined":s(e))&&void 0!==e.length?function(e,t){if(Array.isArray(e))return e;if(Symbol.iterator in Object(e)){var o=e,n=t,i=[],a=!0,e=!1,t=void 0;try{for(var r,l=o[Symbol.iterator]();!(a=(r=l.next()).done)&&(i.push(r.value),!n||i.length!==n);a=!0);}catch(o){e=!0,t=o}finally{try{!a&&l.return&&l.return()}finally{if(e)throw t}}return i}throw new TypeError("Invalid attempt to destructure non-iterable instance")}(e,1)[0]:e)instanceof Element||(e=null),i.options.elementInViewport=e,i.image={src:i.options.imgSrc||null,$container:null,useImgTag:!1,position:/iPad|iPhone|iPod|Android/.test(navigator.userAgent)?"absolute":"fixed"},i.initImg()&&i.canInitParallax()&&i.init()}v.constructor=S,$.default=v}.call(this,P(5))},function(e,t,o){"use strict";var o=o(4),n=o.requestAnimationFrame||o.webkitRequestAnimationFrame||o.mozRequestAnimationFrame||function(e){var t=+new Date,o=Math.max(0,16-(t-i)),e=setTimeout(e,o);return i=t,e},i=+new Date,a=o.cancelAnimationFrame||o.webkitCancelAnimationFrame||o.mozCancelAnimationFrame||clearTimeout;Function.prototype.bind&&(n=n.bind(o),a=a.bind(o)),(e.exports=n).cancel=a}]),!function(o){var n={};function i(e){var t;return(n[e]||(t=n[e]={i:e,l:!1,exports:{}},o[e].call(t.exports,t,t.exports,i),t.l=!0,t)).exports}i.m=o,i.c=n,i.d=function(e,t,o){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:o})},i.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"==typeof t&&t&&t.__esModule)return t;var o=Object.create(null);if(i.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var n in t)i.d(o,n,function(e){return t[e]}.bind(null,n));return o},i.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="",i(i.s=0)}([function(e,t,o){e.exports=o(1)},function(e,t,o){"use strict";var n=i(o(2));function i(e){return e&&e.__esModule?e:{default:e}}(0,i(o(3)).default)(),(0,n.default)(function(){"undefined"!=typeof jarallax&&jarallax(document.querySelectorAll("[data-jarallax-element]"))})},function(e,t,o){"use strict";e.exports=function(e){"complete"===document.readyState||"interactive"===document.readyState?e.call():document.attachEvent?document.attachEvent("onreadystatechange",function(){"interactive"===document.readyState&&e.call()}):document.addEventListener&&document.addEventListener("DOMContentLoaded",e)}},function(e,t,o){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=function(){var e,t=0<arguments.length&&void 0!==arguments[0]?arguments[0]:n.default.jarallax;void 0!==t&&(e=t.constructor,["initImg","canInitParallax","init","destroy","clipContainer","coverImage","isVisible","onScroll","onResize"].forEach(function(r){var l=e.prototype[r];e.prototype[r]=function(){var e=this,t=arguments||[];if("initImg"===r&&null!==e.$item.getAttribute("data-jarallax-element")&&(e.options.type="element",e.pureOptions.speed=e.$item.getAttribute("data-jarallax-element")||e.pureOptions.speed),"element"===e.options.type)switch(e.pureOptions.threshold=e.$item.getAttribute("data-threshold")||"",r){case"init":var o=e.pureOptions.speed.split(" "),o=(e.options.speed=e.pureOptions.speed||0,e.options.speedY=o[0]?parseFloat(o[0]):0,e.options.speedX=o[1]?parseFloat(o[1]):0,e.pureOptions.threshold.split(" "));e.options.thresholdY=o[0]?parseFloat(o[0]):null,e.options.thresholdX=o[1]?parseFloat(o[1]):null;break;case"onResize":var o=e.css(e.$item,"transform"),n=(e.css(e.$item,{transform:""}),e.$item.getBoundingClientRect());e.itemData={width:n.width,height:n.height,y:n.top+e.getWindowData().y,x:n.left},e.css(e.$item,{transform:o});break;case"onScroll":var n=e.getWindowData(),o=(n.y+n.height/2-e.itemData.y-e.itemData.height/2)/(n.height/2),n=o*e.options.speedY,o=o*e.options.speedX,i=n,a=o;null!==e.options.thresholdY&&n>e.options.thresholdY&&(i=0),null!==e.options.thresholdX&&o>e.options.thresholdX&&(a=0),e.css(e.$item,{transform:"translate3d("+a+"px,"+i+"px,0)"});break;case"initImg":case"isVisible":case"clipContainer":case"coverImage":return!0}return l.apply(e,t)}}))};var t=o(4),n=t&&t.__esModule?t:{default:t}},function(t,e,o){"use strict";!function(e){e="undefined"!=typeof window?window:void 0!==e?e:"undefined"!=typeof self?self:{};t.exports=e}.call(this,o(5))},function(e,t,o){"use strict";var n="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},i=function(){return this}();try{i=i||Function("return this")()||(0,eval)("this")}catch(e){"object"===("undefined"==typeof window?"undefined":n(window))&&(i=window)}e.exports=i}]);