var x = prompt("")
x = x.toLowerCase() 
x = x.charAt(0).toUpperCase() + x.slice(1,5) + x.charAt(5).toUpperCase() + x.slice(6)
console.log("Hello, " + x)