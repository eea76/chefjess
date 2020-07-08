// 1 in 25 chance of a popup saying mahal kita

$(document).ready(function() {

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

});
