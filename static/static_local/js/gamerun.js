/*******Fonction pour vérifier que le token peut être envoyé dans l'entete*********/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


ajaxSaveForm = function(that)
{
	//console.log(form_id);
  var form_id = 'form_answers';

  var url_back =  './save_user_answers'; 


  var id = $(that).attr('id').substr(6);
  var value = $(that).val();
  var idplayer = $('#idplayer').val();

  if($(that).attr('type') == 'checkbox')
  	var value = $(that).is(':checked') ? 1 : 0;
  else
  	var value = $(that).val();


  /*Entrer le token csrf dans le header si la route est sécurisé*/
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  /*console.log("csrf token : "+csrftoken);*/
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !that.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
  $.ajax({
  	type: 'POST',
    url: url_back,
    data: {'idplayer':idplayer, 'idPA': id, 'value': value},
    dataType: 'json',
    success: function (data) {

      if (data.is_valid) {
      } 
    }
  });
}

userAnswerTheQuestion = function(idq,id_player,q)
{

  var url_back =  './question_answer_by';

  /*Entrer le token csrf dans le header si la route est sécurisé*/
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  /*console.log("csrf token : "+csrftoken);*/
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
  $.ajax({
  	type: 'POST',
    url: url_back,
    data: {'player':id_player, 'question': idq},
    dataType: 'json',
    success: function (data) {

      if (data.is_valid) {
          if (q > parseInt($('#totalquestions').val()))
	        $('#form_answers').submit();
      }
    }
  });
}

$('input').not( "#chat-message-input-min" ).change(function(){
	ajaxSaveForm(this);
});

$('input[type=text]').not( "#chat-message-input-min" ).keypress(function(){
	ajaxSaveForm(this);
});

$(document).ready(function () {
    if ($('#realtime').val()=='True'){
        $('fieldset[id^="question-"').addClass('hidden');
        $("#question-1").removeClass('hidden');
        $("#question-1").addClass('visible');
    }
});

/*****Chat open/close*****/
$('#chatbtn').click(function () {
	$(this).removeClass('visible');
	$(this).addClass('hidden');

	$('#chatdiv').removeClass('hidden');
	$('#chatdiv').addClass('visible');

	document.querySelector('#chat-message-input-min').focus();
})

$('#closechat').click(function () {
	$('#chatdiv').removeClass('visible');
	$('#chatdiv').addClass('hidden');

	$('#chatbtn').removeClass('hidden');
	$('#chatbtn').addClass('visible');
})
/*******Real Time********/
const idgame = JSON.parse(document.getElementById('idgame').textContent);

var loc = window.location, new_uri;
if (loc.protocol === "https:") {
	new_uri = "wss:";
} else {
	new_uri = "ws:";
}

var chatSocket = new WebSocket(
	new_uri += '//'
	+ window.location.host
	+ '/ws/in_game/'
	+ idgame
	+ '/'
);

chatSocket.onopen = function(e) {
  chatSocket.send(JSON.stringify({
		'type' : 'connect_on',
		'user' : document.getElementById('pseudo').value,
		'message': " a rejoint le chat"
	}));
};


chatSocket.onmessage = function(e) {

	const data = JSON.parse(e.data);
	console.log(data);
	if (data.type == 'next_question'){

	    $('#nextquestionmodal').modal('show');
        $('#userwin').text(data.user);

	    mm = data.message.split('-')
	    q = parseInt(mm[0])+1;
	    idq = mm[1];
	    idp = mm[2];
	    userAnswerTheQuestion(idq,idp,q)
        if (q <= parseInt($('#totalquestions').val())){
            $('fieldset[id^="question-"').removeClass('visible');
            $('fieldset[id^="question-"').addClass('hidden');

            $('#question-'+q).removeClass('hidden');
            $('#question-'+q).addClass('visible');
        }

    }
	else if (data.type == 'connect_on')
		document.querySelector('#chat-log-min').innerHTML += "<div class='connect_on'>"+data.user+data.message+"</div>";
	else if (data.type == 'chat_message')
		document.querySelector('#chat-log-min').innerHTML += "<div class='chat_message_title-min'>"+data.user+" : </div><div class='chat_message-min'>"+data.message+"</div>";

};

chatSocket.onclose = function(e) {
	console.error('Chat socket closed unexpectedly');
	chatSocket = new WebSocket(
		new_uri
	);
};

document.querySelector('#chat-message-input-min').onkeyup = function(e) {
	if (e.keyCode === 13) {  // enter, return
		document.querySelector('#chat-message-submit-min').click();
	}
};

document.querySelector('#chat-message-submit-min').onclick = function(e) {
	const messageInputDom = document.querySelector('#chat-message-input-min');
	const message = messageInputDom.value;
	chatSocket.send(JSON.stringify({
		'type' : 'chat_message',
		'user' : document.getElementById('pseudo').value,
		'message': message
	}));
	messageInputDom.value = '';
};

$('#nextbtn').click(function () {
    $('fieldset[id^="question-"').each(function () {
        if ($(this).hasClass('visible')){
            numq = $(this).attr('id').split('-')[1];
            idq = $(this).attr('idq');
            chatSocket.send(JSON.stringify({
                'type' : 'next_question',
                'user' : document.getElementById('pseudo').value,
                'message': numq+'-'+idq+'-'+$('#idplayer').val()
            }));
        }
    })
})
