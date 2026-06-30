import sys
import subprocess

def _ensure_ctk():
    try:
        import customtkinter
    except ImportError:
        print('Gerekli arayuz kutuphanesi yukleniyor...')
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'customtkinter'], check=True)
_ensure_ctk()
import customtkinter as _ctk

# ---------- KidLang CTK Yardimci Fonksiyonlari ----------

def ctk_window(title, width, height, theme='dark'):
    _ctk.set_appearance_mode(theme)
    app = _ctk.CTk()
    app.title(title)
    app.geometry(f'{width}x{height}')
    return app

def ctk_run(app):
    app.mainloop()

# Icerik elemanlari
def ctk_label(master, text, font_size=14, color=None):
    kw = {'text': text, 'font': ('Segoe UI', font_size)}
    if color: kw['text_color'] = color
    lbl = _ctk.CTkLabel(master, **kw)
    lbl.pack(pady=8, padx=12)
    return lbl

def ctk_button(master, text, command=None, color=None, width=200):
    kw = {'text': text, 'command': command, 'width': width}
    if color: kw['fg_color'] = color
    btn = _ctk.CTkButton(master, **kw)
    btn.pack(pady=8, padx=12)
    return btn

def ctk_entry(master, placeholder='', width=200):
    entry = _ctk.CTkEntry(master, placeholder_text=placeholder, width=width)
    entry.pack(pady=8, padx=12)
    return entry

def ctk_get(widget):
    return widget.get()

def ctk_set(widget, value):
    widget.delete(0, 'end')
    widget.insert(0, str(value))

def ctk_textbox(master, width=400, height=200):
    tb = _ctk.CTkTextbox(master, width=width, height=height)
    tb.pack(pady=8, padx=12)
    return tb

def ctk_textbox_get(widget):
    return widget.get('1.0', 'end-1c')

def ctk_textbox_set(widget, value):
    widget.delete('1.0', 'end')
    widget.insert('1.0', str(value))

def ctk_checkbox(master, text, command=None):
    cb = _ctk.CTkCheckBox(master, text=text, command=command)
    cb.pack(pady=8, padx=12)
    return cb

def ctk_is_checked(widget):
    return widget.get() == 1

def ctk_switch(master, text, command=None):
    sw = _ctk.CTkSwitch(master, text=text, command=command)
    sw.pack(pady=8, padx=12)
    return sw

def ctk_slider(master, min_val=0, max_val=100, command=None):
    sl = _ctk.CTkSlider(master, from_=min_val, to=max_val, command=command)
    sl.pack(pady=8, padx=12)
    return sl

def ctk_slider_value(widget):
    return widget.get()

def ctk_progressbar(master, width=300):
    pb = _ctk.CTkProgressBar(master, width=width)
    pb.set(0)
    pb.pack(pady=8, padx=12)
    return pb

def ctk_progress_set(widget, value):
    widget.set(value / 100.0)

def ctk_combobox(master, options, width=200):
    cb = _ctk.CTkComboBox(master, values=options, width=width)
    cb.pack(pady=8, padx=12)
    return cb

def ctk_combobox_get(widget):
    return widget.get()

def ctk_frame(master, width=None, height=None, color=None):
    kw = {}
    if width: kw['width'] = width
    if height: kw['height'] = height
    if color: kw['fg_color'] = color
    fr = _ctk.CTkFrame(master, **kw)
    fr.pack(pady=8, padx=12, fill='both', expand=True)
    return fr

def ctk_scrollable_frame(master, label=''):
    sf = _ctk.CTkScrollableFrame(master, label_text=label)
    sf.pack(pady=8, padx=12, fill='both', expand=True)
    return sf

def ctk_tabview(master):
    tv = _ctk.CTkTabview(master)
    tv.pack(pady=8, padx=12, fill='both', expand=True)
    return tv

def ctk_add_tab(tabview, name):
    tabview.add(name)
    return tabview.tab(name)

def ctk_alert(title, message):
    import tkinter.messagebox as _mb
    _mb.showinfo(title, message)

def ctk_ask(title, question):
    import tkinter.messagebox as _mb
    return _mb.askyesno(title, question)

def ctk_color_dialog():
    from tkinter import colorchooser as _cc
    color = _cc.askcolor()[1]
    return color

def ctk_set_label(widget, text):
    widget.configure(text=text)

def ctk_set_color(widget, color):
    widget.configure(fg_color=color)

def ctk_bind(widget, event, command):
    widget.bind(event, lambda e: command())

# --------------------------------------------------------

# --- KidLang Kullanici Kodu ---
print("merhaba")

print('\n------------------------------')
try:
    input('Cikmak icin Enter tusuna basiniz...')
except: pass