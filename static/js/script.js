
$(function () {

    // Checks if a profile page
    if (new RegExp('/profiles/.' + '*' + '/profile/').test(location.href)) {
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
    }
});

const mediaQuery = window.matchMedia('(min-width: 768px)')
if (mediaQuery.matches) {
    // Then trigger an alert
    console.log('Media Query Matched!')
  } else {
    console.log(mediaQuery)
  }


  if (new RegExp('/profiles/.' + '*' + '/profile/').test(location.href)) {
    
  }