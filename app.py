# app.py
import time
import random
import html
import streamlit as st

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="AI Chat Assistant (Offline)",
    page_icon="🤖",
    layout="wide",
)

# -----------------------------
# CUSTOM STYLES (4K HD INTERFACE)
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #f8fbff 0%, #ffffff 100%);
    font-family: 'Inter', system-ui, sans-serif;
    color: #0f172a;
}
.chat-container {
    max-width: 1600px;
    margin: 0 auto;
    padding: 20px;
}
.user-bubble {
    background: linear-gradient(90deg, #0ea5e9, #6366f1);
    color: white;
    padding: 14px 18px;
    border-radius: 18px;
    display: inline-block;
    max-width: 78%;
    word-wrap: break-word;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
}
.ai-bubble {
    background: #f1f5f9;
    color: #0f172a;
    padding: 14px 18px;
    border-radius: 18px;
    display: inline-block;
    max-width: 78%;
    word-wrap: break-word;
    box-shadow: 0 8px 24px rgba(2,6,23,0.06);
}
.meta {
    font-size: 12px;
    color: #64748b;
    margin-bottom: 6px;
}
.chat-row { margin: 12px 4px; }
.stTextInput>div>div>input {
    height: 48px;
    font-size: 16px;
    padding: 12px;
}
.stButton>button {
    padding: 10px 18px;
    font-size: 15px;
}
.stMarkdown pre {
    background: #0f172a;
    color: #e6eef8;
    padding: 12px;
    border-radius: 8px;
    overflow: auto;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# STATE INITIALIZATION
# -----------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are an intelligent offline AI assistant that gives helpful and creative answers."}
    ]

# -----------------------------
# LOCAL SIMULATED AI LOGIC
# -----------------------------
def simulate_ai_response(prompt: str) -> str:
    """
    Simple but smart simulated AI logic for offline responses.
    Provides useful, contextual answers without any external API.
    """
    prompt_lower = prompt.lower()

    if any(word in prompt_lower for word in ["code", "python", "function", "program"]):
        return """Sure! Here's a simple Python example:
```python
def greet(name):
    return f"Hello, {name}! How can I help you today?"

print(greet("World"))
```"""

    if "explain" in prompt_lower or "what is" in prompt_lower:
        topic = prompt.replace("explain", "").replace("what is", "").strip().capitalize()
        return f"{topic} is an interesting concept! In simple terms, it means understanding how or why something works by breaking it down clearly and logically."

    if "joke" in prompt_lower:
        return random.choice([
            "Why did the computer go to therapy? It had too many bytes of emotional data!",
            "I told my laptop a joke — it didn’t get it because it was too *deep learning*!",
            "Why do programmers love dark mode? Because light attracts bugs!"
        ])

    if "hello" in prompt_lower or "hi" in prompt_lower:
        return "Hello there! 👋 How can I assist you today?"

    if "summarize" in prompt_lower:
        return "Here's a quick summary: focus on the key idea and keep your explanation short and clear."

    if "translate" in prompt_lower:
        return "Translation (simulated): This is a demo translation of your text."

    # Default smart response
    responses = [
        "That’s an interesting thought — here’s one way to think about it:",
        "Good question! Let’s break it down simply:",
        "Here’s a helpful answer based on what you asked:",
        "Let’s reason through that together:"
    ]
    insights = [
        "It depends on context, but the key idea is clarity and balance.",
        "Always approach such topics with curiosity and logic.",
        "Think of it step-by-step, just like how you’d solve a puzzle.",
        "In short, focus on simplicity and understanding rather than memorization."
    ]
    return f"{random.choice(responses)}\n\n{random.choice(insights)}"

# -----------------------------
# CHAT DISPLAY
# -----------------------------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.title("🤖 AI Chat Assistant (Offline Mode)")
st.caption("Fully working ChatGPT-style chatbot — no API key required!")

# Render existing messages
for msg in st.session_state["messages"]:
    if msg["role"] == "system":
        continue
    is_user = msg["role"] == "user"
    timestamp = time.strftime("%H:%M:%S", time.localtime())
    if is_user:
        st.markdown(f'<div class="meta">You • {timestamp}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-row"><div class="user-bubble">{html.escape(msg["content"])}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="meta">AI • {timestamp}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-row"><div class="ai-bubble">{msg["content"]}</div></div>', unsafe_allow_html=True)

# -----------------------------
# USER INPUT & AI RESPONSE
# -----------------------------
user_input = st.chat_input("Type something...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        time.sleep(0.8)
        ai_reply = simulate_ai_response(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": ai_reply})
    st.experimental_rerun()

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.header("⚙️ Chat Settings")
    if st.button("Clear Chat"):
        st.session_state["messages"] = [
            {"role": "system", "content": "You are an intelligent offline AI assistant that gives helpful and creative answers."}
        ]
        st.experimental_rerun()
    st.markdown("---")
    st.markdown("**App Info**")
    st.info("This is an offline ChatGPT-style chatbot built with Streamlit. No API key needed — responses are simulated intelligently for demos and prototypes.")
