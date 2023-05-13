document.querySelector('#check').addEventListener('click', checkDay)

function checkDay() {
  
  const day = document.querySelector('#day').value

  // logic goes here
  lcDay = day.toLowerCase()
  let week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
  let weekend = ['saturday', 'sunday']
  for (let i = 0; i < 5; i++){
    if(lcDay === week[i]){
      document.querySelector('#placeToSee').innerHTML = "weekday"
      return
    }
  }
  for (let i = 0; i < 2; i++){
    if(lcDay === weekend[i]){
      document.querySelector('#placeToSee').innerHTML = "weekend"
      return
    }
  }
  document.querySelector('#placeToSee').innerHTML = "invalid date"
}
