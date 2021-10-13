$(document).ready(function(){
    $(".product-name").mouseenter(function(){
        $(".cart-item-remove-button").css("color","red");
    });
    $(".product-name").mouseleave(function(){
        $(".cart-item-remove-button").css("color","black");
    });
   
    $(".cart-item-remove-button").click(function(){
        $(".cart-product-list").remove().css();
    })
});