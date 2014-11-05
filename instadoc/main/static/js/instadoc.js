var instadocApp = angular.module('instadocApp', ['tastyResource', 'ngSanitize']);

instadocApp.factory("Category", ["TastyResource", function (TastyResource) {
    return TastyResource({
        url: "/api/v1/category/",
        cache: true
    });
}]);

instadocApp.factory("Documentation", ["TastyResource", function (TastyResource) {
    return TastyResource({
        url: "/api/v1/documentation/",
        cache: true
    });
}]);


instadocApp.controller("instadocAppCtrl",  ["$scope", "$log", "Category", "Documentation", function ($scope, $log, Category, Documentation) {
    $scope.documentations = Documentation.query({category__id: CATEGORY_ID});
    $scope.item_doc = {html: '<span class="alert alert-info">Use the search bar and click the item for details!</span>'};

    $scope.load_documentation = function(id) {
        $scope.item_doc = Documentation.get(id);
    };
}]);
