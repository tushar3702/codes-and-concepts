// Final Async JS Example with async/await and error handling

function checkInventory() {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log('✅ Inventory checked');
            let amount = 400;
            resolve(amount);
        }, 2000);
    });
}

function createOrder() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('✅ Order created');
            reject(new Error("❌ Failed to create order!")); 
            // Change to resolve() to test success case
        }, 1000);
    });
}

function chargePayment() {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log('✅ Payment charged');
            resolve();
        }, 2000);
    });
}

function sendInvoice() {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log('✅ Invoice sent to customer');
            resolve();
        }, 4000);
    });
}

async function main() {
    try {
        const amount = await checkInventory();
        console.log("Amount in stock:", amount);

        await createOrder();
        await chargePayment();
        await sendInvoice();

        console.log("🎉 Other Request Processing :)");
    } catch (err) {
        console.error("❌ Error:", err.message);
    }
}

main();
