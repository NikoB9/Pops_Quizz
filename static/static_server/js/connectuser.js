/*******Fonction pour vérifier que le token peut être envoyé dans l'entete*********/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$('#connectBtn').click(function(){
	$('#connectuserModal').modal('show');
});

openDivCo = function(){
    $('#connectBtn').click();
}

displayConnect = function(){
	$('#connectdiv').css('display','block');
	$('#authdiv').css('display','none');

	$('#btnFieldConnect').addClass('activefield');
	$('#btnFieldAuth').removeClass('activefield');
}

displayAuth = function(){
	$('#authdiv').css('display','block');
	$('#connectdiv').css('display','none');

	$('#btnFieldAuth').addClass('activefield');
	$('#btnFieldConnect').removeClass('activefield');
}

/*******Fonction de soumission générale de formulaire par ajax (dans des modales)*********/
function submitCo() {
  //console.log(form_id);
  form_id = 'connectuserModal';

  create_user = $("#btnFieldAuth").hasClass("activefield");

  url_back =  create_user ? './create_user' : './user_connection'; 

  console.log(create_user)
  console.log(url_back)

  /*
  Avertir l'utilisateur du chargemnt
  */
  btnSubmit = $('#'+form_id).find('.btn.btn-primary');
  btnSubmit.prop("disabled", true);
  var saveBtnName = btnSubmit.text();
  btnSubmit.empty();
  btnSubmit.append(jQuery('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>'));
  btnSubmit.append('&nbsp;&nbsp;Chargement...');


  var arr= {};
  $('#'+form_id+' input, #'+form_id+' select').each(
    function(index){  
        var input = $(this);
        /*alert('id: ' + input.attr('id') + 'Value: ' + input.val());*/
        arr[input.attr('id')] = input.val();
    }
  );

  $('#'+form_id+' input[type=checkbox]').each(
    function(index){  
        var input = $(this);
        arr[input.attr('id')] = input.is(':checked') ? 1 : 0;
    }
  );

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
    data: arr,
    dataType: 'json',
    success: function (data) {

      /*
      On indique à l'utilisateur que le chargement est fini
      */
      btnSubmit = $('#'+form_id).find('.btn.btn-primary');
      btnSubmit.empty();
      btnSubmit.prop("disabled", false);
      btnSubmit.append(saveBtnName);

      if (data.is_valid) {
      	if (create_user)
      	{
      		var successDiv = jQuery('<div class="alert alert-success" role="alert"></div>');
	        var successBody = jQuery('<p>Le compte vient d\'être créé.</p>');
	        $('#'+form_id).find('.modal-body').prepend(successDiv);
	        successDiv.append(successBody);
      	} 
      	else
        	window.location.reload();
      }
      else {
        //alert(data.error_message);
        //On cré les éléments pour ajouter un message d'erreur.
        var dangerDiv = jQuery('<div class="alert alert-danger" role="alert"></div>');
        var dangerBody = jQuery('<p>'+data.error_message+'</p>');
        $('#'+form_id).find('.modal-body').prepend(dangerDiv);
        dangerDiv.append(dangerBody);
      }      
    }
  });
};

$(document).click(function(){
	$('.alert').remove();
});

$('#userBtn').popover();


$('#userBtn').click(function(){
	$('#userBtn').popover('toggle');
});


$(document).on("click", '#disconnect', function(){

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
    url: './disconnect_user',
    dataType: 'json',
    success: function (data) {
      if (data.is_valid)
        window.location.reload();
    }
  });

});


$(document).on("click", '#dashboard', function(){
window.location.pathname = $('#dashboard-url').val();
});


$(document).ready(function () {
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
    url: './categories_menu',
    dataType: 'json',
    success: function (data) {
      menuCat = $('#catMenu');
      menuCat.empty();
      for (c of data.cats) {
          menuCat.append('<a class="dropdown-item" href="/show_cat_'+c.id+'">'+c.label+'<span class="nbQuizzSpan">'+c.nbQuizz+'</span></a>');
        }
    }
  });
});

$('.dropdown-toggle').dropdown();

$('.editbtn').tooltip();

//Ajout d'ami
ajaxAnswerFriendRequest = function(that,realtime)
{
    var url_back =  './answer_friend_request';
    var request_answer = $(that).val().split("|")[0];
    var user_source_login = $(that).val().split("|")[1];

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
        data: {'request_answer':request_answer, 'user_source_login':user_source_login},
        dataType: 'json',
        success: function (data) {
            if (data.is_valid) {
                if (realtime){
                    generalSocket.send(JSON.stringify({
                    'type' : 'friend_invite',
                    'sender' : document.getElementById('user_co_login').value,
                      'receiver' : user_source_login,
                    'message': request_answer
                }));
                    $('#inviteUserModal').modal('hide');
                }
            }
        }
    });
}

$('.accept_friend_realtime').click(function () {
    ajaxAnswerFriendRequest(this,true);
});


var loc = window.location, new_uri;
if (loc.protocol === "https:") {
	new_uri = "wss:";
} else {
	new_uri = "ws:";
}

var generalSocket = new WebSocket(
	new_uri += '//'
	+ window.location.host
	+ '/ws/global/'
);

generalSocket.onopen = function(e) {
  console.log('websocket running')
};


generalSocket.onmessage = function(e) {

	const data = JSON.parse(e.data);
	console.log(data);
	if (data.type == 'friend_invite'){
        if (document.getElementById('user_co_login').value == data.receiver){
            $('#inviteUserModal').modal('show');
            if (data.message == 'invite'){
                $('#invite_receive').css('display','flex');
                $('#invite_send').css('display','none');
                $('#usersource1').text(data.sender);
                $('#acceptinvitefr').val('accept|'+data.sender);
                $('#denyinvitefr').val('deny|'+data.sender);
            }
            else if (data.message == 'accept'){
                $('#invite_send').css('display','flex');
                $('#invite_receive').css('display','none');
                $('#usersource2').text(data.sender);
                $('#answerinvite').text('accepté');
            }
            else if (data.message == 'deny'){
                $('#invite_send').css('display','flex');
                $('#invite_receive').css('display','none');
                $('#usersource2').text(data.sender);
                $('#answerinvite').text('refusé');
            }
        }

    }
	else if (data.type == 'game_invite'){
        if (document.getElementById('user_co_login').value == data.receiver) {
            $('#inviteGameModal').modal('show');
            $('#usersourcegame').text(data.sender);
            $('#generaljoingamebtn').click(function () {
                window.location.pathname = 'joindre-partie/'+data.message+'/';
            });
        }
    }

};

generalSocket.onclose = function(e) {
	console.error('Chat socket closed unexpectedly');
};