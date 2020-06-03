/*******Fonction pour vérifier que le token peut être envoyé dans l'entete*********/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


ajaxRefuseInvitation = function(that)
{
  var url_back =  './refuse_game_invitation';
  var game_uuid = $(that).val();

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
    data: {'game_uuid':game_uuid},
    dataType: 'json',
    success: function (data) {
  	  if(data.is_valid) {
      }
    }
  });
}

$('.refuse_invite').click(function(){
    ajaxRefuseInvitation(this);
    document.getElementById("row-invited-game-"+$(this).val()).style.visibility = "hidden";
});

