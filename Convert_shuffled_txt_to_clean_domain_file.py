import os, tkinter
from tkinter import *
from tkinter import filedialog

def openFile():
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
    filepath = filedialog.askopenfilename(initialdir=desktop,
                                          title="Open file that you want to convert?",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    ficheiro_original = open(filepath,'r')
    ficheiro_esboco = open(desktop+'\\esboço.txt', 'w')
    linhas_ficheiro_original = ficheiro_original.read()
    linhas_ficheiro_original = linhas_ficheiro_original.replace("https", "\n\n\nhttps")
    linhas_ficheiro_original = linhas_ficheiro_original.replace("http", "\n\n\nhttp")
    linhas_ficheiro_original = linhas_ficheiro_original.replace("www.", "")
    ficheiro_esboco.write(linhas_ficheiro_original)
    ficheiro_esboco.close()
    ficheiro_esboco_ler = open(desktop+'\\esboço.txt')
    ficheiro_esboco2 = open(desktop+'\\esboço2.txt', 'w')
    linhas_ficheiro_esboco = ficheiro_esboco_ler.readlines()
    for linha in linhas_ficheiro_esboco:
        if 'www' in linha:
            variavel_numeros = 0
            while variavel_numeros <= 2000:
                if f'www{variavel_numeros}' in linha:
                    linha = linha.replace(f"www{variavel_numeros}.", "")
                variavel_numeros = variavel_numeros + 1
        if '/' in linha[8::]:
            index1 = linha[8::].find('/')
            linha = linha[0:index1+8]
        else:
            linha = linha
        if ':' in linha[8::]:
            index2 = linha[8::].find(':')
            linha = linha[0:index2+8]
        else:
            linha = linha
        ficheiro_esboco2.write(linha+'\n')
    ficheiro_esboco2.close()
    ficheiro_esboco2 = open(desktop+'\\esboço2.txt')
    linhas_ficheiro_esboco2 = ficheiro_esboco2.readlines()
    ficheiro_esboco3 = open(desktop+'\\esboço3.txt', 'w')
    for linha_esboco2 in linhas_ficheiro_esboco2:
        if 'https://' in linha_esboco2 or 'http://' in linha_esboco2:
            ficheiro_esboco3.write(linha_esboco2.replace('https://','')
            .replace('http://','')
            .replace('\n', '/*\n').replace(' ', ''))
    ficheiro_esboco2.close()
    ficheiro_esboco3.close()
    ficheiro_esboco_ler.close()
    ficheiro_original.close()
    ficheiro_esboco4 = open(desktop+'\\esboço3.txt')
    ler_linhas_lista_esboco4 = ficheiro_esboco4.readlines()
    ler_linhas_lista_esboco4 = (list(dict.fromkeys(ler_linhas_lista_esboco4)))
    ficheiro_esboco5 = open(desktop+'\\clean_domain_file.txt', 'w')
    for linhas_finais in ler_linhas_lista_esboco4:
        ficheiro_esboco5.write(linhas_finais)
    ficheiro_esboco4.close()
    ficheiro_esboco5.close()
    os.remove(desktop+'\\esboço.txt')
    os.remove(desktop+'\\esboço2.txt')
    os.remove(desktop+'\\esboço3.txt')
###################################Close Program###################################################
window = Tk()
window.title('Convert shuffled file to clean domain file.')
window.geometry("400x70")
button2 = Button(window, text="Close", command=window.destroy).pack(side=tkinter.BOTTOM)
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()