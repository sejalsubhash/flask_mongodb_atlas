const form = document.getElementById('myForm');
const message = document.getElementById('message');


form.addEventListener('submit', async (e) => {
e.preventDefault();
message.textContent = '';
const name = document.getElementById('name').value.trim();
const email = document.getElementById('email').value.trim();


try {
const resp = await fetch('/submit', {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ name, email })
});


const data = await resp.json();
if (resp.ok && data.ok) {
// redirect on success to /success
window.location.href = '/success';
} else {
// show error on same page (no redirect)
message.textContent = data.error || 'Unknown error occurred.';
}
} catch (err) {
message.textContent = 'Network or server error: ' + err.message;
}
});