import sys
import os
import subprocess
import shutil
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget,
                               QPushButton, QLabel, QHBoxLayout, QSplitter,
                               QFileDialog, QInputDialog, QStatusBar)
from PySide6.QtGui import QFont, QTextCursor, QKeySequence, QShortcut
from PySide6.QtCore import Qt, QThread, Signal

# ===================== Proje Dizini =====================

def get_projects_dir() -> Path:
    if sys.platform == "win32":
        base = Path(os.environ.get("USERPROFILE", str(Path.home())))
    elif sys.platform == "darwin":
        base = Path.home() / "Documents"
    else:
        base = Path.home()
    folder = base / "Modi Projects"
    folder.mkdir(parents=True, exist_ok=True)
    return folder

PROJECTS_DIR = get_projects_dir()
PYTHON = sys.executable  # Her zaman dogru Python yorumlayicisi

# ===================== Derleme Thread =====================

class CompileWorker(QThread):
    finished = Signal(bool, str, str)

    def __init__(self, cmd, build_dir, dist_dir):
        super().__init__()
        self.cmd = cmd
        self.build_dir = build_dir
        self.dist_dir = dist_dir

    def run(self):
        result = subprocess.run(self.cmd, cwd=self.build_dir,
                                capture_output=True, text=True)
        if result.returncode == 0:
            self.finished.emit(True, "Derleme tamamlandi.", self.dist_dir)
        else:
            self.finished.emit(False, result.stderr + "\n" + result.stdout, "")

# ===================== CTK Runtime =====================
# Modi icin CustomTkinter yardimci katmani

CTK_RUNTIME = r'''import sys, subprocess

# Otomatik customtkinter kurulumu
try:
    import customtkinter as _ctk
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "customtkinter"],
                   check=True, capture_output=True)
    import customtkinter as _ctk

# --- Tema / Pencere ---

def set_theme(mode="dark"):
    _ctk.set_appearance_mode(str(mode))

def set_color_theme(theme="blue"):
    _ctk.set_default_color_theme(str(theme))

def window(title, width, height, theme="dark"):
    set_theme(theme)
    app = _ctk.CTk()
    app.title(str(title))
    app.geometry(f"{width}x{height}")
    return app

def run(app):
    app.mainloop()

def set_title(app, title):
    app.title(str(title))

def set_size(app, width, height):
    app.geometry(f"{width}x{height}")

def min_size(app, width, height):
    app.minsize(width, height)

def resizable(app, width=True, height=True):
    app.resizable(bool(width), bool(height))

def fullscreen(app, enabled=True):
    app.attributes("-fullscreen", bool(enabled))

def close(app):
    app.destroy()

# --- Yerlesim ---

def pack(widget, side="top", fill="none", expand=False, padx=8, pady=8):
    widget.pack(side=side, fill=fill, expand=bool(expand), padx=padx, pady=pady)
    return widget

def grid(widget, row=0, column=0, padx=8, pady=8, sticky=""):
    widget.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
    return widget

def hide(widget):
    widget.pack_forget()

def destroy(widget):
    widget.destroy()

def _run_callback(func, value=None):
    if func is None:
        return None
    try:
        return func(value)
    except TypeError:
        return func()

def frame(parent, width=None, height=None, color=None, radius=8):
    kw = {"corner_radius": radius}
    if width is not None:
        kw["width"] = width
    if height is not None:
        kw["height"] = height
    if color is not None:
        kw["fg_color"] = color
    fr = _ctk.CTkFrame(parent, **kw)
    fr.pack(pady=8, padx=12, fill="both", expand=True)
    return fr

def scroll_frame(parent, label=""):
    sf = _ctk.CTkScrollableFrame(parent, label_text=str(label))
    sf.pack(pady=8, padx=12, fill="both", expand=True)
    return sf

# --- Metin / Buton / Giris ---

def label(parent, text, size=14, color=None):
    kw = {"text": str(text), "font": ("Segoe UI", size)}
    if color is not None:
        kw["text_color"] = color
    lbl = _ctk.CTkLabel(parent, **kw)
    lbl.pack(pady=8, padx=12)
    return lbl

def set_text(widget, text):
    widget.configure(text=str(text))

def button(parent, text, on_click=None, color=None, width=180):
    kw = {"text": str(text), "command": on_click, "width": width}
    if color is not None:
        kw["fg_color"] = color
    btn = _ctk.CTkButton(parent, **kw)
    btn.pack(pady=8, padx=12)
    return btn

def entry(parent, placeholder="", width=250):
    ent = _ctk.CTkEntry(parent, placeholder_text=str(placeholder), width=width)
    ent.pack(pady=8, padx=12)
    return ent

def get_text(widget):
    return widget.get()

def set_entry(widget, text):
    widget.delete(0, "end")
    widget.insert(0, str(text))

def clear(widget):
    try:
        widget.delete(0, "end")
    except Exception:
        widget.delete("1.0", "end")

# --- Gelismis CTK Bilesenleri ---

def textbox(parent, width=360, height=180):
    box = _ctk.CTkTextbox(parent, width=width, height=height)
    box.pack(pady=8, padx=12, fill="both", expand=True)
    return box

def get_box(widget):
    return widget.get("1.0", "end-1c")

def set_box(widget, text):
    widget.delete("1.0", "end")
    widget.insert("1.0", str(text))

def checkbox(parent, text, on_change=None):
    cb = _ctk.CTkCheckBox(parent, text=str(text), command=on_change)
    cb.pack(pady=8, padx=12)
    return cb

def switch(parent, text, on_change=None):
    sw = _ctk.CTkSwitch(parent, text=str(text), command=on_change)
    sw.pack(pady=8, padx=12)
    return sw

def is_checked(widget):
    return widget.get() == 1

def set_checked(widget, checked=True):
    widget.select() if checked else widget.deselect()

def slider(parent, min_value=0, max_value=100, on_change=None):
    cmd = (lambda value: _run_callback(on_change, value)) if on_change else None
    sl = _ctk.CTkSlider(parent, from_=min_value, to=max_value, command=cmd)
    sl.pack(pady=8, padx=12, fill="x")
    return sl

def get_value(widget):
    return widget.get()

def set_value(widget, value):
    widget.set(value)

def progressbar(parent, width=280):
    pb = _ctk.CTkProgressBar(parent, width=width)
    pb.set(0)
    pb.pack(pady=8, padx=12)
    return pb

def set_progress(widget, value):
    widget.set(float(value) / 100.0)

def combobox(parent, values, width=220, on_change=None):
    cmd = (lambda value: _run_callback(on_change, value)) if on_change else None
    cb = _ctk.CTkComboBox(parent, values=list(values), width=width, command=cmd)
    cb.pack(pady=8, padx=12)
    return cb

def optionmenu(parent, values, width=220, on_change=None):
    cmd = (lambda value: _run_callback(on_change, value)) if on_change else None
    om = _ctk.CTkOptionMenu(parent, values=list(values), width=width, command=cmd)
    om.pack(pady=8, padx=12)
    return om

def get_selected(widget):
    return widget.get()

def set_selected(widget, value):
    widget.set(str(value))

def tabview(parent):
    tv = _ctk.CTkTabview(parent)
    tv.pack(pady=8, padx=12, fill="both", expand=True)
    return tv

def add_tab(tabview, name):
    tabview.add(str(name))
    return tabview.tab(str(name))

def set_enabled(widget, enabled=True):
    widget.configure(state="normal" if enabled else "disabled")

def set_color(widget, color):
    widget.configure(fg_color=color)

# --- Olaylar / Dialoglar ---

def on_click(btn, func):
    btn.configure(command=func)

def on_key(widget, func, key="<Return>"):
    widget.bind(str(key), lambda e: func())

def event(kind, widget, func):
    kind = str(kind).lower()
    if kind == "clicked":
        widget.configure(command=func)
    elif kind == "enter":
        widget.bind("<Return>", lambda e: func())
    elif kind == "changed":
        try:
            widget.configure(command=lambda value=None: _run_callback(func, value))
        except Exception:
            widget.bind("<KeyRelease>", lambda e: func())
    else:
        widget.bind(str(kind), lambda e: func())
    return widget

def after(widget, ms, func):
    widget.after(ms, func)

def alert(title, message):
    import tkinter.messagebox as mb
    mb.showinfo(str(title), str(message))

def ask(title, question):
    import tkinter.messagebox as mb
    return mb.askyesno(str(title), str(question))
'''

# ===================== Cevirici =====================

class ModiSyntaxError(Exception):
    pass


EVENT_NAMES = {"clicked", "enter", "changed"}


def _syntax_error(line_no: int, line: str, hint: str) -> ModiSyntaxError:
    return ModiSyntaxError(f"Satir {line_no}: {hint}\n> {line}")


def _translate_event_call(stripped: str, indent: str, line_no: int, line: str) -> str:
    inside = stripped[len("event("):-1].strip()
    parts = [part.strip() for part in inside.split(",")]
    if len(parts) != 3:
        raise _syntax_error(line_no, line, "event kullanimi: event(clicked, widget, fonksiyon)")
    kind, widget, func = parts
    if kind.startswith(('"', "'")) and kind.endswith(('"', "'")):
        kind_value = kind
    else:
        if not kind.isidentifier():
            raise _syntax_error(line_no, line, "event adi clicked, enter veya changed gibi yalın yazilmali")
        kind_value = repr(kind)
    return f"{indent}event({kind_value}, {widget}, {func})"


def translate(source: str):
    user_lines = []
    original_lines = source.split("\n")

    for line_no, line in enumerate(original_lines, start=1):
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]

        if not stripped:
            user_lines.append("")
            continue

        if stripped.startswith("//"):
            user_lines.append(indent + "#" + stripped[2:])
            continue

        if stripped.startswith("say("):
            user_lines.append(indent + "print(" + stripped[4:])
            continue

        if stripped.startswith("repeat(") and stripped.endswith(":"):
            content = stripped[7:-2]
            user_lines.append(f"{indent}for _ in range({content}):")
            continue

        if stripped.startswith("func ") and stripped.endswith(":"):
            rest = stripped[5:-1].strip()
            if "(" not in rest or not rest.endswith(")"):
                raise _syntax_error(line_no, line, "fonksiyon kullanimi: func isim(...):")
            user_lines.append(f"{indent}def {rest}:")
            continue

        if stripped.startswith("event(") and stripped.endswith(")"):
            user_lines.append(_translate_event_call(stripped, indent, line_no, line))
            continue

        if stripped.startswith("set ") and "=" in stripped:
            name, value = stripped[4:].split("=", 1)
            user_lines.append(f"{indent}{name.strip()} = {value.strip()}")
            continue

        # Kontrollu ama Python'a yakin: if/else/for/while/call satirlari oldugu gibi gecer.
        user_lines.append(line)

    user_code = "\n".join(user_lines)

    try:
        compile(user_code, "<modi>", "exec")
    except SyntaxError as e:
        line_no = e.lineno or 1
        source_line = original_lines[line_no - 1] if 0 <= line_no - 1 < len(original_lines) else ""
        raise _syntax_error(line_no, source_line, e.msg) from e

    internal = CTK_RUNTIME + "\n# --- Kullanici Kodu ---\n\n" + user_code
    external = internal + (
        "\n\nprint()\nprint('-' * 40)"
        "\ntry:\n    input('Cikmak icin Enter basin...')"
        "\nexcept Exception:\n    pass\n"
    )
    return internal, external

# ===================== Editor Widget =====================

class ModiEditor(QTextEdit):
    PAIRS = {"(": ")", '"': '"', "[": "]", "{": "}"}

    def keyPressEvent(self, event):
        cursor = self.textCursor()
        ch = event.text()

        # Acma karakteri -> otomatik kapatma
        if ch in self.PAIRS:
            closing = self.PAIRS[ch]
            super().keyPressEvent(event)
            self.insertPlainText(closing)
            cursor.movePosition(QTextCursor.Left)
            self.setTextCursor(cursor)
            return

        # Kapatma karakteri: eger sirada zaten varsa atla
        if ch in (")", '"', "]", "}"):
            pos = cursor.position()
            full = self.toPlainText()
            if pos < len(full) and full[pos] == ch:
                cursor.movePosition(QTextCursor.Right)
                self.setTextCursor(cursor)
                return

        # Enter -> akilli girinti
        if event.key() == Qt.Key_Return:
            line = cursor.block().text()
            indent = len(line) - len(line.lstrip(" "))
            super().keyPressEvent(event)
            if line.strip().endswith(":"):
                indent += 4
            self.insertPlainText(" " * indent)
            return

        # Tab -> 4 bosluk
        if event.key() == Qt.Key_Tab:
            self.insertPlainText("    ")
            return

        super().keyPressEvent(event)

# ===================== Ana Pencere =====================

class ModiIDE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modi IDE")
        self.resize(960, 720)
        self.setStyleSheet("background-color:#1f1f1f; color:#cccccc;")
        self._worker = None

        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(10, 6, 10, 6)
        root.setSpacing(6)

        # Header
        header = QHBoxLayout()
        lbl_title = QLabel("Modi IDE")
        lbl_title.setFont(QFont("Segoe UI", 11, QFont.Bold))
        lbl_title.setStyleSheet("color:#ebebeb; letter-spacing:1px;")
        lbl_dir = QLabel(f"Proje: {PROJECTS_DIR}")
        lbl_dir.setFont(QFont("Segoe UI", 9))
        lbl_dir.setStyleSheet("color:#6a6a6a;")
        header.addWidget(lbl_title)
        header.addStretch()
        header.addWidget(lbl_dir)
        root.addLayout(header)

        # Splitter
        splitter = QSplitter(Qt.Vertical)
        root.addWidget(splitter)

        # Editor
        self.editor = ModiEditor()
        self.editor.setFont(QFont("Consolas", 14))
        self.editor.setPlaceholderText(
            "// Modi IDE -- kodunuzu buraya yazin\n\n"
            "// Konsol Ornegi:\n"
            "say(\"Merhaba Modi!\")\n\n"
            "// GUI Ornegi:\n"
            "set app = window(\"Uygulamam\", 420, 320)\n"
            "set panel = frame(app)\n"
            "set etiket = label(panel, \"Merhaba!\", 20)\n"
            "set giris = entry(panel, \"Adinizi girin\")\n"
            "set btn = button(panel, \"Tikla\")\n\n"
            "func tikla():\n"
            "    set_text(etiket, get_text(giris))\n\n"
            "event(clicked, btn, tikla)\n"
            "run(app)\n"
        )
        self.editor.setStyleSheet("""
            QTextEdit {
                background-color:#1e1e1e; color:#d4d4d4;
                border:1px solid #333; border-radius:4px;
                padding:10px; selection-background-color:#264f78;
            }
        """)
        splitter.addWidget(self.editor)

        # Konsol
        self.console = QTextEdit()
        self.console.setFont(QFont("Consolas", 12))
        self.console.setReadOnly(True)
        self.console.hide()
        splitter.addWidget(self.console)
        splitter.setSizes([520, 160])

        # Butonlar
        btns = QHBoxLayout()
        btns.setSpacing(6)
        self.btn_run   = self._make_btn("Calistir",    "#0e639c", "#1177bb", "#094771", self.act_run)
        self.btn_debug = self._make_btn("Hata Ayikla", "#2d2d2d", "#3a3a3a", "#1a1a1a", self.act_debug)
        self.btn_build = self._make_btn("Derle",       "#1b5e20", "#2e7d32", "#124016", self.act_compile, bold=True)
        btns.addWidget(self.btn_run)
        btns.addWidget(self.btn_debug)
        btns.addWidget(self.btn_build)
        root.addLayout(btns)

        # Status bar
        self.status = QStatusBar()
        self.status.setStyleSheet("background:#1a1a1a; color:#6a6a6a; font-size:11px;")
        self.setStatusBar(self.status)
        self.status.showMessage("Hazir.")

        # Kisayollar
        QShortcut(QKeySequence("Ctrl+Return"), self, self.act_run)
        QShortcut(QKeySequence("F5"),          self, self.act_run)
        QShortcut(QKeySequence("F6"),          self, self.act_debug)
        QShortcut(QKeySequence("F7"),          self, self.act_compile)

    # ---- Stiller ----

    def _console_css(self, error=False):
        c = "#f14c4c" if error else "#007acc"
        t = "#f14c4c" if error else "#cccccc"
        return f"""QTextEdit {{
            background-color:#141414; color:{t};
            border:none; border-top:2px solid {c}; padding:10px;
        }}"""

    def _make_btn(self, text, n, h, p, slot, bold=False):
        btn = QPushButton(text)
        w = QFont.Bold if bold else QFont.Normal
        btn.setFont(QFont("Segoe UI", 12, w))
        btn.setCursor(Qt.PointingHandCursor)
        btn.setStyleSheet(f"""
            QPushButton {{ background:{n}; color:#fff; padding:12px 24px; border-radius:4px; border:none; }}
            QPushButton:hover {{ background:{h}; }}
            QPushButton:pressed {{ background:{p}; }}
            QPushButton:disabled {{ background:#2a2a2a; color:#555; }}
        """)
        btn.clicked.connect(slot)
        return btn

    # ---- Yardimci ----

    def _save(self, code: str, name: str) -> Path:
        p = PROJECTS_DIR / name
        p.write_text(code, encoding="utf-8")
        return p

    def _log(self, text: str, error=False):
        self.console.setStyleSheet(self._console_css(error))
        tag = "[ERROR]" if error else "[INFO]"
        self.console.setPlainText(f"{tag}\n\n{text}")
        self.console.show()

    def _find_terminal(self):
        """Sistemdeki ilk kullanilabilir terminal emulatorunu bulur."""
        if sys.platform == "win32":
            return ["cmd", "/c", "start"]
        if sys.platform == "darwin":
            return ["open", "-a", "Terminal"]

        # Linux: sirasila dene
        for term in ["x-terminal-emulator", "gnome-terminal",
                     "konsole", "xfce4-terminal", "xterm"]:
            if shutil.which(term):
                return [term]
        return None

    # ---- Eylemler ----

    def act_run(self):
        self.console.hide()
        code = self.editor.toPlainText().strip()
        if not code:
            return

        try:
            _, external = translate(code)
        except ModiSyntaxError as e:
            self._log(str(e), error=True)
            self.status.showMessage("Sozdizimi hatasi.")
            return

        script = self._save(external, "_modi_run.py")
        self.status.showMessage("Calistiriliyor...")

        term = self._find_terminal()
        if not term:
            self._log("Terminal bulunamadi.\nDosya: " + str(script), error=True)
            return

        try:
            cmd = list(term)
            name = term[0] if term else ""
            py = PYTHON

            if sys.platform == "win32":
                cmd += [py, str(script)]
            elif sys.platform == "darwin":
                cmd = [py, str(script)]
            elif name == "gnome-terminal":
                cmd = [name, "--", py, str(script)]
            elif name == "konsole":
                cmd = [name, "-e", py, str(script)]
            else:
                # x-terminal-emulator, xfce4-terminal, xterm
                cmd = [name, "-e", f'{py} "{script}"']

            subprocess.Popen(cmd)
            self.status.showMessage("Program baslatildi.")
        except Exception as e:
            self._log(f"Terminal baslatma hatasi:\n{e}", error=True)

    def act_debug(self):
        code = self.editor.toPlainText().strip()
        if not code:
            return

        try:
            internal, _ = translate(code)
        except ModiSyntaxError as e:
            self._log(str(e), error=True)
            self.status.showMessage("Sozdizimi hatasi.")
            return

        script = self._save(internal, "_modi_debug.py")
        self.status.showMessage("Hata ayiklaniyor...")

        result = subprocess.run([PYTHON, str(script)],
                                capture_output=True, text=True, timeout=30)

        if result.returncode != 0 or result.stderr.strip():
            msg = result.stderr
            if result.stdout.strip():
                msg += "\n\nCikti:\n" + result.stdout
            self._log(msg, error=True)
        else:
            out = result.stdout.strip() or "Program cikti vermedi."
            self._log(out, error=False)

        self.status.showMessage("Hata ayiklama bitti.")

    def act_compile(self):
        code = self.editor.toPlainText().strip()
        if not code:
            self._log("Derlenecek kod yok.", error=True)
            return

        try:
            _, external = translate(code)
        except ModiSyntaxError as e:
            self._log(str(e), error=True)
            self.status.showMessage("Sozdizimi hatasi.")
            return

        name, ok = QInputDialog.getText(self, "Uygulama Adi",
                                        "Program adi:", text="Modi_App")
        if not ok or not name.strip():
            return
        name = name.strip().replace(" ", "_")

        icon, _ = QFileDialog.getOpenFileName(
            self, "Ikon Sec (Istege Bagli)", "",
            "Ikon (*.ico *.png *.jpg);;Tum (*)")

        # PyInstaller kontrol
        self._log("PyInstaller hazirlaniyor...", error=False)
        QApplication.processEvents()
        try:
            subprocess.run([PYTHON, "-m", "pip", "install", "pyinstaller"],
                           check=True, capture_output=True)
        except Exception as e:
            self._log(f"PyInstaller yuklenemedi:\n{e}", error=True)
            return

        build = PROJECTS_DIR / "builds" / name
        dist  = build / "dist"
        build.mkdir(parents=True, exist_ok=True)

        target = build / f"{name}.py"
        target.write_text(external, encoding="utf-8")

        cmd = [PYTHON, "-m", "PyInstaller", "--onefile",
               "--distpath", str(dist),
               "--workpath", str(build / "work"),
               "--specpath", str(build),
               "--name", name]

        if "window(" in code:
            cmd.append("--windowed")
        if icon:
            cmd.extend(["--icon", icon])
        cmd.append(str(target))

        self._log(f"'{name}' derleniyor... (1-3 dk)", error=False)
        QApplication.processEvents()
        self.btn_build.setEnabled(False)
        self.status.showMessage("Derleniyor...")

        self._worker = CompileWorker(cmd, str(build), str(dist))
        self._worker.finished.connect(self._on_compiled)
        self._worker.start()

    def _on_compiled(self, ok: bool, msg: str, dist: str):
        self.btn_build.setEnabled(True)
        if ok:
            self._log(f"Derleme tamamlandi.\nKlasor: {dist}", error=False)
            self.status.showMessage("Derleme tamamlandi.")
            try:
                if sys.platform == "win32":
                    os.startfile(dist)
                elif sys.platform == "darwin":
                    subprocess.Popen(["open", dist])
                else:
                    subprocess.Popen(["xdg-open", dist])
            except Exception:
                pass
        else:
            self._log(f"Derleme hatasi:\n{msg}", error=True)
            self.status.showMessage("Derleme basarisiz.")

# ===================== Giris =====================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Modi IDE")
    w = ModiIDE()
    w.show()
    sys.exit(app.exec())
