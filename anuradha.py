import streamlit as st
import time
import base64
from pathlib import Path

st.set_page_config(
    page_title="For Anuradha 🌼",
    page_icon="🌼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Nunito:wght@300;400;600;700;800&family=Sacramento&display=swap');

:root {
    --bg:       #fffbf0;
    --surface:  #ffffff;
    --border:   #f59e0b;
    --deep:     #07010f;
    --royal:    #451a03;
    --amber:    #b45309;
    --mid:      #d97706;
    --gold:     #f59e0b;
    --soft:     #fef3c7;
    --muted:    #92400e;
    --text:     #07010f;
}

html, body, [class*="css"] { font-family:'Nunito',sans-serif; color:var(--text); }

h1, h2, h3, h4, h5, h6,
[class*="css"] h1, [class*="css"] h2, [class*="css"] h3 {
    color: #1c0a00 !important;
    -webkit-text-fill-color: #1c0a00 !important;
}

.stApp {
    background-color: #fffbf0;
    background-image:
        radial-gradient(ellipse at 15% 10%, #fde68a66 0%, transparent 40%),
        radial-gradient(ellipse at 85% 85%, #fcd34d44 0%, transparent 40%),
        radial-gradient(ellipse at 50% 50%, #fffbeb33 0%, transparent 60%);
    background-attachment: fixed;
}

#MainMenu, footer, header { visibility:hidden; }
.block-container { padding-top:1rem; padding-bottom:3rem; max-width:860px; }

@keyframes fadeUp    { from{opacity:0;transform:translateY(24px);} to{opacity:1;transform:translateY(0);} }
@keyframes floatY    { 0%,100%{transform:translateY(0);} 50%{transform:translateY(-7px);} }
@keyframes shimmer   { 0%{background-position:-300% center;} 100%{background-position:300% center;} }
@keyframes glowPulse { 0%,100%{box-shadow:0 0 24px #f59e0b33;} 50%{box-shadow:0 0 52px #f59e0b55;} }

/* ── PHOTO HERO ── */
.photo-hero {
    display: flex;
    justify-content: center;
    padding: 2.5rem 1rem 0;
    animation: fadeUp 1s ease both;
}
.photo-frame {
    width: 220px; height: 220px;
    border-radius: 50%;
    background: linear-gradient(135deg, #b45309, #f59e0b, #b45309);
    padding: 5px;
    box-shadow: 0 16px 56px #f59e0b55;
    animation: glowPulse 4s ease-in-out infinite;
}
.photo-inner {
    width: 100%; height: 100%;
    border-radius: 50%;
    background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    gap: 0.4rem;
    overflow: hidden;
}
.photo-inner img { width:100%; height:100%; object-fit:cover; border-radius:50%; }
.photo-inner .ph-icon { font-size:3.5rem; animation:floatY 3s ease-in-out infinite; }
.photo-inner .ph-txt  { font-family:'Sacramento',cursive; font-size:0.95rem; color:var(--muted); }

/* ── HERO TEXT ── */
.hero {
    text-align:center;
    padding: 1.4rem 1rem 1.8rem;
    animation: fadeUp 1s ease both;
}
.hero-badge {
    display:inline-block;
    background:linear-gradient(90deg,#b45309,#f59e0b,#854d0e,#f59e0b,#b45309);
    background-size:300% auto;
    animation:shimmer 4s linear infinite;
    color:#fff; font-size:0.7rem; font-weight:800;
    letter-spacing:0.25em; text-transform:uppercase;
    padding:0.38rem 1.4rem; border-radius:50px;
    margin-bottom:1rem;
    box-shadow:0 4px 20px #f59e0b66;
}
.hero h1 {
    font-family:'Cormorant Garamond',serif;
    font-size:clamp(2.2rem,6vw,4rem);
    font-weight:700; line-height:1.12;
    color:#1c0a00 !important; margin:0 0 0.5rem;
    -webkit-text-fill-color:#1c0a00 !important;
}
.hero h1 span {
    background:linear-gradient(135deg,#b45309,#f59e0b);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent !important; background-clip:text;
}
.hero-sub {
    font-family:'Sacramento',cursive;
    font-size:clamp(1.2rem,3vw,1.7rem);
    color:var(--muted); display:inline-block;
    animation:floatY 4s ease-in-out infinite;
}

.divider { text-align:center; margin:2rem 0; color:var(--gold); font-size:1.2rem; letter-spacing:0.8rem; }

.sec-label { font-size:0.68rem; font-weight:900; letter-spacing:0.28em; text-transform:uppercase; color:#b45309; margin-bottom:0.25rem; }
.sec-title  { font-family:'Cormorant Garamond',serif; font-size:clamp(1.6rem,4vw,2.3rem); font-weight:700; color:#1c0a00 !important; margin:0 0 1.4rem; -webkit-text-fill-color:#1c0a00 !important; }

/* ── Counter ── */
.ctr-row { display:flex; gap:1rem; flex-wrap:wrap; justify-content:center; }
.ctr-chip {
    background:#fff; border:2px solid var(--border);
    border-radius:18px; padding:1.3rem 1.8rem;
    text-align:center; min-width:130px;
    box-shadow:0 6px 24px #f59e0b20;
    animation:fadeUp 1s ease both, glowPulse 5s ease-in-out infinite;
    transition:transform .25s;
}
.ctr-chip:hover { transform:translateY(-4px); }
.ctr-val { font-family:'Cormorant Garamond',serif; font-size:2.3rem; font-weight:700; color:#b45309; line-height:1; }
.ctr-lbl { font-size:.7rem; color:#451a03; margin-top:.3rem; font-weight:900; letter-spacing:.1em; text-transform:uppercase; }

/* ── Quotes ── */
.q-card {
    background:#ffffff;
    border-left:7px solid #b45309;
    border-radius:0 18px 18px 0;
    padding:1.5rem 1.8rem 1.5rem 1.8rem;
    box-shadow:0 6px 28px #b4530930;
    margin-bottom:1.1rem;
    transition:transform .25s, box-shadow .25s;
    position:relative; overflow:hidden;
    animation:fadeUp .9s ease both;
}
.q-card:hover { transform:translateX(7px); box-shadow:0 12px 40px #b4530950; }
.q-card::before {
    content:'\201C'; font-family:'Cormorant Garamond',serif;
    font-size:6rem; color:#fde68a;
    position:absolute; top:-10px; left:10px; line-height:1;
    pointer-events:none;
}
.q-text {
    font-family:'Cormorant Garamond',serif;
    font-style:italic;
    font-size:1.22rem;
    color:#0a0015;
    padding-left:1.2rem;
    line-height:1.75;
    margin:0 0 .6rem;
    font-weight:700;
    position:relative; z-index:1;
}
.q-attr {
    font-size:.8rem;
    color:#451a03;
    padding-left:1.2rem;
    font-weight:900;
    letter-spacing:.1em;
    position:relative; z-index:1;
}

/* ── Reasons ── */
.r-chip {
    background:#fff; border:2px solid var(--border);
    border-radius:18px; padding:1.2rem 0.8rem; text-align:center;
    box-shadow:0 5px 20px #f59e0b15;
    transition:transform .25s, box-shadow .25s, border-color .25s;
    animation:fadeUp 1s ease both;
}
.r-chip:hover { transform:translateY(-5px); box-shadow:0 14px 36px #f59e0b30; border-color:var(--gold); }
.r-chip .ri { font-size:2rem; display:block; margin-bottom:.45rem; animation:floatY 3s ease-in-out infinite; }
.r-chip .rl { font-size:.82rem; font-weight:900; color:#07010f; }

/* ── Timeline ── */
.tl { position:relative; padding-left:2.2rem; }
.tl::before {
    content:''; position:absolute; left:.55rem; top:0; bottom:0; width:2px;
    background:linear-gradient(180deg,#b45309,#f59e0b); border-radius:2px;
}
.tl-item { position:relative; margin-bottom:1.4rem; animation:fadeUp .9s ease both; }
.tl-dot  { position:absolute; left:-1.75rem; top:.35rem; width:14px; height:14px; background:#b45309; border:3px solid #fff; border-radius:50%; box-shadow:0 0 0 3px #f59e0b; }
.tl-card { background:#fff; border:1.5px solid var(--border); border-radius:16px; padding:1rem 1.4rem; box-shadow:0 5px 20px #f59e0b12; }
.tl-year { font-size:.68rem; font-weight:900; letter-spacing:.15em; color:#b45309; text-transform:uppercase; }
.tl-mem  { font-size:.95rem; color:#07010f; margin:.2rem 0 0; line-height:1.7; font-weight:700; }

/* ── Message card ── */
.msg-card {
    background:#fff; border:2px solid var(--border);
    border-radius:26px; padding:2.4rem 2rem; text-align:center;
    box-shadow:0 14px 52px #f59e0b22;
    animation:fadeUp 1s ease both, glowPulse 5s ease-in-out infinite;
}
.msg-card p { font-size:1.04rem; line-height:1.9; color:#07010f; margin:0 0 .9rem; font-weight:700; }
.msg-sig { font-family:'Sacramento',cursive; font-size:1.5rem; color:#b45309; margin-top:.8rem; }

/* ── Hope banner ── */
.hope {
    background:linear-gradient(135deg,#1c0a00 0%,#451a03 35%,#b45309 75%,#d97706 100%);
    border-radius:26px; padding:2.8rem 2rem;
    text-align:center; color:#fff;
    box-shadow:0 24px 64px #b4530950;
    animation:fadeUp 1s ease both, glowPulse 4s ease-in-out infinite;
    position:relative; overflow:hidden;
}
.hope::before {
    content:''; position:absolute; top:-50%; left:-50%; width:200%; height:200%;
    background:radial-gradient(ellipse at 30% 40%,#fde68a22 0%,transparent 60%);
    pointer-events:none;
}
.hope h2 { font-family:'Cormorant Garamond',serif; font-size:clamp(1.5rem,4vw,2.2rem); margin:0 0 1rem; font-weight:700; }
.hope p  { font-size:1.02rem; line-height:1.95; opacity:.95; max-width:640px; margin:0 auto; font-weight:500; }

/* ── Footer ── */
.footer { text-align:center; padding:2rem 0 1rem; font-family:'Sacramento',cursive; font-size:1.15rem; color:var(--muted); }

/* ── Button ── */
.stButton > button {
    background:linear-gradient(135deg,#451a03,#d97706) !important;
    color:#fff !important; border:none !important; border-radius:50px !important;
    font-family:'Nunito',sans-serif !important; font-weight:800 !important;
    font-size:.95rem !important; padding:.6rem 2rem !important;
    box-shadow:0 6px 28px #f59e0b55 !important; transition:transform .2s,box-shadow .2s !important;
}
.stButton > button:hover { transform:translateY(-2px) !important; box-shadow:0 12px 36px #f59e0b77 !important; }
</style>
""", unsafe_allow_html=True)

# ── Balloons on load ───────────────────────────────────────────────────────────
if "balloons" not in st.session_state:
    st.session_state.balloons = True
    st.balloons()

# ── LOAD LOCAL PHOTO ─────────────────────────────────────────────────────────
def get_image_base64(path: str) -> str | None:
    p = Path(path)
    if p.exists():
        with open(p, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

img_b64 = get_image_base64("anuradha.jpg")

if img_b64:
    st.markdown(f"""
    <div class="photo-hero">
      <div class="photo-frame">
        <div class="photo-inner">
          <img src="data:image/jpeg;base64,{img_b64}" alt="Anuradha" />
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="photo-hero">
      <div class="photo-frame">
        <div class="photo-inner">
          <span class="ph-icon">🌼</span>
          <span class="ph-txt">Anuradha's photo</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── HERO TEXT ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-badge">✦ A Treasure from Childhood ✦</div>
  <h1>My First Best Friend —<br><span>Anuradha</span> 🌼</h1>
  <span class="hero-sub">Some friendships begin before we even know what friendship means 🍂</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider">✦ ◈ ✦ ◈ ✦</div>', unsafe_allow_html=True)

# ── COUNTER ───────────────────────────────────────────────────────────────────
st.markdown('<p class="sec-label">🌟 Our Bond in Numbers</p>', unsafe_allow_html=True)
st.markdown('<h2 class="sec-title">A Childhood Like No Other</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="ctr-row">
  <div class="ctr-chip"><div class="ctr-val">3</div><div class="ctr-lbl">Classes Together</div></div>
  <div class="ctr-chip"><div class="ctr-val">🌼</div><div class="ctr-lbl">Pure Bond</div></div>
  <div class="ctr-chip"><div class="ctr-val">∞</div><div class="ctr-lbl">Memories</div></div>
  <div class="ctr-chip"><div class="ctr-val">💛</div><div class="ctr-lbl">First Friend</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider">✦ ◈ ✦ ◈ ✦</div>', unsafe_allow_html=True)

# ── QUOTES ────────────────────────────────────────────────────────────────────
st.markdown('<p class="sec-label">💬 Words That Speak Our Bond</p>', unsafe_allow_html=True)
st.markdown('<h2 class="sec-title">Quotes About Childhood Friendship</h2>', unsafe_allow_html=True)
for q, a in [
    ("Childhood friends are the most precious — they knew you before the world shaped you.", "— Unknown"),
    ("A friend who has known you since childhood holds a piece of your truest self.", "— Unknown"),
    ("In the sweetness of friendship let there be laughter and sharing of pleasures.", "— Kahlil Gibran"),
    ("The memories we make in childhood are the ones we carry closest to our hearts forever.", "— Unknown"),
    ("You don't forget your first real friend — they become a part of who you are.", "— Unknown"),
]:
    st.markdown(f'<div class="q-card"><p class="q-text">{q}</p><p class="q-attr">{a}</p></div>', unsafe_allow_html=True)

st.markdown('<div class="divider">✦ ◈ ✦ ◈ ✦</div>', unsafe_allow_html=True)

# ── REASONS ───────────────────────────────────────────────────────────────────
st.markdown('<p class="sec-label">🌸 Everything She Was & Is</p>', unsafe_allow_html=True)
st.markdown('<h2 class="sec-title">Why Anuradha Is Unforgettable 🌼</h2>', unsafe_allow_html=True)
reasons = [
    ("🧸","My First Friend"),("😂","Endless Giggles"),("🎒","Schoolyard Magic"),("🤝","Always Loyal"),
    ("🌻","Warm & Bright"),("📚","Bench Partner"),("💛","Pure Hearted"),("⭐","One of a Kind"),
]
cols4 = st.columns(4)
for i,(icon,label) in enumerate(reasons):
    cols4[i%4].markdown(f'<div class="r-chip"><span class="ri">{icon}</span><span class="rl">{label}</span></div>', unsafe_allow_html=True)

st.markdown('<div class="divider">✦ ◈ ✦ ◈ ✦</div>', unsafe_allow_html=True)

# ── TIMELINE ──────────────────────────────────────────────────────────────────
st.markdown('<p class="sec-label">⏳ How It All Happened</p>', unsafe_allow_html=True)
st.markdown('<h2 class="sec-title">Our Little Story</h2>', unsafe_allow_html=True)
st.markdown('<div class="tl">', unsafe_allow_html=True)
for yr, mem in [
    ("Class 1 — The Beginning 🎒","Two tiny kids, new school bags, nervous smiles. We sat near each other and somehow, without trying, became inseparable."),
    ("Class 2 — The Real Bond 😄","Shared tiffin boxes, stolen pencils, and whispering during lectures. We didn't just share a classroom — we shared everything."),
    ("Class 3 — The Golden Chapter 🌼","Our last year together before life pulled us different ways. We didn't know it then, but those days were some of the most special of our lives."),
    ("Forever in My Heart ✨","We may have walked different paths after Class 3, but Anuradha never left my heart. Childhood friendships don't end — they just live in a softer place inside us."),
]:
    st.markdown(f'<div class="tl-item"><div class="tl-dot"></div><div class="tl-card"><div class="tl-year">{yr}</div><p class="tl-mem">{mem}</p></div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="divider">✦ ◈ ✦ ◈ ✦</div>', unsafe_allow_html=True)

# ── HEARTFELT MESSAGE ─────────────────────────────────────────────────────────
st.markdown('<p class="sec-label">💌 From My Heart</p>', unsafe_allow_html=True)
st.markdown('<h2 class="sec-title">A Note for Anuradha</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="msg-card">
  <p>Dear Anuradha, you were my very first friend — before I even understood what friendship truly meant.
  You were just there, naturally, the way sunshine is just there in the morning.</p>
  <p>I think about those small, golden days — the classroom, the playground, the way we laughed
  at things that made no sense to anyone but us. Those moments were so simple,
  yet somehow they became some of the most beautiful memories I carry.</p>
  <p>Growing up meant growing apart, and life took us on separate roads after Class 3.
  But you left a mark on me that no distance or time could ever erase.
  You were my first chapter, Anuradha — and what a wonderful chapter it was. 🌼</p>
  <div class="msg-sig">With warmth & nostalgia, always 🍂</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider">✦ ◈ ✦ ◈ ✦</div>', unsafe_allow_html=True)

# ── HOPE BANNER ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="hope">
  <h2>🌅 A Wish Across Time 🌅</h2>
  <p>Wherever you are today, Anuradha — I hope life has been as kind to you as you were to me.
  I hope you're surrounded by laughter, by love, by all the good things you deserve.
  You may not know how much those early years meant, but they meant the world.
  Thank you for being my first real friend. 🌼</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
ca, cb, cc = st.columns([1,2,1])
with cb:
    if st.button("🌼 Celebrate Our Childhood Bond!", use_container_width=True):
        st.balloons()
        st.success("💛 Here's to you, Anuradha — my first friend, forever in my heart!")
        time.sleep(0.4)
        st.snow()

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown('<div class="footer">Made with 💛 for Anuradha · First friends, forever remembered 🌼</div>', unsafe_allow_html=True)