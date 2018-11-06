// Fonction pour envoyer une friend request sur l'application
function send_friend_request() {

    to_username = $('#friend-username-id').val();

    url = '/user/ajax/send_friend_request/';
    console.log(url);

    $.ajax({
        url: url,
        type: 'get',
        data: {'to_username': to_username},
        success: function(data) {

            dropdown = $('#dropdown-add-friend');
            current_html = dropdown.html();

            if(!data['valid_username']) {
                // If the username is invalid, display an error message
                htmltext = '<div style="text-align:center; color: red" class="col-xs-12">Username invalid</div>' + current_html;
                dropdown.html(htmltext);
            } else {
                // Else clean the field
                dropdown.html(current_html);
            };

            $('#button-add-friend-container').addClass('open');
            $('#add-friend-dropdown-button').attr('aria-expanded', true);
        }
    });
}


// Fonction pour accepter une friend request
function accept_friend_request(friend_request_id) {

    url = '/user/ajax/accept_friend_request/';
    console.log(url);

    $.ajax({
        url: url,
        type: 'get',
        data: {'friend_request_id': friend_request_id},
        success: function(data) {

            $('#friend-request-'.friend_request_id).remove();
            
            $('#button-notif-container').addClass('open');
            $('#notif-dropdown-button').attr('aria-expanded', true);
        }
    });
}


// Fonction qui refuse une friend request
function decline_friend_request(friend_request_id) {

    url = '/user/ajax/decline_friend_request/';
    console.log(url);

    $.ajax({
        url: url,
        type: 'get',
        data: {'friend_request_id': friend_request_id},
        success: function(data) {

            $('#friend-request-'.friend_request_id).remove();
            
            $('#button-notif-container').addClass('open');
            $('#notif-dropdown-button').attr('aria-expanded', true);
        }
    });
}



// Fonction pour cocher la notif comme lue au moment de la redirection vers la page correspondante
function see_notif(notif_id) {

    url = '/series/ajax/see_notif/';
    console.log(url);

    $.ajax({
        url: url,
        type: 'get',
        data: {'notif_id': notif_id},
        success: function(data) {
            console.log('notif ' + data['notif_id'] + ' redirect');
        }
    });
};


// Fonction pour check une notif comem lue ou non lue
function check_notif(notif_id) {
    
    url = '/series/ajax/check_notif/';
    console.log(url);

    $.ajax({
        url: url,
        type: 'get',
        data: {'notif_id': notif_id},
        success: function(data) {

            console.log('notif ' + data['notif_id'] + ' checked');
            notif_frame = $('#notif-' + data['notif_id']);

            if(notif_frame.hasClass('notif-message-alert')) {
                notif_frame.removeClass('notif-message-alert');
                notif_frame.addClass('notif-message-no-alert');
            } else {
                notif_frame.removeClass('notif-message-no-alert');
                notif_frame.addClass('notif-message-alert');
            }

            $('#button-notif-container').addClass('open');
            $('#notif-dropdown-button').attr('aria-expanded', true);
            
        }
    });
}