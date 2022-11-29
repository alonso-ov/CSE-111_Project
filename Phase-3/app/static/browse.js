/*
    TODO: Finish reseting table
*/
function reset_table(){
    console.log('reseting..')
    //TODO reset table when button is pressed

    $('.picture-row').remove()
}

/*
    handle search functionality
*/
function search(){

    method = $('select').val()

    user_input = $('#search-value').val()

    const search_value = {
        user_input: user_input
    }    

    fetch(`http://127.0.0.1:5000/search_by/${method}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(search_value)
        })
        .then(response => response.json())
        .then((body) =>{

            reset_table()

            pictures = body['pictures']

            pictures.forEach((item) => {
                markup = `<tr class="picture-row">
                    <td class="picture-link" id="${item[0]}">${item[1]}</td>
                    <td>${item[2]}</td>
                    <td>${item[3]}</td>
                    <td>${item[4]}</td>
                    <td>${item[5]}</td>
                </tr>`

                $("table").append(markup)
            })

            create_picture_links()
        })
}

/*
    For every picture create an animation and create a link to learn more
    about picture
*/
function create_picture_links(){

    // Animation on mouse hover
    $(".picture-link").on("mouseover", function() {
            $(this).css("background-color", "lightblue");
        }).on("mouseout", function() {
            $(this).css("background-color", "");
        });

    // Allow for redirection to picture clicked
    $(".picture-link").each((_, el) => {

            $(el).click(() => {

                picture_id = $(el).attr("id")

                // redirect to picture template
                window.location.href = `http://127.0.0.1:5000/more_info_picture/${picture_id}`
            })
        })
}