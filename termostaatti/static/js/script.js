var termostaatti = angular.module('appname', []);
termostaatti.controller('appCtrl', ['$scope','$http',
  function($scope, get) {
     get({method: 'GET',url: '/temperatura'})
     .then(function successCallback(response) {
            $scope.temperature = {text : response.data.Temperature+'º'}
        }, function errorCallback(response) {
            $scope.temperature ={ text: 'Error' };
        });
}]);

termostaatti.controller('buttonCtrl', ['$scope','$http',
   function($scope, post) {
      $scope.req = {
         method: 'POST',
         url: 'http://192.168.1.129:8000/caldera/',
         headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=$'}
         data: 'state=off'
      };
      $scope.showEncender = true;
      $scope.showApagar = false;
      
      $scope.encender = function() {
        $scope.req.data = 'state=on';
         post($scope.req).then(function(){
            $scope.showEncender = false;
            $scope.showApagar = true; 
         });
      };
      
      $scope.apagar = function() {
         $scope.req.data = 'state=off';
         post($scope.req).then(function(){
            $scope.showEncender = true;
            $scope.showApagar = false; 
         });
      };
}]);