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

$('input').change(function(){
	ajaxSaveForm(this);
});

$('input[type=text]').keypress(function(){
	ajaxSaveForm(this);
});

$('#subbtn').click(function(){
    $('#subbtn').hide();
    $('#resbtn').hide();
    $('#resultbtn').removeAttr('hidden');
    $('#score-affichage').removeAttr('hidden');
    // TODO Calculer le score total, update score dans la table player en BD


});
