import streamlit as st

def calculate_risk(message):
    message = message.lower()

    score = 0
    reasons = []

    if "urgent" in message or "immediately" in message:
        score += 20
        reasons.append("Urgency language detected")

    if "click" in message and "link" in message:
        score += 25
        reasons.append("Suspicious link instruction")

    if "password" in message or "otp" in message:
        score += 30
        reasons.append("Sensitive information request")

    if "win" in message or "prize" in message:
        score += 15
        reasons.append("Too-good-to-be-true offer")

    if "http" in message or "www" in message:
        score += 25
        reasons.append("Suspicious link detected")

    if "account" in message and "verify" in message:
        score += 20
        reasons.append("Account verification scam pattern")

    if "bank" in message or "credit card" in message:
        score += 20
        reasons.append("Financial information targeting")

    if "suspended" in message or "threat" in message:
        score += 15
        reasons.append("Threat-based manipulation detected")

    score = min(score, 100)
    return score, reasons


# UI
st.title("🔐 AI Phishing Detection System")
st.markdown("### 🛡️ Detect phishing messages instantly with AI-powered logic")
st.write("")

user_input = st.text_area(
    "📩 Paste suspicious message/email here:",
    placeholder="Example: Your account has been suspended. Click this link immediately to verify..."
)

analyze = st.button("🔍 Analyze Message")

if analyze:
    if user_input:
        score, reasons = calculate_risk(user_input)

        st.write("")
        st.divider()
        st.subheader("🔎 Analysis Result")
        st.subheader(f"Risk Score: {score}/100")
        st.progress(score / 100)

        if score >= 60:
            st.error("⚠️ High Risk: Likely phishing")
        elif score >= 30:
            st.warning("⚠️ Medium Risk: Be cautious")
        else:
            st.success("✅ Low Risk")

        st.write("### Reasons:")
        for r in reasons:
            st.write(f"- {r}")

        # ✅ Recommended Actions (fixed)
        st.write("### Recommended Actions:")

        if score >= 60:
            st.write("- Do NOT click any links")
            st.write("- Do NOT share personal information")
            st.write("- Report this message as phishing")

        elif score >= 30:
            st.write("- Verify sender before taking action")
            st.write("- Avoid clicking suspicious links")

        else:
            st.write("- Message appears safe, but stay cautious")

    else:
        st.warning("Please enter a message")
        st.divider()
st.caption("Built by Chehak | AI + Cybersecurity Project 🚀")