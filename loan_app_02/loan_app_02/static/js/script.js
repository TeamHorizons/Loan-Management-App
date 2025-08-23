/*
Set's the current year dynamically
 */

document.addEventListener("DOMContentLoaded", function(){
const currentYearSpan = document.getElementById("copy-right-year");
if (currentYearSpan){
    const currentYear = new Date().getFullYear();
    currentYear.innerHTML = `&copy; ${currentYear}Loan Management App. All rights reserved.`;
}
});

