import streamlit as st
from pathlib import Path
import yaml

st.set_page_config(
    page_title="Felo-like Landing",
    page_icon="🪄",
    layout="wide"
)

ROOT = Path(__file__).parent
CONTENT = yaml.safe_load((ROOT / "content.yaml").read_text(encoding="utf-8"))

def load_css():
    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css()

# Top bar
st.markdown(f'''
<header class="topbar">
  <div class="wrap">
    <div class="brand">
      <img src="assets/logo.svg" class="logo" alt="logo"/>
      <span class="brand-text">{CONTENT["brand"]}</span>
    </div>
    <nav class="nav">
      <a href="#features">Features</a>
      <a href="#how">How it works</a>
      <a href="#faq">FAQ</a>
      <a class="btn-primary" href="{CONTENT["cta"]["primary_link"]}" target="_blank" rel="noopener">{CONTENT["cta"]["primary_text"]}</a>
    </nav>
  </div>
</header>
''', unsafe_allow_html=True)

st.markdown("<div class='space-xxl'></div>", unsafe_allow_html=True)

# Hero
st.markdown(f'''
<section class="hero">
  <div class="wrap grid-2">
    <div class="hero-copy">
      <h1>{CONTENT["hero"]["title"]}</h1>
      <p class="lead">{CONTENT["hero"]["subtitle"]}</p>
      <div class="actions">
        <a class="btn-primary" href="{CONTENT["cta"]["primary_link"]}" target="_blank" rel="noopener">{CONTENT["cta"]["primary_text"]}</a>
        <a class="btn-secondary" href="{CONTENT["cta"]["secondary_link"]}" target="_blank" rel="noopener">{CONTENT["cta"]["secondary_text"]}</a>
      </div>
      <div class="badges">
        {''.join([f'<span class="badge">{b}</span>' for b in CONTENT["hero"].get("badges", [])])}
      </div>
    </div>
    <div class="hero-media">
      <img src="assets/hero.jpg" alt="hero" class="hero-img"/>
    </div>
  </div>
</section>
''', unsafe_allow_html=True)

st.markdown("<div class='space-xl' id='features'></div>", unsafe_allow_html=True)

# Features
st.markdown(f"<h2 class='section-title'>{CONTENT['features']['title']}</h2>", unsafe_allow_html=True)
cols = st.columns(3)
for i, item in enumerate(CONTENT["features"]["items"]):
    with cols[i % 3]:
        st.markdown(f'''
        <div class="card feature">
          <div class="icon">{item.get("icon","✨")}</div>
          <h3>{item["title"]}</h3>
          <p>{item["desc"]}</p>
        </div>
        ''', unsafe_allow_html=True)

st.markdown("<div class='space-xl' id='how'></div>", unsafe_allow_html=True)

# How it works
st.markdown(f"<h2 class='section-title'>{CONTENT['how']['title']}</h2>", unsafe_allow_html=True)
for step in CONTENT["how"]["steps"]:
    st.markdown(f'''
    <div class="step">
      <span class="step-index">{step["index"]}</span>
      <div class="step-body">
        <h4>{step["title"]}</h4>
        <p>{step["desc"]}</p>
      </div>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("<div class='space-xl'></div>", unsafe_allow_html=True)

# Quotes / Social proof
if CONTENT.get("quotes"):
    st.markdown(f"<h2 class='section-title'>{CONTENT['quotes']['title']}</h2>", unsafe_allow_html=True)
    row = st.columns(3)
    for i, q in enumerate(CONTENT["quotes"]["items"]):
        with row[i % 3]:
            st.markdown(f'''
            <blockquote class="quote">
              <p>“{q["text"]}”</p>
              <div class="author">
                <img src="{q.get("avatar","")}" class="avatar"/>
                <span>{q["author"]}{(" — " + q["role"]) if q.get("role") else ""}</span>
              </div>
            </blockquote>
            ''', unsafe_allow_html=True)

st.markdown("<div class='space-xl' id='faq'></div>", unsafe_allow_html=True)

# FAQ
if CONTENT.get("faq"):
    st.markdown(f"<h2 class='section-title'>{CONTENT['faq']['title']}</h2>", unsafe_allow_html=True)
    for qa in CONTENT["faq"]["items"]:
        st.markdown(f'''
        <details class="faq">
          <summary>{qa["q"]}</summary>
          <div class="answer">{qa["a"]}</div>
        </details>
        ''', unsafe_allow_html=True)

st.markdown("<div class='space-xl'></div>", unsafe_allow_html=True)

# Footer
st.markdown(f'''
<footer class="footer">
  <div class="wrap grid-3">
    <div>
      <div class="brand">
        <img src="assets/logo.svg" class="logo-sm"/>
        <span class="brand-text">{CONTENT["brand"]}</span>
      </div>
      <p class="muted">{CONTENT["footer"]["blurb"]}</p>
    </div>
    <div>
      <h5>Resources</h5>
      <ul>
        {''.join([f"<li><a href='{l['href']}' target='_blank' rel='noopener'>{l['label']}</a></li>" for l in CONTENT['footer']['links']])}
      </ul>
    </div>
    <div>
      <h5>Get Started</h5>
      <a class="btn-primary" href="{CONTENT["cta"]["primary_link"]}" target="_blank" rel="noopener">{CONTENT["cta"]["primary_text"]}</a>
      <div class="mini-note">No sign-up required</div>
    </div>
  </div>
  <div class="footnote">© {CONTENT["footer"]["year"]} {CONTENT["brand"]}. All rights reserved.</div>
</footer>
''', unsafe_allow_html=True)
