function addPicture(){

    $('#add-picture-form').fadeTo(200, 1)
}

function exitForm() {
    $('#add-picture-form').fadeOut(200, 0)
}

function removePicture(picture_id){
    fetch(`http://127.0.0.1:5000/deletePicture/${picture_id}`, {
        method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then((response) => {
            if (response.status = 200) {
                //change watchlist button
                $('#removePicture').val('Deleted ✓').prop('disabled', true)
            }
        })
}