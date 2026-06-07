// freecodecamp
// Daily Coding Challenges
// Day 290 (2026-05-27)
// Pizza Party

/*
Given an array of hours worked today per person, return the number of pizzas to order for a pizza party.

    Divide each person's hours worked by 3 to get their slice count.
    You can't eat a partial slice, so round each person's slice count up to the nearest whole number.
    Each person gets a minimum of two slices.
    Each pizza has 8 slices. Round the total number of pizzas up to the nearest whole pizza.
*/

export function getPizzasToOrder(hoursWorked) {
    let pizzasToOrder = 0
    let sumPizzaSlices = 0

    for (let i in hoursWorked) {
        let hours = hoursWorked[i]
        let pizzaSlices = Math.ceil(hours / 3)

        if (pizzaSlices < 2) {
            pizzaSlices = 2
        } 

        sumPizzaSlices += pizzaSlices
    }

    pizzasToOrder = Math.ceil(sumPizzaSlices / 8)

    return pizzasToOrder;
}
