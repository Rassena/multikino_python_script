from cassandra.cluster import Cluster


cluster = Cluster()
session = cluster.connect('multikino', wait_for_all_pools=True)
session.execute('USE multikino')
rows = session.execute('SELECT * FROM users')

for row in rows:
    print(row.user_surname)
