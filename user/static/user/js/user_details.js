// Fonction pour enlever une série des favoris du user connecté
function remove_from_fav(user_id, tv_id) {

    url = '/user/ajax/remove_from_favorites/';

    $.ajax({
        url:url,
        type: 'get',
        data: {'user_id': user_id, 'tv_id': tv_id},
        success: function(data) {
            console.log('removed from favorites');

            //Hide the removed favorite
            favorite = $('#' + tv_id)
            favorite.hide()

            //Change page title to update with new number of favorites
            new_title = "Favorites - " + data['num_favorites'] + " show"
            if (data['num_favorites'] != 1) {new_title += "s"}
            $('#favorites_title').text(new_title)
        },
    })
};
