$(function() {
    // Click-handler for the refresh-link
    $('.captcha-refresh').click(function(){
        var form = $(this).parents('form');

        $.ajax({
            url: form.attr("captcha-refresh-url"),
            dataType: 'json',
            success: function (data) {
                form.find('input[name="captcha_0"]').val(data.key);
                form.find('img.captcha').attr('src', data.image_url);
            }
        });

        return false;
    });
});
