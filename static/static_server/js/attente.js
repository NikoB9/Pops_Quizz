/*******Fonction pour vérifier que le token peut être envoyé dans l'entete*********/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

ajaxInvitationGame = function (that){

	var game_uuid = $("#game_uuid").val();
	var friend_id = $(that).attr('id');
	var friend_login = $(that).attr('login');
	var url_back = './invite_friend';

	/*Entrer le token csrf dans le header si la route est sécurisé*/
	var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

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
		data: {'friend_id':friend_id, 'game_uuid':game_uuid},
		dataType: 'json',
    	success: function (data) {
			alert(data.message)
    		if (data.is_valid) {
    			document.getElementById(friend_id).classList.remove("fa-envelope-square");
    			document.getElementById(friend_id).classList.add("fa-check-square");
				refreshForAll();
                generalSocket.send(JSON.stringify({
                'type' : 'game_invite',
                'sender' : document.getElementById('user_co_login').value,
                    'receiver' : friend_login,
                'message': game_uuid
                }));
    		} else {
    			document.getElementById(friend_id).classList.remove("fa-envelope-square");
    			document.getElementById(friend_id).classList.add("fa-times");
    		}
    	}
	});
}


$('.inviteico').click(function(){
	ajaxInvitationGame(this);
});

function attention_commencer() {
	return confirm("Attention, vous êtes sur le point de commencer une partie. \nAssurez-vous que le nombre de joueur maximum a bien été atteind.\nEtes-vous sûr de vouloir continuer ?");
}

function attention_quitter() {
	return confirm("Attention, vous êtes sur le point de quitter la partie. \nVous ne pourrez plus la rejoindre à moins d'y être invité. \nEtes-vous sûr de vouloir continuer ?");
}

ajaxKickUser = function (that){

	var game_uuid = document.getElementById("game_uuid").value;
	var user_id = $(that).val();
	var url_back = './kick_user';

	/*Entrer le token csrf dans le header si la route est sécurisé*/
	var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

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
		data: {'user_id':user_id, 'game_uuid':game_uuid},
		dataType: 'json',
		success: function (data) {
			if (data.is_valid) {

			}
		}
	});
}


$('.exclude_user').click(function(){
	ajaxKickUser(this);
	document.getElementById("row-user-"+$(this).val()).style.display = "None";
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
	+ '/ws/attente_game/'
	+ idgame
	+ '/'
);

function refreshForAll(){
	chatSocket.send(JSON.stringify({
		'type' : 'refresh',
		'user' : '',
		'message': 'here'
	}));
};

function goGame(){
	chatSocket.send(JSON.stringify({
		'type' : 'refresh',
		'user' : '',
		'message': 'game'
	}));
};

chatSocket.onopen = function(e) {
	if (parseInt($('#playerslength').text()) >= parseInt($('#slotmax').text())){
		goGame();
	}
	else {
		chatSocket.send(JSON.stringify({
		'type' : 'connect_on',
		'user' : document.getElementById('pseudo').value,
		'message': " a rejoint le chat"
	}));
	}
};


chatSocket.onmessage = function(e) {
	const data = JSON.parse(e.data);
	console.log(data);
	if (data.type == 'connect_on'){
		document.querySelector('#chat-log-min').innerHTML += "<div class='connect_on'>"+data.user+data.message+"</div>";

		if ($('#row-user_wait-'+data.user).length){
			window.location.href = window.location.href;
		}

	}
	else if (data.type == 'refresh'){
	    if (data.message == 'here') window.location.href = window.location.href;
        else if (data.message == 'game') window.location.pathname = '/game/'+$('#game_uuid').val()+'/';
    }
	else if (data.type == 'chat_message')
		document.querySelector('#chat-log-min').innerHTML += "<div class='chat_message_title-min'>"+data.user+" : </div><div class='chat_message-min'>"+data.message+"</div>";
};

chatSocket.onclose = function(e) {
	console.error('Chat socket closed unexpectedly');
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

