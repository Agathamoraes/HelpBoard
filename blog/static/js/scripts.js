// Empty JS for your own code to be here

var searchBtn = $('#search-btn');
var searchForm = $('#search-form');
var filter = $('#filter');

$(searchBtn).on('click', function() {
    searchForm.submit ();
});