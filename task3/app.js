var $ = jQuery;
var main = function (){
    $(".category").click(function(){
         $("ol").append(" <li><h4>New category<h4></li>.");
        });
}

$(document).ready(main);
