const button = document.querySelector('button');

button.addEventListener('click', function(){

const element = document.createElement('p');
element.innerHTML = '<p> STUFF <p>'
document.body.appendChild(element);
});
