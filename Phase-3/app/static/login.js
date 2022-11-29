
/*
    gather user input and send request to validate credentials
*/
function login() {

    // get user input
    username = $('#username').val()
    password =  $('#password').val()


    // send login request if both input fields are filled
    if (username == '' || password == '') {
        console.log('input fields not filled')
    } else {

        // package user input into json format
        const loginInput = {
            u_username: username,
            u_password: password
        }

        // make http request
        fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(loginInput)
        })
        .then((response) => response.json())
        .then((body) => {
            
            //client-side redirection
            window.location.href = body.redirect
        })
        .catch((response) => {
            console.log('login request was unsuccessful')
        })
    }
}

/*
    redirect to non-user browse dashboard
*/
function browse(){

    window.location.href = 'http://127.0.0.1:5000/browse'
}