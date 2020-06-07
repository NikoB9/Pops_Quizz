/*******Fonction pour vérifier que le token peut être envoyé dans l'entete*********/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

ajaxInvitationGame = function (that){

	var game_uuid = $("#game_uuid").val();
	var friend_id = $(that).attr('id');
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
    		if (data.is_valid) {
    			alert("L'inviation a été envoyée avec succès !")
    			document.getElementById(friend_id).classList.remove("fa-envelope-square");
    			document.getElementById(friend_id).classList.add("fa-check-square");
    			window.location.href = window.location.href;
    		} else {
    			alert("La personne a déjà été invité dans une partie.")
    			document.getElementById(friend_id).classList.remove("fa-envelope-square");
    			document.getElementById(friend_id).classList.add("fa-times");
    		}
    	}
	});
}


$('.fa-envelope-square').click(function(){
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
	var user_login = $(that).val();
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
		data: {'user_login':user_login, 'game_uuid':game_uuid},
		dataType: 'json',
		success: function (data) {
			if (data.is_valid) {

			}
		}
	});
}


$('.exclude_user').click(function(){
	ajaxKickUser(this);
	console.log("row-user-"+$(this).val())
	document.getElementById("row-user-"+$(this).val()).style.visibility = "hidden";
});


/*******Real Time********/
const idgame = JSON.parse(document.getElementById('idgame').textContent);

var loc = window.location, new_uri;
if (loc.protocol === "https:") {
	new_uri = "wss:";
} else {
	new_uri = "ws:";
}

const chatSocket = new WebSocket(
	new_uri += '//'
	+ window.location.host
	+ '/ws/attente_game/'
	+ idgame
	+ '/'
);

chatSocket.onopen = function(e) {
  chatSocket.send(JSON.stringify({
		'type' : 'connect_on',
		'user' : document.getElementById('pseudo').value,
		'message': ""
	}));
};

chatSocket.onmessage = function(e) {
	const data = JSON.parse(e.data);
	console.log(data);
	if (data.type == 'connect_on'){
		if ($('#row-user_wait-'+data.user).length){
			console.log('userdetect')
			window.location.href = window.location.href;
		}
	}
};

chatSocket.onclose = function(e) {
	console.error('Chat socket closed unexpectedly');
};

