
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("scholartrack_applications_cleaned.csv")

# 1. Application status analysis
print("\n--- Application Status ---")
print(df["application_status"].value_counts())

df["application_status"].value_counts().plot(
    kind="bar",
    title="Scholarship Applications by Status"
)
plt.xlabel("Application Status")
plt.ylabel("Number of Applications")
plt.tight_layout()
plt.savefig("status_chart.png")
plt.show()

# 2. State-wise application analysis
print("\n--- Top 10 States by Applications ---")
state_counts = df["state"].value_counts().head(10)
print(state_counts)

state_counts.plot(
    kind="bar",
    title="Top 10 States by Applications"
)
plt.xlabel("State")
plt.ylabel("Number of Applications")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("state_chart.png")
plt.show()

print("\nAnalysis complete!")
print("Charts saved as status_chart.png and state_chart.png")
