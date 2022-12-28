// Runs when page loads
$(function () {

    // Checks if viewing a profile page and ads event listeners to posed and saved toggle
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
