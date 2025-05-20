import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import webbrowser
import os

# Set visual style
sns.set(style="whitegrid")

# File path
file_path = r"c:\Users\Muthu Chandiga\Downloads\tamil_nadu_population_distribution.csv"
data = pd.read_csv(file_path)

# Check for required columns
required_columns = ["District", "Male Population", "Female Population"]
if not all(col in data.columns for col in required_columns):
    raise ValueError(f"One or more required columns are missing: {required_columns}")

# Convert population to lakhs
data["Male Population"] = data["Male Population"] / 100000
data["Female Population"] = data["Female Population"] / 100000

# Melt data to long format
data_melted = pd.melt(data,
                      id_vars="District",
                      value_vars=["Male Population", "Female Population"],
                      var_name="Gender",
                      value_name="Population (in Lakhs)")

# Plot grouped bar chart
plt.figure(figsize=(15, 8))

# Add top-level title
plt.suptitle("Prodigy Task 01", fontsize=18, fontweight='bold', y=1.02)

# Create bar plot
sns.barplot(data=data_melted, x="District", y="Population (in Lakhs)", hue="Gender", palette=["skyblue", "pink"])

# Customize
plt.xticks(rotation=45, ha='right')
plt.title("Male vs Female Population by District in Tamil Nadu", fontsize=16)
plt.xlabel("District")
plt.ylabel("Population (in Lakhs)")
plt.legend(title="Gender")

# Adjust layout to fit suptitle
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Save the plot
output_file = os.path.abspath("population_chart.png")
plt.savefig(output_file, bbox_inches='tight')

# Open in Chrome (Windows-specific)
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.get(f'"{chrome_path}" %s').open(f"file:///{output_file}")
