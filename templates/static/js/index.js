function setList(results, token, crush_endpoint, profile){
    clearList()
    for (const person of results){
        const articleItem = document.createElement('button')
        articleItem.classList.add("result-card");
        articleItem.onclick = function(event) {
           
            var request_name = person.name.replace(/(^\w{1})|(\s+\w{1})/g, letter => letter.toUpperCase());
            var xhr = new XMLHttpRequest();
            xhr.open("POST", crush_endpoint, true);
            xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
            xhr.setRequestHeader('X-CSRFToken', token);
            xhr.send(`name=${request_name}&email=${person.email}`);
            modal.classList.toggle("show-modal");
            document.getElementsByClassName('crush-input')[0].value = ''
            clearList();
        }

        const profileImage = document.createElement('img');
        profileImage.src = profile
        profileImage.classList.add("result-picture");
        
        const container = document.createElement('div');
        const resultName = document.createElement('span');
        resultName.classList.add("result-name");
        name = person.name.replace(/(^\w{1})|(\s+\w{1})/g, letter => letter.toUpperCase());
        resultName.innerHTML = name
        const lineBreak = document.createElement('br');
        const resultEmail = document.createElement('span');
        resultEmail.classList.add("result-email");
        resultEmail.innerHTML = person.email

        container.appendChild(resultName)
        container.appendChild(lineBreak)
        container.appendChild(resultEmail)

        articleItem.appendChild(profileImage)
        articleItem.appendChild(container)
        list.appendChild(articleItem)
    }
    if (results.length === 0 ){
        noResults()
    }
}

function clearList(){
    while (list.firstChild){
        list.removeChild(list.firstChild)
    }
}

function noResults(){
    const error_container = document.createElement('div');
    error_container.classList.add("error-message");
    const error_text = document.createElement('span')
    error_text.classList.add("error-text");
    const text = document.createTextNode('No results found. Sorry!')
    error_text.appendChild(text)
    error_container.appendChild(error_text)
    list.appendChild(error_container)
}

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
        content.style.display = "none";
    } else {
        content.style.display = "block";
    }
    });
}

x = document.getElementsByClassName("tablink");
x[0].className += " red-border"

function loadCrushes(evt, newTabName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("all-tabs");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" red-border", "");
    }
    document.getElementById(newTabName).style.display = "block";
    evt.currentTarget.firstElementChild.className += " red-border";
}

const modal = document.querySelector(".modal");
const trigger = document.querySelector(".trigger");
const closeButton = document.querySelector(".close-button");

function toggleModal() {
    modal.classList.toggle("show-modal");
}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

trigger.addEventListener("click", toggleModal);
closeButton.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);