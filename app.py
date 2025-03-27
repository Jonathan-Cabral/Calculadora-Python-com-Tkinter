import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Python")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1F2937") 
        
        self.display_var = tk.StringVar(value="0")
        self.primeiro_numero = None
        self.operacao = None
        self.novo_numero = False
        self.historico = []
        self.mostrar_historico = False
        
        self.configurar_estilos()
        self.criar_widgets()
        self.configurar_eventos_teclado()
        
    def configurar_eventos_teclado(self):
     """Configura eventos de teclado para a calculadora"""
     self.root.bind('<Key>', self.processar_tecla)

    def processar_tecla(self, evento):
        """Processa eventos de tecla pressionada"""
        tecla = evento.char
        keysym = evento.keysym
        
        # Digitos numericos 
        if tecla.isdigit():
            self.adicionar_digito(tecla)
        
        # Operadores
        elif tecla == '+':
            self.selecionar_operacao('+')
        elif tecla == '-':
            self.selecionar_operacao('-')
        elif tecla == '*':
            self.selecionar_operacao('*')
        elif tecla == '/':
            self.selecionar_operacao('/')
        elif tecla == '^':
            self.selecionar_operacao('^')
        
        # Tecla de igual (Enter)
        elif keysym == 'Return':
            self.calcular_resultado()
        
        # Ponto decimal (. ou ,)
        elif tecla == '.' or tecla == ',':
            self.adicionar_decimal()
        
        # Tecla de apagar (Backspace)
        elif keysym == 'BackSpace':
            self.apagar()
    
        
    def configurar_estilos(self):
        """Configura os estilos personalizados para os widgets"""
        # Cores
        self.cor_bg = "#1F2937"          
        self.cor_display_bg = "#111827"   
        self.cor_botao_num = "#374151"   
        self.cor_botao_op = "#F59E0B"     
        self.cor_botao_igual = "#10B981"  
        self.cor_botao_limpar = "#EF4444" 
        self.cor_botao_funcao = "#4B5563" 
       
        self.fonte_display = tkfont.Font(family="Arial", size=36, weight="normal")
        self.fonte_status = tkfont.Font(family="Arial", size=10)
        self.fonte_botao = tkfont.Font(family="Arial", size=16, weight="bold")
        
        self.estilo = ttk.Style()
        self.estilo.theme_use('clam') 
        
        self.estilo.configure(
            "Numero.TButton",
            background=self.cor_botao_num,
            foreground="white",
            borderwidth=0,
            focusthickness=0,
            focuscolor="none",
            font=self.fonte_botao
        )
        self.estilo.map(
            "Numero.TButton",
            background=[("active", "#4B5563")],
            relief=[("pressed", "flat"), ("!pressed", "flat")]
        )
        
        self.estilo.configure(
            "Operacao.TButton",
            background=self.cor_botao_op,
            foreground="white",
            borderwidth=0,
            focusthickness=0,
            focuscolor="none",
            font=self.fonte_botao
        )
        self.estilo.map(
            "Operacao.TButton",
            background=[("active", "#D97706")],
            relief=[("pressed", "flat"), ("!pressed", "flat")]
        )
        
        self.estilo.configure(
            "Igual.TButton",
            background=self.cor_botao_igual,
            foreground="white",
            borderwidth=0,
            focusthickness=0,
            focuscolor="none",
            font=self.fonte_botao
        )
        self.estilo.map(
            "Igual.TButton",
            background=[("active", "#059669")],
            relief=[("pressed", "flat"), ("!pressed", "flat")]
        )
        
        self.estilo.configure(
            "Limpar.TButton",
            background=self.cor_botao_limpar,
            foreground="white",
            borderwidth=0,
            focusthickness=0,
            focuscolor="none",
            font=self.fonte_botao
        )
        self.estilo.map(
            "Limpar.TButton",
            background=[("active", "#DC2626")],
            relief=[("pressed", "flat"), ("!pressed", "flat")]
        )
        
        self.estilo.configure(
            "Funcao.TButton",
            background=self.cor_botao_funcao,
            foreground="white",
            borderwidth=0,
            focusthickness=0,
            focuscolor="none",
            font=self.fonte_botao
        )
        self.estilo.map(
            "Funcao.TButton",
            background=[("active", "#6B7280")],
            relief=[("pressed", "flat"), ("!pressed", "flat")]
        )
    
    def criar_widgets(self):
        """Cria todos os widgets da interface"""
        
        main_frame = tk.Frame(self.root, bg=self.cor_bg)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        display_frame = tk.Frame(main_frame, bg=self.cor_display_bg, height=100)
        display_frame.pack(fill=tk.X, pady=(0, 10))
        display_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            display_frame, 
            text="Digite um número", 
            font=self.fonte_status,
            bg=self.cor_display_bg,
            fg="#9CA3AF",
            anchor="w"
        )
        self.status_label.pack(fill=tk.X, padx=10, pady=(10, 0))
        
        # Display
        display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=self.fonte_display,
            bg=self.cor_display_bg,
            fg="white",
            anchor="e"
        )
        display.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        botoes_frame = tk.Frame(main_frame, bg=self.cor_bg)
        botoes_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        for i in range(5):  
            botoes_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):  
            botoes_frame.grid_columnconfigure(i, weight=1)
        
        # Primeira linha de botões
        self.criar_botao(botoes_frame, "C", 0, 0, self.limpar, estilo="Limpar.TButton")
        self.criar_botao(botoes_frame, "←", 0, 1, self.apagar, estilo="Funcao.TButton")
        self.criar_botao(botoes_frame, "x^y", 0, 2, lambda: self.selecionar_operacao("^"), estilo="Funcao.TButton")
        self.criar_botao(botoes_frame, "÷", 0, 3, lambda: self.selecionar_operacao("/"), estilo="Operacao.TButton")
        
        # Segunda linha de botões
        self.criar_botao(botoes_frame, "7", 1, 0, lambda: self.adicionar_digito("7"))
        self.criar_botao(botoes_frame, "8", 1, 1, lambda: self.adicionar_digito("8"))
        self.criar_botao(botoes_frame, "9", 1, 2, lambda: self.adicionar_digito("9"))
        self.criar_botao(botoes_frame, "×", 1, 3, lambda: self.selecionar_operacao("*"), estilo="Operacao.TButton")
        
        # Terceira linha de botões
        self.criar_botao(botoes_frame, "4", 2, 0, lambda: self.adicionar_digito("4"))
        self.criar_botao(botoes_frame, "5", 2, 1, lambda: self.adicionar_digito("5"))
        self.criar_botao(botoes_frame, "6", 2, 2, lambda: self.adicionar_digito("6"))
        self.criar_botao(botoes_frame, "−", 2, 3, lambda: self.selecionar_operacao("-"), estilo="Operacao.TButton")
        
        # Quarta linha de botões
        self.criar_botao(botoes_frame, "1", 3, 0, lambda: self.adicionar_digito("1"))
        self.criar_botao(botoes_frame, "2", 3, 1, lambda: self.adicionar_digito("2"))
        self.criar_botao(botoes_frame, "3", 3, 2, lambda: self.adicionar_digito("3"))
        self.criar_botao(botoes_frame, "+", 3, 3, lambda: self.selecionar_operacao("+"), estilo="Operacao.TButton")
        
        # Quinta linha de botões
        self.criar_botao(botoes_frame, "H", 4, 0, self.toggle_historico, estilo="Funcao.TButton")
        self.criar_botao(botoes_frame, "0", 4, 1, lambda: self.adicionar_digito("0"))
        self.criar_botao(botoes_frame, ",", 4, 2, self.adicionar_decimal)
        self.criar_botao(botoes_frame, "=", 4, 3, self.calcular_resultado, estilo="Igual.TButton")
        
        self.historico_frame = tk.Frame(main_frame, bg=self.cor_display_bg, height=200)
        self.historico_frame.pack_forget()
           
        historico_titulo = tk.Label(
            self.historico_frame,
            text="Histórico",
            font=tkfont.Font(family="Arial", size=14, weight="bold"),
            bg=self.cor_display_bg,
            fg="white",
            anchor="w"
        )
        historico_titulo.pack(fill=tk.X, padx=10, pady=10)
        
        # Listbox para o histórico
        self.historico_listbox = tk.Listbox(
            self.historico_frame,
            bg=self.cor_botao_num,
            fg="white",
            font=tkfont.Font(family="Arial", size=12),
            bd=0,
            highlightthickness=0
        )
        self.historico_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
    
    def criar_botao(self, parent, texto, linha, coluna, comando, estilo="Numero.TButton"):
        """Cria um botão na posição especificada"""
        botao = ttk.Button(
            parent, 
            text=texto, 
            command=comando,
            style=estilo
        )
        botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")
        return botao
    
    def adicionar_digito(self, digito):
        """Adiciona um dígito no display"""
        if self.novo_numero:
            self.display_var.set(digito)
            self.novo_numero = False
        else:
            valor_atual = self.display_var.get()
            if valor_atual == "0":
                self.display_var.set(digito)
            else:
                self.display_var.set(valor_atual + digito)
    
    def adicionar_decimal(self):
        """Adiciona um ponto decimal no display"""
        if self.novo_numero:
            self.display_var.set("0,")
            self.novo_numero = False
        else:
            valor_atual = self.display_var.get()
            if "," not in valor_atual:
                self.display_var.set(valor_atual + ",")
    
    def limpar(self):
        """Limpa o display e reinicia a operação"""
        self.display_var.set("0")
        self.primeiro_numero = None
        self.operacao = None
        self.novo_numero = False
        self.atualizar_status()
    
    def apagar(self):
        """Apaga o último dígito do display"""
        valor_atual = self.display_var.get()
        if len(valor_atual) > 1:
            self.display_var.set(valor_atual[:-1])
        else:
            self.display_var.set("0")
    
    def selecionar_operacao(self, op):
        """Seleciona a operação a ser realizada"""
        valor_atual = float(self.display_var.get().replace(",", "."))
        
        if self.primeiro_numero is None:
            self.primeiro_numero = valor_atual
        elif self.operacao:
            resultado = self.calcular(self.primeiro_numero, valor_atual, self.operacao)
            self.display_var.set(str(resultado).replace(".", ","))
            self.primeiro_numero = resultado
        
        self.operacao = op
        self.novo_numero = True
        self.atualizar_status()
    
    def calcular(self, num1, num2, op):
        """Realiza o cálculo com base na operação selecionada"""
        resultado = 0
        if op == "+":
            resultado = num1 + num2
        elif op == "-":
            resultado = num1 - num2
        elif op == "*":
            resultado = num1 * num2
        elif op == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                return "Erro"
        elif op == "^":
            resultado = num1 ** num2
        
        # Arredondar para evitar problemas de ponto flutuante
        if isinstance(resultado, float):
            resultado = round(resultado, 6)
           
            if resultado.is_integer():
                resultado = int(resultado)
        
        return resultado
    
    def calcular_resultado(self):
        """Calcula o resultado final da operação"""
        if not self.operacao or self.primeiro_numero is None:
            return
        
        segundo_numero = float(self.display_var.get().replace(",", "."))
        resultado = self.calcular(self.primeiro_numero, segundo_numero, self.operacao)
        
        resultado_str = str(resultado).replace(".", ",")
        
        operacao_str = f"{self.primeiro_numero} {self.operacao} {segundo_numero} = {resultado}"
        self.historico.insert(0, operacao_str)
        if len(self.historico) > 10:
            self.historico.pop()
        
        self.atualizar_historico_listbox()
        
        self.display_var.set(resultado_str)
        self.primeiro_numero = None
        self.operacao = None
        self.novo_numero = True
        self.atualizar_status()
    
    def toggle_historico(self):
        """Mostra ou oculta o painel de histórico"""
        self.mostrar_historico = not self.mostrar_historico
        if self.mostrar_historico:
            self.historico_frame.pack(fill=tk.X, pady=10, before=self.status_label.master)
            self.atualizar_historico_listbox()
        else:
            self.historico_frame.pack_forget()
    
    def atualizar_historico_listbox(self):
        """Atualiza a listbox do histórico"""
        self.historico_listbox.delete(0, tk.END)
        for item in self.historico:
            self.historico_listbox.insert(tk.END, item)
    
    def atualizar_status(self):
        """Atualiza o texto de status com a operação atual"""
        if self.operacao:
            op_texto = self.get_operacao_texto()
            self.status_label.config(text=f"{op_texto}: {self.primeiro_numero} {self.operacao} ...")
        else:
            self.status_label.config(text="Digite um número")
    
    def get_operacao_texto(self):
        """Retorna o texto descritivo da operação atual"""
        if self.operacao == "+":
            return "Soma"
        elif self.operacao == "-":
            return "Subtração"
        elif self.operacao == "*":
            return "Multiplicação"
        elif self.operacao == "/":
            return "Divisão"
        elif self.operacao == "^":
            return "Expoente"
        return ""

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
    
    
