// Function to remove a show from the favorites of the connected user
function remove_from_fav(user_id, tv_id) {

    url = '/user/ajax/remove_from_favorites/';

    $.ajax({
        url:url,
        type: 'get',
        data: {'user_id': user_id, 'tv_id': tv_id},
        success: function(data) {
            console.log('removed from favorites');

            // The removed favorite is hidden
            favorite = $('#' + tv_id);
            favorite.hide();

            // The page title is updated with the new number of favorites
            new_title = "Favorites - " + data['num_favorites'] + " show"
            if (data['num_favorites'] != 1) {
                new_title += "s";
            }
            $('#favorites_title').text(new_title);
        },
    });
};
