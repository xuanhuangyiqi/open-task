#coding: utf-8

import time
import markdown
import torndb
from configs import DATABASE


def mdfilter(dic):
    if 'content' in dic:
        dic['content'] = markdown.markdown(dic['content'])
    return dic

def tfilter(ti):
    last = time.time()-ti
    if last < 60: return u"%d秒前"%last
    if last < 3600: return u"%d分前"%(last/60)
    if last < 86400: return u"%d小时前"%(last/3600)
    if last < 86400*30: return u"%d天前"%(last/86400)
    return time.strftime("%m-%d", time.localtime(ti))


class Model:
    def __init__(self):
        self.db = torndb.Connection(DATABASE['host'], DATABASE['database'], DATABASE['user'], DATABASE['password'])

    def get_task(self, tid):
        sql = 'SELECT * FROM task WHERE id=%d'%tid
        p = self.db.query(sql)
        return mdfilter(p[0]) if p else {}

    def get_tasks(self, num=50, done=0):
        sql = 'SELECT * FROM task WHERE done=%d ORDER BY ord DESC LIMIT %s'%(done, num)
        p = self.db.query(sql)
        for x in range(len(p)):
            p[x]['time'] = tfilter(p[x]['create_time'])  
        return p

    
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
        p = self.db.query(sql)
        return p[0] if p else {}

    def update_task(self, **args):
        tid = args.pop('tid')
        sql = "UPDATE task SET %s WHERE id=%d"%(', '.join(["%s=%s"%(x, args[x]) for x in args]),int(tid))
        sql = sql.replace('%','%%')
        self.db.execute(sql)

    def task_shell(self):
        li = self.get_tasks()
        return '\n'.join(['%s %s'%(x['id'], x['title']) for x in li])

