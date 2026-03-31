/**
 * background.js
 * Modular floating elements for Mujeeb's Portfolio
 */

document.addEventListener('DOMContentLoaded', () => {
    const bgContainer = document.createElement('div');
    bgContainer.style.position = 'fixed';
    bgContainer.style.top = '0';
    bgContainer.style.left = '0';
    bgContainer.style.width = '100vw';
    bgContainer.style.height = '100vh';
    bgContainer.style.pointerEvents = 'none';
    bgContainer.style.zIndex = '-1';
    bgContainer.style.overflow = 'hidden';
    bgContainer.id = 'floating-bg-elements';
    document.body.appendChild(bgContainer);

    const symbols = ['{ }', '< >', '[ ]', '/', '*', '+', '!', '?', '#', '()', '=>', '01'];
    const colors = ['rgba(245, 166, 35, 0.05)', 'rgba(255, 255, 255, 0.02)'];
    
    for (let i = 0; i < 25; i++) {
        createFloatingElement(bgContainer, symbols, colors);
    }
});

function createFloatingElement(container, symbols, colors) {
    const el = document.createElement('div');
    const symbol = symbols[Math.floor(Math.random() * symbols.length)];
    const color = colors[Math.floor(Math.random() * colors.length)];
    
    el.innerText = symbol;
    el.style.position = 'absolute';
    el.style.color = color;
    el.style.fontSize = Math.random() * 20 + 10 + 'px';
    el.style.fontWeight = 'bold';
    el.style.fontFamily = 'monospace';
    el.style.userSelect = 'none';
    
    // Random initial position
    let x = Math.random() * 100;
    let y = Math.random() * 100;
    el.style.left = x + 'vw';
    el.style.top = y + 'vh';
    
    container.appendChild(el);
    
    // Animations
    animateElement(el, x, y);
}

function animateElement(el, x, y) {
    let dx = (Math.random() - 0.5) * 0.05;
    let dy = (Math.random() - 0.5) * 0.05;
    
    function step() {
        x += dx;
        y += dy;
        
        // Wrap around
        if (x < -5) x = 105;
        if (x > 105) x = -5;
        if (y < -5) y = 105;
        if (y > 105) y = -5;
        
        el.style.left = x + 'vw';
        el.style.top = y + 'vh';
        
        requestAnimationFrame(step);
    }
    
    requestAnimationFrame(step);
}
