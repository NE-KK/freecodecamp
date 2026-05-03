/*
freecodecamp
Daily Coding Challenges
Day 1 (2025-08-11)
Vowel Balance

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

const vowelList = ["A", "a","E", "e","I", "i","O", "o","U", "u",]


function countVowels(text) {
    let len = text.length;
    let vowelLen = vowelList.length;
    let vowelCount = 0;
    
    for (i=0; i < len; i++) {
        for (j=0; j < vowelLen; j++) {
            if (text[i] === vowelList[j] ) {
                vowelCount++;
            }
        }
    }

    return vowelCount;
}


function sliceText(text) {
    console.log(text);
}

function getResult(count1, count2) {
    let result = false;
    
    if (count1 === count2) {
        result = true;
    }

    return result;
}

function isBalanced(text) {
    let textLength = text.length;
    let halfTextLength = Math.floor(text.length / 2);
    
    let textPart1 = text.substr(0, halfTextLength);
    let textPart2 = "";
    
    if (textLength % 2 === 0) {
        textPart2 = text.substr(halfTextLength);
    }
    else {
        textPart2 = text.substr(halfTextLength + 1);
    }

    let vowelCount1 = countVowels(textPart1);
    let vowelCount2 = countVowels(textPart2);

    let result = getResult(vowelCount1, vowelCount2)

    return result;
}


console.log(isBalanced("racecar"))
console.log(isBalanced("raccar"))
console.log(isBalanced("Lorem Ipsum"))
console.log(isBalanced("string"))