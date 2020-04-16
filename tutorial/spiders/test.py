vals = ('job2,name_company1,salary1')
cols = ('job,name_company,salary')
# self.insert_database('findwork',cols,vals)
# for col, val in zip(cols, vals):
# self.mycursor.execute("INSERT INTO findwork("+cols+") VALUES (%s,%s,%s)", vals)
print("INSERT INTO findwork(", cols, ")VALUES(%s,%s,%s),",vals)
print('INSERT INTO find(col) VALUES (%s),', vals)