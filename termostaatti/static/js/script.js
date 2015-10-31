var appname = angular.module('appname', []);
appname.controller('appCtrl', ['$scope','$http',
  function($scope, get) {
     get({method: 'GET',url: '/temperatura'})
     .then(function successCallback(response) {
            $scope.greeting = response.data.Temperature
        }, function errorCallback(response) {
            $scope.greeting ={ text: 'Hello' };
        });
}]);