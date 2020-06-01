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
  	  // Traiter le cas où on demande en ami alors que l'utilisateur nous a déjà envoyé une demande ?
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

$('#user_target').change(function () {
    document.getElementById("btn-add-friend").disabled = $(this).val().trim() === ""
});

$('#btn-add-friend').click(function(){
    if($('#user_target').val().trim() != "")
    ajaxAddUser(this);
});
