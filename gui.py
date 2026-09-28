import tkinter as tk
import sqlite3

def main_window():
    main = tk.Tk()
    main.geometry('550x350')
    main.title('Operasi numerasi')
    
    m_main_text = tk.Label(
        main,
        text='OPERASI NUMERASI',
        font=('inter', 20, 'bold')
        )
    
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