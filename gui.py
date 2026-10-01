import tkinter as tk
import sqlite3
import bangun_ruang as br
import matematika as mtk

def prima():
    p_window = tk.Tk()
    p_window.title('cek bilangan prima')
    p_window.geometry('400x275')
    
    def p_get():
        if mtk.prima(int(p_entry.get())):
            p_status.config(text='True', fg='green')
        else:
            p_status.config(text='False', fg='red')
    
    p_main_text = tk.Label(p_window, text='CEK BILANGAN PRIMA', font=('inter', 20, 'bold'))
    p_main_text.pack(pady=(15, 0))
    
    p_entry = tk.Entry(p_window)
    p_entry.pack(pady=(20, 10))
    
    tk.Button(text='cek', font=('inter', 13), command=p_get).pack(pady=8)
    
    p_status = tk.Label(text='', font=('inter', 11))
    p_status.pack(pady=1)
    
    p_back_button = tk.Button(p_window, text='kembali', font=('arial', 11), command=lambda: (p_window.destroy(), main_window()))
    p_back_button.pack(side='bottom', pady=(0, 15))
    
    p_window.mainloop()
    
def akar():
    a_window = tk.Tk()
    a_window.title('hitung akar bilangan')
    a_window.geometry('400x275')
    
    tk.Label(a_window, text='HITUNG AKAR BILANGAN', font=('inter', 20, 'bold')).pack(pady=(15, 0))
    
    a_entry = tk.Entry(a_window)
    a_entry.pack(pady=(20, 0))
    
    def count():
        a_result.config(text=f'{mtk.akar(int(a_entry.get()))}')
    
    a_button = tk.Button(a_window, text='hitung', font=('inter', 13), command=count)
    a_button.pack(pady=(15, 8))
    
    a_result = tk.Label(a_window, text='', fg='black', font=('inter', 11))
    a_result.pack()
    
    a_back_button = tk.Button(text='kembali', font=('arial', 11), command=lambda: (a_window.destroy(), main_window()))
    a_back_button.pack(side='bottom', pady=(0, 15))
    
    a_window.mainloop()
    
def ganjil_genap():
    gg_window = tk.Tk()
    gg_window.geometry('400x275')
    gg_window.title('cek ganjil / genap')
    
    tk.Label(gg_window, text='CEK GANJIL / GENAP', font=('inter', 20, 'bold')).pack(pady=(15, 0))
    
    gg_entry = tk.Entry(gg_window)
    gg_entry.pack(pady=(20, 0))
    
    def cek():
        if mtk.ganjil_genap(int(gg_entry.get())):
            gg_result.config(text='genap')
        else:
            gg_result.config(text='ganjil')
    
    gg_button = tk.Button(gg_window, text='cek bilangan', font=('inter', 13), command=cek)
    gg_button.pack(pady=(15, 8))
    
    gg_result = tk.Label(gg_window, text='', fg='black')
    gg_result.pack()
    
    tk.Button(gg_window, text='kembali', font=('arial', 11), command=lambda: (gg_window.destroy(), main_window())).pack(side='bottom', pady=(0, 15))
    
    gg_window.mainloop()
    
def luas_kubus():
    lk_window = tk.Tk()
    lk_window.geometry('400x325')
    lk_window.title('hitung luas kubus')
    
    tk.Label(lk_window, text='HITUNG LUAS KUBUS', font=('inter', 20, 'bold')).pack(pady=(15, 0))
    
    tk.Label(lk_window, text='alas: ', font=('arial', 11)).pack(pady=(13, 5))
    
    lk_entry1 = tk.Entry(lk_window)
    lk_entry1.pack(pady=(0, 8))
    
    tk.Label(lk_window, text='tinggi: ', font=('arial, 11')).pack(pady=(5, 5))
    
    lk_entry2 = tk.Entry(lk_window)
    lk_entry2.pack()
    
    def count():
        lk_result.config(text=f'{br.luas_kubus(int(lk_entry1.get()), int(lk_entry2.get()))}')
    
    tk.Button(lk_window, text='hitung', font=('inter', 11), command=count).pack(pady=(15, 8))
    
    lk_result = tk.Label(lk_window, text='', fg='black', font=('inter', 11))
    lk_result.pack(pady=(2, 0))
    
    tk.Button(lk_window, text='kembali', font=('arial', 11), command=lambda: (lk_window.destroy(), main_window())).pack(side='bottom', pady=(0, 15))
    
    lk_window.mainloop()
    
def diagonal():
    d_window = tk.Tk()
    d_window.geometry('460x325')
    d_window.title('hitung diaogonal segiempat')
    
    tk.Label(d_window, text='HITUNG DIAGONAL SEGIEMPAT', font=('inter', 20, 'bold')).pack(pady=(15, 0))
    
    tk.Label(d_window, text='sisi pertama: ', font=('arial', 11)).pack(pady=(13, 5))
    
    d_entry1 = tk.Entry(d_window)
    d_entry1.pack(pady=(0, 8))
    
    tk.Label(d_window, text='sisi kedua: ', font=('arial', 11)).pack(pady=(5, 5))
    
    d_entry2 = tk.Entry(d_window)
    d_entry2.pack()
    
    def count():
        d_result.config(text=f'{br.diagonal_segiempat(int(d_entry1.get()), int(d_entry2.get()))}')
    
    tk.Button(d_window, text='hitung', font=('inter', 11), command=count).pack(pady=(15, 8))
    
    d_result = tk.Label(d_window, text='', fg='black', font=('arial', 11))
    d_result.pack(pady=(2, 0))
    
    tk.Button(d_window, text='kembali', font=('arial', 11), command=lambda: (d_window.destroy(), main_window())).pack(side='bottom', pady=(0, 15))
    
    d_window.mainloop()

def main_window():
    main = tk.Tk()
    main.geometry('550x350')
    main.title('Operasi numerasi')
    
    m_main_text = tk.Label(
        main,
        text='OPERASI NUMERASI',
        font=('inter', 18, 'bold')
        )
    
    m_main_text.pack(pady=20)
    
    m_main_button1 = tk.Button(text='cek bilangan prima', font=('arial', 12), command=lambda: (main.destroy(), prima()))
    m_main_button2 = tk.Button(text='hitung akar bilangan', font=('arial', 12), command=lambda: (main.destroy(), akar()))
    m_main_button3 = tk.Button(text='cek ganjil / genap', font=('arial', 12), command=lambda: (main.destroy(), ganjil_genap()))
    m_main_button4 = tk.Button(text='hitung luas kubus', font=('arial', 12), command=lambda: (main.destroy(), luas_kubus()))
    m_main_button5 = tk.Button(text='hitung diagonal segiempat', font=('arial', 12), command=lambda: (main.destroy(), diagonal()))
    
    m_main_button1.pack(pady=5)
    m_main_button2.pack(pady=5)
    m_main_button3.pack(pady=5)
    m_main_button4.pack(pady=5)
    m_main_button5.pack(pady=5)
    
    main.mainloop()

window = tk.Tk()
window.geometry('450x300')
window.title('Operasi numerasi (login)')

username = ''
password = ''

main_text = tk.Label(window,
                     text='LOGIN USER',
                     font=('arial', 20, 'bold')
                     )
main_text.pack(pady=15)

username_text = tk.Label(window,
                         text='Username: ',
                         font=('inter', 12)
                         )
input_username = tk.Entry(window)

username_text.pack(pady=1)
input_username.pack()


password_text = tk.Label(window,
                         text='Password: ',
                         font=('inter', 12))
input_password = tk.Entry(window)

password_text.pack(pady=1)
input_password.pack()

def get_data():
    username = input_username.get()
    password = input_password.get()
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
                 SELECT * FROM user
                 WHERE username = ? AND password = ?;
                 ''', (username, password))
    
    correct = cursor.fetchone()
    conn.commit()
    conn.close()
    
    if correct:
        login_status.config(
            text='login successfully',
            fg='green'
        )
        window.after(500, lambda: (window.destroy(), main_window()))
    else:
        login_status.config(
            text='login failed!',
            fg='red'
        )
    

login_button = tk.Button(window,
                         text='LOGIN',
                         font=('inter', 13, 'bold'),
                         command=get_data)

login_button.pack(pady=10)

login_status = tk.Label(
    text='',
    font=('inter', 9),
)

login_status.pack()

window.mainloop()