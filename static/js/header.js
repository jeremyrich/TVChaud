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
    })
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
    })
}