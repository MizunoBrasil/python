from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import shutil
import os

root = Tk()
root.title("Cópia de Arquivo com Barra de Progresso - Mizuno")
root.geometry("500x250")

def select_source_file():
    filename = filedialog.askopenfilename(title="Selecionar arquivo de origem")
    source_entry.delete(0, END)
    source_entry.insert(0, filename)

def select_destination_folder():
    foldername = filedialog.askdirectory(title="Selecionar pasta de destino")
    destination_entry.delete(0, END)
    destination_entry.insert(0, foldername)

def copy_file():
    source_file = source_entry.get()
    destination_folder = destination_entry.get()

    if not source_file or not destination_folder:
        messagebox.showwarning("Aviso", "Selecione o arquivo de origem e a pasta de destino.")
        return

    progress1['value'] = 0
    root.update_idletasks()

    # Obtém o tamanho total do arquivo para calcular o progresso
    total_size = os.path.getsize(source_file)
    bytes_copied = 0

    destination_file = os.path.join(destination_folder, os.path.basename(source_file))

    with open(source_file, "rb") as src, open(destination_file, "wb") as dst:
        while True:
            # Lê e escreve em blocos para melhor desempenho
            buf = src.read(4096)
            if not buf:
                break

            dst.write(buf)
            bytes_copied += len(buf)

            # Calcula o progresso e atualiza a barra de progresso
            progress = (bytes_copied / total_size) * 100
            progress1['value'] = progress
            root.update_idletasks()

    progress1['value'] = 100
    root.update_idletasks()

    messagebox.showinfo("CÓPIA OK", "Cópia realizada com sucesso!")

progress1 = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
progress1.pack(pady=20)

source_frame = Frame(root)
source_frame.pack(pady=10)

source_label = Label(source_frame, text="Arquivo de origem:")
source_label.pack(side=LEFT)

source_entry = Entry(source_frame, width=40)
source_entry.pack(side=LEFT)

source_button = Button(source_frame, text="Selecionar arquivo", command=select_source_file)
source_button.pack(side=LEFT)

destination_frame = Frame(root)
destination_frame.pack(pady=10)

destination_label = Label(destination_frame, text="Pasta de destino:")
destination_label.pack(side=LEFT)

destination_entry = Entry(destination_frame, width=40)
destination_entry.pack(side=LEFT)

destination_button = Button(destination_frame, text="Selecionar pasta", command=select_destination_folder)
destination_button.pack(side=LEFT)

button = Button(root, text="Fazer cópia do arquivo", command=copy_file)
button.pack(pady=20)

root.mainloop()
