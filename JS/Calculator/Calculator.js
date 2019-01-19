

// let first = firstNum
// document.getElementById('first').value = firstNum;
// let second = secondNum
// document.getElementById('second').value = secondNum;

// let user = userInput
// document.getElementById('user').value = userInput;


// let Calculate = document.querySelector('#Calculate')
// Calculate.addEventListener("click", function () {

//     if (user === 'add') {
//         result = (firstNum + secondNum)
//         alert(result)
//     }
// })


// if (user == 'sub') {
//    result = (userNum - userNumTwo)
// alert(result)
// }
// if (user == 'multi') {
//    result = (userNum * userNumTwo)
// alert(result)
// }
// if (user == 'div') {
//    result = (userNum / userNumTwo)
// alert(result)
//}

const operationInput = document.querySelector('#operation');
const firstInput = document.querySelector('#first');
const secondInput = document.querySelector('#second');
const submitButton = document.querySelector('#calculate');

submitButton.addEventListener('click', function() {
    const operation = operationInput.value;
    const first = parseFloat(firstInput.value);
    const second = parseFloat(secondInput.value);
    
    if(operation === '+') {
        alert(first + second);
        
    }
    if(operation === '-') {
        alert(first - second);
        
    }
    if(operation === '*') {
        alert(first * second);
        
    }
    if(operation === '/') {
        alert(first / second);
        
    }
});

document.body.onkeydown = function(submitButton)














    



















