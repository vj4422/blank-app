import time import random from datetime import datetime from dateutil.relativedelta import relativedelta import streamlit as st

appliance_info = { “brand”: “Electrolux Professional”, “model”: “WH6-8”, “manufacture_date”: “2021-06” }

def check_warranty(appliance: dict, warranty_years: int) -> str: md = appliance.get(“manufacture_date”, “”) if “-” in md and len(md) == 7: purchase_dt = datetime.strptime(md, “%Y-%m”).date() elif “-” in md and “W” in md: purchase_dt = datetime.strptime(md + “-1”, “%Y-W%W-%w”).date() else: return “⚠️ Unsupported date format.” expiry = purchase_dt + relativedelta(years=warranty_years) today = datetime.today().date() if today <= expiry: left = (expiry - today).days return f”✅ Warranty valid until {expiry:%Y-%m-%d} ({left} days left).” else: late = (today - expiry).days return f”❌ Warranty expired on {expiry:%Y-%m-%d} ({late} days ago).”

def mock_start(program: str, prewash: bool, extra_rinse: bool): time.sleep(1.0) ok = random.random() < 0.9 if ok: return True, f”Start accepted: {program} (prewash={prewash}, extra_rinse={extra_rinse})” return False, “Start rejected: Door open”

st.set_page_config(page_title=“Electrolux Remote Start (Mock)”, page_icon=“🧺”, layout=“centered”) st.title(“Electrolux Remote Start (Mock)”) st.caption(f”{appliance_info[‘brand’]} {appliance_info[‘model’]}”) st.info(check_warranty(appliance_info, 2))

st.subheader(“Ohjelma ja asetukset”) program = st.selectbox(“Program”, [“Cotton 60°C”, “Mixed 40°C”, “Quick 20’”, “Eco 40-60”]) col1, col2 = st.columns(2) with col1: prewash = st.checkbox(“Prewash”, value=False) with col2: extra_rinse = st.checkbox(“Extra rinse”, value=True)

if st.button(“▶ Start (mock)”): with st.status(“Sending start command…”, expanded=True) as status: ok, msg = mock_start(program, prewash, extra_rinse) st.write(msg) if ok: status.update(label=“Running…”, state=“running”) progress = st.progress(0) for i in range(0, 101, 5): time.sleep(0.2) progress.progress(i) status.update(label=“✅ Cycle complete”, state=“complete”) else: status.update(label=“❌ Failed”, state=“error”)

iPhone
