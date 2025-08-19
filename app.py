import streamlit as st
import os
import sys

st.set_page_config(
    page_title="PassGuard Security Analyzer",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="auto"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

try:
    from strength_checker import score_password
    from bruteforce_estimator import estimate_bruteforce_time
    from simulated_dictionary_attack import dictionary_attack
except ImportError:
    st.error("Failed to import required analysis modules from the 'src' directory. Please ensure strength_checker.py, bruteforce_estimator.py, and simulated_dictionary_attack.py are present.")
    st.stop()

def add_custom_css():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
            background-attachment: fixed;
            background-size: cover;
            color: #E2E8F0;
        }

        [data-testid="stAppViewContainer"] > .main {
            background-color: rgba(15, 23, 42, 0.85);
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }
        
        h1 {
            text-align: center;
        }

        .stButton>button {
            border-radius: 10px;
            border: 1px solid #A770EF;
            color: #A770EF;
            background-color: transparent;
            transition: all 0.3s ease-in-out;
            display: block;
            margin: 0 auto;
        }
        .stButton>button:hover {
            border-color: #FFFFFF;
            color: #FFFFFF;
            background: linear-gradient(to right, #A770EF, #CF8BF3, #FDB99B);
        }
        .stButton>button:focus {
            box-shadow: 0 0 0 2px #A770EF;
        }
        
        .stTextInput > div > div > input {
            background-color: #0F172A;
            color: #E2E8F0;
            border-radius: 10px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

add_custom_css()

st.title("🔐 PassGuard: Password Security Analyzer")
st.markdown(
    """
    <p style='text-align: center; font-size:18px;'>
    Enter a password below to receive a comprehensive security report, including strength analysis, brute-force resistance, and a simulated dictionary attack.
    </p>
""", unsafe_allow_html=True)

password = st.text_input("Enter a password to analyze", type="password", label_visibility="collapsed", placeholder="Enter your password here...")

if st.button("Analyze Password"):
    if password:
        with st.spinner('Running comprehensive analysis...'):
            st.subheader("📊 Strength Analysis")
            strength = score_password(password)
            score = strength['score']
            label = strength['label']

            st.metric(label="Strength Score", value=f"{score}/100")
            st.progress(score / 100)
            
            if label == "Very Weak":
                st.error(f"**Status:** {label}")
            elif label == "Weak":
                st.warning(f"**Status:** {label}")
            elif label == "Moderate":
                st.info(f"**Status:** {label}")
            elif label == "Strong":
                st.success(f"**Status:** {label}")
            elif label == "Very Strong":
                st.success(f"**Status:** {label} 💪")

            col1, col2 = st.columns(2)
            with col1:
                st.info(f"**Length:** {strength['length']}")
            with col2:
                st.info(f"**Character Categories:** {', '.join(strength['categorize'])}")

            with st.expander("💡 Improvement Tips"):
                for tip in strength['tips']:
                    st.markdown(f"- {tip}")
            st.markdown("---")

            st.subheader("⏳ Brute Force Resistance")
            estimate = estimate_bruteforce_time(password)
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Charset Size", f"{estimate['charset_size']}")
            col2.metric("Password Length", f"{estimate['length']}")
            col3.metric("Avg. Guesses", f"{estimate['avg_guesses']:.2e}")

            st.write("**Time to Crack Estimates:**")
            st.markdown(f"""
            - **Supercomputer (1B guesses/sec):** `{estimate['time_at_1e9_gps']}`
            - **Online Attack (1M guesses/sec):** `{estimate['time_at_1e6_gps']}`
            - **Offline Attack (1K guesses/sec):** `{estimate['time_at_1e3_gps']}`
            """)
            st.markdown("---")

            st.subheader("📖 Dictionary Attack Simulation")
            result = dictionary_attack(password)

            if result["success"]:
                st.error(f"**Vulnerable!** Password found in the dictionary.")
                st.markdown(f"""
                - **Match Found:** `{result['match']}`
                - **Attempts:** `{result['attempts']}`
                - **Time Taken:** `{result['time']:.6f} seconds`
                """)
            else:
                st.success("**Resistant!** Password was not found in the dictionary.")
                st.markdown(f"Searched **{result['attempts']}** words in **{result['time']:.6f}** seconds.")

    else:
        st.warning("Please enter a password to analyze.")
