// Function to send a friend request to another user
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


// Function to accept a friend request
function accept_friend_request(friend_request_id) {

    url = '/user/ajax/accept_friend_request/';
    console.log(url);

    $.ajax({
        url: url,
        type: 'get',
        data: {'friend_request_id': friend_request_id},
        success: function(data) {

            // The notification is hidden once the user has accepted or declined
            notification = $('#friend-request-' + friend_request_id);
            notification.hide();

            // The dropdown menu is reopened
            $('#button-notif-container').addClass('open');
            $('#notif-dropdown-button').attr('aria-expanded', true);
        }
    });
}


// Function to decline a friend request
function decline_friend_request(friend_request_id) {

    url = '/user/ajax/decline_friend_request/';
    console.log(url);

    $.ajax({
        url: url,
        type: 'get',
        data: {'friend_request_id': friend_request_id},
        success: function(data) {

            // The notification is hidden once the user has accepted or declined
            notification = $('#friend-request-' + friend_request_id);
            notification.hide();

            // The dropdown menu is reopened
            $('#button-notif-container').addClass('open');
            $('#notif-dropdown-button').attr('aria-expanded', true);
        }
    });
}



// Function to mark a notification as read when redirecting to the corresponding page
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


// Function to mark a notification as read or unread
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