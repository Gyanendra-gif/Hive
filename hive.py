from pyhive import hive
import pandas as pd

# connection = hive.connect(
#     host='localhost',  # host on which the database is running
#     database='bridgelabz',  # name of the database to connect to
#     username='hdoop'  # username to run queries as
# )
try:
    con = hive.Connection(host="localhost", port=10000, database="cpulog")
    user_working_count = pd.read_sql("select user_name ,count('') as total from data where keyboard !=0 or mouse !=0 group by user_name", con)
    print(user_working_count)

except Exception as e:
    print(e)