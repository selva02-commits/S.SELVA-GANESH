import pandas as pd
import matplotlib.pyplot as selva
sg = pd.read_csv('gender_submission.csv')
print(sg)
Total_Pass = sg["Survived"].value_counts()
total = len(sg)
non_survivors = Total_Pass[0]  # Assuming 0 = non-survivors
survivors = Total_Pass[1]
print(f"Total survivors:{survivors}")
print(f"Total Non survivors:{non_survivors}")
per = (survivors / total) * 100
print(f"Percentage of Survivors is: {per:.2f}%")
per = (non_survivors / total) * 100
print(f"Percentage of Non-Survivors is: {per:.2f}%")
Total_Pass.plot(kind='bar', color=["red", "blue"])
selva.xlabel("Status (0 = Non Survived, 1 = survived)")
selva.ylabel("Number of People")
selva.title("Survived vs Non Survived")
selva.xticks(rotation=0)
selva.show()