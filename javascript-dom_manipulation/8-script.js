document.addEventListener('DOMContentLoaded', function() {
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(Response => {return Response.json();})
    .then(data => {
        let helloElement = document.getElementById('hello');
        let dataHello = data.hello;
        helloElement.textContent = dataHello;
    })

    .catch(error => {
        console.error('Error fetching hello in french:', error);
    });
});