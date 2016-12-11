/**
 * Created by yang on 10/12/16.
 */

$(document).ready(function() {
    $('#calculate_form').submit(function (event) {
        event.preventDefault();
        $.ajax({
            url: 'http://localhost:8080/',
            type: 'POST',
            data: $('#calculate_form').serialize(),
            success: function (event) {

                $('#calc_result').text('Result is: '+ event.result);
                console.log('form submitted.');

            }
        });
        return false;
    });
});

// action="http://localhost:8080/" method="post"