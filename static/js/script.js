$(function () {

    // Checks if a profile page
    if (new RegExp('/profiles/.' + '*' + '/profile/').test(location.href)) {
        saved = $('#saved').html();
        posted = $('#posted').html();

        $('#content').html(saved);

        $('#btnradiosaved').click(function () {
            $('#content').html(saved);
        })
        $('#btnradioposted').click(function () {
            $('#content').html(posted);
        })
    }   
});
