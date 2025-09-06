#GET SUM OF A COLUMN
import pandas as pd
df=pd.DataFrame({"A":[1,2,3,4]})
print(df["A"].sum())
#GET MEAN OF A COLUMN
import pandas as pd
df=pd.DataFrame({"A":[1,2,3,4]})
print(df["A"].mean())
#GET MEDIAN OF A COLUMN
import pandas as pd
df=pd.DataFrame({"A":[1,2,3,4]})
print(df["A"].median())
#GET MAXIMUM VALUE 
import pandas as pd
df=pd.DataFrame({"A":[1,2,3,4]})
print(df["A"].max())
#GET MINIMUM VALUE
import pandas as pd
df=pd.DataFrame({"A":[1,2,3,4]})
print(df["A"].min())
#CREATE A PANDAS SERIES FROM A LIST
import pandas as pd
data=[10,20,30,40]
s=pd.Series(data)
print(s)
#CREATE A PANDAS DATAFRAME FROM A DICTIONARY
data={"Name":["Alice","Bob","Charlie"],"Age":[25,30,35]}
df=pd.DataFrame(data)
print(df)
#GET THE FIRST 3 ROWS OF A DATAFRAME
data={"Name":["Alice","Bob","Charlie"],"Age":[25,30,35]}
df=pd.DataFrame(data)
print(df.head(3))
#GET THE LAST 2 ROWS OF A DATAFRAME
data={"Name":["Alice","Bob","Charlie"],"Age":[25,30,35]}
df=pd.DataFrame(data)
print(df.tail(2))
#GET COLUMN NAMES OF A DATAFRAME
data={"Name":["Alice","Bob","Charlie"],"Age":[25,30,35]}
df=pd.DataFrame(data)
print(df.columns)
#SELECT A SINGLE COLUMN
data={"Name":["Alice","Bob","Charlie"],"Age":[25,30,35]}
df=pd.DataFrame(data)
print(df["Name"])
#SELECT MULTIPLE COLUMNS
data={"Name":["Alice","Bob","Charlie"],"Age":[25,30,35]}
df=pd.DataFrame(data)
print(df[["Name","Age"]])
#SELECT A ROW BY INDEX 
data={"Name":["Alice","Bob","Charlie"],"Age":[25,30,35]}
df=pd.DataFrame(data)
print(df.loc[0])
#ADD A NEW COLUMN

data={"Name":["Alice","Bob","Charlie"],"Age":[25,30,35]}
df=pd.DataFrame(data)

df["City"]=["Delhi","Mumbai","Odisha"]
print(df)
#DROP A COLUMN
data={"Name":["Alice","Bob","Charlie"],"Age":[25,30,35]}
df=pd.DataFrame(data)
df["City"]=["Delhi","Mumbai","Odisha"]
df=df.drop("City",axis=1)
print(df)
#RENAME A COLUMN
df=df.rename(columns={"Name":"FullName"})
print(df)
#SORT BY AGE
data={"Name":["Alice","Bob","Charlie"],"Age":[25,30,35]}
df=pd.DataFrame(data)
print(df.sort_values("Age"))
#RESET INDEX
data={"Name":["Alice","Bob","Charlie"],"Age":[25,30,35]}
df=pd.DataFrame(data)
df=df.reset_index(drop=True)
print(df)
#CREATE DATAFRAME WITH MISSING VALUE
import pandas as pd
import numpy as np
df=pd.DataFrame({"A":[1,2,np.nan],"B":[4,np.nan,6]})
print(df)
#CHECK FOR MISING VALUES
import pandas as pd
import numpy as np
df=pd.DataFrame({"A":[1,2,np.nan],"B":[4,np.nan,6]})
print(df.isnull())
#COUNT MISSING VALUES IN EACH COLUMN
import pandas as pd
import numpy as np
df=pd.DataFrame({"A":[1,2,np.nan],"B":[4,np.nan,6]})
print(df.isnull().sum())
#FILL MISSING VALUES WITH ZERO
import pandas as pd
import numpy as np
df=pd.DataFrame({"A":[1,2,np.nan],"B":[4,np.nan,6]})
print(df.fillna(0))
#REPLACE SPECIFIC VALUE
df2=pd.DataFrame({"A":[1,2,-1,4]})
print(df2.replace(-1,0))
