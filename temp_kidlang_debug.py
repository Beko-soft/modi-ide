import sys
import subprocess
def _ensure_ctk():
    try:
        import customtkinter
    except ImportError:
        print('Gerekli arayüz kütüphanesi yükleniyor, lütfen bekleyin...')
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'customtkinter'], check=True)
_ensure_ctk()
import customtkinter as _ctk

def ctk_window(title, width, height):
    _ctk.set_appearance_mode('dark')
    app = _ctk.CTk()
    app.title(title)
    app.geometry(f'{width}x{height}')
    return app

def ctk_button(master, text, command=None):
    btn = _ctk.CTkButton(master, text=text, command=command)
    btn.pack(pady=10, padx=10)
    return btn

def ctk_label(master, text):
    lbl = _ctk.CTkLabel(master, text=text)
    lbl.pack(pady=10, padx=10)
    return lbl

def ctk_run(app):
    app.mainloop()

# --- KidLang Kullanıcı Kodu ---
print("merhaba")