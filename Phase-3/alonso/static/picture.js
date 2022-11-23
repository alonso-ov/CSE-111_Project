function change_tab(tabName) {

    // hide all tabs
    $(".tab-content").hide()
    
    // show selected tab
    $(`#${tabName}`).show()
}
