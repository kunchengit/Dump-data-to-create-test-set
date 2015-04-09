BUGZILLA_DATABASE_HOST = "bz3-db3.eng.vmware.com"
BUGZILLA_DATABASE_PORT = 3306
BUGZILLA_DATABASE_USER ="mts"
BUGZILLA_DATABASE_PW="mts"
BUGZILLA_DATABASE_DATABASE="bugzilla"
bzdb_conn = MySQLdb.connect(host=BUGZILLA_DATABASE_HOST, port=BUGZILLA_DATABASE_PORT, user=BUGZ     ILLA_DATABASE_USER, passwd=BUGZILLA_DATABASE_PW, db=BUGZILLA_DATABASE_DATABASE)

LOCAL_DATABASE_HOST = "10.117.8.41"
LOCAL_DATABASE_PORT = 3306
LOCAL_DATABASE_USER = "root"
LOCAL_DATABASE_PW = "vmware"
LOCAL_DATABASE_DATABASE = "test"
local_conn = MySQLdb.connect(host=LOCAL_DATABASE_HOST, port=LOCAL_DATABASE_PORT, user=LOCAL_DA     TABASE_USER, passwd=LOCAL_DATABASE_PW, db=LOCAL_DATABASE_DATABASE)

bzdb_cursor = bzdb_conn.cursor()
local_cursor = local_conn.cursor()

sql = """
      select bug_id from bugs where assigned_to in (
      select userid from profiles where login_name in (
      'hfu','letian','vbhakta','weili','nmukuri','zhoum','hxie','shiyaoy','shanpeic',
      'souravk','vaibhavk','fangchiw','gengshengl'))
      """

try:
    bzdb_cursor.execute(sql)
    res = bzdb_cursor.fetchall()
    bug_id = [str(item[0]) for item in res]
except:
    print "Error: unable to fetch data"

def dump_data(table, bug_list):
    sql = """select * from %s where bug_id in (%s)""" %(table, ','.join(buglist))
    try:
        bzdbz_cursor.execute(sql)
        res = bzdb_cursor.fetchall();
    except:
        print "Error: unable to fetch data"
    for item in res:
        sql = """insert into %s values %s"""#nc
        try:
            local_cursor.execute(sql)
            local_conn.commit()
        except:
            local_conn.rollback()

tables=#nc

for item in tables:
    dump_data(item, bug_id)

