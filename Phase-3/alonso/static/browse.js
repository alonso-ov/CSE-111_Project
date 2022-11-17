function search(){

    method = $('select').val()

    fetch(`http://127.0.0.1:5000/search_by/${method}`, {
            method: 'GET'
        })
        .then(response => response.json())
        .then((body) =>{
            pictures = body['pictures']

            pictures.forEach((item) => {
                markup = `<tr><td>${item[0]}</td><td>${item[1]}</td><td>${item[2]}</td><td>${item[3]}</td><td>${item[4]}</td></tr>`
                $("table").append(markup)
            })
        })
        .catch((response) => {
            console.log('search request was unsuccessful')
        })
}

function reset_table(){
    console.log('reseting..')
    //TODO reset table when button is pressed
}