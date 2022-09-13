
from dbm import _Database 
from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog


from tkinter import  filedialog as fd

# importanto PILLow
from pickletools import Imagettk, ImageTk

# importanto TKcalendar
from calendar import DateEntry
from datetime import date


# importando view
from view import *


#cores

co0 = "#2e2d2b" # Preta
co1 = "#feffff" # branca
co2 = "#4fa882" # verde
co3 = "#38576b" # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # azul
co7 = "#3fbfb9"  # verde
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # + verde

# Criando janela

janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frames

frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1,padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)



# criando funcoes ---------------------------------------
global tree

# Funcao inserir
def inserir():
    global imagem, imagem_string, l_imagem

    obra = e_obra.get()
    editora = e_editora.get()
    publicacao = e_publicacao.get()
    autor = e_autor.get()
    data = e_cal.get()
    valor = e_valor.get()
    imagem = imagem_string

    lista_inserir = [obra, editora, publicacao, autor, data, valor]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    
    inserir_form(lista_inserir)

    messagebox;messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    e_obra.delete(0, 'end')
    e_editora.delete(0, 'end')
    e_publicacao.delete(0, 'end')
    e_autor.delete(0, 'end')
    _Database.delete(0, 'end')
    e_valor.delete(0, 'end')

    for widget in frameMeio.winfo_children():
        widget.destroy()

    mostrar()


# funcao para escolher imagem
global imagem, imagem_string, l_imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    # Abrindo imagem
    imagem= Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)


    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)








# trabalhando no frame cima ----------------------------------

# Abrindo imagens
app_img = Image.open('inventorio.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)


app_logo = Label(frameCima, image=app_img, text=' Biblioteca', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# trabalhando no frame meio ----------------------------------

# criando entradas
l_obra = Label(frameMeio, text='Obra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_obra.place(x=10, y=10)
e_obra = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_obra.place(x=130, y=11)

l_editora = Label(frameMeio, text='Editora', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_editora.place(x=10, y=40)
e_editora = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_editora.place(x=130, y=41)

l_publicacao = Label(frameMeio, text='Publicação', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_publicacao.place(x=10, y=70)
e_publicacao = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_publicacao.place(x=130, y=71)

l_autor = Label(frameMeio, text='Autor', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_autor.place(x=10, y=100)
e_autor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_autor.place(x=130, y=101)

l_cal = Label(frameMeio, text='Ano da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12,Background='darkblue', bordewidth=2, year=2022)
e_cal.place(x=130, y=131)

l_valor = Label(frameMeio, text='Valor da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=161)

l_seriel = Label(frameMeio, text='Número de série', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_seriel.place(x=10, y=190)
e_seriel = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_seriel.place(x=130, y=191)

# criando botoes -----------------------------------
# botao carregar
l_carregar = Label(frameMeio, text='Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)
b_carregar = Button(frameMeio,command=escolher_imagem, width=29, text='carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_carregar.place(x=130, y=221)

# botao inserir
img_add = Image.open('add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(frameMeio,command=inserir, image=img_add, width=95, text='  Adicionar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=330, y=10)

# botao atualizar
img_update = Image.open('update.png')
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)

b_update = Button(frameMeio, image=img_update, width=95, text='  Atualizar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_update.place(x=330, y=50)

# botao deletar
img_delete = Image.open('delete.png')
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)

b_delete = Button(frameMeio, image=img_delete, width=95, text='  Delete'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_delete.place(x=330, y=90)

# botao ver imagem
img_item = Image.open('item.png')
img_item = img_item.resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)

b_item = Button(frameMeio, image=img_item,width=95, text='  Ver item'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_item.place(x=330, y=221)

# Labels Quantidade total e Valores

l_total = Label(frameMeio, text='',width=14, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total.place(x=450, y=17)
l_total_ = Label(frameMeio, text='  Valor Total de todos os itens  ', height=1,anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_total_.place(x=450, y=12)

l_qtd = Label(frameMeio, text='', width=14, height=2,pady=5, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_qtd.place(x=450, y=90)
l_qtd_ = Label(frameMeio, text='  Quantidade total de itens', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd_.place(x=450, y=92)


# tabela -----------------------------------------------------------
def mostrar():

    # creating a treeview with dual scrollbars
    tabela_head = ['#Item', 'Obra',  'Editora', 'Publicação','Autor', 'Ano da compra', 'Valor da compra', 'Número de série']

    lista_itens = []



    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd = ["center", "center", "center", "center","center", "center", "center", 'center']
    h = [40, 150, 100, 160, 130, 100, 100, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1


    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)



    quantidade = []
    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens

mostrar()





janela.mainloop()
