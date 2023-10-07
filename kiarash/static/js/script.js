document.addEventListener("DOMContentLoaded", function() {
    const aboutSection = document.querySelector(".about-section");
    const aboutLink = document.querySelector(".nav-link[href='#about']");

    function handleScroll() {
        const aboutSectionRect = aboutSection.getBoundingClientRect();
        const isAboutSectionVisible = aboutSectionRect.top >= 0 && aboutSectionRect.bottom <= window.innerHeight;

        if (isAboutSectionVisible) {
            aboutLink.classList.add("underline");
        } else {
            aboutLink.classList.remove("underline");
        }
    }

    // Listen for scroll events and update the link style
    window.addEventListener("scroll", handleScroll);
});