import pandas as pd

# print(pd.__version__)

# data = [67, 69, 100]

# index = pd.Series(data, index =["block 1", "block 2", "block 3"])

# print (index.loc["block 1"])

# here we do data frame from dictionary


data = {
    "Name" : ["Ayan", "mita", "ram"],
    "Age" : ["20", "40", "67"]
}

df = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])

df["Job"] = ["scientist", "engineer", "product manager"]

new_rows = pd.DataFrame([{"name" : "Mark", "Age" : "45", "Job" : "Manager"},
                         {"name" : "Mark", "Age" : "45", "Job" : "Engineer"}],
                         index =["Employee 4", "Employee 5"])

df =pd.concat([df, new_rows])

print(df)