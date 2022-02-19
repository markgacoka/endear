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