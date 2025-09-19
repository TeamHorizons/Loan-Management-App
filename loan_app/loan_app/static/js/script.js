/*
Set's the current year dynamically
 */

document.addEventListener("DOMContentLoaded", function(){
    const currentYearSpan = document.getElementById("copy-right-year");
    if (currentYearSpan){
        currentYear = new Date().getFullYear();
        currentYearSpan.innerHTML = `&copy; ${currentYear} Loan Management App. All rights reserved.`;
    }
})

// get dynamic display of bank names
const selectedBank = "{{ form.bank_name.value|default:'' }}"; // Keep selection after form reload

async function loadBanks() {
    try {
        const response = await fetch("{% url 'banks-list' %}"); // Your API endpoint
        const data = await response.json();

        if (data.banks) {
            const select = document.getElementById("branchDropdown");

            data.banks.forEach(bank => {
                const option = document.createElement("option");
                option.value = bank.code; // Send code as value (better for backend processing)
                option.textContent = bank.name;

                // If the user had selected this bank before, keep it selected
                if (bank.code === selectedBank) {
                    option.selected = true;
                }

                select.appendChild(option);
            });
        } else {
            console.error("No banks received:", data);
        }
    } catch (error) {
        console.error("Error fetching banks:", error);
    }
}

document.addEventListener("DOMContentLoaded", loadBanks);