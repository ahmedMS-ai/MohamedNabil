\
# Agent Thread Landing — Streamlit (Pixel-Match Starter)

This repo is a **pixel-matchable** Streamlit landing template for your Felo preview page.  
It ships with tokens and sections to mirror the layout 1:1 once you replace content and assets.

## Quickstart
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Match 1:1 Checklist
1. Replace headlines/subcopy in `content.yaml` with your exact text.
2. Put your exported hero/screenshot images into `assets/` using the same filenames (`hero.png`, `logo.svg`…).
3. If spacing/widths differ, tweak values in `tokens.yaml` (e.g., `maxw`, `radius`, colors).
4. If needed, adjust section order/visibility by editing `content.yaml` blocks.

## Optional: Import script
Use `scripts/import_from_preview.py` to fetch basic metadata (title/desc/og:image) from your preview URL to prefill `content.yaml`. (Dynamic/JS-driven content may still require manual paste.)

## Folder
```
.
├─ app.py
├─ styles.css
├─ tokens.yaml
├─ content.yaml
├─ .streamlit/config.toml
├─ assets/
│  ├─ hero.png
│  └─ logo.svg
└─ scripts/
   └─ import_from_preview.py
```
