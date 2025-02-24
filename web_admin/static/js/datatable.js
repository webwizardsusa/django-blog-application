function initializeDataTable(tableId, ajaxUrl, columns, additionalData) {
    $(tableId).DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": ajaxUrl,
            "type": "GET",
            "data": function(data) {
                return $.extend({}, data, additionalData);
            }
        },
        "columns": columns,
        "pageLength": 10,
        "lengthMenu": [10, 25, 50, 100],
        "order": [[5, "desc"]]  
    });
}