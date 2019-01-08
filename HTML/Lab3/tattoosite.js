//  * Applies parallax scrolling to an element's background image.
//     * @return { jQuery } jQuery object.
//      * /

$.fn._parallax = (skel.vars.browser == 'ie' || skel.vars.mobile) ? function () { return $(this) } : function (intensity) {
    var $window = $(window),
        $this = $(this);
    if (this.length == 0 || intensity === 0)
        return $this;
    if (this.length > 1) {
        for (var i = 0; i < this.length; i++)
            $(this[i])._parallax(intensity);
        return $this;
    }
    if (!intensity)
        intensity = 0.25;
    $this.each(function () {
        var $t = $(this),
            on, off;
        on = function () {
            $t.css('background-position', 'center 100%, center 100%, center 0px');
            $window
                .on('scroll._parallax', function () {
                    var pos = parseInt($window.scrollTop()) - parseInt($t.position().top);
                    $t.css('background-position', 'center ' + (pos * (-1 * intensity)) + 'px');
                });
        };
        off = function () {
            $t
                .css('background-position', '');
            $window
                .off('scroll._parallax');
        };
        skel.on('change', function () {
            if (skel.breakpoint('medium').active)
                (off)();
            else
                (on)();
        });
    });
    $window
        .off('load._parallax resize._parallax')
        .on('load._parallax resize._parallax', function () {
            $window.trigger('scroll');
        });
    return $(this);
};