$(document).ready(function () {
    // Init

    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
    });

    // Predict
    $('#btn-predict').click(function () {
        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'GET',
            url: '/robin-api/?url=https://images-na.ssl-images-amazon.com/images/I/61SwuRMAPqL._SX342_.jpg',
            cache: false,
            async: true,
            data: {
              format: 'json'
            },
            error: function(e) {
              $('#info').html('<p>' + e + '</p>');
            },
            dataType: 'jsonp',
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#result').text(' Prediction:  ' + data.category);
                console.log('Success!');
            },
        });
    });

});
