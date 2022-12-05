function register() {

    // get user input
    username = $('#username').val()
    password =  $('#password').val()
    email =  $('#email').val()
    firstname =  $('#firstname').val()
    lastname = $('#lastname').val()
    preferredstreamsite = $('#preferedstreamsite').val()

    // send request for input fields to be filled
    if (username == '' || password == '' || email == '' || firstname == '' || lastname == '' || preferredstreamsite == '') {
        console.log('input fields not filled')
    } else {

        // package user input into json format
        const registerInput = {
            u_username: username,
            u_password: password,
            u_email: email,
            u_firstname: firstname,
            u_lastname: lastname,
            u_preferredstreamsite: preferredstreamsite
        }

        // make http request
        fetch('http://127.0.0.1:5000/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(registerInput)
        })
        .then((response) => response.json())
        .then((body) => {
            
            //client-side redirection
            window.location.href = body.redirect
        })
        .catch((response) => {
            console.log('register request was unsuccessful')
        })
    }
}

/*
    redirect to log-in
*/
function login_page(){
    window.location.href = 'http://127.0.0.1:5000/'
}
