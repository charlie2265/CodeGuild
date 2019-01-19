console.clear();

// <div class="todo-list-item">
//   <input type="checkbox" class="todo-list-done">
//   <div class="todo-list-task">Buy Eggs for Bart</div>
//   <div class="todo-list-delete-item">×</div>
// </div>

const todoListInput = document.querySelector('#todo-list-input');
const todoListItems = document.querySelector('#todo-list-items');


function createListItem(task) {
  const listItem = document.createElement('div');
  listItem.classList.add('todo-list-item');
  
  const listDone = document.createElement('input');
  listDone.type = "checkbox";
  listDone.classList.add('todo-list-done');
  
  const listTask = document.createElement('div');
  listTask.classList.add('todo-list-task');
  listTask.innerText = task;
  
  const listDelete = document.createElement('div');
  listDelete.classList.add('todo-list-delete-item');
  listDelete.innerText = '×';
  
  listItem.appendChild(listDone);
  listItem.appendChild(listTask);
  listItem.appendChild(listDelete);
  
  // Add events...
  listDone.addEventListener('click', function(){
    if(listDone.checked){
    listTask.style.textDecoration = "line-through";
    }
      else{
        listTask.style.textDecoration = "none";
      
      
    }
   })
 
  listDelete.addEventListener('click',function(){
    todoListItems.removeChild(listItem);
    
  })
  
  return listItem;
}

todoListInput.addEventListener('keydown', function(event) {
  if(event.key === 'Enter') {
    todoListItems.appendChild(
      createListItem(todoListInput.value)
    )
    todoListInput.value = '';
  } 
});

