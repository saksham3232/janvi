import streamlit as st
import time
import base64
from pathlib import Path

st.set_page_config(
    page_title="For Janvi 💜",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Nunito:wght@300;400;600;700;800&family=Sacramento&display=swap');

:root {
    --bg:       #f0eaff;
    --surface:  #ffffff;
    --border:   #a78bfa;
    --deep:     #07010f;
    --royal:    #1e0050;
    --violet:   #4a0ea0;
    --mid:      #5b21b6;
    --amethyst: #6d28d9;
    --lavender: #7c3aed;
    --soft:     #ede9fe;
    --muted:    #3b0764;
    --text:     #07010f;
}

html, body, [class*="css"] { font-family:'Nunito',sans-serif; color:var(--text); }

.stApp {
    background-color: #ede8fc;
    background-image:
        radial-gradient(ellipse at 15% 10%, #ddd6fe88 0%, transparent 40%),
        radial-gradient(ellipse at 85% 85%, #c4b5fd55 0%, transparent 40%),
        radial-gradient(ellipse at 50% 50%, #f5f3ff33 0%, transparent 60%);
    background-attachment: fixed;
}

#MainMenu, footer, header { visibility:hidden; }
.block-container { padding-top:1rem; padding-bottom:3rem; max-width:860px; }

@keyframes fadeUp    { from{opacity:0;transform:translateY(24px);} to{opacity:1;transform:translateY(0);} }
@keyframes floatY    { 0%,100%{transform:translateY(0);} 50%{transform:translateY(-7px);} }
@keyframes shimmer   { 0%{background-position:-300% center;} 100%{background-position:300% center;} }
@keyframes glowPulse { 0%,100%{box-shadow:0 0 24px #6d28d933;} 50%{box-shadow:0 0 52px #6d28d955;} }

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
    background: linear-gradient(135deg, #5b21b6, #8b5cf6, #5b21b6);
    padding: 5px;
    box-shadow: 0 16px 56px #6d28d955;
    animation: glowPulse 4s ease-in-out infinite;
}
.photo-inner {
    width: 100%; height: 100%;
    border-radius: 50%;
    background: linear-gradient(135deg, #e4d9ff 0%, #d4c5fc 100%);
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
    background:linear-gradient(90deg,#5b21b6,#7c3aed,#c4a000,#7c3aed,#5b21b6);
    background-size:300% auto;
    animation:shimmer 4s linear infinite;
    color:#fff; font-size:0.7rem; font-weight:800;
    letter-spacing:0.25em; text-transform:uppercase;
    padding:0.38rem 1.4rem; border-radius:50px;
    margin-bottom:1rem;
    box-shadow:0 4px 20px #6d28d966;
}
.hero h1 {
    font-family:'Cormorant Garamond',serif;
    font-size:clamp(2.2rem,6vw,4rem);
    font-weight:700; line-height:1.12;
    color:var(--deep); margin:0 0 0.5rem;
}
.hero h1 span {
    background:linear-gradient(135deg,#5b21b6,#7c3aed);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
}
.hero-sub {
    font-family:'Sacramento',cursive;
    font-size:clamp(1.2rem,3vw,1.7rem);
    color:var(--muted); display:inline-block;
    animation:floatY 4s ease-in-out infinite;
}

.divider { text-align:center; margin:2rem 0; color:var(--lavender); font-size:1.2rem; letter-spacing:0.8rem; }

.sec-label { font-size:0.68rem; font-weight:900; letter-spacing:0.28em; text-transform:uppercase; color:#5b21b6; margin-bottom:0.25rem; }
.sec-title  { font-family:'Cormorant Garamond',serif; font-size:clamp(1.6rem,4vw,2.3rem); font-weight:700; color:#07010f; margin:0 0 1.4rem; }

/* ── Counter ── */
.ctr-row { display:flex; gap:1rem; flex-wrap:wrap; justify-content:center; }
.ctr-chip {
    background:#fff; border:2px solid var(--border);
    border-radius:18px; padding:1.3rem 1.8rem;
    text-align:center; min-width:130px;
    box-shadow:0 6px 24px #6d28d920;
    animation:fadeUp 1s ease both, glowPulse 5s ease-in-out infinite;
    transition:transform .25s;
}
.ctr-chip:hover { transform:translateY(-4px); }
.ctr-val { font-family:'Cormorant Garamond',serif; font-size:2.3rem; font-weight:700; color:#4a0ea0; line-height:1; }
.ctr-lbl { font-size:.7rem; color:#1e0050; margin-top:.3rem; font-weight:900; letter-spacing:.1em; text-transform:uppercase; }

/* ── Quotes ── */
.q-card {
    background:#ffffff;
    border-left:7px solid #4a0ea0;
    border-radius:0 18px 18px 0;
    padding:1.5rem 1.8rem 1.5rem 1.8rem;
    box-shadow:0 6px 28px #4a0ea030;
    margin-bottom:1.1rem;
    transition:transform .25s, box-shadow .25s;
    position:relative; overflow:hidden;
    animation:fadeUp .9s ease both;
}
.q-card:hover { transform:translateX(7px); box-shadow:0 12px 40px #4a0ea050; }
.q-card::before {
    content:'\201C'; font-family:'Cormorant Garamond',serif;
    font-size:6rem; color:#e0d4ff;
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
    color:#2d0654;
    padding-left:1.2rem;
    font-weight:900;
    letter-spacing:.1em;
    position:relative; z-index:1;
}

/* ── Reasons ── */
.r-chip {
    background:#fff; border:2px solid var(--border);
    border-radius:18px; padding:1.2rem 0.8rem; text-align:center;
    box-shadow:0 5px 20px #6d28d915;
    transition:transform .25s, box-shadow .25s, border-color .25s;
    animation:fadeUp 1s ease both;
}
.r-chip:hover { transform:translateY(-5px); box-shadow:0 14px 36px #6d28d930; border-color:var(--lavender); }
.r-chip .ri { font-size:2rem; display:block; margin-bottom:.45rem; animation:floatY 3s ease-in-out infinite; }
.r-chip .rl { font-size:.82rem; font-weight:900; color:#07010f; }

/* ── Timeline ── */
.tl { position:relative; padding-left:2.2rem; }
.tl::before {
    content:''; position:absolute; left:.55rem; top:0; bottom:0; width:2px;
    background:linear-gradient(180deg,var(--violet),var(--lavender)); border-radius:2px;
}
.tl-item { position:relative; margin-bottom:1.4rem; animation:fadeUp .9s ease both; }
.tl-dot  { position:absolute; left:-1.75rem; top:.35rem; width:14px; height:14px; background:var(--violet); border:3px solid #fff; border-radius:50%; box-shadow:0 0 0 3px var(--lavender); }
.tl-card { background:#fff; border:1.5px solid var(--border); border-radius:16px; padding:1rem 1.4rem; box-shadow:0 5px 20px #6d28d912; }
.tl-year { font-size:.68rem; font-weight:900; letter-spacing:.15em; color:#4a0ea0; text-transform:uppercase; }
.tl-mem  { font-size:.95rem; color:#07010f; margin:.2rem 0 0; line-height:1.7; font-weight:700; }

/* ── Message card ── */
.msg-card {
    background:#fff; border:2px solid var(--border);
    border-radius:26px; padding:2.4rem 2rem; text-align:center;
    box-shadow:0 14px 52px #6d28d922;
    animation:fadeUp 1s ease both, glowPulse 5s ease-in-out infinite;
}
.msg-card p { font-size:1.04rem; line-height:1.9; color:#07010f; margin:0 0 .9rem; font-weight:700; }
.msg-sig { font-family:'Sacramento',cursive; font-size:1.5rem; color:var(--violet); margin-top:.8rem; }

/* ── Hope banner ── */
.hope {
    background:linear-gradient(135deg,#0f0520 0%,#2d0654 35%,#5b21b6 75%,#6d28d9 100%);
    border-radius:26px; padding:2.8rem 2rem;
    text-align:center; color:#fff;
    box-shadow:0 24px 64px #5b21b650;
    animation:fadeUp 1s ease both, glowPulse 4s ease-in-out infinite;
    position:relative; overflow:hidden;
}
.hope::before {
    content:''; position:absolute; top:-50%; left:-50%; width:200%; height:200%;
    background:radial-gradient(ellipse at 30% 40%,#a78bfa33 0%,transparent 60%);
    pointer-events:none;
}
.hope h2 { font-family:'Cormorant Garamond',serif; font-size:clamp(1.5rem,4vw,2.2rem); margin:0 0 1rem; font-weight:700; }
.hope p  { font-size:1.02rem; line-height:1.95; opacity:.95; max-width:640px; margin:0 auto; font-weight:500; }

/* ── Footer ── */
.footer { text-align:center; padding:2rem 0 1rem; font-family:'Sacramento',cursive; font-size:1.15rem; color:var(--muted); }

/* ── Button ── */
.stButton > button {
    background:linear-gradient(135deg,#2d0654,#6d28d9) !important;
    color:#fff !important; border:none !important; border-radius:50px !important;
    font-family:'Nunito',sans-serif !important; font-weight:800 !important;
    font-size:.95rem !important; padding:.6rem 2rem !important;
    box-shadow:0 6px 28px #6d28d955 !important; transition:transform .2s,box-shadow .2s !important;
}
.stButton > button:hover { transform:translateY(-2px) !important; box-shadow:0 12px 36px #6d28d977 !important; }
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

img_b64 = get_image_base64("janvi.jpg")

if img_b64:
    st.markdown(f"""
    <div class="photo-hero">
      <div class="photo-frame">
        <div class="photo-inner">
          <img src="data:image/jpeg;base64,{img_b64}" alt="Janvi" />
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="photo-hero">
      <div class="photo-frame">
        <div class="photo-inner">
          <span class="ph-icon">🌸</span>
          <span class="ph-txt">Janvi's photo</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── HERO TEXT ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-badge">✦ A Celebration of Friendship ✦</div>
  <h1>A Special Friendship<br>for <span>Janvi</span> 💜</h1>
  <span class="hero-sub">Because some people find you randomly — and stay forever 🌌</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider">✦ ◈ ✦ ◈ ✦</div>', unsafe_allow_html=True)

# ── COUNTER ───────────────────────────────────────────────────────────────────
st.markdown('<p class="sec-label">✨ Our Bond in Numbers</p>', unsafe_allow_html=True)
st.markdown('<h2 class="sec-title">A Friendship Like No Other</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="ctr-row">
  <div class="ctr-chip"><div class="ctr-val">∞</div><div class="ctr-lbl">Memories</div></div>
  <div class="ctr-chip"><div class="ctr-val">💜</div><div class="ctr-lbl">Pure Bond</div></div>
  <div class="ctr-chip"><div class="ctr-val">1</div><div class="ctr-lbl">Random Meet</div></div>
  <div class="ctr-chip"><div class="ctr-val">✨</div><div class="ctr-lbl">Real Friend</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider">✦ ◈ ✦ ◈ ✦</div>', unsafe_allow_html=True)

# ── QUOTES ────────────────────────────────────────────────────────────────────
st.markdown('<p class="sec-label">💬 Words That Speak Our Bond</p>', unsafe_allow_html=True)
st.markdown('<h2 class="sec-title">Quotes About Friendship</h2>', unsafe_allow_html=True)
for q, a in [
    ("A true friend is one soul in two bodies.", "— Aristotle"),
    ("Friends are the family we choose for ourselves.", "— Edna Buchanan"),
    ("Good friends make the good times better and the hard times easier.", "— Unknown"),
    ("Distance means so little when someone means so much.", "— Tom McNeal"),
    ("We didn't meet by accident — the universe planned it perfectly.", "— Unknown"),
]:
    st.markdown(f'<div class="q-card"><p class="q-text">{q}</p><p class="q-attr">{a}</p></div>', unsafe_allow_html=True)

st.markdown('<div class="divider">✦ ◈ ✦ ◈ ✦</div>', unsafe_allow_html=True)

# ── REASONS ───────────────────────────────────────────────────────────────────
st.markdown('<p class="sec-label">🌟 Everything She Is</p>', unsafe_allow_html=True)
st.markdown('<h2 class="sec-title">Why Janvi Is So Special 💜</h2>', unsafe_allow_html=True)
reasons = [
    ("🌙","Always There"),("💡","Incredibly Wise"),("😄","Makes Me Smile"),("🤝","Genuinely Kind"),
    ("🎨","Wonderfully Creative"),("🌿","Calming Soul"),("🔮","Deeply Thoughtful"),("⭐","One of a Kind"),
]
cols4 = st.columns(4)
for i,(icon,label) in enumerate(reasons):
    cols4[i%4].markdown(f'<div class="r-chip"><span class="ri">{icon}</span><span class="rl">{label}</span></div>', unsafe_allow_html=True)

st.markdown('<div class="divider">✦ ◈ ✦ ◈ ✦</div>', unsafe_allow_html=True)

# ── TIMELINE ──────────────────────────────────────────────────────────────────
st.markdown('<p class="sec-label">⏳ How It All Happened</p>', unsafe_allow_html=True)
st.markdown('<h2 class="sec-title">Our Story Together</h2>', unsafe_allow_html=True)
st.markdown('<div class="tl">', unsafe_allow_html=True)
for yr, mem in [
    ("A Random Hello 🌐","Somewhere in the vast internet, two strangers crossed paths. One simple message changed everything."),
    ("Getting to Know Each Other 💬","Casual chats turned into real conversations — shared laughs, random memes, and a growing connection."),
    ("A Real Friendship Forms 💜","Between the late-night talks and honest moments, a genuine bond was born. Distance meant nothing."),
    ("Today & Always ✨","Here we are. Found each other randomly. Choosing each other every single day since."),
]:
    st.markdown(f'<div class="tl-item"><div class="tl-dot"></div><div class="tl-card"><div class="tl-year">{yr}</div><p class="tl-mem">{mem}</p></div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="divider">✦ ◈ ✦ ◈ ✦</div>', unsafe_allow_html=True)

# ── HEARTFELT MESSAGE ─────────────────────────────────────────────────────────
st.markdown('<p class="sec-label">💌 From My Heart</p>', unsafe_allow_html=True)
st.markdown('<h2 class="sec-title">A Note for Janvi</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="msg-card">
  <p>Dearest Janvi, we met randomly — no plan, no introduction, just a chance moment on the internet.
  Yet here we are, with a friendship that feels anything but accidental.</p>
  <p>You have a rare kind of warmth that travels across screens and still reaches the heart perfectly.
  Talking to you feels like home, even though we may have never shared the same room.</p>
  <p>Thank you for being real in a world full of noise. Thank you for your kindness, your humor,
  your honesty — and for showing up in the most unexpected yet beautiful way.
  I'm so glad the internet brought us together. 💜</p>
  <div class="msg-sig">With love, always 🌙</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider">✦ ◈ ✦ ◈ ✦</div>', unsafe_allow_html=True)

# ── HOPE BANNER ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="hope">
  <h2>🌌 A Wish for Forever 🌌</h2>
  <p>No matter where life takes us — different cities, different timezones, different chapters —
  I hope our friendship stays strong, grows with time, and never comes to an end.
  We found each other randomly, but I choose to keep you intentionally.
  Thank you for being such an amazing friend, Janvi. 💜</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
ca, cb, cc = st.columns([1,2,1])
with cb:
    if st.button("🎉 Celebrate Our Friendship!", use_container_width=True):
        st.balloons()
        st.success("💜 Here's to us, Janvi — found randomly, friends forever!")
        time.sleep(0.4)
        st.snow()

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown('<div class="footer">Made with 💜 for Janvi · Found randomly, friends forever 🌌</div>', unsafe_allow_html=True)