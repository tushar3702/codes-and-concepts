// Example of Rest and Spread Operators in ES6

// -------------------------
// Rest Operator (Functions)
// -------------------------
function add(a, b, c, ...others) {
    console.log("Extra arguments (rest):", others);
    return a + b + c;
}

const result = add(2, 5, 6, 5, 43);
console.log("Sum of first three:", result);

// -------------------------
// Spread Operator (Arrays)
// -------------------------
const names = ['tushar', 'anuj', 'vivek'];

function getNames(name1, name2, name3) {
    console.log("Names:", name1, name2, name3);
}

// Without spread
getNames(names[0], names[1], names[2]);

// With spread
getNames(...names);

// -------------------------
// Rest with Objects (Destructuring)
// -------------------------
const student = {
    name: 'Ajay',
    age: 28,
    hobbies: ['Cricket', 'Reading']
};

const { name, age } = student;
console.log("Student details:", name, age);

// -------------------------
// Spread with Objects
// -------------------------
const newStudent = {
    ...student,   // clone all properties
    age: 29       // override age
};

console.log("Updated student:", newStudent);
