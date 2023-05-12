let total = 0
let number = []
let answer = []
document.querySelector('#one').addEventListener('click', one)
document.querySelector('#two').addEventListener('click', two)
document.querySelector('#three').addEventListener('click', three)
document.querySelector('#four').addEventListener('click', four)
document.querySelector('#five').addEventListener('click', five)
document.querySelector('#six').addEventListener('click', six)
document.querySelector('#seven').addEventListener('click', seven)
document.querySelector('#eight').addEventListener('click', eight)
document.querySelector('#nine').addEventListener('click', nine)
document.querySelector('#zero').addEventListener('click', zero)
document.querySelector('#plus').addEventListener('click', plus)
document.querySelector('#minus').addEventListener('click', minus)
document.querySelector('#times').addEventListener('click', times)
document.querySelector('#divide').addEventListener('click', divide)
document.querySelector('#equal').addEventListener('click', equal)
document.querySelector('#clear').addEventListener('click', clear)

function one() {
    number.push(1)
    document.querySelector('#placeToPutResult').innerText = answer.join('')+number.join('')
}

function two() {
    number.push(2)
    document.querySelector('#placeToPutResult').innerText = answer.join('')+number.join('')
}

function three() {
    number.push(3)
    document.querySelector('#placeToPutResult').innerHTML = answer.join('')+number.join('')
}

function four() {
    number.push(4)
    document.querySelector('#placeToPutResult').innerHTML = answer.join('')+number.join('')
}

function five() {
    number.push(5)
    document.querySelector('#placeToPutResult').innerHTML = answer.join('')+number.join('')
}

function six() {
    number.push(6)
    document.querySelector('#placeToPutResult').innerHTML = answer.join('')+number.join('')
}

function seven() {
    number.push(7)
    document.querySelector('#placeToPutResult').innerHTML = answer.join('')+number.join('')
}

function eight() {
    number.push(8)
    document.querySelector('#placeToPutResult').innerHTML = answer.join('')+number.join('')
}

function nine() {
    number.push(9)
    document.querySelector('#placeToPutResult').innerHTML = answer.join('')+number.join('')
}

function zero() {
    number.push(0)
    document.querySelector('#placeToPutResult').innerHTML = answer.join('')+number.join('')
}

function plus() {
    answer.push(number.join(''))
    if(answer.join('').slice(-1) !== '+')
    {
       answer.push('+') 
    }
    number = []
    document.querySelector('#placeToPutResult').innerHTML = answer.join('')+number.join('')
}

function minus() {
    answer.push(number.join(''))
    if(answer.join('').slice(-1) !== '-')
    {
       answer.push('-') 
    }
    number = []
    document.querySelector('#placeToPutResult').innerHTML = answer.join('')+number.join('')
}

function times() {
    answer.push(number.join(''))
    if(answer.join('').slice(-1) !== '*')
    {
       answer.push('*') 
    }
    number = []
    document.querySelector('#placeToPutResult').innerHTML = answer.join('')+number.join('')
}

function divide() {
    answer.push(number.join(''))
    if(answer.join('').slice(-1) !== '/')
    {
       answer.push('/') 
    }
    number = []
    document.querySelector('#placeToPutResult').innerHTML = answer.join('')+number.join('')
}

function equal() {
    answer.push(number.join(''))
    total = eval(answer.join(''))
    document.querySelector('#placeToPutResult').innerHTML = total
    number=[]
    answer=[]
    answer.push(total)
}

function clear() {
    total = 0
    number = []
    answer =[]
    document.querySelector('#placeToPutResult').innerHTML = total
}