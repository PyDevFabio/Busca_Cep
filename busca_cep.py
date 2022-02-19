from tkinter import *
from click import command
import requests
import json



class App:

    def __init__(self):
        self.window = Tk()
        self.windowConfig()
        self.widgetsWindow()

        self.window.mainloop()
    
    def windowConfig(self):
        self.window.title('Busca Cep')
        self.window.minsize(450, 450)
        self.window.maxsize(550, 550)
        self.window.resizable(True, True)
        self.window.configure(bg='#796fd9')
    

    def widgetsWindow(self):
        #Label 
        self.txt_cep = Label(self.window, text='CEP',
        bg='#796fd9', fg='white', font='arial 10 bold')
        #relx = horizontal, rely= vertical.
        self.txt_cep.place(relx=0.03, rely=0.08)

        #Input -> Entry -> Recebe o CEP.
        self.entry = Entry(self.window, width=40)
        self.entry.place(relx=0.2, rely=0.08)

        #Botão Pesquisar.
        self.btn_enviar = Button(self.window, text='Enviar',
        bg='#231c66', fg='white', command=self.send_info)
        self.btn_enviar.place(relx=0.03, rely=0.2)

        self.btn_enviar.bind('Enter', self.send_info)

        #Botão excluir.
        self.btn_clean = Button(self.window, text='clean', bg='#231c66',
        fg='white', font='arial 10', command=self.clean)
        self.btn_clean.place(relx=0.03, rely=0.30)


        #Lista de informações.
        self.list_cep = Listbox(self.window, width=350, height=350)
        self.list_cep.place(relx=0.01, rely=0.4)



    def send_info(self):
        text = self.entry.get()
        url = requests.get(f'https://viacep.com.br/ws/{text}/json/')
        if url.status_code == 200:
            print('Requisão de Cep feita com Sucesso.')
        else:
            print('Requisição Falhou...')
            self.window_tp = Toplevel()
            self.window_tp.title('Erro de Requisição')
            self.window_tp.minsize(300, 300)
            self.window_tp.resizable(False, False)
            self.window_tp.config(bg='#796fd9')
            lbl_erro = Label(self.window_tp, text='Ocorreu um ERRO, tente novamente.',
            bg='#796fd9', fg='red', font='arial 10 bold')
            lbl_erro.place(relx=0.1, rely=0.1)

            btn_ok = Button(self.window_tp, text='OK',fg='white',
             bg='#231c66', height=2, width=5, command=self.close)
            btn_ok.place(relx=0.4, rely=0.3)
        
        #Retorna o endereço do CEP em formato json/chaves/dicionário.
        endereço_postal = url.json()

        #Insere o endereço do CEP no ListBox.
        
        for v in endereço_postal.values():
            self.list_cep.insert(END, v)
            print()
        self.entry.delete(0, END)



    def clean(self):
        self.entry.delete(0, END)
        selected_item = self.list_cep.curselection()
        

        for item in selected_item:
            self.list_cep.delete(item)

    
    def close(self):
        self.window_tp.destroy()



obj = App()

