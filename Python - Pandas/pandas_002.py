import pandas as pd 
import numpy as np 

#variable input
n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

#membuat DataFrame
df = pd.DataFrame(np.random.randint(1,10,size=(n_rows,n_cols)),columns=cols)
df.add_prefix('kolom_')

print(df) 