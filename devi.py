import streamlit as st
import time

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="For Janvi 💖",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lato:wght@300;400;700&family=Dancing+Script:wght@600;700&display=swap');

/* ── Root palette ── */
:root {
    --rose:     #f43f72;
    --blush:    #fde8ef;
    --petal:    #fbb6ce;
    --mauve:    #c084a0;
    --lavender: #ede9fe;
    --gold:     #f59e0b;
    --cream:    #fffbf7;
    --text:     #3d1f2e;
    --muted:    #9d6b80;
}

/* ── Base reset ── */
html, body, [class*="css"] {
    font-family: 'Lato', sans-serif;
    color: var(--text);
}

.stApp {
    background: linear-gradient(135deg, #fff0f6 0%, #fde8ef 30%, #ede9fe 70%, #fff0f6 100%);
    background-attachment: fixed;
}

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1rem; padding-bottom: 3rem; max-width: 900px; }

/* ── Floating hearts background ── */
.hearts-bg {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    pointer-events: none; z-index: 0; overflow: hidden;
}
.heart {
    position: absolute; bottom: -60px; font-size: 1.4rem; opacity: 0;
    animation: floatUp 8s ease-in infinite;
}
.heart:nth-child(1)  { left:  5%; animation-delay: 0s;   animation-duration: 9s; }
.heart:nth-child(2)  { left: 15%; animation-delay: 1.5s; animation-duration: 7s; }
.heart:nth-child(3)  { left: 25%; animation-delay: 3s;   animation-duration: 8s; }
.heart:nth-child(4)  { left: 38%; animation-delay: 0.7s; animation-duration: 10s; }
.heart:nth-child(5)  { left: 52%; animation-delay: 2.2s; animation-duration: 7.5s; }
.heart:nth-child(6)  { left: 65%; animation-delay: 4s;   animation-duration: 9s; }
.heart:nth-child(7)  { left: 75%; animation-delay: 1s;   animation-duration: 8.5s; }
.heart:nth-child(8)  { left: 88%; animation-delay: 3.5s; animation-duration: 7s; }
.heart:nth-child(9)  { left: 92%; animation-delay: 5s;   animation-duration: 9.5s; }
.heart:nth-child(10) { left: 45%; animation-delay: 6s;   animation-duration: 8s; }

@keyframes floatUp {
    0%   { bottom: -60px; opacity: 0; transform: translateX(0) scale(0.8); }
    10%  { opacity: 0.6; }
    90%  { opacity: 0.3; }
    100% { bottom: 110vh; opacity: 0; transform: translateX(30px) scale(1.2); }
}

/* ── Sparkle shimmer animation ── */
@keyframes shimmer {
    0%   { background-position: -200% center; }
    100% { background-position: 200% center; }
}
@keyframes pulse-glow {
    0%, 100% { box-shadow: 0 0 20px rgba(244,63,114,0.2); }
    50%       { box-shadow: 0 0 40px rgba(244,63,114,0.5); }
}
@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(30px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes wiggle {
    0%,100% { transform: rotate(-3deg); }
    50%     { transform: rotate(3deg); }
}

/* ── Hero section ── */
.hero {
    text-align: center;
    padding: 3.5rem 1rem 2.5rem;
    animation: fadeSlideUp 1s ease both;
    position: relative; z-index: 1;
}
.hero-badge {
    display: inline-block;
    background: linear-gradient(90deg, var(--rose), var(--mauve), var(--rose));
    background-size: 200% auto;
    animation: shimmer 3s linear infinite;
    color: white;
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    padding: 0.35rem 1.2rem;
    border-radius: 50px;
    margin-bottom: 1.2rem;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 6vw, 3.8rem);
    font-weight: 700;
    line-height: 1.15;
    background: linear-gradient(135deg, var(--rose) 0%, var(--mauve) 50%, #a855f7 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 0.6rem;
}
.hero-sub {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(1.1rem, 3vw, 1.6rem);
    color: var(--mauve);
    margin-bottom: 0;
}

/* ── Section labels ── */
.section-label {
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--mauve);
    margin-bottom: 0.4rem;
    animation: fadeSlideUp 0.8s ease both;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.5rem, 4vw, 2.2rem);
    font-weight: 700;
    color: var(--text);
    margin: 0 0 1.5rem;
    animation: fadeSlideUp 0.9s ease both;
}

/* ── Divider ── */
.fancy-divider {
    text-align: center;
    margin: 2.5rem 0;
    color: var(--petal);
    font-size: 1.4rem;
    letter-spacing: 0.6rem;
    animation: fadeSlideUp 0.8s ease both;
}

/* ── Photo cards ── */
.photo-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.5rem; margin-bottom: 2rem; }
.photo-card {
    background: white;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 8px 30px rgba(244,63,114,0.12);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    animation: fadeSlideUp 1s ease both;
    animation: pulse-glow 4s ease-in-out infinite;
}
.photo-card:hover { transform: translateY(-6px) scale(1.02); box-shadow: 0 16px 40px rgba(244,63,114,0.25); }
.photo-placeholder {
    width: 100%; aspect-ratio: 4/3;
    background: linear-gradient(135deg, var(--blush) 0%, var(--lavender) 100%);
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    gap: 0.5rem;
}
.photo-placeholder .ph-icon { font-size: 2.8rem; animation: wiggle 3s ease-in-out infinite; }
.photo-placeholder .ph-text { font-family: 'Dancing Script', cursive; font-size: 1rem; color: var(--mauve); }
.photo-caption {
    padding: 0.9rem 1rem 1rem;
    text-align: center;
    font-family: 'Dancing Script', cursive;
    font-size: 1.05rem;
    color: var(--mauve);
    font-weight: 600;
}

/* ── Quote cards ── */
.quote-stack { display: flex; flex-direction: column; gap: 1.2rem; }
.quote-card {
    background: white;
    border-left: 5px solid var(--rose);
    border-radius: 0 16px 16px 0;
    padding: 1.2rem 1.5rem;
    box-shadow: 0 4px 20px rgba(244,63,114,0.08);
    transition: transform 0.25s ease;
    animation: fadeSlideUp 1s ease both;
    position: relative;
}
.quote-card:hover { transform: translateX(6px); }
.quote-card::before {
    content: '"';
    font-family: 'Playfair Display', serif;
    font-size: 5rem;
    color: var(--blush);
    position: absolute;
    top: -10px; left: 12px;
    line-height: 1;
}
.quote-text {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 1.05rem;
    color: var(--text);
    margin: 0 0 0.4rem;
    padding-left: 1rem;
}
.quote-attr { font-size: 0.78rem; color: var(--muted); padding-left: 1rem; }

/* ── Message card ── */
.message-card {
    background: linear-gradient(135deg, #fff5f8 0%, #fdf4ff 100%);
    border: 2px solid var(--petal);
    border-radius: 24px;
    padding: 2.5rem;
    text-align: center;
    box-shadow: 0 12px 40px rgba(244,63,114,0.12);
    animation: fadeSlideUp 1s ease both, pulse-glow 5s ease-in-out infinite;
}
.message-card p {
    font-family: 'Lato', sans-serif;
    font-size: 1.05rem;
    line-height: 1.85;
    color: var(--text);
    margin: 0 0 1rem;
}
.message-signature {
    font-family: 'Dancing Script', cursive;
    font-size: 1.4rem;
    color: var(--rose);
    margin-top: 1rem;
}

/* ── Reasons grid ── */
.reasons-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; }
.reason-chip {
    background: white;
    border-radius: 16px;
    padding: 1.2rem 1rem;
    text-align: center;
    box-shadow: 0 4px 16px rgba(244,63,114,0.1);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
    animation: fadeSlideUp 1s ease both;
}
.reason-chip:hover { transform: translateY(-4px); box-shadow: 0 10px 30px rgba(244,63,114,0.2); }
.reason-chip .r-icon { font-size: 2rem; margin-bottom: 0.5rem; display: block; }
.reason-chip .r-text { font-size: 0.88rem; font-weight: 700; color: var(--text); }

/* ── Memory timeline ── */
.timeline { position: relative; padding-left: 2rem; }
.timeline::before {
    content: '';
    position: absolute; left: 0.5rem; top: 0; bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, var(--rose), var(--petal), var(--lavender));
}
.timeline-item {
    position: relative;
    margin-bottom: 1.5rem;
    animation: fadeSlideUp 0.9s ease both;
}
.timeline-dot {
    position: absolute;
    left: -1.65rem; top: 0.3rem;
    width: 14px; height: 14px;
    background: var(--rose);
    border: 3px solid white;
    border-radius: 50%;
    box-shadow: 0 0 0 2px var(--petal);
}
.timeline-card {
    background: white;
    border-radius: 14px;
    padding: 1rem 1.3rem;
    box-shadow: 0 4px 16px rgba(244,63,114,0.08);
}
.timeline-year { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.15em; color: var(--rose); text-transform: uppercase; }
.timeline-memory { font-size: 0.92rem; color: var(--text); margin: 0.2rem 0 0; }

/* ── Hope banner ── */
.hope-banner {
    background: linear-gradient(135deg, var(--rose) 0%, #c026a0 50%, #7c3aed 100%);
    border-radius: 24px;
    padding: 2.5rem 2rem;
    text-align: center;
    color: white;
    box-shadow: 0 16px 50px rgba(244,63,114,0.35);
    animation: fadeSlideUp 1s ease both, pulse-glow 4s ease-in-out infinite;
}
.hope-banner h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.4rem, 4vw, 2rem);
    margin: 0 0 1rem;
    font-weight: 700;
}
.hope-banner p {
    font-size: 1.05rem;
    line-height: 1.9;
    opacity: 0.92;
    max-width: 620px;
    margin: 0 auto;
}

/* ── Counter bar ── */
.counter-row { display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center; }
.counter-chip {
    background: white;
    border-radius: 16px;
    padding: 1.3rem 1.8rem;
    text-align: center;
    box-shadow: 0 4px 20px rgba(244,63,114,0.1);
    min-width: 130px;
    animation: fadeSlideUp 1s ease both;
}
.counter-val {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--rose);
    line-height: 1;
}
.counter-lbl { font-size: 0.75rem; color: var(--muted); margin-top: 0.3rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; }

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 2rem 0 1rem;
    font-family: 'Dancing Script', cursive;
    font-size: 1.1rem;
    color: var(--mauve);
    animation: fadeSlideUp 1s ease both;
}
</style>
""", unsafe_allow_html=True)

# ── Floating hearts background ─────────────────────────────────────────────
st.markdown("""
<div class="hearts-bg">
  <span class="heart">💗</span><span class="heart">🌸</span><span class="heart">💖</span>
  <span class="heart">✨</span><span class="heart">💕</span><span class="heart">🌺</span>
  <span class="heart">💗</span><span class="heart">🌸</span><span class="heart">💖</span>
  <span class="heart">💞</span>
</div>
""", unsafe_allow_html=True)

# ── HERO ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-badge">✨ A Celebration of Friendship ✨</div>
  <h1>A Special Friendship<br>for Janvi 💖</h1>
  <p class="hero-sub">Because some bonds are simply meant to last forever 🌸</p>
</div>
""", unsafe_allow_html=True)

# ── Balloons on first load ─────────────────────────────────────────────────
if "balloons" not in st.session_state:
    st.session_state.balloons = True
    st.balloons()

st.markdown('<div class="fancy-divider">❀ ♡ ❀ ♡ ❀</div>', unsafe_allow_html=True)

# ── FRIENDSHIP COUNTER ─────────────────────────────────────────────────────
st.markdown('<p class="section-label">📅 Our Journey Together</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Friendship at a Glance</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="counter-row">
  <div class="counter-chip">
    <div class="counter-val">∞</div>
    <div class="counter-lbl">Memories Made</div>
  </div>
  <div class="counter-chip">
    <div class="counter-val">💯</div>
    <div class="counter-lbl">Trust &amp; Loyalty</div>
  </div>
  <div class="counter-chip">
    <div class="counter-val">☕</div>
    <div class="counter-lbl">Chats &amp; Coffee</div>
  </div>
  <div class="counter-chip">
    <div class="counter-val">1</div>
    <div class="counter-lbl">Friendship Like This</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="fancy-divider">❀ ♡ ❀ ♡ ❀</div>', unsafe_allow_html=True)

# ── PHOTO SECTION ──────────────────────────────────────────────────────────
st.markdown('<p class="section-label">📸 Our Story in Pictures</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Snapshots of Us</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="photo-card">
      <div class="photo-placeholder">
        <span class="ph-icon">🌸</span>
        <span class="ph-text">Add your photo here</span>
      </div>
      <div class="photo-caption">📍 The day we first met</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="photo-card">
      <div class="photo-placeholder">
        <span class="ph-icon">🎉</span>
        <span class="ph-text">Add your photo here</span>
      </div>
      <div class="photo-caption">🎂 Celebrating together</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="photo-card">
      <div class="photo-placeholder">
        <span class="ph-icon">✨</span>
        <span class="ph-text">Add your photo here</span>
      </div>
      <div class="photo-caption">🌟 Making memories</div>
    </div>
    """, unsafe_allow_html=True)

# ── Custom photo upload (optional) ─────────────────────────────────────────
with st.expander("📷 Upload your own friendship photos"):
    uploaded = st.file_uploader("Choose photos", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    if uploaded:
        cols = st.columns(min(len(uploaded), 3))
        for i, f in enumerate(uploaded):
            cols[i % 3].image(f, use_container_width=True, caption=f.name)

st.markdown('<div class="fancy-divider">❀ ♡ ❀ ♡ ❀</div>', unsafe_allow_html=True)

# ── QUOTES ─────────────────────────────────────────────────────────────────
st.markdown('<p class="section-label">💬 Words That Speak Our Bond</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Quotes About Friendship</h2>', unsafe_allow_html=True)

quotes = [
    ("A true friend is one soul in two bodies.", "— Aristotle"),
    ("Friends are the family we choose for ourselves.", "— Edna Buchanan"),
    ("Good friends make the good times better and the hard times easier.", "— Unknown"),
    ("A real friend is one who walks in when the rest of the world walks out.", "— Walter Winchell"),
    ("In the cookie of life, friends are the chocolate chips.", "— Salman Rushdie"),
]

for q, attr in quotes:
    st.markdown(f"""
    <div class="quote-card">
      <p class="quote-text">{q}</p>
      <p class="quote-attr">{attr}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="fancy-divider">❀ ♡ ❀ ♡ ❀</div>', unsafe_allow_html=True)

# ── REASONS ────────────────────────────────────────────────────────────────
st.markdown('<p class="section-label">🌟 All the Reasons</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Why Janvi Is So Special 💝</h2>', unsafe_allow_html=True)

reasons = [
    ("🌟", "Always Genuine"),
    ("💪", "Incredibly Strong"),
    ("😂", "Makes Me Laugh"),
    ("🤗", "Warm & Caring"),
    ("🎨", "Wildly Creative"),
    ("🌿", "Calming Presence"),
    ("🔥", "Fiercely Loyal"),
    ("💡", "Endlessly Wise"),
]

cols = st.columns(4)
for i, (icon, label) in enumerate(reasons):
    cols[i % 4].markdown(f"""
    <div class="reason-chip">
      <span class="r-icon">{icon}</span>
      <span class="r-text">{label}</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="fancy-divider">❀ ♡ ❀ ♡ ❀</div>', unsafe_allow_html=True)

# ── TIMELINE ───────────────────────────────────────────────────────────────
st.markdown('<p class="section-label">⏳ The Road We've Walked</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Our Friendship Timeline</h2>', unsafe_allow_html=True)

memories = [
    ("The Beginning 🌱", "The universe did something wonderful the day it brought us together. Our story started with a simple hello."),
    ("Building Trust 🤝", "Late-night conversations, shared secrets, and a friendship that grew stronger with every passing day."),
    ("Growing Together 🌸", "Through laughter and tears, celebrations and challenges — we showed up for each other, always."),
    ("Today & Always 💖", "Here we are — and wherever life takes us next, this friendship is one of my greatest treasures."),
]

st.markdown('<div class="timeline">', unsafe_allow_html=True)
for year, mem in memories:
    st.markdown(f"""
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-card">
        <div class="timeline-year">{year}</div>
        <p class="timeline-memory">{mem}</p>
      </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="fancy-divider">❀ ♡ ❀ ♡ ❀</div>', unsafe_allow_html=True)

# ── HEARTFELT MESSAGE ──────────────────────────────────────────────────────
st.markdown('<p class="section-label">💌 From My Heart to Yours</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">A Note for Janvi</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="message-card">
  <p>
    Dearest Janvi, there are people who come into your life and quietly make everything better.
    You are that person for me. You have a rare gift — the ability to see the good in people,
    to listen without judgment, and to love without condition.
  </p>
  <p>
    Thank you for every laugh we've shared, every secret kept, every moment you chose
    to show up when it mattered most. You make ordinary days feel extraordinary,
    and you remind me that life is so much more beautiful when lived alongside a true friend.
  </p>
  <p>
    Words will never be enough to express how grateful I am to have you in my life.
    You are not just a friend — you are family, chosen and cherished. 💖
  </p>
  <div class="message-signature">With all my love, always 🌸</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="fancy-divider">❀ ♡ ❀ ♡ ❀</div>', unsafe_allow_html=True)

# ── HOPE BANNER ────────────────────────────────────────────────────────────
st.markdown("""
<div class="hope-banner">
  <h2>🌟 A Wish for Forever 🌟</h2>
  <p>
    No matter where life takes us, I hope our friendship stays strong, grows with time,
    and never comes to an end. May we always find our way back to each other —
    through distance, through change, through every season of life.
    Thank you for being such an amazing friend, Janvi.
    Here's to us, today, tomorrow, and always. 💖
  </p>
</div>
""", unsafe_allow_html=True)

# ── Interactive celebration button ─────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
col_a, col_b, col_c = st.columns([1, 2, 1])
with col_b:
    if st.button("🎉 Celebrate Our Friendship!", use_container_width=True):
        st.balloons()
        st.success("💖 Here's to a friendship that lasts forever, Janvi!")
        time.sleep(0.5)
        st.snow()

# ── Personalized message input ─────────────────────────────────────────────
st.markdown('<div class="fancy-divider">❀ ♡ ❀ ♡ ❀</div>', unsafe_allow_html=True)
st.markdown('<p class="section-label">✍️ Add Your Words</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Leave a Message for Janvi 💌</h2>', unsafe_allow_html=True)

user_msg = st.text_area(
    "Write something special...",
    placeholder="Type your heartfelt message here... 🌸",
    height=130,
    label_visibility="collapsed",
)
if st.button("💖 Share this message", use_container_width=False):
    if user_msg.strip():
        st.markdown(f"""
        <div class="message-card" style="margin-top:1rem;">
          <p style="font-style:italic;">"{user_msg}"</p>
          <div class="message-signature">— Written with love 💖</div>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.warning("Please write something before sharing 🌸")

# ── FOOTER ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  Made with 💖 for Janvi · Because every great friendship deserves to be celebrated 🌸
</div>
""", unsafe_allow_html=True)