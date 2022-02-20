# endear
Minerva Dating App on Heroku

Google Client ID: 254201803228-i548au48ad8oe7fkkivg0ss0at3vjahf.apps.googleusercontent.com
Google Client Secret: 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

### Attempt 1
var xhr = new XMLHttpRequest();
xhr.open("POST", '{% url 'dashboard' %}', true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.setRequestHeader("Accept", "application/json");
xhr.setRequestHeader('X-CSRFToken', token);
var request_name = person.name.replace(/(^\w{1})|(\s+\w{1})/g, letter => letter.toUpperCase());
xhr.send(JSON.stringify({"name": request_name, "email": person.email}));


### Attempt 2
var token = '{{csrf_token}}';
var request_name = person.name.replace(/(^\w{1})|(\s+\w{1})/g, letter => letter.toUpperCase());
const response = fetch('{% url 'dashboard' %}', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-CSRFToken': token
    },
    body: `{"name": ${request_name}, "email": ${person.email}}`,
    });

    response.then(data => {
        console.log(data);
});