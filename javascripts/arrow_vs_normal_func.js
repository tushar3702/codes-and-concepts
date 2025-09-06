// ------------------------------
// 1. Syntax
// Normal function
function add(a, b) {
  return a + b;
}

// Arrow function
const addArrow = (a, b) => a + b;

console.log("Normal add:", add(2, 3));      // 5
console.log("Arrow add:", addArrow(2, 3));  // 5


// ------------------------------
// 2. 'this' Binding
const obj = {
  value: 10,
  normalFunc: function () {
    console.log("Normal function this.value:", this.value); // 10
  },
  arrowFunc: () => {
    console.log("Arrow function this.value:", this.value); // undefined
  }
};

obj.normalFunc();
obj.arrowFunc();


// ------------------------------
// 3. 'arguments' Object
function normalArgs(a, b) {
  console.log("Normal function arguments:", arguments); 
}
const arrowArgs = (a, b) => {
  // console.log(arguments); // ❌ ReferenceError: arguments is not defined
  console.log("Arrow function needs rest operator:", a, b);
};

normalArgs(1, 2);
arrowArgs(1, 2);

// ------------------------------
// 4. Methods in Objects
// ------------------------------
const user = {
  name: "Tushar",
  normalMethod: function () {
    console.log("Normal method:", this.name); // "Tushar"
  },
  arrowMethod: () => {
    console.log("Arrow method:", this.name); // undefined
  }
};

user.normalMethod();
user.arrowMethod();

// ------------------------------
// 5. Implicit Return
function square(n) {
  return n * n;
}
const squareArrow = n => n * n; // implicit return

console.log("Normal square:", square(4));       // 16
console.log("Arrow square:", squareArrow(4));   // 16
