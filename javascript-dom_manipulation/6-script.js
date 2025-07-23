fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
.then(Response => {
    return Response.json();
})
.then(data => {
    let characterElement = document.getElementById('character');
    characterElement.textContent = data.name;
})
.catch(error => {
    console.error('Error getting the name:', error);
});