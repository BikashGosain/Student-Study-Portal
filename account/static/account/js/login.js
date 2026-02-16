document.addEventListener('DOMContentLoaded', () => {
  const toggleButton = document.getElementById('togglePassword');
  const passwordInput = document.getElementById('password');

  if (!toggleButton || !passwordInput) return;

  toggleButton.addEventListener('click', () => {
    const isHidden = passwordInput.type === 'password';
    passwordInput.type = isHidden ? 'text' : 'password';
    toggleButton.classList.toggle('fa-eye-slash', isHidden);
    toggleButton.setAttribute('aria-label', isHidden ? 'Hide password' : 'Show password');
  });
});
