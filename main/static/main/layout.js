document.addEventListener('DOMContentLoaded', function () {
    options = {};

    var els = document.querySelectorAll('.collapsible');
    M.Collapsible.init(els, options);
    // ScrollSpy
    const ss = document.querySelectorAll('.scrollspy');
    M.ScrollSpy.init(ss, options);

    var elems = document.querySelectorAll('.materialboxed');
    M.Materialbox.init(elems, options);

    var el = document.querySelectorAll('.tabs');
    M.Tabs.init(el, options);

    var options = {
        "constrainWidth": false,
        "coverTrigger": false
    }

    var elems = document.querySelectorAll('.dropdown-trigger');
    M.Dropdown.init(elems, options);

    var options = {
        "onCloseStart": pauseVideo
    }
    var elems = document.querySelectorAll('.modal');
    M.Modal.init(elems, options);
});

function pauseVideo() {
    var div = document.getElementsByClassName("open")[0];
    var iframe = div.getElementsByTagName("iframe")[0].contentWindow;
    iframe.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
}