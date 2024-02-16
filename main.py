import subprocess
import tkinter as tk
from tkinter import messagebox


def get_vm_list():
    try:
        output = subprocess.check_output(["C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe", "list", "vms"], shell=True)
        vm_list = output.decode().splitlines()
        return vm_list
    except subprocess.CalledProcessError:
        return []

def enable_nested_virtualization(vm_name):
    try:
        subprocess.check_call(["C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe", "modifyvm", vm_name, "--nested-hw-virt", "on"], shell=True)
        messagebox.showinfo("Success", f"Nested virtualization enabled for {vm_name}")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to enable nested virtualization")

def on_vm_selected(event):
    selected_vm_index = vm_listbox.curselection()[0]
    selected_vm_name = vm_listbox.get(selected_vm_index)
    enable_nested_virtualization(selected_vm_name)

# Создание окна
window = tk.Tk()
window.title("Enable Nested Virtualization")

# Получение списка виртуальных машин
vm_list = get_vm_list()

# Создание списка виртуальных машин
vm_listbox = tk.Listbox(window)
for vm in vm_list:
    vm_listbox.insert(tk.END, vm)
vm_listbox.pack()

# Привязка события к выбору виртуальной машины
vm_listbox.bind("<<ListboxSelect>>", on_vm_selected)

window.mainloop()

