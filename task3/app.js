var $ = jQuery;
var main = function() {
    // $(".category").click(function() {
    //     $("ol").append(" <li><h4>New category<h4></li>.");
    // });

    $('#add').click(function() {
        var Description = $('#description').val();
        if ($("#description").val() == '') {
            $('#alert').html("<strong>Warning!</strong> You left the category empty");
            $('#alert').fadeIn().delay(1000).fadeOut();
            return false;
        }
        $('.categories').appendpend("<li><h4>" + Description + "</h4></li>");
        $('#form')[0].reset();
        var categories = $('.categories').html();
        localStorage.setItem('categories', categories);
        // return false;
    });
}

$(document).ready(main);
