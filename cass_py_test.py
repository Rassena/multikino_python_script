from cassandra.cluster import Cluster


cluster = Cluster()
session = cluster.connect('cityinfo',wait_for_all_pools=True)
session.execute('USE cityinfo')
rows = session.execute('SELECT * FROM users')

for row in rows:
    print(row.age,row.name,row.username)
    