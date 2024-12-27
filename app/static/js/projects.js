document.addEventListener('DOMContentLoaded', () => {
    const slider = document.querySelector('.slider-container');
    const firstCard = document.querySelector('.project-card');

    // Scroll to the first project card and center it
    if (firstCard) {
        const cardOffset = firstCard.offsetLeft - (window.innerWidth / 2) + (firstCard.offsetWidth / 2);
        slider.scrollTo({
            left: cardOffset,
            behavior: 'smooth'
        });
    }

    // Navigation buttons
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    prevBtn.addEventListener('click', () => {
        slider.scrollBy({
            left: -window.innerWidth * 0.9,
            behavior: 'smooth'
        });
    });

    nextBtn.addEventListener('click', () => {
        slider.scrollBy({
            left: window.innerWidth * 0.9,
            behavior: 'smooth'
        });
    });
});
