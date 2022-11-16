function search(){

    method = $('select').val()

    fetch(`http://127.0.0.1:5000/search_by/${method}`, {
            method: 'GET'
        })
        .catch((response) => {
            console.log('login request was unsuccessful')
        })
}