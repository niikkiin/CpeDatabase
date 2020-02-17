const $button  = document.querySelector('#sidebar-toggle');
const $wrapper = document.querySelector('#wrapper');
const $image = document.querySelector('#profile-pic');
const $imageContainer = document.querySelector('#profile-container');

const $sidebarBrand = document.querySelector('.sidebar-brand');
const $sidebarNav = document.querySelector('.sidebar-nav');
$button.addEventListener('click', (e) => {
    e.preventDefault();
    $wrapper.classList.toggle('toggled');
    $image.classList.toggle('minimized');
    $imageContainer.classList.toggle('minimized');
    $sidebarBrand.classList.toggle('minimized');
    $sidebarNav.classList.toggle('minimized');
    
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

