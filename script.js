// Nav background on scroll
const nav = document.getElementById('nav');
const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 40);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Mobile menu
const burger = document.getElementById('burger');
const navLinks = document.getElementById('navLinks');
burger.addEventListener('click', () => {
  const open = navLinks.classList.toggle('open');
  burger.setAttribute('aria-expanded', String(open));
  document.body.style.overflow = open ? 'hidden' : '';
});
navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
  navLinks.classList.remove('open');
  burger.setAttribute('aria-expanded', 'false');
  document.body.style.overflow = '';
}));

// Reveal on scroll
const io = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Contact form -> mailto (no backend)
document.getElementById('contactForm').addEventListener('submit', e => {
  e.preventDefault();
  const f = e.target;
  const body = `Imię i nazwisko: ${f.elements.name.value}\nKontakt: ${f.elements.contact.value}\n\n${f.elements.message.value}`;
  window.location.href = `mailto:biuro@pkwadwokaci.pl?subject=${encodeURIComponent('Zapytanie ze strony www')}&body=${encodeURIComponent(body)}`;
  document.getElementById('formNote').hidden = false;
});

document.getElementById('year').textContent = new Date().getFullYear();
