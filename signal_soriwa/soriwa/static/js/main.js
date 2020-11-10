let scrollEvent = false;
let count = 0;

$("html, body").on('mousewheel', function(e) {
    e.preventDefault();
    var m = e.originalEvent.wheelDelta;
    var sb = $("#window1").height();

    if (m > 1 && scrollEvent == false && count >= 1) {
        console.log(count);
        scrollEvent = true;
        count--;
        $('html, body').animate({scrollTop: sb*count},
            { duration: 500, complete: function() {
                    scrollEvent = false; }
            });
    } else if (m < 1 && scrollEvent == false && count < 3) {
        console.log(count);
        scrollEvent = true;
        count++;
        $('html, body').animate({scrollTop: sb*count},
            { duration: 500, complete: function() {
                    scrollEvent = false; }
            });
    }
});
// window.addEventListener('resize', function() {
//   console.log('Resizing...');
// }, true);

$(window).resize(function() {
    console.log('resize');
    $("html, body").animate({scrollTop: $("html, body").offset().top}, 400);
});