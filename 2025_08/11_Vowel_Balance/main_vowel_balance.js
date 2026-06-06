/*
freecodecamp
Daily Coding Challenges
Day 1 (2025-08-11)
Vowel Balance
*/

const vowelList = ["A", "a","E", "e","I", "i","O", "o","U", "u"]


function countVowels(text) {
    let len = text.length;
    let vowelLen = vowelList.length;
    let vowelCount = 0;
    
    for (let i=0; i < len; i++) {
        for (let j=0; j < vowelLen; j++) {
            if (text[i] === vowelList[j] ) {
                vowelCount++;
            }
        }
    }

    return vowelCount;
}


function getResult(count1, count2) {
    let result = false;
    
    if (count1 === count2) {
        result = true;
    }

    return result;
}

export function isBalanced(text) {
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
