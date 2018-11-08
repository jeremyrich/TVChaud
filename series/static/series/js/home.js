$(function() {

    $('#tv-shows-table').dataTable({
        'paging': false,
        'info': false,
        'order': [0, 'asc']
    });

    // hide the search label, which is ugly
    $('label').addClass('hide-label-class');

    // add custom style to the search field
    search_field = $('input[type="search"]');
    search_field.addClass('form-control search-tv-shows');
    search_field.attr('placeholder', 'Search...');

});