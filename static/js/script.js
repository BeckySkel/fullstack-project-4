// Profile page
$(function(){
    saved = $('#saved').html();
    posted = $('#posted').html();
    info = $('#info').html();
    
    $('#content').html((typeof saved === 'undefined') ? info : saved);
    
    $('#btnradiosaved').click(function () {
        $('#content').html(saved);
    })
    $('#btnradioposted').click(function () {
        $('#content').html(posted);
    })
    $('#btnradioinfo').click(function () {
        $('#content').html(info);
    })
  });
