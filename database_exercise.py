import sqlite3

con = sqlite3.connect(r'C:\..\university.db') 

for row in con.execute("SELECT * from Students;"):
    print(row)
    
    
  
    
def select_table(table):
     try:
         result = []
         with sqlite3.connect('university.db') as con:
             cursor = con.execute("SELECT * from \
                                  {}".format(table))
                                  
             result.append([d[0] for d in cursor.description])
             for row in cursor:
                 result.append(row)
                 
         con.close()
         return result
     except sqlite3.Error as er:
         print ("select_table:", er)
         con.close()
     return False


def show_table(table):
    for row in table:
        print("\t".join([str(x) for x in row]))

table = select_table('Courses')
print(table)

show_table(table)


tables = {"1": "Students", "2": "Professors", "3": "Courses"}
while True:
    print("\n".join([":".join(x) for x in tables.items()]))
    reply = input("Επιλογή:")
    if not reply: break

    if reply in tables.keys():
        show_table(select_table(tables[reply]))







