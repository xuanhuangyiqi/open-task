import markdown
import tornado.database
from configs import DATABASE

def mdfilter(li):
    for x in li:
        x.content = markdown.markdown(x.content)
    return li


class Model:
    def __init__(self):
        self.db = tornado.database.Connection(**DATABASE)

    def get_task(self, tid):
        sql = 'SELECT * FROM task WHERE id=%d'%tid
        p = mdfilter(self.db.query(sql))
        return p[0] if p else {}

    def get_tasks(self, num=50, done=0):
        sql = 'SELECT * FROM task WHERE done=%d ORDER BY ord DESC LIMIT %s'%(done, num)
        return mdfilter(self.db.query(sql))
    
    def find_task(self, title):
        sql = "SELECT * FROM task WHERE title = '%s'"%title
        return self.db.query(sql) 

    def create_task(self, *args):
        sql = "INSERT INTO task(create_time, ord, title, content, done) VALUES (%d, %d, '%s', '%s', %d)"%args
        self.db.execute(sql)

    def max_task_ord(self):
        sql = "SELECT * FROM task ORDER BY ord DESC LIMIT 1"
        p = self.db.query(sql)
        return p[0] if p else {}

    def min_task_ord(self):
        sql = "SELECT * FROM task ORDER BY ord LIMIT 1"
        p = self.db.query(sql)[0]
        return p[0] if p else {}

    def update_task(self, **args):
        tid = args.pop('tid')
        sql = "UPDATE task SET %s WHERE id=%d"%(', '.join(["%s=%s"%(x, args[x]) for x in args]),int(tid))
        self.db.execute(sql)

    def task_shell(self):
        li = self.get_tasks()
        return '\n'.join(['%s %s'%(x['id'], x['title']) for x in li])

