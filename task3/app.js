var $ = jQuery;
var main = function() {

    $('#add').click( function() {
      var Description = $('#description').val();
      $('.categories').append('<li><a><h4>'+Description+'</h4></a></li>');
      var categories = $('.categories').html();
      localStorage.setItem('categories', categories);
    });

    $('.delete').click(function() {
        $('h4').remove();
    });

    if(localStorage.getItem('categories')){
      $('.categories').html(localStorage.getItem('categories'));
    }
}

$(document).ready(main);
