let total = 0
let stringNums = ''
document.querySelector('#clear').addEventListener('click', clearFunction)
document.querySelector('#one').addEventListener('click', addOne)
document.querySelector('#plus').addEventListener('click', add)
document.querySelector('#equals').addEventListener('click', equals)

function clearFunction() {
  stringNums = ''
  total = 0
  document.querySelector('#placeToPutResult').innerText = total
}

function addOne() {
  stringNums+='1'
  document.querySelector('#placeToPutResult').innerText = stringNums
}

function add() {
  stringNums+='+'
  document.querySelector('#placeToPutResult').innerText = stringNums
}

function equals() {
  total = eval(stringNums)
  document.querySelector('#placeToPutResult').innerText = `total: ${total}`
}
