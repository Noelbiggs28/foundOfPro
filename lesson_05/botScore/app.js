localStorage.setItem('count', 0)

let points = localStorage.getItem('count')
document.querySelector('#show').innerText = points
document.querySelector('#addOne').addEventListener('click',addOne)
document.querySelector('#subOne').addEventListener('click',subOne)
document.querySelector('#zero').addEventListener('click',zero)

function addOne(){
    points++
    localStorage.setItem('count', points)
    document.querySelector('#show').innerText = points
}

function subOne(){
    points--
    localStorage.setItem('count',points)
    document.querySelector('#show').innerText = points
}

function zero(){
    points = 0
    localStorage.setItem('count', points)
    document.querySelector('#show').innerText = points
}