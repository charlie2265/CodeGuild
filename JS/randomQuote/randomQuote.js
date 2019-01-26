console.clear()

const quote = document.querySelector('#quote')
const quotee = document.querySelector('quotee')

axios.get('https://favqs.com/api/qotd')
.then(function(response){
  const data = response.data.quote
  
  quote.innerText = data.body
  quotee.innerText = data.author
  console.log(response)
})