export default function Post(data){
  console.log("wow")
    console.log(JSON.stringify(data));
    console.log("wow")
    fetch('http://localhost/echo', {
      method: "POST",
      body: JSON.stringify(data),
      headers: {"Content-type": "application/json; charset=UTF-8"}
      // "Origin": "http:/localhost:3000",
      // "Access-Control-Request-Method": "POST",
      // "Access-Control-Request-Headers": {"Content-type": "application/json; charset=UTF-8"}
  })
.then(response => {
  console.log("owo");
  if(response.ok){return response.json();}
  throw response;
}) 
.then(json => console.log(json))
.catch(err => console.log(err));
}