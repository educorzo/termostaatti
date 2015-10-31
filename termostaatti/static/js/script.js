var appname = angular.module('appname', []);
appname.controller('appCtrl', ['$scope','$http',
  function($scope, get) {
     get({method: 'GET',url: '/temperatura'})
     .then(function successCallback(response) {
            $scope.temperature = {text : response.data.Temperature+'º'}
        }, function errorCallback(response) {
            $scope.temperature ={ text: 'Error' };
        });
}]);