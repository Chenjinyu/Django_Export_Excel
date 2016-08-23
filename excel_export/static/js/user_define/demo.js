/*
 author: Chen Jinyu
 email: jinyu2010.chen@gmail.com
 date: 06/30/2016
 */
var weburl = this.location.href.match(/http:\/\/([a-zA-Z0-9-_\.]+\/)+/gi);
var webpath = this.location.href.match(/http:\/\/([a-zA-Z0-9-_\.]+\/)/gi);
if (weburl == null) {
    weburl = 'http://127.0.0.1:8080/onlineform/';
}


$(document).ready(function() {
			
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	function cancel_del()
	{
           bootbox.confirm("Are you sure cancel this form? If yes, all of information you added/modified would be lost.", function(result) {
		  if(result){
		     var pathname = window.location.pathname;
		     var len = pathname.length;
		     var new_url = pathname.substring(0, (len - 5));
		     $(location).attr('href',new_url);
	       }
    	});
  
	}

	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
		var csrftoken = Cookies.get('csrftoken');
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});


	$('#edit_cnl_btn').click(function() {
		cancel_del();
	});

});



