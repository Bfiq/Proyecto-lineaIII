$(document).ready(function() {
    $(document).on('click', '.edit', function() {
        var studentCode = $('#studentCode').text()

        $('.studentCode').val(studentCode)
    })
})