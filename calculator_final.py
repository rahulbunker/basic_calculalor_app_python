import os
import sys
import tkinter as tk
from tkinter import PhotoImage
import base64

# Icon as base64 string (embedded - no external file needed)
ICON_B64 = ""

# ─── Color Theme ───────────────────────────────────────────────
BG         = "#1e1e2e"
DISP_BG    = "#11111b"
BTN_NUM    = "#313244"
BTN_OP     = "#7c3aed"
BTN_EQ     = "#10b981"
BTN_CLR    = "#ef4444"
BTN_SPEC   = "#2563eb"
TEXT_MAIN  = "#cdd6f4"
TEXT_OP    = "#ffffff"
FONT_DISP  = ("Segoe UI", 30, "bold")
FONT_BTN   = ("Segoe UI", 16, "bold")
FONT_SMALL = ("Segoe UI", 11)

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)
        self.expression = ""
        self.result_shown = False
        self._build_ui()

    def _build_ui(self):
        self.expr_var = tk.StringVar(value="")
        expr_lbl = tk.Label(self.root, textvariable=self.expr_var,
            bg=DISP_BG, fg="#585b70", font=FONT_SMALL, anchor="e", padx=16)
        expr_lbl.grid(row=0, column=0, columnspan=4, sticky="ew", ipady=4)

        self.disp_var = tk.StringVar(value="0")
        disp = tk.Label(self.root, textvariable=self.disp_var,
            bg=DISP_BG, fg=TEXT_MAIN, font=FONT_DISP, anchor="e", padx=16, pady=10)
        disp.grid(row=1, column=0, columnspan=4, sticky="ew")

        buttons = [
            ("AC",2,0,1,BTN_CLR), ("⌫",2,1,1,BTN_CLR), ("%",2,2,1,BTN_SPEC), ("÷",2,3,1,BTN_OP),
            ("7",3,0,1,BTN_NUM),  ("8",3,1,1,BTN_NUM),  ("9",3,2,1,BTN_NUM),  ("×",3,3,1,BTN_OP),
            ("4",4,0,1,BTN_NUM),  ("5",4,1,1,BTN_NUM),  ("6",4,2,1,BTN_NUM),  ("−",4,3,1,BTN_OP),
            ("1",5,0,1,BTN_NUM),  ("2",5,1,1,BTN_NUM),  ("3",5,2,1,BTN_NUM),  ("+",5,3,1,BTN_OP),
            ("±",6,0,1,BTN_SPEC), ("0",6,1,1,BTN_NUM),  (".",6,2,1,BTN_NUM),  ("=",6,3,1,BTN_EQ),
        ]
        for (text,r,c,cs,color) in buttons:
            btn = tk.Button(self.root, text=text, bg=color, fg=TEXT_OP, font=FONT_BTN,
                relief="flat", bd=0, activebackground=self._lighten(color),
                activeforeground=TEXT_OP, cursor="hand2",
                command=lambda t=text: self._on_click(t))
            btn.grid(row=r, column=c, columnspan=cs, sticky="nsew", padx=3, pady=3, ipady=14)

        for i in range(4): self.root.columnconfigure(i, weight=1)
        for i in range(7): self.root.rowconfigure(i, weight=1)

    def _on_click(self, key):
        if key == "AC":
            self.expression = ""; self.disp_var.set("0")
            self.expr_var.set(""); self.result_shown = False
        elif key == "⌫":
            if self.result_shown:
                self.expression = ""; self.disp_var.set("0"); self.result_shown = False
            else:
                self.expression = self.expression[:-1]
                self.disp_var.set(self.expression if self.expression else "0")
        elif key == "=":
            try:
                expr_clean = self.expression.replace("×","*").replace("÷","/").replace("−","-")
                self.expr_var.set(self.expression + " =")
                result = eval(expr_clean)
                if isinstance(result, float) and result == int(result): result = int(result)
                self.disp_var.set(str(result)); self.expression = str(result); self.result_shown = True
            except ZeroDivisionError:
                self.disp_var.set("÷ 0 Error"); self.expression = ""; self.result_shown = True
            except:
                self.disp_var.set("Error"); self.expression = ""; self.result_shown = True
        elif key == "%":
            try:
                val = float(self.expression) / 100
                if val == int(val): val = int(val)
                self.expression = str(val); self.disp_var.set(self.expression)
            except: pass
        elif key == "±":
            try:
                val = -float(self.expression)
                if val == int(val): val = int(val)
                self.expression = str(val); self.disp_var.set(self.expression)
            except: pass
        else:
            if self.result_shown and key not in "+-×÷−":
                self.expression = ""; self.expr_var.set("")
            self.result_shown = False
            if key == ".":
                parts = self.expression.replace("×","+").replace("÷","+").replace("−","+").split("+")
                if parts and "." in parts[-1]: return
            self.expression += key
            self.disp_var.set(self.expression)

    @staticmethod
    def _lighten(hex_color):
        h = hex_color.lstrip("#")
        r,g,b = int(h[0:2],16),int(h[2:4],16),int(h[4:6],16)
        return f"#{min(255,r+40):02x}{min(255,g+40):02x}{min(255,b+40):02x}"

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("360x520")
    
    # ── Set window icon (works without external file) ──
    try:
        # Try ICO file first (same folder)
        ico_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "calculator.ico")
        if os.path.exists(ico_path):
            root.iconbitmap(ico_path)
        else:
            # Fallback: PNG icon
            png_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "calculator_icon.png")
            if os.path.exists(png_path):
                img = PhotoImage(file=png_path)
                root.iconphoto(True, img)
    except Exception:
        pass  # Icon load na ho toh bhi app chalega

    app = Calculator(root)
    root.mainloop()