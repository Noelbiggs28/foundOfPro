document.querySelector('button').addEventListener('click', getFetch)

async function getFetch() {
    const choice = document.querySelector('input').value
    const url = 'https://pokeapi.co/api/v2/pokemon/'+choice

    let data = await fetch(url)
    let pokemonInfo = await data.json()
    document.querySelector('#name').innerText = data.name
    document.querySelector('#type').innerText = data.drinks[0].strInstructions
    document.querySelector('img').src = data.drinks[0].strDrinkThumb
    console.log(pokemonInfo)
}