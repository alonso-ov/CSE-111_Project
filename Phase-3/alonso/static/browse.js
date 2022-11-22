function search(){

    method = $('select').val()

    fetch(`http://127.0.0.1:5000/search_by/${method}`, {
            method: 'GET'
        })
        .then(response => response.json())
        .then((body) =>{
            pictures = body['pictures']

            pictures.forEach((item) => {
                markup = `<tr>
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

function reset_table(){
    console.log('reseting..')
    //TODO reset table when button is pressed
}

function create_picture_links(){
    $(".picture-link").on("mouseover", function() {
            $(this).css("background-color", "lightblue");
        }).on("mouseout", function() {
            $(this).css("background-color", "");
        });

    $(".picture-link").each((_, el) => {

            $(el).click(() => {
                picture_id = $(el).attr("id")

                window.location.href = `http://127.0.0.1:5000/more_info_picture/${picture_id}`
            })
        })
}