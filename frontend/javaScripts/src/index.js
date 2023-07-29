console.log('Hello World')
console.log('Hello Rafik')
//alert('Hello Rafik')
//confirm('Hello Rafik')
// prompt('Hello Rafik')
// document.write('Hello Rafik')
// document.getElementById('root').innerHTML = 'Hello Rafik'


document.getElementById("btn").onclick = function () {

    let name=document.getElementById("name").value;
    console.log(name)
    document.getElementById('label1').innerHTML=name;
}

