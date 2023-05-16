document.querySelector('button').addEventListener('click', getFetch)

async function getFetch() {
    const url = 'https://apod.nasa.gov/apod/'
    let data = await fetch(url)
    let photo = await data.json()
    console.log(photo)

    document.querySelector('img').src = photo

}