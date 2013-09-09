'use strict';

var users, userId = 1;
var url = "http://127.0.0.1:8000/users/";

var getUsers = function($http, $q) {

    var deferred = $q.defer();
    console.log(users);
    if (!users) {
        console.log("Trying to get data");
        $http.get("http://127.0.0.1:8000/users/").success(function(data) {
            console.log("successful");
            users = data.items;
            deferred.resolve(data.items);
        });
    } else {
        console.log("unsuccessful");
        deferred.resolve(users);
    }
    console.log("End of operation, users: " + users);
    return deferred.promise;
};

lemonpi.run(function($rootScope, $log, $http, $cookies) {
    console.log("in the run");
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];

});

lemonpi.controller('MainCtrl', function($scope, $http, $q) {

    getUsers($http, $q).then(function(users) {
        console.log("In the main control");
        $scope.users = users;
    });
});


