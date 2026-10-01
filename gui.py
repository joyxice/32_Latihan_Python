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
    
    p_main_text = tk.Label(text='CEK BILANGAN PRIMA', font=('inter', 20, 'bold'))
    
    p_main_text.pack(pady=15)
    
    p_entry = tk.Entry(p_window)
    
    p_entry.pack(pady=10)
    
    tk.Button(text='cek', font=('inter', 13), command=p_get).pack(pady=8)
    
    p_status = tk.Label(text='', font=('inter', 11))
    
    p_status.pack(pady=1)
    
    p_window.mainloop()

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
    
    def a():
        print('no-func')
    
    m_main_button1 = tk.Button(text='cek bilangan prima', font=('arial', 12), command=lambda: (main.destroy(), prima()))
    m_main_button2 = tk.Button(text='hitung akar bilangan', font=('arial', 12), command=a)
    m_main_button3 = tk.Button(text='cek ganjil / genap', font=('arial', 12), command=a)
    m_main_button4 = tk.Button(text='hitung luas kubus', font=('arial', 12), command=a)
    m_main_button5 = tk.Button(text='hitung diagonal segiempat', font=('arial', 12), command=a)
    
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