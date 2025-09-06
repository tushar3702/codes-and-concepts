#include <iostream>
using namespace std;

int main() {
    // ------------------------------
    // 1. Basic Pointer
    //------------------------------
    int x = 5;
    int *j = &x; // 'j' is a pointer variable that stores the address of 'x'

    // A pointer stores an address (size depends on system: 4 bytes on 32-bit, 8 bytes on 64-bit)
    cout << "Value of x: " << x << endl;       // 5
    cout << "Address of x (&x): " << &x << endl; 
    cout << "Pointer j (stores &x): " << j << endl;
    cout << "Dereferencing *j (value at address): " << *j << endl;

    // ------------------------------
    // 2. Double Pointer (Pointer to Pointer)
    // ------------------------------
    int y = 10;
    int *p;   // pointer to int
    int **q;  // pointer to pointer (stores address of 'p')

    p = &y;
    q = &p;

    cout << "\nUsing double pointer:" << endl;
    cout << "y = " << y << endl;         // 10
    cout << "*p = " << *p << endl;       // 10 (value of y)
    cout << "**q = " << **q << endl;     // 10 (value of y via double pointer)

    // ------------------------------
    // 3. Pointer Arithmetic
    // ------------------------------
    int a = 10, b = 20;
    int *p1 = &a;
    int *q1 = &b;

    // ❌ Invalid operations:
    // p1 + q1;   // error: cannot add two addresses
    // p1 * q1;   // error
    // p1 / q1;   // error

    // ✅ Valid operation: subtracting two pointers (if they point to same array)
    cout << "\nPointer arithmetic:" << endl;
    cout << "Address in p1: " << p1 << endl;
    cout << "Address in p1+1: " << (p1 + 1) << endl;
    cout << "Address difference (q1 - p1): " << (q1 - p1) << " (may be garbage if unrelated)" << endl;

    // Rule: pointer + n = pointer + (n * sizeof(type))
    // Example: int = 4 bytes, so p1+1 jumps 4 bytes ahead.

    return 0;
}
