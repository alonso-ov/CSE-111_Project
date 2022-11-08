import pandas as pd
import numpy as np

df = pd.read_csv("cast_member.csv")

df["cm_cmid"] = np.arange(len(df))

df.to_csv("cast_member_mod.csv", index=False)