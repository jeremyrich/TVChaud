// Function to add a show to the connected user's favorites
function add_to_fav(user_id, tv_id) {

    url = '/user/ajax/add_to_favorites/';
    console.log(url);

    $.ajax({
        url: url,
        type: 'get',
        data: {'user_id': user_id, 'tv_id': tv_id},
        success: function(data) {
            console.log('added to favorites');

            // The button updates its display to either "Added to favorites" or "+ Add to favorites"
            mybutton = $('#add-fav-button');
            mybutton.html(data['button_text']);
            mybutton.removeClass();
            mybutton.addClass(data['class']);
        }
    })
};
