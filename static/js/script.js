// Profile page
$(function(){
    saved = $('#saved').html();
    posted = $('#posted').html();

    $('#content').html(saved);
    
    $('#btnradio1').click(function () {
        $('#content').html(saved);
    })
    $('#btnradio2').click(function () {
        $('#content').html(posted);
    })
  });
