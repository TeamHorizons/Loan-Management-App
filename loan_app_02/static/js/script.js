/*
Set's the current year dynamically
 */


document.addEventListener("DOMContentLoaded", function(){
    const currentYearSpan = document.getElementById("copy-right-year");
    currentYear = new Date().getFullYear();
    currentYearSpan.innerHTML = `&copy; ${currentYear} Loan Management App. All rights reserved.`;
})