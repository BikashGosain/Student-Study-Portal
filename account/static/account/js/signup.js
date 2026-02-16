    const togglePassword1 = document.getElementById('togglePassword1');
    const password1 = document.getElementById('password1');
    togglePassword1.addEventListener('click', () => {
      const type = password1.getAttribute('type') === 'password' ? 'text' : 'password';
      password1.setAttribute('type', type);
      togglePassword1.classList.toggle('fa-eye-slash');
    });

    const togglePassword2 = document.getElementById('togglePassword2');
    const password2 = document.getElementById('password2');
    togglePassword2.addEventListener('click', () => {
      const type = password2.getAttribute('type') === 'password' ? 'text' : 'password';
      password2.setAttribute('type', type);
      togglePassword2.classList.toggle('fa-eye-slash');
    });