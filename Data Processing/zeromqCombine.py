import pandas as pd

# Load the CSV data into a DataFrame
df1 = pd.read_csv('ZEROMQ_Normal.csv')

# Create a new column with calculated values
df1['Traffic'] = 'Normal'

# Write the updated DataFrame back to a CSV file
df1.sample(n = 10000).to_csv('zeromqNormal.csv', index=False)

#===========================================

# Load the CSV data into a DataFrame
df2 = pd.read_csv('ZEROMQ_MHDdos.csv')

# Create a new column with calculated values
df2['Traffic'] = 'MHDdos'

# Write the updated DataFrame back to a CSV file
df2.sample(n = 10000).to_csv('zeromqMHDdos.csv', index=False)

#===========================================

# Load the CSV data into a DataFrame
df3 = pd.read_csv('ZEROMQ_Smurf.csv')

# Create a new column with calculated values
df3['Traffic'] = 'Smurf'

# Write the updated DataFrame back to a CSV file
df3.sample(n = 10000).to_csv('zeromqSmurf.csv', index=False)

#===========================================

# Load the CSV data into a DataFrame
df4 = pd.read_csv('ZEROMQ_SynAttack.csv')

# Create a new column with calculated values
df4['Traffic'] = 'Syn'

# Write the updated DataFrame back to a CSV file
df4.sample(n = 10000).to_csv('zeromqSyn.csv', index=False)

#===========================================

# Load the CSV data into a DataFrame
df5 = pd.read_csv('ZEROMQ_SynRandomSource.csv')

# Create a new column with calculated values
df5['Traffic'] = 'SynRandom'

# Write the updated DataFrame back to a CSV file
df5.sample(n = 10000).to_csv('zeromqSynRandom.csv', index=False)

#===========================================

# Load the CSV data into a DataFrame
df6 = pd.read_csv('ZEROMQ_TCPSpa.csv')

# Create a new column with calculated values
df6['Traffic'] = 'TCPSpa'

# Write the updated DataFrame back to a CSV file
df6.sample(n = 6000).to_csv('zeromqTCPSpa.csv', index=False)