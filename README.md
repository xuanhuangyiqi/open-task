open-task
=========

# Introduction
A opensource GTD software, also shown to public. 

Web client to show tasks and related notes, also support **Markdown**.

Update information by HTTP-POST, which can collaborate with **Alfred**, **VIM**, **GeekTool** and so on.

# Requirement
###Python
    * Tornado 2.2
    * Markdown
    * python-mysql
# Procedure
    - Make sure you have all the requirements installed.
    - Server: 
        git clone
        cp .gitignore.sample .gitignore
        cp configs.py.sample configs.py
        change databases info in configs.py
        source ./scripts/models.sql
        python main.py
        work with nginx
    - Client:
        put open-task.py somewhere
        add a function like:
            func TaskCont()
                exec "w"
                exec "!python ~/scripts/open-task.py u %< %"
            endfunc
# Usage
    ### task_id -> task_title
        curl example.com/?shell=1
    ### create task
        python open-task.py c Python Handbook
    ### update content
        python open-task.py u {task_id}.txt
    ### wait a task(move to the last)
        python open-task.py o {task_id}
    ### done task
        python open-task.py d {task_id}


