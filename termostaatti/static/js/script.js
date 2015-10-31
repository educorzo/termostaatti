var appname = angular.module('appname', []);
appname.controller('appCtrl', ['$scope',
  function($scope) {
     $http({method: 'GET',url: '/temperatura'})
     .then(function successCallback(response) {
            $scope.greeting = response
        }, function errorCallback(response) {
            $scope.greeting ={ text: 'Hello' };
        });
}]);