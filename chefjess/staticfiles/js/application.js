$(document).ready(function() {

    var $nav = $('.navbar');
    var $body = $('body');
    var navOffsetTop = $nav.offset().top;
    var $window = $(window);

    function init() {
        $window.on('scroll', onScroll)
        $window.on('resize', resize)
        $('a[href^="#"]').on('click', smoothScroll)
    }

    function smoothScroll(e) {
        e.preventDefault();
        $(document).off("scroll");
        var target = this.hash,
            menu = target;
            $target = $(target);
        $('html, body').stop().animate({
            'scrollTop': $target.offset().top-40
            }, 0, 'swing', function () {
                window.location.hash = target;
                $(document).on("scroll", onScroll);
            });
    }

    function resize() {
        $body.removeClass('has-docked-nav')
        navOffsetTop = $nav.offset().top
        onScroll()
    }

    // add fixed class to header on scroll
    function onScroll() {
        if(navOffsetTop < $window.scrollTop() && !$body.hasClass('has-docked-nav')) {
            $body.addClass('has-docked-nav')
        }

        if(navOffsetTop > $window.scrollTop() && $body.hasClass('has-docked-nav')) {
            $body.removeClass('has-docked-nav')
        }
    }

    (function () {
        function logElementEvent(eventName, element) {
            console.log(Date.now(), eventName, element.getAttribute("data-src")
            );
        }

        var callback_enter = function (element) {
            logElementEvent("🔑 ENTERED", element);
        };

        var callback_exit = function (element) {
            logElementEvent("🚪 EXITED", element);
        };

        var callback_loading = function (element) {
            logElementEvent("⌚ LOADING", element);
        };

        var callback_loaded = function (element) {
            logElementEvent("👍 LOADED", element);
        };

        var callback_error = function (element) {
            logElementEvent("💀 ERROR", element);
            element.src ="https://via.placeholder.com/440x560/?text=Error+Placeholder";
        };

        var callback_finish = function () {
            logElementEvent("✔️ FINISHED", document.documentElement);
        };

        var callback_cancel = function (element) {
            logElementEvent("🔥 CANCEL", element);
        };

        var ll = new LazyLoad({
            threshold: 0,
            // Assign the callbacks defined above
            callback_enter: callback_enter,
            callback_exit: callback_exit,
            callback_cancel: callback_cancel,
            callback_loading: callback_loading,
            callback_loaded: callback_loaded,
            callback_error: callback_error,
            callback_finish: callback_finish
        });
    })();

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

    init();
});
