// let globalvar = 28
// let x
// console.log(x)

// let kills = 9999

// if (kills < 1000) {
//     console.log("You are NOOB")
// }
// else if (kills <= 1500) {
//     console.log("You are HITMAN")
// }
// else {
//     console.log("You are JOHN WICK")
// }

// let day="sunday"

// switch(day) {
//     case "monday":
//         console.log("starting the week");
//         break;
//     case "monday":
//         console.log("ending the week");
//         break;
//     default:
//         console.log("just another day of the week");
// }

// let age= 16
// let status =age>=18? "adult" : "minor"

// console.log(status)  // minor

// let a=5, b="5"
// console.log(a==b)
// console.log(a===b) 
// console.log(a!=b)
// console.log(a!==b)  
// console.log(a>b)
// console.log(a<=b)  

// let single = `hello`;
// let double = "world";
// let template = `greetings, ${single} ${double}!`;
// console.log(single);
// console.log(double);
// console.log(template);


// const arr = ["1", "2", "3", "4", "5"];
// console.log(arr[0])
// arr.push("5")
// console.log(arr)
// arr.unshift("7")   
// console.log(arr)
// arr.pop()
// console.log(arr)
// arr.shift()
// console.log(arr)
// arr.splice(1, 2)
// console.log(arr)
// arr.sort()
// console.log(arr)
// arr.reverse()
// console.log(arr)
// arr.join("-")
// console.log(arr)
// arr.concat([1,2,3])
// console.log(arr)
// arr.includes("2")
// console.log(arr)
// arr.indexOf("2")
// console.log(arr)
// arr.lastIndexOf("2")
// console.log(arr)

// const arr1=["34", "45"]
// console.log(arr + arr1)


// Spread Operator

// let f1 = ["football", "basketball"]
// let f2 = ["tennis", "golf"]

// let f3 = [...f1, ...f2]
// console.log(f3)
// console.log(typeof(f3.toString()))

// Objects

// const person = {
//     name : "Ankit",
//     age : 22,
//     occupation : "StartUp"
// }
// console.log(person)
// person.salary = undefined
// console.log(person)

// const key = "age"
// const user = {
//     name : "Ashu",
//     [key] : 123
// }
// console.log(user.id)



// FUNCTIONS

// function add(a, b) {
//     return a + b
//     }
// console.log(add(5, 7))


// function read(name) {
//     console.log(`Hello ${name}, How are you?`)
// }
// read("Ankit")


// function kuchbhi(side) {
//     return (side <= 0)? ("Invalid Side :(") : (side*side)
// }
// console.log(kuchbhi(0))


// Function as a Variable:

// const createMessage = function(message, prefix = "INFO") {
//     return `[${prefix}] ${message}`
// }
// console.log(createMessage("Hello, World!", "DEBUG"))
// console.log(createMessage("Hello, World!"))

// Code for finding average of an array:

// function avg(arr) {
//     let sum = 0;
//     for (let i = 0; i < arr.length; i++) {
//         sum += arr[i];
//         }
//         const obj = {}
//         obj.sum_arr = sum
//         obj.avg_arr = sum / arr.length;
//         return obj
//     }

// let arr = [1,2,3,4,5]
// console.log(avg(arr))


// Arrow Function or CallBack Function:

// function sqr(num) {
//     return num*num
// }
// console.log(sqr(5))

// Basic Example 
// const sun = num => num*num
// console.log(sun(5))

// Intermediate Example 
// const filterEvens = numbers => numbers.filter(num => num%2 !== 0) // We are passing arrow func in inbuilt function
const numbers = [1, 2, 3, 4, 5]
// console.log(filterEvens(numbers)) // [2, 4, 6] it will return new array and not make changes in argument array
// console.log(numbers)

// const double = numbers.map(i => i*2)

// console.log(double)
// console.log(numbers)const numbers = [1, 2, 3, 4];
// const numbers = [10, 20, 30, 40;

numbers.forEach((value, index, arr) => {
  console.log(`Value: ${value*2}, Index: ${index}, Full Array: [${arr}]`);
});

// Advanced Example 

const matrix = [[1,2], [3,4], [5,6]]
const sum = matrix.reduce((acc, current) => acc.concat(curr), [])
console.log(sum) // [1,2,3,4,5,6]