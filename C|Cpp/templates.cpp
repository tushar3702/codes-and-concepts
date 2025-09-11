/*
    Title: Function & Class Templates in C++
    Description:
    --------------------------------------------
    This program demonstrates:
    1. A generic function template `big` that compares 
       two values of possibly different types and returns 
       the bigger one.
    2. A class template `Array` that implements a fixed-size 
       array with basic insert and get operations.

    Concepts covered:
    - Function templates with type deduction
    - Class templates with generic data types
    - Encapsulation with private members and public methods
*/

#include <iostream>
using namespace std;

// -------------------------------
// Function Template
// -------------------------------
// Compares two values (of possibly different types)
// and returns the bigger one.
template <typename X, typename Y>
auto big(X a, Y b) {
    return (a > b) ? a : b;
}

// -------------------------------
// Class Template
// -------------------------------
// Generic Array class that stores up to 10 elements of type Z.
// Provides insert() to store values at an index
// and getVal() to retrieve values safely.
template <class Z>
class Array {
private:
    Z arr[10];   // fixed-size array
    int size;    // capacity of array
public:
    // Constructor
    Array() {
        size = 10;
    }

    // Insert a value at a given index
    void insert(Z val, int index) {
        if (index >= 0 && index < size) {
            arr[index] = val;
        }
    }

    // Get value at a given index (default if invalid)
    Z getVal(int index) {
        if (index >= 0 && index < size) {
            return arr[index];
        }
        return Z(); // default constructed value
    }
};

// -------------------------------
// Main Function
// -------------------------------
int main() {
    // Function template demonstration
    cout << "Bigger of (2.2, 2): " << big(2.2, 2) << endl;

    // Class template demonstration
    Array<int> o1;
    o1.insert(10, 0);
    o1.insert(12, 1);
    o1.insert(14, 2);

    cout << "Value at index 2: " << o1.getVal(2) << endl;

    return 0;
}
