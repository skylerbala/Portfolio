$(document).ready(function(){
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

var controller = new ScrollMagic.Controller();
 


		// build scene
		var scene = new ScrollMagic.Scene({
							triggerElement: "#trigger1"
						})
						.setTween("#animate1", 0.5, {backgroundColor: "green", scale: 2.5}) // trigger a TweenMax.to tween
						.addIndicators({name: "1 (duration: 0)"}) // add indicators (requires plugin)
						.addTo(controller);
