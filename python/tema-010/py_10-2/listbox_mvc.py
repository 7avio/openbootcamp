import tkinter as tk
from tkinter import GROOVE, MULTIPLE


class Model(object):
    def __init__(self):
        self.task_list = ['Wake up at 6:30 AM', 'Make breakfast and pack lunch', 'Take a shower and get dressed', 'Check and respond to emails', 'Work on this project from 11:00 AM to 12:00 PM', 'Make dinner']

    def add_task(self, task):
        self.task = task
        self.task_list.extend(self.task)

    def delete_task(self):
        pass

    def clear_list(self):
        pass


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.chart_columns = list(range(3))
        self.chart_rows = list(range(6))
        self.lbl_title = tk.Label(self, text='To-do list', font=("Arial", 16, "bold"))
        self.frm_task = tk.Frame(self, bd=2, relief=GROOVE)
        self.lbx_tasks = tk.Listbox(self.frm_task, font='size=36', height=5, selectmode=MULTIPLE)
        self.scrll_to_lbx = tk.Scrollbar(self.frm_task, orient='vertical', command=self.lbx_tasks.yview)
        self.lbx_tasks.configure(yscrollcommand=self.scrll_to_lbx.set)
        self.entry_new_task = tk.Entry(self, font='size=24', bg='#ADE6EF')
        self.btn_add = tk.Button(self, text='Add a task', state='disabled')
        self.btn_delete = tk.Button(self, text='Delete selected tasks')
        self.btn_clear = tk.Button(self, text='Clear All')


        self.define_grid(len(self.chart_columns), len(self.chart_rows))
        self.lbl_title.grid(column=0, row=0,columnspan=3)
        self.frm_task.grid(column=0, row=1, sticky='ew', columnspan=3, padx=5)

        self.define_grid(2, 5, self.frm_task)
        self.lbx_tasks.grid(column=0, row=0, sticky='nsew', columnspan=2)
        self.scrll_to_lbx.grid(column=2, row=0, sticky='nsew')

        self.entry_new_task.grid(column=0, row=self.chart_rows[-4], sticky='ew', columnspan=3, padx=5)
        self.entry_new_task.configure(fg='gray', justify='center')
        self.entry_new_task.insert(0, '--- Enter your new task ---')
        self.btn_add.grid(column=0, row=self.chart_rows[-3], columnspan=3)
        self.btn_delete.grid(column=0, row=self.chart_rows[-2], columnspan=3)
        self.btn_clear.grid(column=0, row=self.chart_rows[-1], columnspan=3)


    def define_grid(self, columns, rows, subdomain=None):
        def create_range(number):
            return list(range(number))
        columns = create_range(columns)
        rows = create_range(rows)
        if subdomain==None:
            for column in columns:
                self.columnconfigure(column, weight=1)
            for row in rows:
                self.rowconfigure(row, weight=1)
        else:
            self.subdomain = subdomain
            for column in columns:
                self.subdomain.columnconfigure(column, weight=1)
            for row in rows:
                self.subdomain.rowconfigure(row, weight=1)

    def show_task_list(self, options):
        for item in options:
            self.lbx_tasks.insert('end', item)

class Controller:
    def __init__(self, model, view):

        # controller_properties
        self.model = model
        self.view = view
        self.view_task = self.view.lbx_tasks


        # bindings
        self.view.btn_clear.bind('<Button-1>', lambda event: self.clear_to_list())
        self.view.btn_delete.bind('<Button-1>', lambda event: self.delete_tasks())
        self.view.btn_add.bind('<Button-1>', lambda event: self.create_task())
        self.view.entry_new_task.bind('<FocusIn>', lambda event: self.on_focus_in())
        self.view.entry_new_task.bind('<FocusOut>', lambda event: self.on_focus_out())
        self.view.entry_new_task.bind('<Return>', lambda event: self.create_task())

        self.view.show_task_list(self.model.task_list)

        self.run()

    def run(self):
        self.view.title('To do list')
        self.view.geometry('400x600')
        self.view.resizable(False, False)
        self.view.mainloop()

    def clear_to_list(self):
        self.model.task_list = []
        self.view.lbx_tasks.delete(0, 'end')

    def update_list_view(self):
        self.model.task_list = [self.view_task.get(i) for i in range(self.view_task.size())]

    def delete_tasks(self):

        selection = list(self.view.lbx_tasks.curselection())
        for item in selection:
            self.view_task.delete(selection[0])
            self.update_list_view()

    def create_task(self):
        if self.view.btn_add['state'] == 'active':
            new_task = self.view.entry_new_task.get()
            self.view.lbx_tasks.insert('end', new_task)
            self.update_list_view()
            self.on_focus_in()

    def on_focus_in(self):
        self.view.entry_new_task.delete(0, 'end')
        self.view.entry_new_task.configure(justify='left', fg='black')
        self.view.btn_add.configure(state='active')

    def on_focus_out(self):
        self.view.entry_new_task.delete(0, 'end')
        self.view.entry_new_task.insert(0, '--- Enter your new task ---')
        self.view.entry_new_task.configure(fg='gray', justify='center')
        self.view.btn_add.configure(state='disabled')


app = Controller(Model(), View())
