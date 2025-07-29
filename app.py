import streamlit as st
import requests
import cohere

st.set_page_config(page_title="AI Moodboard Composer", layout="centered")
st.title("🎨 AI Moodboard Composer")
st.caption("Generate visual inspiration with the power of Generative AI.")

# ---- API KEYS ----

COHERE_API_KEY = os.getenv("COHERE_API_KEY"))  
co = cohere.Client(COHERE_API_KEY)

prompt = st.text_input("Enter a moodboard theme (e.g., nature calm, tech futuristic, cozy vintage):")

if st.button("✨ Generate Moodboard"):
    if not prompt.strip():
        st.error("Please enter a valid theme prompt.")
        st.stop()

    with st.spinner("🧠 Expanding your idea..."):

        try:
            co_response = co.generate(
                model='command',
                prompt=f"""Expand this theme into a detailed, vivid moodboard description with sensory-rich visuals. 
Include elements like textures, setting, lighting, and emotions. 
Also include made-up but imaginative object ideas or layout suggestions the user could consider: {prompt}""",
                max_tokens=120,
                temperature=0.8
            )
            expanded_prompt = co_response.generations[0].text.strip()
        except Exception as e:
            st.error("⚠️ Prompt expansion failed. Check your Cohere API key.")
            st.stop()

    st.subheader("🔍 Expanded Moodboard Idea")
    st.markdown(f"> {expanded_prompt}")


    with st.spinner("🎨 Generating color palette..."):
        try:
            colormind_resp = requests.post("http://colormind.io/api/", json={"model": "default"})
            palette_rgb = colormind_resp.json().get("result", [])
        except Exception:
            palette_rgb = []

    if palette_rgb:
        st.subheader("🎨 Color Palette")
        cols = st.columns(len(palette_rgb))
        for i, color in enumerate(palette_rgb):
            hex_color = '#%02x%02x%02x' % tuple(color)
            with cols[i]:
                st.markdown(f"<div style='background-color:{hex_color};height:60px;border-radius:5px;'></div>", unsafe_allow_html=True)
                st.caption(hex_color)
    else:
        st.warning("⚠️ Could not fetch color palette.")
