#include <iostream>
#include <string>
using namespace std;

/*
  ============================================
  C++ Functions & Memory Concepts Cheat Sheet
  ============================================
  Topics Covered:
  1. Function Overloading
  2. Default Arguments
  3. Inline Functions
  4. Recursion
  5. Pass by Value vs Reference
  6. Dynamic Memory Allocation (new, delete, malloc, free)
  7. Memory Leaks & Management
  8. Stack vs Heap
*/

//////////////////////////
// 1. Function Overloading
//////////////////////////
void print(int x) { 
    cout << "Integer: " << x << endl; 
}

void print(double x) { 
    cout << "Double: " << x << endl; 
}

void print(string s) { 
    cout << "String: " << s << endl; 
}

//////////////////////////
// 2. Default Arguments
//////////////////////////
void greet(string name = "User") {
    cout << "Hello, " << name << "!" << endl;
}

//////////////////////////
// 3. Inline Function
//////////////////////////
inline int square(int x) {
    return x * x;
}

//////////////////////////
// 4. Recursion
//////////////////////////
int factorial(int n) {
    if(n <= 1) return 1; // Base case
    return n * factorial(n - 1);
}

//////////////////////////
// 5. Pass by Value vs Reference
//////////////////////////
void addOneByValue(int x) { // Value: original variable not changed
    x++;
}
2
void addOneByReference(int &x) { // Reference: original variable changes
    x++;
}

//////////////////////////
// 6. Dynamic Memory Allocation
//////////////////////////
void dynamicMemoryDemo() {
    // Single variable
    int* ptr = new int; 
    *ptr = 10;
    cout << "Dynamic int value: " << *ptr << endl;
    delete ptr; // free memory

    // Array
    int* arr = new int[5];
    for(int i = 0; i < 5; i++) arr[i] = i + 1;

    cout << "Dynamic array values: ";
    for(int i = 0; i < 5; i++) cout << arr[i] << " ";
    cout << endl;
    delete[] arr; // free array
}

//////////////////////////
// 7 & 8. Memory Management + Stack vs Heap
//////////////////////////
void stackVsHeapDemo() {
    int stackVar = 100;          // Stored in stack
    int* heapVar = new int(200); // Stored in heap

    cout << "Stack variable: " << stackVar << endl;
    cout << "Heap variable: " << *heapVar << endl;

    delete heapVar; // Always free heap memory to avoid leaks
}

//////////////////////////
// Main Function to Demo All
//////////////////////////
int main() {
    cout << "=== Function Overloading ===" << endl;
    print(5);
    print(3.14);
    print("Hello");

    cout << "\n=== Default Arguments ===" << endl;
    greet();
    greet("Tushar");

    cout << "\n=== Inline Function ===" << endl;
    cout << "Square of 5: " << square(5) << endl;

    cout << "\n=== Recursion ===" << endl;
    cout << "Factorial of 5: " << factorial(5) << endl;

    cout << "\n=== Pass by Value vs Reference ===" << endl;
    int a = 5;
    addOneByValue(a);
    cout << "After addOneByValue: " << a << endl; // 5
    addOneByReference(a);
    cout << "After addOneByReference: " << a << endl; // 6

    cout << "\n=== Dynamic Memory Allocation ===" << endl;
    dynamicMemoryDemo();

    cout << "\n=== Stack vs Heap Demo ===" << endl;
    stackVsHeapDemo();

    return 0;
}


