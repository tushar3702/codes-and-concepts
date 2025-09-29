/**
 * Callback Hell Example
 * ---------------------
 * This simulates an e-commerce order flow with asynchronous operations:
 * 1️⃣ Check inventory
 * 2️⃣ Create order
 * 3️⃣ Charge payment
 * 4️⃣ Send invoice
 *
 * Each step uses setTimeout() to mimic a real API call or database query.
 * Errors (if any) are passed to the next callback.
 */

// ✅ Step 1: Check if inventory is available
function checkInventory(callback) {
    setTimeout(() => {
        // Toggle between `null` and an Error to test success/failure
        const err = null; // new Error("❌ Inventory check failed!");
        console.log('✅ Inventory checked');
        callback(err);
    }, 2000);
}

// ✅ Step 2: Create a new order
function createOrder(callback) {
    setTimeout(() => {
        console.log('✅ Order created');
        callback();
    }, 1000);
}

// ✅ Step 3: Charge the customer’s payment
function chargePayment(callback) {
    setTimeout(() => {
        // Simulate a successful payment
        let err = null;
        let amount = 5000; // Example: amount in INR
        console.log('✅ Payment charged');
        callback(err, amount);
    }, 2000);
}

// ✅ Step 4: Send an invoice to the customer
function sendInvoice(callback) {
    setTimeout(() => {
        console.log('✅ Invoice sent to customer');
        callback();
    }, 4000);
}

/**
 * MAIN FUNCTION
 * -------------
 * Demonstrates "callback hell" by nesting callbacks to ensure
 * each step runs only after the previous step finishes.
 */
function main() {
    checkInventory((err) => {
        if (err) {
            console.error(err.message);
            return;
        }

        createOrder(() => {
            chargePayment((err, amount) => {
                if (err) {
                    console.error(err.message);
                    return;
                }

                console.log(`💰 Payment Amount: ₹${amount}`);

                sendInvoice(() => {
                    console.log("🎯 All steps completed successfully!");
                });
            });
        });
    });
}

main();
