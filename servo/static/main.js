var app = angular.module('ServoApp',[]);

app.directive('servoConfig',function(){
    return {
        scope: {
            'servo' : '=servo'
        },
        templateUrl : '/static/servo.html',
        controller : 'ConfigController'
    }
});

app.controller('ConfigController',['$scope','$http',function($scope,$http){
    var servo = $scope.servo;
    $scope.active = false;
    $scope.raw = (servo.min + servo.max)/2.0;
    $scope.pos = ($scope.raw - servo.offset)/servo.scale;
    $scope.stringraw = $scope.raw;
    $scope.$watch('raw', function() {
        console.log($scope.raw + ',' + $scope.stringraw + ',' + $scope.pos);
        $scope.stringraw = $scope.raw;
        $scope.pos = ($scope.raw - servo.offset)/servo.scale;
        console.log($scope.raw + ',' + $scope.stringraw + ',' + $scope.pos);
        if($scope.active) {
            $http.post('/raw/'+servo.id,$scope.raw);
        }
    });
    $scope.$watch('stringraw', function() {
        console.log($scope.raw + ',' + $scope.stringraw + ',' + $scope.pos);
        $scope.raw = parseFloat($scope.stringraw);
    });
    $scope.$watch('pos', function() {
        console.log($scope.raw + ',' + $scope.stringraw + ',' + $scope.pos);
        $scope.raw = $scope.pos*$scope.servo.scale + $scope.servo.offset;
    });
    var update = function() {
        console.log($scope.servo.scale + ',' + $scope.servo.offset);
        console.log($scope.raw + ',' + $scope.stringraw + ',' + $scope.pos);
        $scope.pos = ($scope.raw - servo.offset)/servo.scale;
    };
    $scope.$watch('servo.scale',update);
    $scope.$watch('servo.offset',update);
    $scope.update = function(){
        $http.post('/config/'+servo.name,JSON.stringify(servo));
    };
    console.log($scope);
}]);

app.controller('ServoController',['$scope','$http',function($scope,$http) {
    $scope.servos = [];

    var transform = function(data) {
        var output = [];
        angular.forEach(Object.keys(data),function(key){
            var subject = data[key];
            subject.name = key;
            output.push(subject);
        },this);
        return output;
    }
    console.log('hello?');

    $http.get('/config').then(function(result){
        console.log(result);
        $scope.servos = transform(result.data);
    },function(error){console.log(error);});
}]);
