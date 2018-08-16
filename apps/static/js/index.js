$(document).ready(function(){
  $('.sidenav').sidenav();
  M.AutoInit();

  $('.form-main').submit(function (e) {
    e.preventDefault();

    var formData = $(this).serialize();

  });
});

$(document).ready(function(){
  $('#dynamic-title')
});


$(document).on("submit", "form", function(event) {
    event.preventDefault();        
    $.ajax({
        url: $(this).attr("action"),
        type: $(this).attr("method"),
        data: new FormData(this),
        processData: false,
        contentType: false,
        success: function (data, status) {
          M.toast({ html: 'Message Sent!' })
        },
        error: function (xhr, desc, err) {
          M.toast({ html: 'Error Sending Message; Try messaging me directly.' })
        }
    });        
});

