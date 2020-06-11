/*******Fonction pour vérifier que le token peut être envoyé dans l'entete*********/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


ajaxAddUser = function(that)
{
  var url_back =  './add_friend';
  var user_target = $('#user_target').val();

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
    data: {'user_target':user_target},
    dataType: 'json',
    success: function (data) {
  	  if(data.cant_invite_himself) {
  	      alert("vous avez rentré votre login")
      } else {
          if (!data.is_valid_login) {
              alert("utilisateur inconnu")
          } else {
              if(data.relationship_already_established) {
                  if(data.accepted) {
                      alert("Vous êtes déjà ami")
                  } else {
                      alert("invitation déjà envoyée")
                  }
              } else {
                  alert("invitation envoyée")
              }
          }
      }
    }
  });
}

ajaxChangeUserInvite = function(that)
{
    var url_back =  './change_user_invite';
    var user_target = $('#user_target').val();

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
        data: {'user_target':user_target},
        dataType: 'json',
        success: function (data) {
            if(data.is_valid) {
                console.log(data.users)
                var list_users = document.getElementById("list-users");
                list_innerhtml = ""
                for(const user_login of data.users) {
                    console.log("login"+user_login)
                    list_innerhtml+="<option value=\""+user_login+"\" label=\""+user_login+"\">\n";
                }
                console.log(list_innerhtml)
                list_users.innerHTML = list_innerhtml
            }
        }
    });
}

$('#user_target').keyup(function () {
    ajaxChangeUserInvite(this);
    document.getElementById("btn-add-friend").disabled = $(this).val().trim() === "";
    if ($(this).val() == "") {
      document.getElementById("btn-add-friend").classList.add('iconBtnSpe');
      document.getElementById("btn-add-friend").classList.remove('iconBtn');
    } else {
      document.getElementById("btn-add-friend").classList.remove('iconBtnSpe');
      document.getElementById("btn-add-friend").classList.add('iconBtn');
    }
    
});

$('#btn-add-friend').click(function(){
    if($('#user_target').val().trim() != "")
    ajaxAddUser(this);
});


ajaxRemoveFriend = function(that)
{
    var url_back =  './remove_friend';
    var user_target_login = $(that).val();

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
        data: {'user_target_login':user_target_login},
        dataType: 'json',
        success: function (data) {
            if (data.is_valid) {

            }
        }
    });
}

$('.remove_friend').click(function(){removeFriend(this)});

removeFriend = function(that)
{
    ajaxRemoveFriend(that);
    document.getElementById("row-friend-"+$(that).val()).style.display = "none";
}

ajaxAnswerFriendRequest = function(that)
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

            }
        }
    });
}

$('.accept_friend').click(function(){
    ajaxAnswerFriendRequest(this);
    let val = $(this).val().split("|");
    if(val[0] == "accept")
    {
        //Build element of the friends list
        let $friend = document.createElement("li");
        $friend.id = "row-friend-" + val[1];
        $friend.innerText = val[1] + " ";
        let $btnRemoveFriend = document.createElement("button");
        $btnRemoveFriend.value = val[1];
        $btnRemoveFriend.classList.add("remove_friend", "connectBtn", "iconBtn");
        $btnRemoveFriend.onclick = function(e){removeFriend($($btnRemoveFriend))};
        let $btnIcon = document.createElement("i");
        $btnIcon.classList.add("fas", "fa-user-slash");
        $btnRemoveFriend.appendChild($btnIcon);
        $friend.appendChild($btnRemoveFriend);
        document.getElementById("friends_list").appendChild($friend);
    }
    document.getElementById("row-accept-"+val[1]).remove();
});

