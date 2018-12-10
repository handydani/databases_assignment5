angular.module('listings').controller('ListingsController', ['$scope', 'Listings', 
  function($scope, Listings) {
    /* Get all the listings, then bind it to the scope */
    Listings.getAll().then(function(response) {
      $scope.listings = response.data;
    }, function(error) {
      console.log('Unable to retrieve listings:', error);
    });

    $scope.detailedInfo = undefined;

    $scope.addListing = function() {
	  /**TODO 
	  *Save the article using the Listings factory. If the object is successfully 
	  saved redirect back to the list page. Otherwise, display the error
	 */


      Listings.create($scope.newListing);
      // .then(function(response){
      //   // $scope.listings = ressponse.data;
      // }, function(error){
      //   console.log('Unable to add listings: ', error);
      // });
            $scope.newListing = {};

            location.reload();
    };

    $scope.deleteListing = function(index) {
	   /**TODO
        Delete the article using the Listings factory. If the removal is successful, 
		navigate back to 'listing.list'. Otherwise, display the error. 
       */
       // console.log($scope.listings[index]._id);
       var myListing = $scope.listings[index];
       // Listings.delete(myListing._id);
       // location.reload();
       /*
       .then(function(response){
        $scope.listings = response.data;
       }, function(error){
        console.log('Unable to delete listings: ', error);
       });*/


      Listings.delete(myListing._id).then(function(response) {
        $scope.listings = response.data;
        location.reload();
      }, function(error) {
        console.log('Unable to delete listings:', error);
      });

    };

    $scope.showDetails = function(index) {
      $scope.detailedInfo = $scope.listings[index];
    };
  }
]);