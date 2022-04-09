webpackHotUpdate("app",{

/***/ "./src/router.js":
/*!***********************!*\
  !*** ./src/router.js ***!
  \***********************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var core_js_modules_es_object_to_string_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! core-js/modules/es.object.to-string.js */ \"./node_modules/core-js/modules/es.object.to-string.js\");\n/* harmony import */ var core_js_modules_es_object_to_string_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(core_js_modules_es_object_to_string_js__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var vue__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! vue */ \"./node_modules/vue/dist/vue.esm.js\");\n/* harmony import */ var vue_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! vue-router */ \"./node_modules/vue-router/dist/vue-router.esm-bundler.js\");\n/* harmony import */ var _components_login__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @/components/login */ \"./src/components/login/index.vue\");\n/* harmony import */ var _components_home__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @/components/home */ \"./src/components/home/index.vue\");\n\n\n\n\n\nvue__WEBPACK_IMPORTED_MODULE_1__[\"default\"].use(vue_router__WEBPACK_IMPORTED_MODULE_2__[\"default\"]);\nvar router = new vue_router__WEBPACK_IMPORTED_MODULE_2__[\"default\"]({\n  routes: [{\n    path: '/',\n    redirect: '/login'\n  }, {\n    path: '/login',\n    name: 'login',\n    component: _components_login__WEBPACK_IMPORTED_MODULE_3__[\"default\"]\n  }, {\n    path: '/home',\n    name: 'home',\n    component: _components_home__WEBPACK_IMPORTED_MODULE_4__[\"default\"]\n  }]\n}); // 导航守卫\n// 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆\n\nrouter.beforeEach(function (to, from, next) {\n  if (to.path === '/login') {\n    next();\n  } else {\n    var token = localStorage.getItem('Authorization');\n\n    if (token === null || token === '') {\n      next('/login');\n    } else {\n      next();\n    }\n  }\n});\n/* harmony default export */ __webpack_exports__[\"default\"] = (router); // 添加请求拦截器，在请求头中加token\n\naxios.interceptors.request.use(function (config) {\n  if (localStorage.getItem('Authorization')) {\n    config.headers.Authorization = localStorage.getItem('Authorization');\n  }\n\n  return config;\n}, function (error) {\n  return Promise.reject(error);\n});//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcm91dGVyLmpzLmpzIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vLy4vc3JjL3JvdXRlci5qcz80MWNiIl0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCBWdWUgZnJvbSAndnVlJztcbmltcG9ydCBSb3V0ZXIgZnJvbSAndnVlLXJvdXRlcic7XG5pbXBvcnQgbG9naW4gZnJvbSAnQC9jb21wb25lbnRzL2xvZ2luJztcbmltcG9ydCBob21lIGZyb20gJ0AvY29tcG9uZW50cy9ob21lJztcbiBcblZ1ZS51c2UoUm91dGVyKTtcblxuY29uc3Qgcm91dGVyID0gbmV3IFJvdXRlcih7XG4gIHJvdXRlczogW1xuICAgIHtcbiAgICAgIHBhdGg6ICcvJyxcbiAgICAgIHJlZGlyZWN0OiAnL2xvZ2luJ1xuICAgIH0sXG4gICAge1xuICAgICAgcGF0aDogJy9sb2dpbicsXG4gICAgICBuYW1lOiAnbG9naW4nLFxuICAgICAgY29tcG9uZW50OiBsb2dpblxuICAgIH0sXG4gICAge1xuICAgICAgcGF0aDogJy9ob21lJyxcbiAgICAgIG5hbWU6ICdob21lJyxcbiAgICAgIGNvbXBvbmVudDogaG9tZVxuICAgIH1cbiAgXVxufSk7XG4gXG4vLyDlr7zoiKrlrojljatcbi8vIOS9v+eUqCByb3V0ZXIuYmVmb3JlRWFjaCDms6jlhozkuIDkuKrlhajlsYDliY3nva7lrojljavvvIzliKTmlq3nlKjmiLfmmK/lkKbnmbvpmYZcbnJvdXRlci5iZWZvcmVFYWNoKCh0bywgZnJvbSwgbmV4dCkgPT4ge1xuICBpZiAodG8ucGF0aCA9PT0gJy9sb2dpbicpIHtcbiAgICBuZXh0KCk7XG4gIH0gZWxzZSB7XG4gICAgbGV0IHRva2VuID0gbG9jYWxTdG9yYWdlLmdldEl0ZW0oJ0F1dGhvcml6YXRpb24nKTtcbiBcbiAgICBpZiAodG9rZW4gPT09IG51bGwgfHwgdG9rZW4gPT09ICcnKSB7XG4gICAgICBuZXh0KCcvbG9naW4nKTtcbiAgICB9IGVsc2Uge1xuICAgICAgbmV4dCgpO1xuICAgIH1cbiAgfVxufSk7XG4gXG5leHBvcnQgZGVmYXVsdCByb3V0ZXI7XHJcblxyXG4vLyDmt7vliqDor7fmsYLmi6bmiKrlmajvvIzlnKjor7fmsYLlpLTkuK3liqB0b2tlblxuYXhpb3MuaW50ZXJjZXB0b3JzLnJlcXVlc3QudXNlKFxuICBjb25maWcgPT4ge1xuICAgIGlmIChsb2NhbFN0b3JhZ2UuZ2V0SXRlbSgnQXV0aG9yaXphdGlvbicpKSB7XG4gICAgICBjb25maWcuaGVhZGVycy5BdXRob3JpemF0aW9uID0gbG9jYWxTdG9yYWdlLmdldEl0ZW0oJ0F1dGhvcml6YXRpb24nKTtcbiAgICB9XG4gXG4gICAgcmV0dXJuIGNvbmZpZztcbiAgfSxcbiAgZXJyb3IgPT4ge1xuICAgIHJldHVybiBQcm9taXNlLnJlamVjdChlcnJvcik7XG4gIH0pOyJdLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7QUFBQTtBQUNBO0FBQ0E7QUFDQTtBQUVBO0FBRUE7QUFDQTtBQUVBO0FBQ0E7QUFGQTtBQUtBO0FBQ0E7QUFDQTtBQUhBO0FBTUE7QUFDQTtBQUNBO0FBSEE7QUFYQTtBQW9CQTtBQUNBO0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBO0FBRUE7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFFQTtBQUNBIiwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./src/router.js\n");

/***/ })

})