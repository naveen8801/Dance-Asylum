
$(document).ready(function() {

    $('.menue_hamburger').click(() =>{
        $('.menue_hamburger').toggle().toggleClass("menue_burger_clicked_icon");
        $('.my_navbar').toggle().toggleClass("menue_burger_clicked_navabr").slideDown("slow");
        console.log("HI");
    });

    $('.list_items').click(()=>{
        $('.menue_hamburger').toggle().toggleClass("menue_burger_clicked_icon");
        $('.my_navbar').toggle().toggleClass("menue_burger_clicked_navabr");
    });



});