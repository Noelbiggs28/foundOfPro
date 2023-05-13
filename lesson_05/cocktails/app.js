fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita')
    .then(res => res.json()) // parse response as JSON
    .then(data => {
      document.querySelector('#name').innerText = data.drinks[0].strDrink
      document.querySelector('#instruct').innerText = data.drinks[0].strInstructions
      document.querySelector('img').src = data.drinks[0].strDrinkThumb
    })
    .catch(err => {
        console.log(`error ${err}`)
    });
    
    document.querySelector('button').addEventListener('click',getCocktail)

    function getCocktail(){
      let userInput=document.querySelector('input').value
      fetch('https://www.thecocktaildb.com/api/json/v1/1/search.php?s='+userInput)
      .then(res => res.json()) // parse response as JSON
      .then(data => {
        document.querySelector('#name').innerText = data.drinks[0].strDrink
        document.querySelector('#instruct').innerText = data.drinks[0].strInstructions
        document.querySelector('img').src = data.drinks[0].strDrinkThumb
      })
      .catch(err => {
          console.log(`error ${err}`)
      });
    }
