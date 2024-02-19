## Python Code For Gender Guesser

import pandas as pd
import gender_guesser.detector as gender

df = pd.read_csv("/content/train.csv")

# Checking for dublicates
if df.duplicated().sum() > 0:
  print("There are dublicates and they have been removed")
  df = pd.DataFrame(df)
else:
  print("There are no Dublicates")

# Seperating First and Last Name
if "First Name" in df.columns:
  print("No action needed, they are already seperate")
else:
  df[['first_name', 'last_name']] = df['Customer Name'].str.split(' ', 1, expand=True)

# Demography Customer
if "Gender" in df.columns:
  print("Gender is present")
else:
  print("Gender is not present")
  gender_input = input("Do you want to add gender based on names (yes/no)(default = yes): ")
  gender_input = gender_input.lower()
  if gender_input == "no":
    print("Genders have not been assigned.")
  else:
    gd = gender.Detector()
    df['Gender'] = df['first_name'].map(gd.get_gender)
    print("Estimated Genders have been assigned.")

df.to_csv('data.csv', index=False)
