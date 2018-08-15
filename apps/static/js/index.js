$(document).ready(function(){
  $('.sidenav').sidenav();
  M.AutoInit();

  $('.form-main').submit(function (e) {
    e.preventDefault();

    var formData = $(this).serialize();

  });

  $('.pushpin-demo-nav').each(function() {
    var $this = $(this);
    var $target = $('#' + $(this).attr('data-target'));
    $this.pushpin({
      top: $target.offset().top,
      bottom: $target.offset().top + $target.outerHeight() - $this.height()
    });
  });
});


