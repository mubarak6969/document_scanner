function showMessage(text, isSuccess = true) {
    const msg = document.getElementById('message');
    msg.textContent = text;
    msg.className = 'message ' + (isSuccess ? 'success' : 'error');
    msg.style.opacity = '1';
    setTimeout(() => {
        msg.style.opacity = '0';
        setTimeout(() => msg.style.display = 'none', 500);
    }, 3000);
    msg.style.display = 'block';
}

function showRegister() {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('register-form').style.display = 'block';
}

function showLogin() {
    document.getElementById('login-form').style.display = 'block';
    document.getElementById('register-form').style.display = 'none';
}

document.getElementById('show-register')?.addEventListener('click', (e) => {
    e.preventDefault();
    showRegister();
});

document.getElementById('show-login')?.addEventListener('click', (e) => {
    e.preventDefault();
    showLogin();
});

document.getElementById('login-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch('/auth/login', { method: 'POST', body: formData });
    const data = await response.json();
    showMessage(data.message, data.success);
    if (data.success) setTimeout(() => location.reload(), 1000);
});

document.getElementById('register-submit')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch('/auth/register', { method: 'POST', body: formData });
    const data = await response.json();
    showMessage(data.message, data.success);
    if (data.success) setTimeout(showLogin, 1000);
});

document.getElementById('scan-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch('/scan', { method: 'POST', body: formData });
    const data = await response.json();
    showMessage(data.message, data.success);
    if (data.success) {
        document.getElementById('credits').textContent = data.credits;
        const matchesList = document.getElementById('matches-list');
        matchesList.innerHTML = data.matches.map(m => `<li>${m.filename} - ${m.similarity.toFixed(1)}%</li>`).join('');
        document.getElementById('matches').style.display = 'block';
        const scans = document.getElementById('scans');
        scans.innerHTML += `<li>${formData.get('file').name} - Uploaded: ${new Date().toLocaleString()}</li>`;
    }
});

document.getElementById('credit-request-form')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch('/credits/request', { method: 'POST', body: formData });
    const data = await response.json();
    showMessage(data.message, data.success);
    if (data.success) e.target.reset();
});

document.querySelectorAll('.approve-btn')?.forEach(btn => {
    btn.addEventListener('click', async (e) => {
        const form = e.target.closest('form');
        const requestId = form.dataset.id;
        const formData = new FormData();
        formData.append('request_id', requestId);
        formData.append('action', 'approve');
        const response = await fetch('/admin/credits', { method: 'POST', body: formData });
        const data = await response.json();
        showMessage(data.message, data.success);
        if (data.success) {
            const row = form.closest('tr');
            row.cells[3].textContent = 'approved';
            row.cells[4].innerHTML = '';
            const credits = parseInt(document.getElementById('credits').textContent) + parseInt(row.cells[2].textContent);
            document.getElementById('credits').textContent = credits;
        }
    });
});

document.querySelectorAll('.deny-btn')?.forEach(btn => {
    btn.addEventListener('click', async (e) => {
        const form = e.target.closest('form');
        const requestId = form.dataset.id;
        const formData = new FormData();
        formData.append('request_id', requestId);
        formData.append('action', 'deny');
        const response = await fetch('/admin/credits', { method: 'POST', body: formData });
        const data = await response.json();
        showMessage(data.message, data.success);
        if (data.success) {
            const row = form.closest('tr');
            row.cells[3].textContent = 'denied';
            row.cells[4].innerHTML = '';
        }
    });
});

document.getElementById('change-role-form')?.addEventListener('submit', async (e) => {  // New handler
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch('/admin/change_role', { method: 'POST', body: formData });
    const data = await response.json();
    showMessage(data.message, data.success);
    if (data.success) e.target.reset();
});

document.getElementById('logout-link')?.addEventListener('click', async (e) => {
    e.preventDefault();
    const response = await fetch('/logout', { method: 'POST' });
    const data = await response.json();
    showMessage(data.message, data.success);
    if (data.success) setTimeout(() => window.location.href = '/', 1000);  // Updated to redirect
});