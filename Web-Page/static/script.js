document.addEventListener("DOMContentLoaded", function () {

    window.toggleMenu = function ()  {
        document.getElementById("nav-links").classList.toggle("active")
    }

    const toggleButton = document.getElementById("language-toggle");
    const elements = document.querySelectorAll("[data-en]");

    // Load language from LocalStorage (default to English)
    let currentLanguage = localStorage.getItem("language") || "en";
    updateLanguage(currentLanguage);

    // Toggle Language on Button Click
    toggleButton.addEventListener("click", function () {
        currentLanguage = currentLanguage === "en" ? "es" : "en";
        localStorage.setItem("language", currentLanguage);
        updateLanguage(currentLanguage);
    });

    function updateLanguage(lang) {
        elements.forEach(el => {
            el.textContent = lang === "en" ? el.dataset.en : el.dataset.es;
        });

        // Change button text
        toggleButton.textContent = lang === "en" ? "Español" : "English";
    }
} )


