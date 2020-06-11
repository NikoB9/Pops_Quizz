/*******Fonction pour vérifier que le token peut être envoyé dans l'entete*********/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


ajaxCorrectionQuestion = function(that)
{
  var url_back =  './correction_question';
  var question_id = $(that).val();

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
    data: {'question_id':question_id},
    dataType: 'json',
    success: function (data) {
      if (data.is_valid) {
          alert("Correction demandée")
      }
    }
  });
}

$('.btn_correction').click(function(){
    ajaxCorrectionQuestion(this)
    document.getElementById("need_correction"+$(this).val()).disabled = 'True';
    document.getElementById("need_correction"+$(this).val()).title = 'Une demande de correction a déjà été faite';
});
