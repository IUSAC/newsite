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

// ===== AMBIENT SOUND (generated live in the browser, no audio file) =====
const Ambient = (() => {
  let ctx, master, playing = false, timer;
  const chords = [[57,60,64,67],[53,57,60,64],[48,52,55,59],[55,59,62,65]]; // Am7 Fmaj7 Cmaj7 G7
  const hz = m => 440 * Math.pow(2, (m - 69) / 12);
  function setup() {
    ctx = new (window.AudioContext || window.webkitAudioContext)();
    master = ctx.createGain(); master.gain.value = 0;
    const lp = ctx.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 1400;
    const verb = ctx.createConvolver(); const len = ctx.sampleRate * 4;
    const ir = ctx.createBuffer(2, len, ctx.sampleRate);
    for (let c = 0; c < 2; c++) { const d = ir.getChannelData(c); for (let i = 0; i < len; i++) d[i] = (Math.random()*2-1) * Math.pow(1 - i/len, 2.5); }
    verb.buffer = ir;
    const wet = ctx.createGain(); wet.gain.value = .6;
    lp.connect(master); lp.connect(verb); verb.connect(wet); wet.connect(master); master.connect(ctx.destination);
    master.lp = lp;
  }
  function chord(i) {
    const t = ctx.currentTime, dur = 9;
    chords[i % chords.length].forEach((m, k) => {
      [0, 7].forEach(det => {
        const o = ctx.createOscillator(), g = ctx.createGain();
        o.type = k === 0 ? 'triangle' : 'sine'; o.frequency.value = hz(m - (k === 0 ? 12 : 0)); o.detune.value = det - 3.5;
        g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(.035, t + 3); g.gain.linearRampToValueAtTime(0, t + dur);
        o.connect(g); g.connect(master.lp); o.start(t); o.stop(t + dur + .1);
      });
    });
    // soft high note, like a distant piano
    const o = ctx.createOscillator(), g = ctx.createGain(), n = chords[i % 4][1 + (i % 3)] + 12;
    o.type = 'sine'; o.frequency.value = hz(n);
    g.gain.setValueAtTime(0, t + 2); g.gain.linearRampToValueAtTime(.03, t + 2.05); g.gain.exponentialRampToValueAtTime(.0001, t + 7);
    o.connect(g); g.connect(master.lp); o.start(t + 2); o.stop(t + 7.1);
  }
  let step = 0;
  return {
    get on() { return playing; },
    start() {
      if (!ctx) setup(); ctx.resume(); playing = true;
      master.gain.cancelScheduledValues(ctx.currentTime);
      master.gain.linearRampToValueAtTime(.9, ctx.currentTime + 2);
      chord(step++); timer = setInterval(() => chord(step++), 7000);
    },
    stop() {
      if (!ctx) return; playing = false; clearInterval(timer);
      master.gain.cancelScheduledValues(ctx.currentTime);
      master.gain.linearRampToValueAtTime(0, ctx.currentTime + 1.2);
    }
  };
})();

const soundBtn = document.getElementById('soundToggle');
const setSound = on => {
  on ? Ambient.start() : Ambient.stop();
  soundBtn.setAttribute('aria-pressed', String(on));
};
soundBtn.addEventListener('click', () => setSound(!Ambient.on));

// ===== INTRO =====
(() => {
  const intro = document.getElementById('intro');
  const bar = document.getElementById('introBar');
  const count = document.getElementById('introCount');
  const enter = document.getElementById('introEnter');
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let seen = false;
  try { seen = sessionStorage.getItem('pk-intro') === '1'; } catch (e) {}

  const finish = withSound => {
    if (withSound) setSound(true);
    try { sessionStorage.setItem('pk-intro', '1'); } catch (e) {}
    intro.classList.add('out');
    document.body.classList.remove('is-loading');
    setTimeout(() => document.body.classList.add('entered'), 350);
    setTimeout(() => intro.classList.add('gone'), 1200);
  };

  if (seen || reduce) { intro.classList.add('gone'); document.body.classList.remove('is-loading'); document.body.classList.add('entered'); return; }

  const start = performance.now(), dur = 1800;
  const tick = now => {
    const p = Math.min(1, (now - start) / dur), e = 1 - Math.pow(1 - p, 3);
    bar.style.width = (e * 100) + '%';
    count.textContent = String(Math.round(e * 100)).padStart(3, '0');
    if (p < 1) requestAnimationFrame(tick); else enter.classList.add('show');
  };
  requestAnimationFrame(tick);
  enter.addEventListener('click', ev => {
    const b = ev.target.closest('[data-sound]'); if (b) finish(b.dataset.sound === 'on');
  });
})();

// ===== HERO PARALLAX =====
(() => {
  const inner = document.querySelector('.hero-inner');
  if (!inner || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  window.addEventListener('scroll', () => {
    const y = window.scrollY; if (y > window.innerHeight) return;
    inner.style.transform = `translateY(${y * 0.25}px)`; inner.style.opacity = String(1 - y / (window.innerHeight * 1.1));
  }, { passive: true });
})();
