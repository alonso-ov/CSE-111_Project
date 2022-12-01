function change_tab(tabName) {

    // hide all tabs
    $(".tab-content").hide()
    
    // show selected tab
    $(`#${tabName}`).show()

    if (tabName == 'WL')
        reset_table()
}

function addToWatchlist(picture_id){

    fetch(`http://127.0.0.1:5000/addToWatchlist/${picture_id}`, {
        method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then((response) => {
            if (response.status = 201) {
                //change watchlist button
                $('#addButton').val('Added to Watchlist ✓').css({"color": "white", "background-color": "lightseagreen"}).prop('disabled', true)

            }
        })
}