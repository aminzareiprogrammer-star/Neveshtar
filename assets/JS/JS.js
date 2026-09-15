// Navbar scroll
window.addEventListener('scroll', () => {
  const nb = document.getElementById('navbar');
  const st = document.getElementById('scrollTop');
  if(window.scrollY > 50) { nb.classList.add('scrolled'); st.classList.add('show'); }
  else { nb.classList.remove('scrolled'); st.classList.remove('show'); }
  revealElements();
});

// Scroll reveal
function revealElements() {
  document.querySelectorAll('.reveal, .reveal-left').forEach(el => {
    const rect = el.getBoundingClientRect();
    if(rect.top < window.innerHeight - 80) el.classList.add('visible');
  });
}

// Nav scroll
function scrollToSection(id) {
  const el = document.getElementById(id);
  if(el) el.scrollIntoView({behavior:'smooth', block:'start'});
}

// Mobile menu
function toggleMobile() {
  const mm = document.getElementById('mobileMenu');
  mm.classList.toggle('open');
  const hm = document.getElementById('hamburger');
  hm.classList.toggle('open');
}

// Modal
function openModal(type) {
  document.getElementById(type+'Modal').classList.add('open');
  document.body.style.overflow='hidden';
}
function closeModal(type) {
  document.getElementById(type+'Modal').classList.remove('open');
  document.body.style.overflow='';
}
function switchModal(from,to) {
  closeModal(from);
  setTimeout(()=>openModal(to),200);
}
document.querySelectorAll('.modal-overlay').forEach(mo => {
  mo.addEventListener('click', e => { if(e.target===mo) { const id=mo.id.replace('Modal',''); closeModal(id); } });
});
document.addEventListener('keydown', e => {
  if(e.key==='Escape') { document.querySelectorAll('.modal-overlay.open').forEach(m=>{ const id=m.id.replace('Modal',''); closeModal(id); }); }
});

// Toast
let toastTimer;
function showToast(msg) {
  const t = document.getElementById('toast');
  document.getElementById('toastMsg').textContent = msg;
  const bar = document.getElementById('toastBar');
  t.classList.add('show');
  bar.style.animation = 'none'; bar.offsetWidth; bar.style.animation = '';
  clearTimeout(toastTimer);
  toastTimer = setTimeout(()=>t.classList.remove('show'), 3200);
}

// Filter articles
function filterArticles(btn, cat) {
  document.querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  document.querySelectorAll('.article-card').forEach(card => {
    if(cat==='all' || card.dataset.cat===cat) {
      card.style.display='block';
      card.style.animation='fadeIn 0.4s ease';
    } else {
      card.style.display='none';
    }
  });
}

// Form progress
function updateProgress() {
  const fields = [
    document.getElementById('artTitle').value.trim(),
    document.getElementById('artCat').value,
    document.getElementById('artExcerpt').value.trim(),
    document.getElementById('artBody').value.trim()
  ];
  const filled = fields.filter(f=>f.length>0).length;
  const pct = Math.round((filled/fields.length)*100);
  document.getElementById('formProgress').style.width = pct+'%';
}

function updateCharCount(el, max, spanId) {
  const len = el.value.length;
  document.getElementById(spanId).textContent = len;
  if(len > max*0.8) document.getElementById(spanId).style.color='var(--orange)';
  else document.getElementById(spanId).style.color='var(--gray-light)';
}

// Tags
const tags = [];
function addTag(e) {
  if(e.key === 'Enter') {
    const val = e.target.value.trim();
    if(val && !tags.includes(val) && tags.length < 6) {
      tags.push(val);
      const container = document.getElementById('tagsContainer');
      const tagEl = document.createElement('div');
      tagEl.className = 'tag-item';
      tagEl.innerHTML = `${val}<button onclick="removeTag('${val}',this.parentElement)">×</button>`;
      container.insertBefore(tagEl, e.target);
    }
    e.target.value = '';
    e.preventDefault();
  }
}
function removeTag(val, el) {
  const idx = tags.indexOf(val);
  if(idx>-1) tags.splice(idx,1);
  el.remove();
}

// Submit article
function submitArticle() {
  const title = document.getElementById('artTitle').value.trim();
  const body = document.getElementById('artBody').value.trim();
  if(!title) { showToast('⚠️ لطفاً عنوان مقاله را وارد کنید'); return; }
  if(!body) { showToast('⚠️ لطفاً متن مقاله را بنویسید'); return; }
  showToast('🎉 مقاله شما با موفقیت منتشر شد!');
  document.getElementById('artTitle').value='';
  document.getElementById('artExcerpt').value='';
  document.getElementById('artBody').value='';
  document.getElementById('artCat').value='';
  document.getElementById('formProgress').style.width='0%';
  document.getElementById('titleCount').textContent='0';
  document.getElementById('excCount').textContent='0';
}

// Login

function showToast(msg) {
  const t = document.getElementById('toast');
  const text = document.getElementById('toastMsg');
  const bar = document.getElementById('toastBar');

  text.textContent = msg;

  t.classList.add('show');

  bar.style.animation = 'none';
  bar.offsetWidth;
  bar.style.animation = '';

  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => {
    t.classList.remove('show');
  }, 3000);
}
// Register
const registerForm = document.querySelector('#registerModal form');

registerForm.addEventListener('submit', function (e) {
    const name = document.getElementById('regLastname').value.trim();
    const email = document.getElementById('regEmail').value.trim();
    const pass = document.getElementById('regPass').value;
    const agree = document.getElementById('agreeTerms').checked;

    if (!name || !email || !pass) {
        e.preventDefault();
        showToast('⚠️ لطفاً همه فیلدها را پر کنید');
        return;
    }

    if (!agree) {
        e.preventDefault();
        showToast('⚠️ لطفاً شرایط را بپذیرید');
        return;
    }

});

// Password toggle
function togglePassword(id, btn) {
  const input = document.getElementById(id);
  if(input.type==='password') { input.type='text'; btn.textContent='🙈'; }
  else { input.type='password'; btn.textContent='👁'; }
}

// Password strength
function checkStrength(val) {
  let score = 0;
  if(val.length>=8) score++;
  if(/[A-Z]/.test(val)) score++;
  if(/[0-9]/.test(val)) score++;
  if(/[^a-zA-Z0-9]/.test(val)) score++;
  const colors = ['','#FF6B6B','#FFB800','#6BCB77','#00A86B'];
  const labels = ['','ضعیف','متوسط','قوی','بسیار قوی'];
  for(let i=1;i<=4;i++) {
    const s = document.getElementById('s'+i);
    s.style.background = i<=score ? colors[score] : 'var(--border)';
  }
  document.getElementById('strengthText').textContent = score>0 ? labels[score] : 'قدرت رمز عبور';
  document.getElementById('strengthText').style.color = score>0 ? colors[score] : 'var(--gray-light)';
}

// Rating
let currentRating = 0;
function setRating(n) {
  currentRating = n;
  const stars = document.querySelectorAll('#ratingStars span');
  stars.forEach((s,i) => s.classList.toggle('active', i<n));
}

// Contact
function submitContact() {
  document.getElementById('contactSuccess').style.display='block';
  showToast('📬 پیام شما ارسال شد!');
  setTimeout(()=>document.getElementById('contactSuccess').style.display='none', 4000);
}

// Newsletter
function subscribeNewsletter() {
  const email = document.getElementById('nlEmail').value.trim();
  if(!email) { showToast('⚠️ لطفاً ایمیل خود را وارد کنید'); return; }
  document.getElementById('nlEmail').value='';
  showToast('🎉 با موفقیت عضو خبرنامه شدید!');
}

// About pattern animation
function buildAboutPattern() {
  const container = document.getElementById('aboutPattern');
  if(!container) return;
  for(let i=0;i<15;i++) {
    const dot = document.createElement('div');
    dot.className = 'about-pattern-dot';
    container.appendChild(dot);
  }
  setInterval(()=>{
    const dots = container.querySelectorAll('.about-pattern-dot');
    dots.forEach(d=>d.classList.remove('active'));
    const count = Math.floor(Math.random()*8)+3;
    const shuffled = [...dots].sort(()=>Math.random()-0.5).slice(0,count);
    shuffled.forEach(d=>d.classList.add('active'));
  }, 1500);
}

// Animate numbers
function animateNumbers() {
  document.querySelectorAll('.stat-num').forEach(el => {
    const text = el.innerHTML;
    const num = parseFloat(text.replace(/[^0-9.]/g,''));
    if(!num) return;
    let start = 0; const duration = 2000; const step = 16;
    const timer = setInterval(()=>{
      start += num/(duration/step);
      if(start>=num) { start=num; clearInterval(timer); }
      const suffix = text.match(/[KMB+]+/)?.[0] || '';
      el.innerHTML = Math.round(start) + '<span>' + suffix + '</span>';
    }, step);
  });
}

// Init
setTimeout(()=>{ revealElements(); buildAboutPattern(); animateNumbers(); }, 100);

const trigger = document.getElementById("userTrigger");
const dropdown = document.getElementById("userDropdown");

function toggleDropdown() {

    trigger.classList.toggle("open");
    dropdown.classList.toggle("open");

}

document.addEventListener("click", function (e) {

    if (!trigger.contains(e.target) && !dropdown.contains(e.target)) {

        trigger.classList.remove("open");
        dropdown.classList.remove("open");

    }

});

document.addEventListener("keydown", function (e) {

    if (e.key === "Escape") {

        trigger.classList.remove("open");
        dropdown.classList.remove("open");

    }

});

const input = document.querySelector(".article-search-input");
const clearBtn = document.querySelector(".article-clear");

if(input){

    const toggleButton = ()=>{

        clearBtn.style.display =
            input.value.length ? "block" : "none";

    }

    toggleButton();

    input.addEventListener("input",toggleButton);

    clearBtn.addEventListener("click",()=>{

        input.value="";

        input.focus();

        toggleButton();

    });

}
document.addEventListener("DOMContentLoaded", function () {
    if (window.location.hash === "#add-article") {
        const section = document.getElementById("add-article");

        if (section) {
            setTimeout(() => {
                section.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }, 100);
        }
    }
});