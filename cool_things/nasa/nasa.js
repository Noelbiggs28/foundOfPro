
fetch("https://api.nasa.gov/planetary/apod?api_key=eHan37z6O7R11DB3p8LXp9SGKN5PhvJ7lAHqvvFY")
    .then(res => res.json())
    .then(data => {
        document.querySelector("#title").innerHTML = data.title;
        document.querySelector("#date").innerHTML = data.date;
        document.querySelector("#url").src = data.url;
        document.querySelector("#explanation").innerHTML = data.explanation;
    })
    .catch(err=> {
        console.log('error ${err}')
    })

    document.querySelector('#newbutton').addEventListener('click', newphoto)

    function newphoto(){
        let newdate = document.querySelector("#newdate").value
        fetch("https://api.nasa.gov/planetary/apod?api_key=eHan37z6O7R11DB3p8LXp9SGKN5PhvJ7lAHqvvFY&date="+newdate)
        .then(res => res.json())
        .then(data => {
        document.querySelector("#title").innerHTML = data.title;
        document.querySelector("#date").innerHTML = data.date;
        document.querySelector("#url").src = data.url;
        document.querySelector("#explanation").innerHTML = data.explanation;
        })
        .catch(err=> {
        console.log('error ${err}')
        })
    }
