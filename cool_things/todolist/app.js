
console.log('connected')

document.querySelector('button').addEventListener('click', addItem)

const unorderedList = document.querySelector('ul')



function addItem(){
    let userInputTodo = document.querySelector('input').value
    let newTodo = document.createElement('li')
    newTodo.innerHTML = userInputTodo
    
    let deleteButton = document.createElement('button')
    deleteButton.innerText = 'Delete'
    deleteButton.addEventListener('click', () => {
        let listItem = deleteButton.parentNode
        listItem.parentNode.removeChild(listItem)
    })

    let doneButton = document.createElement('button')
    doneButton.innerText = 'Done'
    doneButton.addEventListener('click', () => {
        let listItem = doneButton.parentNode
        listItem.style['background'] = 'green'
        listItem.style['color'] = 'white'
    })


    newTodo.appendChild(doneButton)
    newTodo.appendChild(deleteButton)
    unorderedList.appendChild(newTodo)
    console.log(userInputTodo)
}

