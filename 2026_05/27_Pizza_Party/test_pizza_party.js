import { getPizzasToOrder } from "./main_pizza_party.js";

/*
1. getPizzasToOrder([8, 8, 8]) should return 2.
2. getPizzasToOrder([10, 9, 8, 2, 2, 6, 10]) should return 3.
3. getPizzasToOrder([1, 2, 3, 4, 5]) should return 2.
4. getPizzasToOrder([8, 8, 8, 8, 8, 8, 8, 8]) should return 3.
5. getPizzasToOrder([9, 9, 6]) should return 1.
6. getPizzasToOrder([10, 12, 16, 9, 8, 11, 15, 8, 0]) should return 5.
*/

// Tests ------------------------------------------------------------

console.log("Test 1: --------------------------------------")
console.log(`Result: ${getPizzasToOrder([8, 8, 8])}`);
console.log("Expected: 2");

console.log("Test 2: --------------------------------------")
console.log(`Result: ${getPizzasToOrder([10, 9, 8, 2, 2, 6, 10])}`);
console.log("Expected: 3");

console.log("Test 3: --------------------------------------")
console.log(`Result: ${getPizzasToOrder([1, 2, 3, 4, 5])}`);
console.log("Expected: 2");

console.log("Test 4: --------------------------------------")
console.log(`Result: ${getPizzasToOrder([8, 8, 8, 8, 8, 8, 8, 8])}`);
console.log("Expected: 3");

console.log("Test 5: --------------------------------------")
console.log(`Result: ${getPizzasToOrder([9, 9, 6])}`);
console.log("Expected: 1");

console.log("Test 6: --------------------------------------")
console.log(`Result: ${getPizzasToOrder([10, 12, 16, 9, 8, 11, 15, 8, 0])}`);
console.log("Expected: 5");
