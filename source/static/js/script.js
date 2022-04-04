document.getElementById("quote-form").addEventListener("submit", createQuote);

function showForm() {
    document.getElementById("form-container").style.display = 'block';
    document.getElementById("quotes-container").style.display = 'none';
}

function hideForm() {
    document.getElementById("form-container").style.display = 'none';
    document.getElementById("quotes-container").style.display = 'block';
}

function createQuote(e) {
    e.preventDefault();
    let url = e.target.action;
    let method = e.target.method;
    let data = new FormData(e.target);
    let token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let headers = {'X-Csrftoken': token};
    fetch(url, {method: method, body: data, headers: headers})
        .then(res => res.json())
        .then(res => {
            console.log(res);
            hideForm();
        });
}