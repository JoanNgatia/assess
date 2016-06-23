var $ = jQuery;
var main = function (){
    $(".category").click(function(){
         $("ol").append(" <li>New category</li>.");
        });
}

$(document).ready(main);
