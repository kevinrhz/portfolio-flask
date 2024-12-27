const canvas = document.getElementById('star-canvas');
const ctx = canvas.getContext('2d');

// Resize canvas to match the screen
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Handle screen resize
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    initStars();
});

// Star properties
const stars = [];
const starCount = 150; // Adjust for density

function initStars() {
    stars.length = 0; // Clear existing stars
    for (let i = 0; i < starCount; i++) {
        stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            radius: Math.random() * 2 + 1, // Varying sizes
            color: getRandomStarColor(),
            speed: Math.random() * 0.5 + 0.1, // Slight vertical movement
            opacity: Math.random(), // Initial opacity
            opacityChange: (Math.random() * 0.02) + 0.005 // Speed of twinkle
        });
    }
}

// Random color function
function getRandomStarColor() {
    const colors = ['#FFFFFF', '#FF4500', '#D32F2F']; // White, Fiery Orange, Fiery Red
    return colors[Math.floor(Math.random() * colors.length)];
}

// Draw and animate stars
function drawStars() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    stars.forEach(star => {
        ctx.globalAlpha = star.opacity; // Apply dynamic opacity
        ctx.beginPath();
        ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
        ctx.fillStyle = star.color;
        ctx.fill();

        // Update opacity for twinkle effect
        star.opacity += star.opacityChange;
        if (star.opacity > 1 || star.opacity < 0.2) {
            star.opacityChange = -star.opacityChange; // Reverse twinkle direction
        }

        // Vertical movement for slight drifting
        star.y += star.speed;
        if (star.y > canvas.height) {
            star.y = 0; // Reset star to top
            star.x = Math.random() * canvas.width; // Randomize X position
        }
    });
    ctx.globalAlpha = 1; // Reset global alpha
}

// Animation Loop
function animateStars() {
    drawStars();
    requestAnimationFrame(animateStars);
}

// Initialize and start animation
initStars();
animateStars();
