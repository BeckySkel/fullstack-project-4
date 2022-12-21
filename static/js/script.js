// Profile page
$(function(){
    saved = $('#saved').html();
    console.log(saved);
    posted = $('#posted').html();
    console.log(posted);
    info = $('#info').html();
    console.log(info);
    
    // if (typeof saved === 'undefined') {
    // $('#content').html(info);
    // } else {
    // $('#content').html(saved);
    // }

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
