document.addEventListener('DOMContentLoaded', () => {
    const slider = document.querySelector('.slider-container');
    const projectCards = document.querySelectorAll('.project-card');

    // Function to scroll to a specific card
    function scrollToCard(card) {
        const cardOffset = card.offsetLeft - (window.innerWidth / 2) + (card.offsetWidth / 2);
        slider.scrollTo({
            left: cardOffset,
            behavior: 'smooth'
        });
    }

    // Click event for each project card
    projectCards.forEach((card, index) => {
        card.addEventListener('click', (event) => {
            const cardRect = card.getBoundingClientRect();
            const clickX = event.clientX;

            // Click on the right side of the card
            if (clickX > cardRect.right - card.offsetWidth / 3) {
                if (index < projectCards.length - 1) {
                    scrollToCard(projectCards[index + 1]);
                }
            }
            // Click on the left side of the card
            else if (clickX < cardRect.left + card.offsetWidth / 3) {
                if (index > 0) {
                    scrollToCard(projectCards[index - 1]);
                }
            }
            // Click in the middle focuses on the card itself
            else {
                scrollToCard(card);
            }
        });
    });
});
