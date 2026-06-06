import  { isBalanced }  from "./main_vowel_balance.js";

/*
Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.
Vowels are: a, A, e, E, i, I, o, O, u, U
If there's an odd number of characters in the string, ignore the center character.
examples:
    1. is_balanced("racecar") should return True.
    2. is_balanced("Lorem Ipsum") should return True.
    3. is_balanced("Kitty Ipsum") should return False.
    4. is_balanced("string") should return False.
    5. is_balanced(" ") should return True.
    6. is_balanced("abcdefghijklmnopqrstuvwxyz") should return False.
    7. is_balanced("123A#b!E&*456-o.U") should return True.
*/

// --------------------------------------------------------------------------------------
// Test cases

let test_1 = String(isBalanced("racecar"))
let test_2 = String(isBalanced("Lorem Ipsum"))
let test_3 = String(isBalanced("Kitty Ipsum"))
let test_4 = String(isBalanced("string")) 
let test_5 = String(isBalanced(" "))
let test_6 = String(isBalanced("abcdefghijklmnopqrstuvwxyz"))
let test_7 = String(isBalanced("123A#b!E&*456-o.U"))

console.log(`Test 1: \n Ergebnis: ${test_1} \n Erwartet: true \n -------------------`)
console.log(`Test 2: \n Ergebnis: ${test_2} \n Erwartet: true \n -------------------`)
console.log(`Test 3: \n Ergebnis: ${test_3} \n Erwartet: false \n -------------------`)
console.log(`Test 4: \n Ergebnis: ${test_4} \n Erwartet: false \n -------------------`)
console.log(`Test 5: \n Ergebnis: ${test_5} \n Erwartet: true \n -------------------`)
console.log(`Test 6: \n Ergebnis: ${test_6} \n Erwartet: false \n -------------------`)
console.log(`Test 7: \n Ergebnis: ${test_7} \n Erwartet: true \n -------------------`)

// --------------------------------------------------------------------------------------
