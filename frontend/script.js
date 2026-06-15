// ── CropWise Shared JS ──

function toggleNav() {
  const links = document.getElementById('navLinks');
  links.classList.toggle('open');
}

// Close nav when clicking outside
document.addEventListener('click', function(e) {
  const nav = document.getElementById('navLinks');
  const toggle = document.querySelector('.nav-toggle');
  if (nav && toggle && !nav.contains(e.target) && !toggle.contains(e.target)) {
    nav.classList.remove('open');
  }
});
