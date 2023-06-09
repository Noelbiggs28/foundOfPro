document.querySelector('button').addEventListener('click', getFetch)

async function getFetch() {
    const choice = document.querySelector('input').value
    const url = 'https://pokeapi.co/api/v2/pokemon/'+choice
    const isShiny = document.querySelector('input[id="shiny"]:checked')

    let data = await fetch(url)
    let pokemonInfo = await data.json()
    console.log(pokemonInfo)
    document.querySelector('#name').innerText = pokemonInfo.species.name
    let amount = pokemonInfo.types.length
    let arr=[]
    for (let i = 0; i < amount; i++){
        arr.push(pokemonInfo.types[i].type.name)
    }
    string = arr.join(' + ')
    document.querySelector('#type').innerText = string
    if(isShiny){
        document.querySelector('img').src = pokemonInfo.sprites.front_shiny
    }
    else{
        document.querySelector('img').src = pokemonInfo.sprites.front_default
    }
}