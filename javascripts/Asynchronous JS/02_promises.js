// Example of handling asynchronous operations with Promises
// Demonstrates a sequence of tasks: Inventory check -> Order creation -> Payment -> Invoice
// Includes basic error handling to understand which step fails

function checkInventory() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('✅ Inventory checked'); 
            // resolve(); // Uncomment this line to simulate successful inventory check
            reject(new Error("Failed to check inventory!")); // Example failure
        }, 2000); 
    });
}

// Simulate creating an order
function createOrder() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('✅ Order created'); 
            resolve(); // Simulate success
            // reject(new Error("Failed to create order!")); // Uncomment to simulate failure
        }, 1000); 
    });
}

// Simulate charging payment
function chargePayment() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('✅ Payment charged'); 
            resolve(); // Simulate success
        }, 2000); 
    });
}

function sendInvoice() {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log('✅ Invoice sent to customer'); 
            resolve(); // Always resolves, no failure simulated
        }, 4000); 
    });
}

function main() {
    checkInventory()
        .then(createOrder) 
        .catch((err) => {
        // This catches errors from checkInventory() or createOrder()
            console.log("❌ Error in createOrder:", err.message);
            // Decide: continue flow or stop; currently flow continues
        })
        .then(chargePayment) 
        .then(sendInvoice)   
        .then(() => console.log('🎉 All tasks completed successfully')) 
        .catch((err) => {
        // This catches any unhandled errors from the remaining chain
            console.log("❌ Flow stopped due to error:", err.message);
        });
}

main();
