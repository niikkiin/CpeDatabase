const $button  = document.querySelector('#sidebar-toggle');
const $wrapper = document.querySelector('#wrapper');

$button.addEventListener('click', (e) => {
    e.preventDefault();
    $wrapper.classList.toggle('toggled');
});

function copyToClipboard(element) {
    var $temp = $("<input>");
    var $toolTip = $('span.student-copy');
    var originalTitle = $toolTip.attr('title');

    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $temp.remove();

    $('span.student-copy').tooltip('hide')
                        .attr('title', 'Copied!')
                        .tooltip('fixTitle')
                        .tooltip('show');
    
}

  