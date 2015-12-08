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

termostaatti.controller('setTemperatureCtrl',['$scope','$http',
        function($scope, post) {
                $scope.req = {
                        method: 'POST',
                        url: '/settemperatura/',
                        headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=$'},
                        data: 'temperature = 20'
                };
                $scope.editTemperature = 20;
                $scope.disminuir = function(){
                        $scope.editTemperature = $scope.editTemperature - 1;
                };
                $scope.aumentar = function(){
                        $scope.editTemperature = $scope.editTemperature + 1;
                };
                $scope.setTemperature = function(){
                        $scope.req.data = 'temperature='+$scope.editTemperature;
                        post($scope.req).then(function(response){

                        });
                };
}]);

termostaatti.controller('buttonCtrl', ['$scope','$http',
   function($scope, post) {
      $scope.req = {
         method: 'POST',
         url: '/caldera/',
         headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=$'},
         data: 'state=off'
      };
      $scope.showEncender = true;
      $scope.showApagar = false;

      $scope.encender = function() {
        $scope.req.data = 'state=on';
         post($scope.req).then(function(response){
            $scope.showEncender = false;
            $scope.showApagar = true;
         });
      };

      $scope.apagar = function() {
         $scope.req.data = 'state=off';
         post($scope.req).then(function(response){
            $scope.showEncender = true;
            $scope.showApagar = false;
         });
      };
}]);