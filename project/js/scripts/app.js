'use strict';

var lemonpi = angular.module('lemonpi', ['ngCookies'])
.config(['$routeProvider', function($routeProvider) {
  $routeProvider
  .when('/', {
    templateUrl: 'views/main.html',
    controller: 'MainCtrl'
  })
}]);
