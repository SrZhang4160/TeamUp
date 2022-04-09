webpackHotUpdate("app",{

/***/ "./node_modules/cache-loader/dist/cjs.js?!./node_modules/babel-loader/lib/index.js!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/components/home.vue?vue&type=script&lang=js&":
false,

/***/ "./node_modules/cache-loader/dist/cjs.js?!./node_modules/babel-loader/lib/index.js!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/components/login.vue?vue&type=script&lang=js&":
false,

/***/ "./node_modules/cache-loader/dist/cjs.js?{\"cacheDirectory\":\"node_modules/.cache/vue-loader\",\"cacheIdentifier\":\"4088ea3a-vue-loader-template\"}!./node_modules/vue-loader/lib/loaders/templateLoader.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/components/home.vue?vue&type=template&id=957c9522&scoped=true&":
false,

/***/ "./node_modules/cache-loader/dist/cjs.js?{\"cacheDirectory\":\"node_modules/.cache/vue-loader\",\"cacheIdentifier\":\"4088ea3a-vue-loader-template\"}!./node_modules/vue-loader/lib/loaders/templateLoader.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/components/login.vue?vue&type=template&id=10d9df09&":
false,

/***/ "./node_modules/css-loader/dist/cjs.js?!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src/index.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/components/home.vue?vue&type=style&index=0&id=957c9522&scoped=true&lang=css&":
false,

/***/ "./node_modules/vue-style-loader/index.js?!./node_modules/css-loader/dist/cjs.js?!./node_modules/vue-loader/lib/loaders/stylePostLoader.js!./node_modules/postcss-loader/src/index.js?!./node_modules/cache-loader/dist/cjs.js?!./node_modules/vue-loader/lib/index.js?!./src/components/home.vue?vue&type=style&index=0&id=957c9522&scoped=true&lang=css&":
false,

/***/ "./src/components/home.vue":
false,

/***/ "./src/components/home.vue?vue&type=script&lang=js&":
false,

/***/ "./src/components/home.vue?vue&type=style&index=0&id=957c9522&scoped=true&lang=css&":
false,

/***/ "./src/components/home.vue?vue&type=template&id=957c9522&scoped=true&":
false,

/***/ "./src/components/login.vue":
false,

/***/ "./src/components/login.vue?vue&type=script&lang=js&":
false,

/***/ "./src/components/login.vue?vue&type=template&id=10d9df09&":
false,

/***/ "./src/router.js":
/*!***********************!*\
  !*** ./src/router.js ***!
  \***********************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var core_js_modules_es_object_to_string_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! core-js/modules/es.object.to-string.js */ \"./node_modules/core-js/modules/es.object.to-string.js\");\n/* harmony import */ var core_js_modules_es_object_to_string_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(core_js_modules_es_object_to_string_js__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var core_js_modules_es_string_iterator_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! core-js/modules/es.string.iterator.js */ \"./node_modules/core-js/modules/es.string.iterator.js\");\n/* harmony import */ var core_js_modules_es_string_iterator_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(core_js_modules_es_string_iterator_js__WEBPACK_IMPORTED_MODULE_1__);\n/* harmony import */ var core_js_modules_web_dom_collections_iterator_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! core-js/modules/web.dom-collections.iterator.js */ \"./node_modules/core-js/modules/web.dom-collections.iterator.js\");\n/* harmony import */ var core_js_modules_web_dom_collections_iterator_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(core_js_modules_web_dom_collections_iterator_js__WEBPACK_IMPORTED_MODULE_2__);\n/* harmony import */ var vue__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! vue */ \"./node_modules/vue/dist/vue.esm.js\");\n/* harmony import */ var vue_router__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! vue-router */ \"./node_modules/vue-router/dist/vue-router.esm-bundler.js\");\n\n\n\n\n\n\nvar Login = function Login() {\n  return __webpack_require__.e(/*! import() */ 0).then(__webpack_require__.bind(null, /*! ./components/Login.vue */ \"./src/components/Login.vue\"));\n};\n\nvar Home = function Home() {\n  return __webpack_require__.e(/*! import() */ 1).then(__webpack_require__.bind(null, /*! ./components/Home.vue */ \"./src/components/Home.vue\"));\n};\n\nvue__WEBPACK_IMPORTED_MODULE_3__[\"default\"].use(vue_router__WEBPACK_IMPORTED_MODULE_4__[\"default\"]);\nvar router = new vue_router__WEBPACK_IMPORTED_MODULE_4__[\"default\"]({\n  routes: [{\n    path: '/',\n    redirect: '/login'\n  }, {\n    path: '/login',\n    component: Login\n  }, {\n    path: '/home',\n    component: Home,\n    redirect: '/welcome'\n  }]\n}); // 挂载路由导航守卫\n\nrouter.beforeEach(function (to, from, next) {\n  // to 将要访问的路径\n  // from 代表从哪个路径跳转而来\n  // next 是一个函数，表示放行\n  //     next()  放行    next('/login')  强制跳转\n  if (to.path === '/login') return next(); // 获取token\n\n  var tokenStr = window.sessionStorage.getItem('token');\n  if (!tokenStr) return next('/login');\n  next();\n});\n/* harmony default export */ __webpack_exports__[\"default\"] = (router);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcm91dGVyLmpzLmpzIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vLy4vc3JjL3JvdXRlci5qcz80MWNiIl0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCBWdWUgZnJvbSAndnVlJztcbmltcG9ydCBSb3V0ZXIgZnJvbSAndnVlLXJvdXRlcic7XG5cclxuY29uc3QgTG9naW4gPSAoKSA9PiBpbXBvcnQoJy4vY29tcG9uZW50cy9Mb2dpbi52dWUnKVxyXG5jb25zdCBIb21lID0gICgpID0+IGltcG9ydCgnLi9jb21wb25lbnRzL0hvbWUudnVlJylcclxuXHJcblxuVnVlLnVzZShSb3V0ZXIpO1xuXHJcbmNvbnN0IHJvdXRlciA9IG5ldyBSb3V0ZXIoe1xuICByb3V0ZXM6IFtcbiAgICB7IHBhdGg6ICcvJywgcmVkaXJlY3Q6ICcvbG9naW4nIH0sXG4gICAgeyBwYXRoOiAnL2xvZ2luJywgY29tcG9uZW50OiBMb2dpbiB9LFxuICAgIHtcbiAgICAgIHBhdGg6ICcvaG9tZScsXG4gICAgICBjb21wb25lbnQ6IEhvbWUsXG4gICAgICByZWRpcmVjdDogJy93ZWxjb21lJ1xuICAgIH1cbiAgXVxufSlcblxuLy8g5oyC6L296Lev55Sx5a+86Iiq5a6I5Y2rXG5yb3V0ZXIuYmVmb3JlRWFjaCgodG8sIGZyb20sIG5leHQpID0+IHtcbiAgLy8gdG8g5bCG6KaB6K6/6Zeu55qE6Lev5b6EXG4gIC8vIGZyb20g5Luj6KGo5LuO5ZOq5Liq6Lev5b6E6Lez6L2s6ICM5p2lXG4gIC8vIG5leHQg5piv5LiA5Liq5Ye95pWw77yM6KGo56S65pS+6KGMXG4gIC8vICAgICBuZXh0KCkgIOaUvuihjCAgICBuZXh0KCcvbG9naW4nKSAg5by65Yi26Lez6L2sXG5cbiAgaWYgKHRvLnBhdGggPT09ICcvbG9naW4nKSByZXR1cm4gbmV4dCgpXG4gIC8vIOiOt+WPlnRva2VuXG4gIGNvbnN0IHRva2VuU3RyID0gd2luZG93LnNlc3Npb25TdG9yYWdlLmdldEl0ZW0oJ3Rva2VuJylcbiAgaWYgKCF0b2tlblN0cikgcmV0dXJuIG5leHQoJy9sb2dpbicpXG4gIG5leHQoKVxufSlcblxuZXhwb3J0IGRlZmF1bHQgcm91dGVyIl0sIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7QUFBQTtBQUNBO0FBQ0E7QUFDQTtBQUFBO0FBQUE7QUFDQTtBQUFBO0FBQUE7QUFBQTtBQUNBO0FBRUE7QUFFQTtBQUNBO0FBQ0E7QUFBQTtBQUFBO0FBQ0E7QUFBQTtBQUFBO0FBRUE7QUFDQTtBQUNBO0FBSEE7QUFKQTtBQUNBO0FBWUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUVBIiwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/router.js\n");

/***/ })

})