let clickList = document.getElementById('add_item');

clickList.addEventListener('click', function() {
    let ulElement = document.querySelector('.my_list');
    let liElement = document.createElement('li');
    liElement.textContent = 'Item';

    ulElement.appendChild(liElement);
});