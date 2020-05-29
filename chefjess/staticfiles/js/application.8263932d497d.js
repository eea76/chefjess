// 1 in 25 chance of a popup saying mahal kita

$(document).ready(function() {
    // hamburger menu animation
    var forEach=function(t,o,r){if("[object Object]"===Object.prototype.toString.call(t))for(var c in t)Object.prototype.hasOwnProperty.call(t,c)&&o.call(r,t[c],c,t);else for(var e=0,l=t.length;l>e;e++)o.call(r,t[e],e,t)};

    var hamburgers = document.querySelectorAll(".hamburger");
    if (hamburgers.length > 0) {
        forEach(hamburgers, function(hamburger) {
            hamburger.addEventListener("click", function() {
                this.classList.toggle("is-active");
            }, false);
        });
    }


    // toggle mobile menu
    $('.hamburger').on('click', function() {
        $('.mobile-menu').slideToggle(250, 'swing', function() {

        });
    });


    //get page load info
    var user = detect.parse(navigator.userAgent);

    var data_message = {};
    data_message.browser = user.browser.name;
    data_message.os = user.os.name;
    data_message.url = window.location.href;
    data_message.mealName = $('.meal-name').text()

    $.ajax({
        type: 'post',
        data: JSON.stringify(data_message),
        url: '/detect_browser/',
        success: function(response) {

        },
        processData: false,
        contentType: false,
        async: true
    });

});
