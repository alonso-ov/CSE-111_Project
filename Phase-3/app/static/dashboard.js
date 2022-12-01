var picture_id

function editWatchlistPicture(picture_id){

    $('#edit-form').fadeTo(200, 1)

    this.picture_id = picture_id
}

function exitForm() {
    $('#edit-form').fadeOut(200, 0)
}

function editWatchlist() {
    watchstatus = $('#watchstatus').val()
    completitiondate = $('#completitiondate').val()

    if (completitiondate == '') {
        completitiondate = 'NA'
    }

    const package = {
        watchstatus: watchstatus,
        completitiondate: completitiondate
    }

    fetch(`http://127.0.0.1:5000/editWatchlist/${picture_id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(package)
        })
        .then(() => {
            window.location.reload();
        })
}