document.addEventListener('DOMContentLoaded', () => {
    // Add hover effect to project cards
    const projectCards = document.querySelectorAll('.project-card');

    projectCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'scale(1.03)';
            card.style.boxShadow = '0 6px 15px hsla(0, 0%, 0%, 0.3)';
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'scale(1)';
            card.style.boxShadow = '0 4px 10px hsla(0, 0%, 0%, 0.2)';
        });
    });

    // Ensure project links open in a new tab
    const projectLinks = document.querySelectorAll('.project-links a');
    projectLinks.forEach(link => {
        link.setAttribute('target', '_blank');
    });


});
