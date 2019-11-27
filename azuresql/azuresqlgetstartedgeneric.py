#%%
import pyodbc
server = 'server.database.windows.net'
database = 'database'
username = 'username'
password = 'password'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#%%
#Sample select query to get SQL server version
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()

#%%
# Sample Query from dbo.Campaign
cursor.execute("SELECT * FROM table ")
row = cursor.fetchone()
while row:
    print (str(row[0]))
    row = cursor.fetchone()


#%%
# INSERT ROW
#Sample insert query
cursor.execute("INSERT table (Id, StartDate, EndDate, StartLat, StartLong, EndLat, EndLong, Locomotion, IsAIDriven, TracedRiverSide ) VALUES (NEWID(),'2007-04-30', '2007-04-30', 1, 1, 1, 1, 'paris',0, 'test' )")
cnxn.commit()

#%%
# Sample Query from dbo.Campaign
cursor.execute("SELECT * FROM table ")
row = cursor.fetchone()
while row:
    print (str(row[0]))
    row = cursor.fetchone()


#%%
cursor.execute("SELECT COUNT(*) FROM table ")
row = cursor.fetchone()
while row:
    print (str(row[0]))
    row = cursor.fetchone()

# %%
cursor.execute("DELETE FROM table WHERE Id = '<one-id-previously-created>' ")
cnxn.commit()

#%%
cursor.execute("SELECT COUNT(*) FROM table ")
row = cursor.fetchone()
while row:
    print (str(row[0]))
    row = cursor.fetchone()

