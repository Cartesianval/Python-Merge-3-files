import pandas as pd
df1 = pd.read_csv(r'C:/Users/sunan/OneDrive/Desktop/Cassie and Friends/Mailing List/Python Coding/Mailist from Salesforce for Family Day.csv')
df2 = pd.read_csv(r'C:/Users/sunan/OneDrive/Desktop/Cassie and Friends/Mailing List/Python Coding/Maillist from Salesforce for Runs.csv')
df3 = pd.read_csv(r'C:/Users/sunan/OneDrive/Desktop/Cassie and Friends/Mailing List/Python Coding/Subscribed Maillist from Mailchimp.csv')
print("Columns in df1:", df1.columns)
print("Columns in df2:", df2.columns)
print("Columns in df3:", df3.columns)

merge = pd.merge(left=df1, right = df2, how='left', on = 'First Name')
merge2 = pd.merge(left = df2, right = df3, how = 'left', on = 'First Name')
print(merge, merge2)

