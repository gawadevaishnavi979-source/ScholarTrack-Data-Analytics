
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="ScholarTrack Dashboard",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 ScholarTrack Dashboard")
st.write("Scholarship Application Analysis System")

# Load cleaned data
df = pd.read_csv("scholartrack_applications_cleaned.csv")

# Summary metrics
total = len(df)
status = df["application_status"].astype(str).str.strip().str.lower()

approved = status.eq("approved").sum()
pending = status.eq("pending").sum()
rejected = status.eq("rejected").sum()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Applications", total)
c2.metric("Approved", int(approved))
c3.metric("Pending", int(pending))
c4.metric("Rejected", int(rejected))

st.divider()

# Status chart
st.subheader("Applications by Status")
status_counts = df["application_status"].value_counts()

fig1, ax1 = plt.subplots()
status_counts.plot(kind="bar", ax=ax1)
ax1.set_xlabel("Application Status")
ax1.set_ylabel("Number of Applications")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
st.pyplot(fig1)
plt.close(fig1)

# State chart
st.subheader("Applications by State")
state_counts = df["state"].fillna("Unknown").value_counts().head(10)

fig2, ax2 = plt.subplots()
state_counts.plot(kind="bar", ax=ax2)
ax2.set_xlabel("State")
ax2.set_ylabel("Number of Applications")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
st.pyplot(fig2)
plt.close(fig2)

# Data table
st.subheader("Application Records")
st.dataframe(df, use_container_width=True)

# Download cleaned data
csv_data = df.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download Cleaned Dataset",
    data=csv_data,
    file_name="scholartrack_applications_cleaned.csv",
    mime="text/csv"
)
