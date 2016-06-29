var $ = jQuery;
var main = function() {

    $('#add').click( function() {
      var Description = $('#description').val();
      console.log(Description)
      $('.categories').append('<li><a>'+Description+'</a></li>');
      var categories = $('.categories').html();
      localStorage.setItem('categories', categories);
    });

    if(localStorage.getItem('categories')){
      $('.categories').html(localStorage.getItem('categories'));
    }
}

$(document).ready(main);
