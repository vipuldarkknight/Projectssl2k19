import sys, csv, sqlite3
# program_name = sys.argv[0]
table_name = input()
# arg = tuple(sys.argv[2:])
# print(arg)
arg=[]
lst=[]
# lst.append(arg)
# print(lst)
con = sqlite3.connect("ipl.db")
cur = con.cursor()
# cur.execute("CREATE TABLE t (col1, col2);") # use your column names here

if (table_name=="TEAM"):
	# to_db = [(arg['name'], arg['class'], arg['id']) ]
	for x in range(2):
		var=input()
		arg.append(var)
	arg=tuple(arg)
	lst.append(arg)
	cur.executemany("INSERT INTO TEAM VALUES (?, ?);", lst)
elif (table_name=="PLAYER"):
	# to_db = [(i['name'], i['class'], i['id']) for i in arg]
	for x in range(6):
		var=input()
		arg.append(var)
	arg=tuple(arg)
	lst.append(arg)
	cur.executemany("INSERT INTO PLAYER VALUES (?, ?, ?, ?, ?, ?);", lst)
elif (table_name=="MATCH"):
	# to_db = [(i['name'], i['class'], i['id']) for i in arg]
	for x in range(15):
		var=input()
		arg.append(var)
	arg=tuple(arg)
	lst.append(arg)
	cur.executemany("INSERT INTO MATCH VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", lst)
elif (table_name=="PLAYER_MATCH"):
	# to_db = [(i['name'], i['class'], i['id']) for i in arg]
	for x in range(7):
		var=input()
		arg.append(var)
	arg=tuple(arg)
	lst.append(arg)
	cur.executemany("INSERT INTO PLAYER_MATCH VALUES (?, ?, ?, ?, ?, ?, ?);", lst)
elif (table_name=="BALL_BY_BALL"):
	# to_db = [(i['name'], i['class'], i['id']) for i in arg]
	for x in range(11):
		var=input()
		arg.append(var)
	arg=tuple(arg)
	lst.append(arg)
	cur.executemany("INSERT INTO BALL_BY_BALL VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", lst)
else:
	print("No such Table")

# cur.executemany("INSERT INTO POKEMON VALUES (?, ?, ?);", to_db)
con.commit()
con.close()