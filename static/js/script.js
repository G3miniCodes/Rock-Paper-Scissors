let countdown = document.getElementById('countdown');
let resultImage = document.getElementById('result');
let playAgainButton = document.getElementById('play-again');

let count = 3;
let countdownInterval = setInterval(() => {
    countdown.innerHTML = count;
    count--;

    if (count < 0) {
        clearInterval(countdownInterval);
        countdown.style.display = 'none';
        resultImage.style.display = 'block';
        playAgainButton.style.display = 'block';
    }
}, 1000);
