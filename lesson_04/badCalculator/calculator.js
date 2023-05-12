let total = 0
let number = []
document.querySelector('#one').addEventListener('click', One)
document.querySelector('#two').addEventListener('click', Two)
document.querySelector('#three').addEventListener('click', Three)
document.querySelector('#cantThinkOfAnything').addEventListener('click', sub2)

function One() {
  total = total + 1
  document.querySelector('#placeToPutResult').innerText = total
}

function Two() {
  total = total + 3
  document.querySelector('#placeToPutResult').innerText = total
}

function Three() {
  total = total + 9
  document.querySelector('#placeToPutResult').innerHTML = total
}

function sub2() {
  total = total - 2
  document.querySelector('#placeToPutResult').innerHTML = total
}
