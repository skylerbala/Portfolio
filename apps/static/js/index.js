$(document).ready(function(){
  $('.sidenav').sidenav();
  M.AutoInit();

  $('.form-main').submit(function (e) {
    e.preventDefault();

    var formData = $(this).serialize();

  });
});
