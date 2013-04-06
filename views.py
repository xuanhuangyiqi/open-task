import time
import markdown
import tornado.web
import MySQLdb
from models import Model


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return Model()


class MainHandler(BaseHandler):
    def get(self):
        if self.get_argument('shell', None): return self.write(self.db.task_shell())
        tid = int(self.get_argument('id', self.db.max_task_ord().get('id', 0)))
        current_task = self.db.get_task(tid)
        done = int(self.get_argument('done', current_task.get('done',0)))
        li = self.db.get_tasks(50, done)
        self.render('task.html', li=li, cur=current_task, done=done)

    def post(self):
        title = self.get_argument('title', None)
        if not title:
            tid = self.get_argument('tid', None)
            if not tid:
                return self.render('error.html', msg='no id')
            done = self.get_argument('done', None)
            if done:
                self.db.update_task(tid=tid, done=done)
                return self.render('success.html')
            
            content = self.get_argument('content', None)
            if content:
                self.db.update_task(tid=tid, content="'%s'"%MySQLdb.escape_string(content.encode('utf-8')))
                return self.render('success.html')

            order = self.get_argument('order', None)
            if order:
                self.db.update_task(tid=tid, ord=self.db.min_task_ord().ord-1)
                return self.render('success.html')
            
        if self.db.find_task(title): #dump task
            return self.render('error.html', msg='Dump')
        else:# create task
            self.db.create_task(
                    int(time.time()),
                    self.db.max_task_ord().ord + 1,
                    MySQLdb.escape_string(title),
                    '',
                    0,
                    )
            return self.render('success.html')
class TaskHandler(BaseHandler):
    def get(self):
        pass
