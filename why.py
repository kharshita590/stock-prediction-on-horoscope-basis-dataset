import pandas as pd
import numpy as np
df = pd.read_csv("hi1.csv")
def nu():
    df["instruction"]="you have to provide investment advice on the basis of which planet is present in which house for following  person, tell them in which sector they should invest and provide some sample stocks."
    df["input"] = df.apply(lambda row: f"My name is {row['Name_of_person']}, I was born on {row['DOB']}, and my place of birth is {row['place_of_birth']} at {row['time_of_birth']}, and my zodiac sign is {row['Sign']}.", axis=1)
    df["output"] = df["Investment_Advice"]
    df["output"] = df["output"].replace(np.nan,"Jupiter retrograding, so you should not invest in IT and technology stocks.")
    df.drop(["Planetary_pos","Sign","DOB","Name_of_person","place_of_birth","time_of_birth","latitude","longitude","Investment_Advice"
],axis=1,inplace=True)
    df.to_csv("why.csv", index=False)
nu()
