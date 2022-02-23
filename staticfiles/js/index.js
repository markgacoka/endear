function setList(results, token, crush_endpoint, profile){
    clearList()
    for (const person of results){
        var request_name = person.name.replace(/(^\w{1})|(\s+\w{1})/g, letter => letter.toUpperCase());
        var userForm = document.createElement('form');
        userForm.method = 'post';
        var listInput1 = document.createElement('input')
        var listInput2 = document.createElement('input')
        var listInput3 = document.createElement('input')
        listInput1.type = 'hidden';
        listInput1.name = 'name';
        listInput1.value = request_name;

        listInput2.type = 'hidden';
        listInput2.name = 'email';
        listInput2.value = person.email;

        listInput3.type = 'hidden';
        listInput3.name = 'csrfmiddlewaretoken';
        listInput3.value = token;
        
        userForm.appendChild(listInput1);
        userForm.appendChild(listInput2);
        userForm.appendChild(listInput3);

        const user_button = document.createElement('button')
        user_button.classList.add("result-card");
        user_button.onclick = function(event) {
            userForm.submit();
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

        user_button.appendChild(profileImage)
        user_button.appendChild(container)
        userForm.appendChild(user_button);
        list.appendChild(userForm)
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
    if (content.style.display === "flex") {
        content.style.display = "none";
    } else {
        content.style.display = "flex";
    }
    });
}

x = document.getElementsByClassName("tablink");
x[0].className += " red-border"

function loadCrushes(evt, newTabName, crush_length) {
    var i, x, tablinks;
    x = document.getElementsByClassName("all-tabs");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" red-border", "");
    }
    if (crush_length == 1) {
        document.getElementById(newTabName).style.display = "block";    
    } else {
        document.getElementById(newTabName).style.display = "flex";
    }
    evt.currentTarget.firstElementChild.className += " red-border";
}

const modal = document.querySelector(".modal");
const trigger = document.querySelector(".trigger");
const closeButton = document.querySelector(".close-button");

function toggleModal() {
    if (modal) {
        modal.classList.toggle("show-modal");
    } else {
        console.log('Error: modal does not exist');
    }
}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

trigger && trigger.addEventListener('click', toggleModal, false);
closeButton && closeButton.addEventListener('click', toggleModal, false);
window && window.addEventListener('click', windowOnClick, false);