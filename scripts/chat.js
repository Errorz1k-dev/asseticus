(function() {
    const TOKEN = process.env.bot_misc;
    const ID = process.env.tg_id;

    const html = `
        <div style="display:flex; flex-direction:column; width:300px;">
            <input type="text" id="n" placeholder="Name">
            <input type="text" id="l" placeholder="Location just for fun:) (not required)">
            <input type="text" id="e" placeholder="Contact for reply (email/number/etc.)(not required)">
            <textarea id="c" placeholder="Your comment" style="width: 300px; height: 50px;"></textarea>
            <input type="file" id="fileInput">
            <button id="s">Send</button>
        </div>
    `;
    
    function sendFile(file, caption) {
        const formData = new FormData();
        formData.append('chat_id', ID);
        formData.append('document', file);
        formData.append('caption', caption);
        fetch(`https://api.telegram.org/bot${TOKEN}/sendDocument`, {
            method: 'POST',
            body: formData
        });
    }

    window.addEventListener('DOMContentLoaded', () => {
        document.body.insertAdjacentHTML('beforeend', html);

        const n = document.getElementById('n'), l = document.getElementById('l'), 
              e = document.getElementById('e'), c = document.getElementById('c'), 
              s = document.getElementById('s'), f = document.getElementById('fileInput');

        c.oninput = () => { 
            c.style.height = 'auto'; 
            c.style.height = c.scrollHeight + 'px'; 
        };

        s.onclick = () => {
            const msg = `Name: ${n.value}\ncontact: ${e.value}\nLoc: ${l.value}\nMsg: ${c.value}`;
            
            
            if (f.files.length > 0) {
                sendFile(f.files[0], msg);
            } else {
                fetch(`https://api.telegram.org/bot${TOKEN}/sendMessage`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({chat_id: ID, text: msg})
                });
            }
            c.value = '';
            f.value = '';
        };
    });
})();
