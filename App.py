import streamlit as st

st.set_page_config(page_title="Loan Calculator", page_icon="💰", layout="centered")

st.title("💰 Loan EMI Calculator")
st.markdown("Fill in the details below to calculate your **EMI**, **Interest**, and **Total Closing Amount**.")

st.divider()

# --- Inputs ---
principle = st.number_input("📥 Principal Amount (₹)", min_value=0.0, step=1000.0, format="%.2f",
                             help="The amount you borrowed")

rate = st.number_input("📈 Monthly Interest Rate (%)", min_value=0.0, step=0.1, format="%.2f",
                        help="Enter the monthly rate of interest")

col1, col2 = st.columns(2)
with col1:
    time_years = st.number_input("🗓️ Loan Period (Years)", min_value=0, step=1)
with col2:
    time_months = st.number_input("🗓️ Loan Period (Months)", min_value=0, max_value=11, step=1)

st.divider()

# --- Calculate ---
if st.button("Calculate EMI", use_container_width=True, type="primary"):
    if principle <= 0:
        st.error("Please enter a valid principal amount greater than 0.")
    elif rate <= 0:
        st.error("Please enter a valid interest rate greater than 0.")
    elif time_years == 0 and time_months == 0:
        st.error("Please enter a loan period of at least 1 month.")
    else:
        rate_yearly = rate * 12
        time_total = time_years + (time_months / 12)   # total time in years
        interest = (principle * rate_yearly * time_total) / 100
        final_closing = principle + interest
        emi = (final_closing / time_total) / 12

        st.success("✅ Calculation Complete!")

        c1, c2, c3 = st.columns(3)
        c1.metric("🏦 Total Interest", f"₹ {interest:,.2f}")
        c2.metric("💳 Final Closing Amount", f"₹ {final_closing:,.2f}")
        c3.metric("📅 Monthly EMI", f"₹ {emi:,.2f}")

        st.divider()
        st.markdown("#### 📋 Summary")
        st.table({
            "Detail": ["Principal", "Annual Interest Rate", "Loan Period", "Total Interest", "Final Closing Amount", "Monthly EMI"],
            "Value": [
                f"₹ {principle:,.2f}",
                f"{rate_yearly:.2f}%",
                f"{time_years} yr {time_months} mo",
                f"₹ {interest:,.2f}",
                f"₹ {final_closing:,.2f}",
                f"₹ {emi:,.2f}"
            ]
        })