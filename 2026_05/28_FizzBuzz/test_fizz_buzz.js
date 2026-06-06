import { fizzBuzzCount } from './main_fizz_buzz.js'

/*
1. fizz_buzz_count(1, 11) should return {"fizz": 3, "buzz": 2}.
2. fizz_buzz_count(14, 41) should return {"fizz": 9, "buzz": 6}.
3. fizz_buzz_count(24, 100) should return {"fizz": 26, "buzz": 16}.
4. fizz_buzz_count(-635, -14) should return {"fizz": 207, "buzz": 125}.
5. fizz_buzz_count(-5432, 6789) should return {"fizz": 4074, "buzz": 2444}.
*/


console.log("Test 1: ------------------------")
console.log(fizzBuzzCount(1, 11))
console.log(`Erwartet: {fizz: 3, buzz: 2}`)

console.log("Test 2: ------------------------")
console.log(fizzBuzzCount(14, 41))
console.log(`Erwartet: {fizz: 9, buzz: 6}`)

console.log("Test 3: ------------------------")
console.log(fizzBuzzCount(24, 100))
console.log(`Erwartet: {fizz: 26, buzz: 16}`)

console.log("Test 4: ------------------------")
console.log(fizzBuzzCount(-635, -14))
console.log(`Erwartet: {fizz: 207, buzz: 125}`)

console.log("Test 5: ------------------------")
console.log(fizzBuzzCount(-5432, 6789))
console.log(`Erwartet: {fizz: 4074, buzz: 2444}`)
