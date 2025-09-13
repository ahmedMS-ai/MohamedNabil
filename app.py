\
import streamlit as st
from pathlib import Path
import yaml, json

st.set_page_config(page_title="Agent Thread Landing", page_icon="🧩", layout="wide")

ROOT = Path(__file__).parent
THEME = yaml.safe_load((ROOT / "tokens.yaml").read_text(encoding="utf-8"))
CONTENT = yaml.safe_load((ROOT / "content.yaml").read_text(encoding="utf-8"))

# Inject CSS and theme tokens
def inject_css():
    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    # Expose tokens as CSS variables
    token_vars = ":root{"+ ";".join([f"--{k}:{v}" for k,v in THEME["css_vars"].items()]) +"}"
    st.markdown(f"<style>{token_vars}\n{css}</style>", unsafe_allow_html=True)

inject_css()

# Topbar
with st.container():
    st.markdown(f"""
    <header class="topbar">
      <div class="wrap">
        <div class="brand">
          <img src="assets/logo.svg" class="logo" alt="logo"/>
          <span class="brand-text">{CONTENT['brand']}</span>
        </div>
        <nav class="nav">
          {''.join([f"<a href='#{item['href']}'>{item['label']}</a>" for item in CONTENT['nav']])}
          <a class="btn-primary" href="{CONTENT['cta']['primary_link']}" target="_blank" rel="noopener">{CONTENT['cta']['primary_text']}</a>
        </nav>
      </div>
    </header>
    """, unsafe_allow_html=True)

st.markdown("<div class='space-xxl'></div>", unsafe_allow_html=True)

# HERO
hero = CONTENT["hero"]
with st.container():
    st.markdown(f"""
    <section class="hero">
      <div class="wrap grid-2">
        <div class="hero-copy">
          <h1>{hero['title']}</h1>
          <p class="lead">{hero['subtitle']}</p>
          <div class="actions">
            <a class="btn-primary" href="{CONTENT['cta']['primary_link']}" target="_blank">{CONTENT['cta']['primary_text']}</a>
            <a class="btn-secondary" href="{CONTENT['cta']['secondary_link']}" target="_blank">{CONTENT['cta']['secondary_text']}</a>
          </div>
          <div class="badges">
            {''.join([f"<span class='badge'>{b}</span>" for b in hero.get('badges',[])])}
          </div>
        </div>
        <div class="hero-media">
          <img src="assets/hero.png" alt="hero" class="hero-img"/>
        </div>
      </div>
    </section>
    """, unsafe_allow_html=True)

# FEATURES
st.markdown(f"<div class='space-xl' id='features'></div>", unsafe_allow_html=True)
if CONTENT.get("features"):
    st.markdown("<h2 class='section-title'>"+CONTENT["features"]["title"]+"</h2>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i, item in enumerate(CONTENT["features"]["items"]):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card feature">
              <div class="icon">{item.get('icon','✨')}</div>
              <h3>{item['title']}</h3>
              <p>{item['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

# STEPS / HOW
st.markdown(f"<div class='space-xl' id='how'></div>", unsafe_allow_html=True)
if CONTENT.get("how"):
    st.markdown("<h2 class='section-title'>"+CONTENT["how"]["title"]+"</h2>", unsafe_allow_html=True)
    for step in CONTENT["how"]["steps"]:
        st.markdown(f"""
        <div class="step">
          <span class="step-index">{step['index']}</span>
          <div class="step-body">
            <h4>{step['title']}</h4>
            <p>{step['desc']}</p>
          </div>
        </div>
        """, unsafe_allow_html=True)

# STATS (optional)
if CONTENT.get("stats"):
    st.markdown("<div class='space-xl'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>"+CONTENT["stats"]["title"]+"</h2>", unsafe_allow_html=True)
    cols = st.columns(len(CONTENT["stats"]["items"]))
    for i, stat in enumerate(CONTENT["stats"]["items"]):
        with cols[i]:
            st.markdown(f"<div class='stat'><div class='stat-num'>{stat['num']}</div><div class='stat-label'>{stat['label']}</div></div>", unsafe_allow_html=True)

# QUOTES
if CONTENT.get("quotes"):
    st.markdown("<div class='space-xl'></div>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>"+CONTENT["quotes"]["title"]+"</h2>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i, q in enumerate(CONTENT["quotes"]["items"]):
        with cols[i % 3]:
            st.markdown(f"""
            <blockquote class="quote">
              <p>“{q['text']}”</p>
              <div class="author">
                <img src="{q.get('avatar','')}" class="avatar"/>
                <span>{q['author']} — {q.get('role','')}</span>
              </div>
            </blockquote>
            """, unsafe_allow_html=True)

# FAQ
st.markdown(f"<div class='space-xl' id='faq'></div>", unsafe_allow_html=True)
if CONTENT.get("faq"):
    st.markdown("<h2 class='section-title'>"+CONTENT["faq"]["title"]+"</h2>", unsafe_allow_html=True)
    for qa in CONTENT["faq"]["items"]:
        st.markdown(f"""
        <details class="faq">
          <summary>{qa['q']}</summary>
          <div class="answer">{qa['a']}</div>
        </details>
        """, unsafe_allow_html=True)

# CTA Footer
st.markdown("<div class='space-xl'></div>", unsafe_allow_html=True)
with st.container():
    st.markdown(f"""
    <footer class="footer">
      <div class="wrap grid-3">
        <div>
          <div class="brand">
            <img src="assets/logo.svg" class="logo-sm"/>
            <span class="brand-text">{CONTENT['brand']}</span>
          </div>
          <p class="muted">{CONTENT['footer']['blurb']}</p>
        </div>
        <div>
          <h5>Resources</h5>
          <ul>
            {''.join([f"<li><a href='{l['href']}' target='_blank' rel='noopener'>{l['label']}</a></li>" for l in CONTENT['footer']['links']])}
          </ul>
        </div>
        <div>
          <h5>Get Started</h5>
          <a class="btn-primary" href="{CONTENT['cta']['primary_link']}" target="_blank" rel="noopener">{CONTENT['cta']['primary_text']}</a>
          <div class="mini-note">No sign-up required</div>
        </div>
      </div>
      <div class="footnote">© {CONTENT['footer']['year']} {CONTENT['brand']}. All rights reserved.</div>
    </footer>
    """, unsafe_allow_html=True)
