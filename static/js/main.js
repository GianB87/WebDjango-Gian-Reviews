// get search form and page links
// let searchForm = document.getElementById('searchForm')
let searchForm = document.getElementById('searchForm2')
let pageLinks = document.querySelectorAll('a[data-page]');
// ensure search form exist
for (let i = 0;pageLinks.length > i; i++){
    pageLinks[i].addEventListener('click', function (e) {
        e.preventDefault()
        // get data attribute
        let page = this.dataset.page
        // add hidden search input to form
        searchForm.innerHTML += `<input value="${page}" name="page" hidden>`
        searchForm.submit()
    })
}

$(document).on('submit','#loginForm', function(e) {
    e.preventDefault();
    let username = $('#username').val()
    let password = $('#password').val()

$.ajax({
    type: 'POST',
    url: '/login/',
    data:{
        username:username,
        password: password,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    },
        success:function(response){
            if(response=='Reload'){
                location.reload()
            }else{
                document.getElementById('loginfail').removeAttribute('hidden')
                $('#loginfail').html('<i class="fa fa-times-circle"></i>  '+response)
            }
        
    }
});
});

$(function() {
 
    if (localStorage.chkbx && localStorage.chkbx != '') {
        $('#remember_me').attr('checked', 'checked');
        $('#xip_Name').val(localStorage.usrname);
        $('#xip_Password').val(localStorage.pass);
    } else {
        $('#remember_me').removeAttr('checked');
        $('#xip_Name').val('');
        $('#xip_Password').val('');
    }

    $('#remember_me').click(function() {

        if ($('#remember_me').is(':checked')) {
            // save username and password
            localStorage.usrname = $('#xip_Name').val();
            localStorage.pass = $('#xip_Password').val();
            localStorage.chkbx = $('#remember_me').val();
        } else {
            localStorage.usrname = '';
            localStorage.pass = '';
            localStorage.chkbx = '';
        }
    });
});