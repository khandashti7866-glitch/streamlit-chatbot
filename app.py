# app_4k_glass.py
import time
import random
import html
import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Chat Assistant - 4K Glass Edition",
    page_icon="💎",
    layout="wide",
)

# -----------------------------
# CUSTOM CSS — 4K GLASS DESIGN
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
.stApp {
    background: radial-gradient(circle at top right, #e0f2fe 0%, #ffffff 50%, #f8fafc 100%);
    color: #0f172a;
    font-family: 'Inter', system-ui, sans-serif;
}
.chat-container {
    max-width: 1600px;
    margin: 0 auto;
    padding: 30px 60px;
}
.user-bubble, .ai-bubble {
    backdrop-filter: blur(12px) saturate(180%);
    -webkit-backdrop-filter: blur(12px) saturate(180%);
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.3);
    padding: 16px 22px;
    max-width: 75%;
    word-wrap: break-word;
    font-size: 17px;
    line-height: 1.6;
    box-shadow: 0 12px 28px rgba(0,0,0,0.08);
}
.user-bubble {
    background: rgba(56,189,248,0.65);
    color: white;
    margin-left: auto;
}
.ai-bubble {
    background: rgba(241,245,249,0.7);
    color: #0f172a;
    margin-right: auto;
}
.meta {
    font-size: 12px;
    color: #64748b;
    margin: 4px 8px;
}
.chat-row { margin: 18px 0; }
.stTextInput>div>div>input {
    height: 50px;
    font-size: 17px;
    padding: 12px;
    border-radius: 12px;
    border: 1px solid #cbd5e1;
}
.stMarkdown pre {
    background: rgba(15,23,42,0.95);
    color: #e2e8f0;
    padding: 14px;
    border-radius: 10px;
    overflow: auto;
    font-size: 15px;
}
footer, .stToolbar {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# INITIALIZE SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are an intelligent offline AI assistant that provides creative, thoughtful, and clear responses."}
    ]

# -----------------------------
# LOCAL SIMULATED AI RESPONSE
# -----------------------------
def simulate_glass_ai(prompt: str) -> str:
    """Offline intelligent response generator."""
    text = prompt.lower()
    if "hello" in text or "hi" in text:
        return "Hey there 👋! Welcome to your 4K Glass Chat. How can I help you today?"
    if "code" in text or "python" in text:
        return """Sure! Here’s a neat little Python example:
```python
def greet(name):
    print(f"Hello, {name}! How’s your day going?")

greet("User")
```"""
    if "explain" in text:
        return "Sure — let's simplify that: it's basically about understanding the concept by breaking it into small, clear parts."
    if "joke" in text:
        return random.choice([
            "Why did the AI go on a diet? Too many bytes!",
            "Parallel lines have so much in common — it’s a shame they’ll never meet.",
            "Why do computers hate nature? Too many bugs!"
        ])
    if "motivate" in text or "quote" in text:
        return random.choice([
            "💡 Believe in the process — progress always begins with a single step.",
            "🚀 Every expert was once a beginner who refused to give up.",
            "🔥 You don’t need to be extreme — just consistent."
        ])
    return random.choice([
        "That’s an interesting question — here’s one way to think about it:",
        "Let’s reason this through together — step by step:",
        "Hmm 🤔 good thought — here’s my take on it:",
    ]) + "\n\n" + random.choice([
        "It depends on your context, but focus on clarity and curiosity.",
        "Try to simplify the concept in your own words — that’s real understanding.",
        "Balance logic with creativity — that’s how innovation happens."
    ])

# -----------------------------
# RENDER CHAT INTERFACE
# -----------------------------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.title("💎 4K Glass Chat Assistant")
st.caption("An elegant, offline AI assistant with a cinematic, glassmorphic interface — no API key required.")

# Display messages
for msg in st.session_state["messages"]:
    if msg["role"] == "system":
        continue
    is_user = msg["role"] == "user"
    timestamp = time.strftime("%H:%M:%S", time.localtime())
    bubble_class = "user-bubble" if is_user else "ai-bubble"
    role_label = "You" if is_user else "AI"
    st.markdown(f'<div class="meta">{role_label} • {timestamp}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="chat-row"><div class="{bubble_class}">{html.escape(msg["content"]).replace("\\n", "<br/>")}</div></div>', unsafe_allow_html=True)

# Input box
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        time.sleep(0.8)
        ai_reply = simulate_glass_ai(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": ai_reply})
    st.experimental_rerun()

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.header("✨ Chat Controls")
    if st.button("🧹 Clear Chat"):
        st.session_state["messages"] = [
            {"role": "system", "content": "You are an intelligent offline AI assistant that provides creative, thoughtful, and clear responses."}
        ]
        st.experimental_rerun()
    st.markdown("---")
    st.subheader("💡 About This App")
    st.write(
        "This 4K Glass Edition chatbot runs **entirely offline** using a local simulation engine. "
        "It features a modern frosted-glass chat interface and adaptive responses for realistic conversations."
    )
    st.info("Try prompts like:\n- 'Tell me a joke'\n- 'Show me Python code'\n- 'Explain black holes'\n- 'Give me a motivational quote'")
