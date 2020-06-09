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


$('#clock').ready(function(){
    date_limit = $('#date_limit').val();
    timer_int = $('#timer').val();
    player_id = $('#player_id').val();
    timer(timer_int, date_limit, player_id);
});

function timer(timer_int, date_limit, player_id) {
    // Set the date we're counting down to
    var countDownDate = new Date(date_limit).getTime();

    // Update the count down every 1 second
    var x = setInterval(function() {

        // Get today's date and time
        var now = new Date().getTime();

        // Find the distance between now and the count down date
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the element with id="clock"
        document.getElementById("clock").innerHTML =
            // days + "d " + hours + "h " +
            minutes + "m " + seconds + "s ";
        update_progress_bar((-distance / timer_int+1)*100)

        // If the count down is finished, write some text
        if (distance < 0) {
            clearInterval(x);
            document.getElementById("clock").innerHTML = "Fin du temps";
            update_progress_bar(100)
            window.location.pathname=$('#correction_url').val();
        }
    }, 1000);
}

function update_progress_bar(progress) {
    $('#progress-bar').width(progress + "%").attr('aria-valuenow', progress)

}
