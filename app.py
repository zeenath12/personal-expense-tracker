import streamlit as st
import pandas as pd
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💸",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: #0f172a;
    color: white;
}

section[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #1f2937;
}

.main-title {
    font-size: 42px;
    font-weight: 700;
    color: white;
    margin-bottom: 5px;
}

.sub-text {
    color: #94a3b8;
    font-size: 16px;
    margin-bottom: 25px;
}

.card {
    background: linear-gradient(145deg,#1e293b,#111827);
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #334155;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}

.metric-value {
    font-size: 32px;
    font-weight: bold;
    color: white;
}

.metric-label {
    color: #94a3b8;
    font-size: 15px;
}

.small-card {
    background: #1e293b;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #334155;
    height: 160px;
}

div[data-testid="metric-container"] {
    background-color: #1e293b;
    border: 1px solid #334155;
    padding: 10px;
    border-radius: 15px;
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(90deg,#6366f1,#8b5cf6);
    color: white;
    border: none;
    height: 45px;
    font-weight: 600;
}

.stButton>button:hover {
    transform: scale(1.01);
    transition: 0.2s;
}

.shortcut-box {
    background: #111827;
    border: 1px solid #334155;
    padding: 12px;
    border-radius: 12px;
    margin-top: 10px;
}

.welcome-box {
    background: linear-gradient(145deg,#1e293b,#111827);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #334155;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "transactions" not in st.session_state:
    st.session_state.transactions = []

# ---------------- SIDEBAR ----------------
st.sidebar.title("💸 Expense Tracker")

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

page = st.sidebar.radio(
    "Navigate",
    ["Dashboard", "Add Transaction", "Transactions", "Analytics"],
    index=["Dashboard", "Add Transaction", "Transactions", "Analytics"].index(
        st.session_state.page
    )
)

st.session_state.page = page

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚡ Shortcuts")

if st.sidebar.button("➕ Quick Add Income"):
    st.session_state.quick_type = "Income"
    st.session_state.page = "Add Transaction"

if st.sidebar.button("💸 Quick Add Expense"):
    st.session_state.quick_type = "Expense"
    st.session_state.page = "Add Transaction"

st.sidebar.markdown("""
<div class="shortcut-box">
<b>Keyboard Friendly Tips</b><br><br>

• Press TAB → Move fields<br>
• ENTER → Submit quickly<br>
• Sidebar → Fast navigation
</div>
""", unsafe_allow_html=True)

# ---------------- DATAFRAME ----------------
df = pd.DataFrame(st.session_state.transactions)

# ---------------- CALCULATIONS ----------------
if not df.empty:
    total_income = df[df["Type"] == "Income"]["Amount"].sum()
    total_expense = df[df["Type"] == "Expense"]["Amount"].sum()
    balance = total_income - total_expense
else:
    total_income = 0
    total_expense = 0
    balance = 0

# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    st.markdown(
        '<div class="main-title">💰 Personal Expense Tracker</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-text">Track income, control spending, and manage your money smarter.</div>',
        unsafe_allow_html=True
    )

    # ---------------- WELCOME NOTE ----------------

    st.markdown("""
    <div class="welcome-box">

    <h3 style="color:white;">👋 Welcome</h3>

    <p style="color:#cbd5e1; font-size:15px;">
    Welcome to your smart Personal Expense Tracker.
    Easily manage your income and expenses, monitor your balance,
    and understand your spending habits with clean analytics and fast shortcuts.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # ---------------- FEATURES ----------------

    st.markdown("## ✨ Features")

    f1, f2, f3, f4 = st.columns(4)

    with f1:
        st.markdown("""
        <div class="small-card">
        <h4>💵 Income Tracking</h4>
        <p>Add and manage income records quickly.</p>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="small-card">
        <h4>💸 Expense Tracking</h4>
        <p>Track all expenses category-wise.</p>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="small-card">
        <h4>📊 Analytics</h4>
        <p>View spending summaries and charts.</p>
        </div>
        """, unsafe_allow_html=True)

    with f4:
        st.markdown("""
        <div class="small-card">
        <h4>⚡ Quick Access</h4>
        <p>Use shortcuts for faster transaction entry.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- METRIC CARDS ----------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
            <div class="metric-label">💵 Total Income</div>
            <div class="metric-value">₹ {total_income:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <div class="metric-label">💸 Total Expenses</div>
            <div class="metric-value">₹ {total_expense:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card">
            <div class="metric-label">🏦 Remaining Balance</div>
            <div class="metric-value">₹ {balance:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## 📌 Quick Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="small-card">
        <h3>{len(df)}</h3>
        <p>Total Transactions</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        expense_count = len(df[df["Type"] == "Expense"]) if not df.empty else 0

        st.markdown(f"""
        <div class="small-card">
        <h3>{expense_count}</h3>
        <p>Expenses Added</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        income_count = len(df[df["Type"] == "Income"]) if not df.empty else 0

        st.markdown(f"""
        <div class="small-card">
        <h3>{income_count}</h3>
        <p>Income Entries</p>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="small-card">
        <h3>₹ {balance:,.0f}</h3>
        <p>Current Balance</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- ADD TRANSACTION ----------------
elif page == "Add Transaction":

    st.title("➕ Add New Transaction")

    default_type = st.session_state.get("quick_type", "Expense")

    with st.form("transaction_form", clear_on_submit=True):

        transaction_type = st.selectbox(
            "Transaction Type",
            ["Income", "Expense"],
            index=0 if default_type == "Income" else 1
        )

        if transaction_type == "Income":
            category = st.text_input(
                "Income Source",
                placeholder="Salary / Freelancing / Business"
            )

        else:
            category = st.selectbox(
                "Expense Category",
                ["Food", "Travel", "Shopping",
                 "Bills", "Education", "Medical", "Others"]
            )

        col1, col2 = st.columns(2)

        with col1:
            amount = st.number_input(
                "Amount (₹)",
                min_value=0.0,
                format="%.2f"
            )

        with col2:
            transaction_date = st.date_input("Date")

        description = st.text_area(
            "Description",
            placeholder="Add small note..."
        )

        submit = st.form_submit_button("Save Transaction")

        if submit:

            new_transaction = {
                "Type": transaction_type,
                "Category": category,
                "Amount": amount,
                "Date": transaction_date.strftime("%d-%m-%Y"),
                "Description": description,
                "Time": datetime.now().strftime("%I:%M %p")
            }

            st.session_state.transactions.append(new_transaction)

            st.success("✅ Transaction Added Successfully")

# ---------------- TRANSACTIONS ----------------
elif page == "Transactions":

    st.title("📜 Transaction History")

    if not df.empty:

        search = st.text_input(
            "🔍 Search Transactions",
            placeholder="Search category or description..."
        )

        filtered_df = df.copy()

        if search:
            filtered_df = filtered_df[
                filtered_df.astype(str)
                .apply(lambda x: x.str.contains(search, case=False))
                .any(axis=1)
            ]

        st.dataframe(
            filtered_df,
            use_container_width=True,
            height=450
        )

    else:
        st.info("No transactions added yet.")

# ---------------- ANALYTICS ----------------
elif page == "Analytics":

    st.title("📊 Expense Analytics")

    if not df.empty:

        expense_df = df[df["Type"] == "Expense"]

        if not expense_df.empty:

            st.subheader("Category-wise Spending")

            category_summary = (
                expense_df.groupby("Category")["Amount"]
                .sum()
                .sort_values(ascending=False)
            )

            st.bar_chart(category_summary)

            st.subheader("Expense Breakdown")

            st.dataframe(
                category_summary.reset_index(),
                use_container_width=True
            )

        else:
            st.warning("No expense data available.")

    else:
        st.info("Add some transactions to view analytics.")