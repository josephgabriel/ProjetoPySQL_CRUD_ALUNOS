from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class crud():

    def __init__(self):
        #configurações da Janela
        self.root = Tk()
        self.root.title("CRUD ALUNO")
        self.root.geometry(self.centralizar_janela(self.root, 650, 500))
        self.root.resizable(False, False)
        self.root.config(bg='black')
        
        #Variaveis
        self.var_id = StringVar()
        self.var_id.set('?')

        #chamando funções iniciais
        self.containers()
        self.itens_container01()
        self.itens_containers02()
        self.preencher_tabela()


        self.root.mainloop()
        
    def containers(self):

        self.fr_container01 = Frame(
            self.root,
            height=200,
            width=650,
            bg='#3d4957'
        )

        self.fr_container02 = Frame(
            self.root,
            height=300,
            width=650,
            bg='#eef2f5'
        )

        self.fr_container01.propagate(0)
        self.fr_container02.propagate(0)
        self.fr_container01.pack()
        self.fr_container02.pack()

    def itens_container01(self):
        #criando subcontainers
        self.fr_container_title = Frame(
            self.fr_container01,
            bg=self.fr_container01.cget('bg')
        )

        self.fr_container_dados = Frame(
            self.fr_container01,
            bg=self.fr_container01.cget('bg')
        )

        self.fr_container_botoes = Frame(
            self.fr_container01,
            bg=self.fr_container01.cget('bg')
        )

        #itens do container Title
        self.lb_title = Label(
            self.fr_container_title,
            text='Sistema de cadastro de alunos',
            font='Calibri 19 bold',
            fg='#ffd546',
            bg=self.fr_container_title.cget('bg')
        )
        #posicionando containers
        self.fr_container_title.pack(anchor=W)
        self.fr_container_dados.pack(anchor=W)
        self.fr_container_botoes.pack(anchor=W, padx=215, pady=5)

        #itens do container Dados

        self.lb_id_aluno = Label(
            self.fr_container_dados,
            text='id do valor',
            font='Calibri 11 bold',
            fg='White',
            bg=self.fr_container_dados.cget('bg')
        )

        self.lb_id_aluno_value = Label(
            self.fr_container_dados,
            textvariable=self.var_id,
            font='Calibri 11 bold',
            fg='White',
            bg=self.fr_container_dados.cget('bg')
        )
        
        #nome do aluno
        self.lb_nome_aluno = Label(
            self.fr_container_dados,
            text='Nome do aluno:',
            font='Calibri 11 bold',
            fg='White',
            bg=self.fr_container_dados.cget('bg')
        )

        self.en_nome_aluno = Entry(
            self.fr_container_dados,
            width=30,
            font='Calibri 11',
            bd=0,
            fg='White',
            insertbackground='white',
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor='#ffd444',
            bg=self.fr_container_dados.cget('bg')
        )

        #email do aluno
        self.lb_email_aluno = Label(
            self.fr_container_dados,
            text='Email do aluno:',
            font='Calibri 11 bold',
            fg='White',
            bg=self.fr_container_dados.cget('bg')
        )

        self.en_email_aluno = Entry(
            self.fr_container_dados,
            width=30,
            font='Calibri 11',
            bd=0,
            fg='White',
            insertbackground='white',
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor='#ffd444',
            bg=self.fr_container_dados.cget('bg')
        )

        # Curso
        self.lb_curso_aluno = Label(
            self.fr_container_dados,
            text='Curso:',
            font='Calibri 11 bold',
            fg='White',
            bg=self.fr_container_dados.cget('bg')
        )

        self.en_curso_aluno = Entry(
            self.fr_container_dados,
            width=30,
            font='Calibri 11',
            bd=0,
            fg='White',
            insertbackground='white',
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor='#ffd444',
            bg=self.fr_container_dados.cget('bg')
        )

        # Valor

        self.lb_valor_aluno = Label(
            self.fr_container_dados,
            text='Valor do curso:',
            font='Calibri 11 bold',
            fg='White',
            bg=self.fr_container_dados.cget('bg')
        )

        self.en_valor_aluno = Entry(
            self.fr_container_dados,
            width=30,
            font='Calibri 11',
            bd=0,
            fg='White',
            insertbackground='white',
            highlightthickness=1,
            highlightbackground='gray',
            highlightcolor='#ffd444',
            bg=self.fr_container_dados.cget('bg')
        )

        #posicionando os botoes
        self.btn_adicionar = Button(
            self.fr_container_botoes,
            text='ADD',
            bg='green',
            command= self.adicionar_registro
        )

        self.btn_update = Button(
            self.fr_container_botoes,
            text='UPDATE',
            bg='blue',
            command= self.update_registro
        )

        self.btn_delete = Button(
            self.fr_container_botoes,
            text='DELETE',
            bg='red',
            command= self.excluir_registro
        )

        #posicionando itens do container Title
        self.lb_title.pack()

        #posicionando itens do container Dados
        self.lb_id_aluno.grid(row=0, column=0, sticky=W)
        self.lb_id_aluno_value.grid(row=0, column=1, sticky=W)

        self.lb_nome_aluno.grid(row=1, column=0, sticky=W)
        self.en_nome_aluno.grid(row=1, column=1, sticky=W)

        self.lb_email_aluno.grid(row=2, column=0, sticky=W)
        self.en_email_aluno.grid(row=2, column=1, sticky=W)

        self.lb_curso_aluno.grid(row=3, column=0, sticky=W)
        self.en_curso_aluno.grid(row=3, column=1, sticky=W)

        self.lb_valor_aluno.grid(row=4, column=0, sticky=W)
        self.en_valor_aluno.grid(row=4, column=1, sticky=W)

        #posicionando itens do container botoes
        self.btn_adicionar.grid(row=0, column=0, sticky=W)
        self.btn_update.grid(row=0, column=1, sticky=W)
        self.btn_delete.grid(row=0, column=2, sticky=W)

    def adicionar_registro(self):

        if self.var_id.get() == '?':
          if self.validar_entrys() == True:
                try:
                  conexao = mysql.connector.connect(
                     host='localhost',
                     user='root',
                     password='MySql@1234',
                     database='CRUD_ALUNO'
        )
                  
                  nome = self.en_nome_aluno.get()
                  email = self.en_email_aluno.get()
                  curso = self.en_curso_aluno.get()
                  valor = self.en_valor_aluno.get()

                  query = f"INSERT INTO TBaluno (nome, email, curso, valor) VALUES ('{nome}', '{email}', '{curso}', '{valor}')"
                  cursor = conexao.cursor()
                  cursor.execute(query)
                  conexao.commit()

                  cursor.close()
                  conexao.close()

                  self.resetar_entrys()
                  self.atualizar_tabela()
                  self.preencher_tabela()

                except mysql.connector.Error as erro:
                    messagebox.showerror("Erro MySQL", f"Erro ao conectar ao banco:\n{erro}")
                    return []
          else:
              messagebox.showinfo("","Existem campos vazios")

    def update_registro(self):
        id_aluno = self.var_id.get()

        if id_aluno != '?':
            confirmed = messagebox.askyesno("Confirmação", "Deseja atualizar registro?")

            if confirmed:
                try:
                  conexao = mysql.connector.connect(
                     host='localhost',
                     user='root',
                     password='MySql@1234',
                     database='CRUD_ALUNO'
        )
                  
                  nome = self.en_nome_aluno.get()
                  email = self.en_email_aluno.get()
                  curso = self.en_curso_aluno.get()
                  valor = self.en_valor_aluno.get()
                  cursor = conexao.cursor()

                  query = f"UPDATE TBaluno SET nome = '{nome}', email = '{email}', curso = '{curso}', valor = '{valor}' WHERE id = '{id_aluno}'"
                  cursor.execute(query)
                  conexao.commit()

                  cursor.close()
                  conexao.close()

                  messagebox.showinfo("",f"Registro {id_aluno} Atualiazado na tabela com sucesso")

                  self.resetar_entrys()
                  self.preencher_tabela()

                except mysql.connector.Error as erro:
                    messagebox.showerror("Erro MySQL", f"Erro ao conectar ao banco:\n{erro}")
        else:
            pass

    def excluir_registro(self):
        id_aluno = self.var_id.get()

        if id_aluno != '?':
            confirmed = messagebox.askyesno("Confirmação", "Deseja excluir registro?")

            if confirmed:
                try:
                  conexao = mysql.connector.connect(
                     host='localhost',
                     user='root',
                     password='MySql@1234',
                     database='CRUD_ALUNO'
        )
                  
                  cursor = conexao.cursor()

                  query = f"DELETE FROM TBaluno WHERE id = {id_aluno}"
                  cursor.execute(query)
                  conexao.commit()

                  cursor.close()
                  conexao.close()

                  messagebox.showinfo("",f"Registro {id_aluno} Excluido da tabela com sucesso")

                  self.resetar_entrys()
                  self.preencher_tabela()

                except mysql.connector.Error as erro:
                    messagebox.showerror("Erro MySQL", f"Erro ao conectar ao banco:\n{erro}")
        else:
            pass


    def captar_registros(self, event):
        item = self.treeview.focus()
        self.valores = self.treeview.item(item, 'values')

        self.en_nome_aluno.delete(0, 'end')
        self.en_email_aluno.delete(0, 'end')
        self.en_curso_aluno.delete(0, 'end')
        self.en_valor_aluno.delete(0, 'end')

        self.var_id.set(self.valores[0])
        self.en_nome_aluno.insert(0, self.valores[1])
        self.en_email_aluno.insert(0, self.valores[2])
        self.en_curso_aluno.insert(0, self.valores[3])
        self.en_valor_aluno.insert(0, self.valores[4])

    def itens_containers02(self):
        self.treeview = ttk.Treeview(
             self.fr_container02,
             columns=('id','nome','email','curso','valor'),
             show='headings'
        )

        self.treeview.heading('id', text='ID')
        self.treeview.heading('nome', text='Nome')
        self.treeview.heading('email', text='Email')
        self.treeview.heading('curso', text='Curso')
        self.treeview.heading('valor', text='Valor')

        self.treeview.bind('<Double-1>', self.captar_registros)

        self.treeview.pack(fill='both', expand=True, padx=10, pady=10)

    def validar_entrys(self):
        campos = [self.en_nome_aluno.get(),self.en_email_aluno.get(),self.en_curso_aluno.get(),self.en_valor_aluno.get()]

        if all(campo.strip() for campo in campos):
            return True
        else:
            return False
        
    def resetar_entrys(self):
        self.en_nome_aluno.delete(0, 'end')
        self.en_email_aluno.delete(0, 'end')
        self.en_curso_aluno.delete(0, 'end')
        self.en_valor_aluno.delete(0, 'end')
        self.var_id.set('?')

    def atualizar_tabela(self):
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='MySql@1234',
                database='CRUD_ALUNO'
        )

            query = 'SELECT * FROM TBaluno;'
            cursor = conexao.cursor()
            cursor.execute(query)

            registros = cursor.fetchall()

            cursor.close()
            conexao.close()

            return registros

        except mysql.connector.Error as erro:
            messagebox.showerror("Erro MySQL", f"Erro ao conectar ao banco:\n{erro}")
            return []

    def preencher_tabela(self):

        registros = self.atualizar_tabela()

        for i in self.treeview.get_children():
            self.treeview.delete(i)

        for registro in registros:
            if registro == None:
                print(registro)
            self.treeview.insert("","end", values=registro)

    def centralizar_janela(self,janela, largura, altura):
        janela = janela
        largura = largura
        altura = altura

        largura_screen = janela.winfo_screenwidth()
        altura_screen = janela.winfo_screenheight()

        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2

        centro = '%dx%d+%d+%d' % (largura, altura, posx, posy)
        return centro

crud()
