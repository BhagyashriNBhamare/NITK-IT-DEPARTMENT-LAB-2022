var times = [];
function add(time) 
{
    times.push(time);  
    window.alert("added")
    window.alert(time);
}
function displayUserName()
{

for(var i = 0; i < times.length; i++) {
    document.getElementById("printarray").innerHTML += times[i] + "<br>";
    window.alert(times[i]);
}
}
