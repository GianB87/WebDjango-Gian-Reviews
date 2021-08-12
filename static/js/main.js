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
