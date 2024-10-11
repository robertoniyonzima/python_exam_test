import tkinter as tk
import tkinter.font as tkFont
from random import randint
from tkinter.ttk import Combobox

import mysql.connector
from mysql.connector import Error
from tkinter import ttk, messagebox


#from question2Exam import clear_treeview

root = tk.Tk()
root.geometry("800x800")
root.title("Student Management System")

frame_background_color= '#BC8F8F'
frame_border_color = '#8B4513'

#labels
label_background_color = '#5C3A3A'
label_color = '#FFF1E6'

#images
login_stud_icon = tk.PhotoImage(file='images/icon_student1.png')
login_admin_icon = tk.PhotoImage(file='images/icon_admin.png')
locked_icon = tk.PhotoImage(file='images/icon_locked.png')
unlocked_icon = tk.PhotoImage(file='images/icon_unlocked.png')
student_photo1 = tk.PhotoImage(file='images/student4.png')
admin_photo1 = tk.PhotoImage(file='images/admin1.png')

#buttons
button_background_color = '#D6CDA4'
button_font = tkFont.Font(family="Times New Roman", size=14, weight='bold')

# Global connection variables
connection = None
connection_admin = None




#frame
def welcome_page():
    welcome_page_fm = tk.Frame(root, bg=frame_background_color, highlightbackground=frame_border_color, highlightthickness='20')
    welcome_page_fm.pack(pady=30)
    welcome_page_fm.pack_propagate(False)
    welcome_page_fm.config(width=800, height=700)

    #labels

    heading_labels = tk.Label(welcome_page_fm, bg = label_background_color, text='Welcome !', fg=label_color, font=('Overstrike', 18)  )
    heading_labels.place(width = 300, x=200, y=40)

    def forward_to_login_student():
        welcome_page_fm.destroy()
        root.update()
        student_login_page()


    def forward_to_login_admin():
        welcome_page_fm.destroy()
        root.update()
        admin_login_page()

    def forward_to_register_student():
        welcome_page_fm.destroy()
        root.update()
        register_student()

    def forward_to_register_admin():
        welcome_page_fm.destroy()
        root.update()
        register_admin()








    #buttons
    student_loginBtn = tk.Button(welcome_page_fm, text='Login as a student', bg= label_background_color,
                                 fg = label_color, font=('Overstrike', 18), command=forward_to_login_student)
    student_loginBtn.place(x=230, y = 90 , width=300)

    student_registerBtn = tk.Button(welcome_page_fm, text='Register as a student', bg= label_background_color,
                                    fg = label_color, font=('Overstrike', 18), command=forward_to_register_student)
    student_registerBtn.place(x=230, y = 150 , width=300)





    student_login_icon = tk.Button(welcome_page_fm, image =login_stud_icon, bd= 0)
    student_login_icon.place(x= 170, y= 120)

    admin_loginBtn = tk.Button(welcome_page_fm, text='Login as administrator', bg= label_background_color,
                               fg = label_color, font=('Overstrike', 18), command=forward_to_login_admin)
    admin_loginBtn.place(x=230, y = 300 , width=300)

    admin_registerBtn = tk.Button(welcome_page_fm, text='Register as administrator', bg= label_background_color,
                                  fg = label_color, font=('Overstrike', 18), command=forward_to_register_admin)
    admin_registerBtn.place(x=230, y = 360 , width=300)

    admin_login_icon = tk.Button(welcome_page_fm, image =login_admin_icon, bd= 0)
    admin_login_icon.place(x= 160, y= 320)





def student_login_page():
    student_page_fm = tk.Frame(root, bg=frame_background_color, highlightbackground=frame_border_color,
                               highlightthickness='10')
    student_page_fm.pack(pady=30)
    student_page_fm.pack_propagate(False)
    student_page_fm.config(width=800, height=500)

    # labels

    heading_labels = tk.Label(student_page_fm, bg=label_background_color, text='Welcome on the Student login page',
                              fg=label_color, font=('Overstrike', 18))
    heading_labels.place(width=380, x=200, y=20)

    def back_to_welcome_page():
        student_page_fm.destroy()
        root.update()
        welcome_page()

    def authenticate_user(name: str, password: str) -> bool:
        try:
            global connection
            connection = mysql.connector.connect(
                host='localhost',  # or your host
                database='exam_python',
                user='root',  # replace with your MySQL username
                password=''  # replace with your MySQL password
            )

            if connection.is_connected():
                cursor = connection.cursor()
                sql_query = """SELECT * FROM students WHERE name = %s  AND password = %s"""
                cursor.execute(sql_query, (name, password))
                result = cursor.fetchone()  # Fetch one record

                if result:
                    return True  # Credentials are valid
                else:
                    return False  # Invalid credentials

        except Error as e:
            print("Error while connecting to MySQL", e)
            return False
        finally:
            if connection.is_connected():
                connection.close()

    def login():
        name = id_number_entry.get()
        password = password_entry.get()

        if authenticate_user(name, password):
            print("Login successful!")
            student_page_fm.destroy()  # Close the current login page
            root.update()  # Update the root window
            welcome_page()  # Navigate to the student menu
        else:
            print("Login failed! Invalid credentials.")

    #icon
    student_login_icon = tk.Button(student_page_fm, image=login_stud_icon, bd=0)
    student_login_icon.place(x=350, y=60)

    #labels
    id_number_lb = tk.Label(student_page_fm, text='Enter Your Name',font=button_font, bg=frame_background_color )
    id_number_lb.place(x = 250, y=120)

    password_lb = tk.Label(student_page_fm, text='Enter Your Password', font=button_font, bg=frame_background_color)
    password_lb.place(x=250, y= 200)

    #Entries
    id_number_entry= tk.Entry(student_page_fm, font=button_font, bg=frame_background_color, fg= 'black',
                              justify= tk.CENTER ,highlightcolor=button_background_color, highlightthickness=2)
    id_number_entry.place(x= 250, y=150)

    global password_entry, show_hide_btn
    password_entry = tk.Entry(student_page_fm, font=button_font, bg=frame_background_color, fg='black',
                              justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2,
                              show='*')
    password_entry.place(x=250, y=230)

    #Buttons
    login_btn = tk.Button(student_page_fm, font=button_font, text="Login", bg=button_background_color
                          , command=login)
    login_btn.place(x = 300, y = 300, width=100, height=30)

    show_hide_btn = tk.Button(student_page_fm, image=locked_icon, command=show_hide_password)
    show_hide_btn.place(x=460, y=230)

    back_btn = tk.Button(student_page_fm, text='←', font=button_font, bg=frame_background_color, bd=0
                         , command=back_to_welcome_page)
    back_btn.place(x=50, y=40)





def show_hide_password():
    if password_entry['show'] == '*':
        password_entry.configure(show='')
        show_hide_btn.config(image=unlocked_icon)

    else:
        password_entry.configure(show='*')
        show_hide_btn.config(image=locked_icon)



def admin_login_page():
    admin_page_fm = tk.Frame(root, bg=frame_background_color, highlightbackground=frame_border_color,
                               highlightthickness='10')
    admin_page_fm.pack(pady=10)
    admin_page_fm.pack_propagate(False)
    admin_page_fm.config(width=800, height=800)



    # labels

    heading_labels = tk.Label(admin_page_fm, bg=label_background_color, text='Welcome on the Administrator login page',
                              fg=label_color, font=('Overstrike', 18))
    heading_labels.place(width=450, x=200, y=20)

    def back_to_welcome_page():
        admin_page_fm.destroy()
        root.update()
        welcome_page()

    def authenticate_user(name: str, password: str) -> bool:

        try:
            connection = mysql.connector.connect(
                host='localhost',  # or your host
                database='exam_python',
                user='root',  # replace with your MySQL username
                password=''  # replace with your MySQL password
            )

            if connection.is_connected():
                cursor = connection.cursor()
                sql_query = """SELECT * FROM admins WHERE name = %s  AND password_admin = %s"""
                cursor.execute(sql_query, (name, password))
                result = cursor.fetchone()  # Fetch one record

                if result:
                    return True  # Credentials are valid
                else:
                    return False  # Invalid credentials

        except Error as e:
            print("Error while connecting to MySQL", e)
            return False
        finally:
            if connection.is_connected():
                connection.close()

    def login():
        name = id_number_entry.get()
        password = password_entry.get()

        if authenticate_user(name, password):
            print("Login successful!")
            admin_page_fm.destroy()  # Close the current login page
            root.update()  # Update the root window
            #admin_page()  # Navigate to the student menu
            menu_admin()
        else:
            print("Login failed! Invalid credentials.")

    # icon
    student_login_icon = tk.Button(admin_page_fm, image=login_admin_icon, bd=0)
    student_login_icon.place(x=350, y=60)

    # labels
    id_number_lb = tk.Label(admin_page_fm, text='Enter Your ID Number Or Your Email', font=button_font,
                            bg=frame_background_color)
    id_number_lb.place(x=250, y=120)

    password_lb = tk.Label(admin_page_fm, text='Enter Your Password', font=button_font, bg=frame_background_color)
    password_lb.place(x=250, y=200)

    # Entries
    id_number_entry = tk.Entry(admin_page_fm, font=button_font, bg=frame_background_color, fg='black',
                               justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2)
    id_number_entry.place(x=250, y=150)

    global password_entry, show_hide_btn
    password_entry = tk.Entry(admin_page_fm, font=button_font, bg=frame_background_color, fg='black',
                              justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2,
                              show='*')
    password_entry.place(x=250, y=230)

    # Buttons
    login_btn = tk.Button(admin_page_fm, font=button_font, text="Login", bg=button_background_color,
                          command=login)
    login_btn.place(x=300, y=300, width=100, height=30)

    show_hide_btn = tk.Button(admin_page_fm, image=locked_icon, command=show_hide_password)
    show_hide_btn.place(x=460, y=230)


    back_btn = tk.Button(admin_page_fm, text='←', font=button_font, bg=frame_background_color, bd=0
                         , command=back_to_welcome_page)
    back_btn.place(x=50, y=20)


def register_student():
    def id_number():
        x = randint(100000, 300000)
        return x

    courses_list = ['Biology', 'Chemistry', 'Mathematics', 'Physics', 'Poetry', 'Philosophy', 'Socilogy']

    register_page_fm = tk.Frame(root, bg=frame_background_color, highlightbackground=frame_border_color,
                             highlightthickness='10')
    register_page_fm.pack(pady=10)
    register_page_fm.pack_propagate(False)
    register_page_fm.config(width=800, height=800)

    def insert_user(name, age, enrollment_number, student_course, password):
        try:
            connection = mysql.connector.connect(
                host='localhost',  # or your host
                database='exam_python',
                user='root',  # replace with your MySQL username
                password=''  # replace with your MySQL password
            )
            if connection.is_connected():
                cursor = connection.cursor()
                sql_insert_query = """ INSERT INTO students (name, age,enrollment_number, enrolled_course, password)
                                       VALUES (%s, %s, %s, %s, %s) """
                cursor.execute(sql_insert_query, (name, age, enrollment_number, student_course, password))
                connection.commit()
                messagebox.showinfo('Your Id Number is: ',f'{x}' )
                cursor.close()
                print("User registered successfully")
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                connection.close()

    def show_hide_password():

        if password_entry['show'] == '*':
            password_entry.configure(show='')
            show_hide_btn.config(image=unlocked_icon)

        else:
            password_entry.configure(show='*')
            show_hide_btn.config(image=locked_icon)

    # labels

    heading_labels = tk.Label(register_page_fm, bg=label_background_color, text='Register as a student',
                              fg=label_color, font=('Overstrike', 18))
    heading_labels.place(width=450, x=200, y=20)



    #icon
    student_login_icon = tk.Button(register_page_fm, image=login_stud_icon, bd=0)
    student_login_icon.place(x=350, y=60)

    show_hide_btn = tk.Button(register_page_fm, image=locked_icon, command=show_hide_password)
    show_hide_btn.place(x=460, y=390)

    #labels
    name_lb = tk.Label(register_page_fm, text='Enter Your Name', font=button_font,
                            bg=frame_background_color)
    name_lb.place(x=250, y=120)

    enrolled_course_lb = tk.Label(register_page_fm, text='Choose Course', font=button_font, bg=frame_background_color)
    enrolled_course_lb.place(x=250, y=200)

    password_lb = tk.Label(register_page_fm, text='Enter Your Password', font=button_font,
                            bg=frame_background_color)
    password_lb.place(x=250, y=360)

    age_lb = tk.Label(register_page_fm, text='Enter Your Age', font=button_font, bg=frame_background_color)
    age_lb.place(x=250, y=280)

    enrollment_number_lb = tk.Label(register_page_fm, text='This is your enrollment number', font=button_font, bg=frame_background_color)
    enrollment_number_lb.place(x=250, y=420)





    #Entries
    name_entry = tk.Entry(register_page_fm, font=button_font, bg=frame_background_color, fg='black',
                               justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2)
    name_entry.place(x=250, y=150)

    enrolled_course_entry = Combobox(register_page_fm, font=button_font, state='readonly', values=courses_list)
    enrolled_course_entry.place(x=250, y=230)

    age_entry = tk.Entry(register_page_fm, font=button_font, bg=frame_background_color, fg='black',
                           justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2)
    age_entry.place(x=250, y=310)

    password_entry = tk.Entry(register_page_fm, font=button_font, bg=frame_background_color, fg='black',
                               justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2,
                              show='*')
    password_entry.place(x=250, y=390)
    x = str(id_number())
    enrollment_number_entry = tk.Entry(register_page_fm, font=button_font, bg=frame_background_color, fg='black',
                               justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2)
    enrollment_number_entry.insert(tk.END, x)
    enrollment_number_entry.config(state='readonly')
    enrollment_number_entry.place(x=250, y=450)


    def on_register():
        name = name_entry.get()
        student_course = enrolled_course_entry.get()
        age = age_entry.get()
        enrollment_number = enrollment_number_entry.get()
        password = password_entry.get()
        insert_user(name, age,enrollment_number, student_course, password)

    register_btn = tk.Button(register_page_fm, font=button_font, text="Register", bg=button_background_color,
                             command=on_register)
    register_btn.place(x=300, y=500, width=100, height=30)



    def back_to_welcome_page():
        register_page_fm.destroy()
        root.update()
        welcome_page()
    back_btn = tk.Button(register_page_fm, text='←', font=button_font, bg=frame_background_color, bd=0
                         , command=back_to_welcome_page)
    back_btn.place(x=50, y=20)


def register_admin():

    role_list =['System Admin', 'Teacher']
    register_admin_page_fm = tk.Frame(root, bg=frame_background_color, highlightbackground=frame_border_color,
                                highlightthickness='10')
    register_admin_page_fm.pack(pady=10)
    register_admin_page_fm.pack_propagate(False)
    register_admin_page_fm.config(width=800, height=800)

    student_gender = tk.StringVar()

    def from_register_to_page_admin():
        register_admin_page_fm.destroy()
        root.update()
        admin_login_page()


    def insert_user(name, role, gender, password):
        try:
            connection = mysql.connector.connect(
                host='localhost',  # or your host
                database='exam_python',
                user='root',  # replace with your MySQL username
                password=''  # replace with your MySQL password
            )
            if connection.is_connected():
                cursor = connection.cursor()
                sql_insert_query = """ INSERT INTO admins (name, role, gender, password_admin)
                                       VALUES (%s, %s, %s, %s) """
                cursor.execute(sql_insert_query, (name, role, gender, password))
                connection.commit()
                cursor.close()
                print("User registered successfully")
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                connection.close()

    # change picture
    # pic_path = tk.StringVar()
    # pic_path.set('')
    #
    # def open_pic():
    #     path = askopenfilename()
    #
    #     if path:
    #         print(path)

    #add picture frame
    add_picture_fm = tk.Frame(register_admin_page_fm,bg=frame_background_color, highlightbackground=frame_border_color,
                                highlightthickness='3' )
    add_picture_fm.place(x= 650, y=60, height=80, width=80)
    add_picture_btn = tk.Button(add_picture_fm, image=admin_photo1, bd=0)
    add_picture_btn.pack()
    add_picture_btn.place(x=0, y=0, height=80, width=80)

    def show_hide_password():

        if password_entry['show'] == '*':
            password_entry.configure(show='')
            show_hide_btn.config(image=unlocked_icon)

        else:
            password_entry.configure(show='*')
            show_hide_btn.config(image=locked_icon)

    # labels

    heading_labels = tk.Label(register_admin_page_fm, bg=label_background_color, text='Register as an Administrator',
                              fg=label_color, font=('Overstrike', 18))
    heading_labels.place(width=450, x=200, y=20)

    # icon
    student_login_icon = tk.Button(register_admin_page_fm, image=login_admin_icon, bd=0)
    student_login_icon.place(x=350, y=60)

    show_hide_btn = tk.Button(register_admin_page_fm, image=locked_icon, command=show_hide_password)
    show_hide_btn.place(x=460, y=390)

    # labels
    name_lb = tk.Label(register_admin_page_fm, text='Enter Your Name', font=button_font,
                       bg=frame_background_color)
    name_lb.place(x=250, y=120)

    role_lb = tk.Label(register_admin_page_fm, text='Enter Your Role', font=button_font, bg=frame_background_color)
    role_lb.place(x=250, y=200)

    password_lb = tk.Label(register_admin_page_fm, text='Enter Your password', font=button_font,
                           bg=frame_background_color)
    password_lb.place(x=250, y=360)

    gender_lb = tk.Label(register_admin_page_fm, text='Select your gender', font=button_font, bg=frame_background_color)
    gender_lb.place(x=250, y=280)

    # Entries
    name_entry = tk.Entry(register_admin_page_fm, font=button_font, bg=frame_background_color, fg='black',
                          justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2)
    name_entry.place(x=250, y=150)

    role_entry = Combobox(register_admin_page_fm, values= role_list)
    role_entry.place(x=250, y=230)



    password_entry = tk.Entry(register_admin_page_fm, font=button_font, bg=frame_background_color, fg='black',
                              justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2,
                              show='*')
    password_entry.place(x=250, y=390)

    #buttons

    male_gender_btn = tk.Radiobutton(register_admin_page_fm,font= button_font, bg= frame_background_color, fg='black',
                                     text='Male', variable=student_gender, value='male')
    male_gender_btn.place(x=250, y=320)

    female_gender_btn = tk.Radiobutton(register_admin_page_fm, font=button_font, bg=frame_background_color, fg='black',
                                     text='Female', variable=student_gender, value='female')
    female_gender_btn.place(x=330, y=320)

    student_gender.set('Male')

    def on_register():
        name = name_entry.get()
        role = role_entry.get()
        gender = student_gender.get()
        password = password_entry.get()
        insert_user(name, role, gender, password)
        from_register_to_page_admin()

    register_btn = tk.Button(register_admin_page_fm, font=button_font, text="Register", bg=button_background_color
                             , command=on_register)
    register_btn.place(x=300, y=440, width=100, height=30)

    def back_to_welcome_page():
        register_admin_page_fm.destroy()
        root.update()
        welcome_page()

    back_btn = tk.Button(register_admin_page_fm, text='←', font=button_font, bg=frame_background_color, bd=0
                         , command=back_to_welcome_page)
    back_btn.place(x=50, y=20)




def admin_page():
    def GetValue(event):

        name_entry.delete(0, 'end')
        age_entry.delete(0, 'end')
        enrollment_number_entry.delete(0, 'end')
        enrolled_course_entry.delete(0, 'end')
        row_id = listBox.selection()[0]
        select = listBox.item(row_id)['values']
        name_entry.insert(0, select[0])
        age_entry.insert(0, select[1])
        enrollment_number_entry.insert(0, select[2])
        enrolled_course_entry.insert(0, select[3])

    def show():
        def connection_admin():
            global connection_admin
            if connection_admin is None or not connection_admin.is_connected():
                connection_admin = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="exam_python")
            return connection_admin

        conn = connection_admin()
        cursor = conn.cursor()
        cursor.execute("SELECT name, age, enrollment_number, enrolled_course FROM students")
        records = cursor.fetchall()
        for (name, age, enrollment_number, enrolled_course) in records:
            listBox.insert("", "end", values=(name, age, enrollment_number, enrolled_course))
        cursor.close()

    def id_number():
        x = randint(100000, 300000)
        return x

    courses_list = ['Biology', 'Chemistry', 'Mathematics', 'Physics', 'Poetry', 'Philosophy', 'Socilogy']
    admin_page_fm = tk.Frame(root, bg=frame_background_color, highlightbackground=frame_border_color,
                                      highlightthickness='10')
    admin_page_fm.pack(pady=10)
    admin_page_fm.pack_propagate(False)
    admin_page_fm.config(width=800, height=800)

    #functions
    #Add
    def add_from_admin():
        name = name_entry.get()
        age = age_entry.get()
        number = enrollment_number_entry.get()
        course = enrolled_course_entry.get()
        def connection_admin():
            global connection_admin
            if connection_admin is None or not connection_admin.is_connected():
                connection_admin = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="exam_python")
            return connection_admin

        conn = connection_admin()
        cursor = conn.cursor()
        try:
            sql = "insert into students (name, age, enrollment_number, enrolled_course) values (%s, %s, %s, %s)"
            val = (name, age, number, course)
            cursor.execute(sql, val )
            conn.commit()
            messagebox.showinfo("Information", "Records inserted successfully...")

            #clear fields
            name_entry.delete(0,'end')
            age_entry.delete(0,'end')
            enrollment_number_entry.delete(0,'end')
            enrolled_course_entry.delete(0,'end')

            name_entry.focus_set()

            #empty Tree View
            #clear_treeview()
            #refresh Tree View
            #show_tree_view()

        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()





    def update():
        name = name_entry.get()
        age = age_entry.get()
        number = enrollment_number_entry.get()
        course = enrolled_course_entry.get()
        def connection_admin():
            global connection_admin
            if connection_admin is None or not connection_admin.is_connected():
                connection_admin = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="exam_python")
            return connection_admin

        conn = connection_admin()
        cursor = conn.cursor()
        try:

            sql = "UPDATE students SET name=%s, age=%s, enrollment_number=%s, enrolled_course=%s WHERE name=%s"
            val = (name, age, number, course, name)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("information", "Record Updated successfully...")
            # Clear entry fields
            name_entry.delete(0, 'end')
            age_entry.delete(0, 'end')
            enrollment_number_entry.delete(0, 'end')
            enrolled_course_entry.delete(0, 'end')
            name_entry.focus_set()
            # empty the treeview
            #clear_treeview()
            # Refresh Treeview to show updated data         show()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()

    def delete():
        name = name_entry.get()
        def connection_admin():
            global connection_admin
            if connection_admin is None or not connection_admin.is_connected():
                connection_admin = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="exam_python")
            return connection_admin
        conn = connection_admin()
        cursor = conn.cursor()

        try:
            sql = "DELETE FROM students WHERE name=%s"
            val = (name,)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("information", "Record deleted successfully...")
            # Clear entry fields
            name_entry.delete(0, 'end')
            age_entry.delete(0, 'end')
            enrollment_number_entry.delete(0, 'end')
            enrolled_course_entry.delete(0, 'end')
            name_entry.focus_set()
            # empty the treeview
            # clear_treeview()
            # Refresh Treeview to show updated data         show()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()


    #labels
    student_name_lb = tk.Label(admin_page_fm, text='Student Name:', font=button_font,
                       bg=frame_background_color, bd=0 )
    student_name_lb.place(x=50, y=30)

    age_lb = tk.Label(admin_page_fm, text='Student Age:', font=button_font,
                                bg=frame_background_color, bd=0)
    age_lb.place(x=50, y=80)

    enrollment_number_lb = tk.Label(admin_page_fm, text='Course:', font=button_font,
                                bg=frame_background_color, bd=0)
    enrollment_number_lb.place(x=50, y=130)

    enrollment_courses_lb = tk.Label(admin_page_fm, text='Enrollment Number:', font=button_font,
                                      bg=frame_background_color, bd=0)
    enrollment_courses_lb.place(x=50, y=180)

    #Entries
    name_entry = tk.Entry(admin_page_fm, font=button_font, bg=frame_background_color, fg='black',
                          justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2)
    name_entry.place(x=230, y=30)

    age_entry = tk.Entry(admin_page_fm, font=button_font, bg=frame_background_color, fg='black',
                          justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2)
    age_entry.place(x=230, y=80)

    enrolled_course_entry = Combobox(admin_page_fm, font=button_font, state='readonly', values=courses_list)
    enrolled_course_entry.place(x=230, y=130)

    enrollment_number_entry = tk.Entry(admin_page_fm, font=button_font, bg=frame_background_color, fg='black',
                          justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2)
    x = str(id_number())
    enrollment_number_entry.insert(tk.END, x)
    enrollment_number_entry.place(x=230, y=180)


    #buttons
    add_btn = tk.Button(admin_page_fm, font=button_font, text="Add", bg=button_background_color
                             , command=add_from_admin)
    add_btn.place(x=500, y=25, width=100, height=30)

    update_btn = tk.Button(admin_page_fm, font=button_font, text="Update", bg=button_background_color,
                           command=update
                        )
    update_btn.place(x=500, y=100, width=100, height=30)

    delete_btn = tk.Button(admin_page_fm, font=button_font, text="Delete", bg=button_background_color,
                           command=delete
                        )
    delete_btn.place(x=500, y=175, width=100, height=30)

    def back_to_welcome_page():
        admin_page_fm.destroy()
        root.update()
        menu_admin()
    back_btn = tk.Button(admin_page_fm, text='←', font=button_font, bg=frame_background_color, bd=0
                         , command=back_to_welcome_page)
    back_btn.place(x=20, y=20)


    #create the Treeview and bind it to GetValue function
    cols = ('Name', 'Age', 'enrollement_number', 'Enrolled_courses')
    listBox = ttk.Treeview(admin_page_fm, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1)
    listBox.place(x=10, y=450)


    show()  # Call to populate the Treeview
    def clear_treeview():
        # Clear all items from the Treeview
        for item in listBox .get_children():
            listBox .delete(item)
    listBox.bind('<Double-Button-1>', GetValue)





def managing_courses():
    list_of_credits = ['3', '5', '10', '15']
    # functions
    #show function
    def show():
        def connection_admin():
            global connection_admin
            if connection_admin is None or not connection_admin.is_connected():
                connection_admin = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="exam_python")
            return connection_admin

        conn = connection_admin()
        cursor = conn.cursor()
        cursor.execute("SELECT name, credits FROM courses")
        records = cursor.fetchall()
        for (name, credits) in records:
            listBox.insert("", "end", values=(name, credits))
        cursor.close()
    #Get value function
    def GetValue(event):

        name_course_entry.delete(0, 'end')
        credit_entry.delete(0, 'end')
        row_id = listBox.selection()[0]
        select = listBox.item(row_id)['values']
        name_course_entry.insert(0, select[0])
        credit_entry.insert(0, select[1])
    # Add
    def add():

        name = name_course_entry.get()
        credits = credit_entry.get()

        def connection_admin():
            global connection_admin
            if connection_admin is None or not connection_admin.is_connected():
                connection_admin = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="exam_python")
            return connection_admin

        conn = connection_admin()
        cursor = conn.cursor()
        try:
            sql = "insert into courses (name, credits) values (%s, %s)"
            val = (name,credits)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("Information", "New course inserted successfully...")

            # clear fields

            name_course_entry.delete(0, 'end')
            credit_entry.delete(0, 'end')

            name_course_entry.focus_set()

            # empty Tree View
            # clear_treeview()
            # refresh Tree View
            # show_tree_view()

        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()




    def update():
        name = name_course_entry.get()
        credits = credit_entry.get()

        def connection_admin():
            global connection_admin
            if connection_admin is None or not connection_admin.is_connected():
                connection_admin = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="exam_python")
            return connection_admin

        conn = connection_admin()
        cursor = conn.cursor()
        try:

            sql = "UPDATE courses SET name=%s, credits=%s WHERE name=%s"
            val = (name, credits, name)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("information", "Record Updated successfully...")
            # Clear entry fields
            name_course_entry.delete(0, 'end')
            credit_entry.delete(0, 'end')

            name_course_entry.focus_set()
            # empty the treeview
            #clear_treeview()
            # Refresh Treeview to show updated data         show()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()


    def delete():
        name = name_course_entry.get()
        def connection_admin():
            global connection_admin
            if connection_admin is None or not connection_admin.is_connected():
                connection_admin = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="exam_python")
            return connection_admin
        conn = connection_admin()
        cursor = conn.cursor()

        try:
            sql = "DELETE FROM courses WHERE name=%s"
            val = (name,)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("information", "Record deleted successfully...")
            # Clear entry fields
            name_course_entry.delete(0, 'end')
            credit_entry.delete(0, 'end')

            name_course_entry.focus_set()
            # empty the treeview
            # clear_treeview()
            # Refresh Treeview to show updated data         show()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()

    #labels
    managing_course_fm = tk.Frame(root, bg=frame_background_color, highlightbackground=frame_border_color,
                                      highlightthickness='10')
    managing_course_fm.pack(pady=10)
    managing_course_fm.pack_propagate(False)
    managing_course_fm.config(width=800, height=800)
    name_lb = tk.Label(managing_course_fm, text='Name of the course:', font=button_font,
                                    bg=frame_background_color, bd=0)
    name_lb.place(x=20, y=80)

    credit_lb = tk.Label(managing_course_fm, text='Choose credits of the course:', font=button_font,
                                    bg=frame_background_color, bd=0)
    credit_lb.place(x=20, y=160)

    #entries
    name_course_entry= tk.Entry(managing_course_fm, font=button_font, bg=frame_background_color, fg='black',
                         justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2)
    name_course_entry.place(x=230, y=80)

    credit_entry = Combobox(managing_course_fm, values= list_of_credits)
    credit_entry.place(x=280, y=160)




    # buttons
    add_btn = tk.Button(managing_course_fm, font=button_font, text="Add", bg=button_background_color
                        , command=add)
    add_btn.place(x=500, y=25, width=100, height=30)

    update_btn = tk.Button(managing_course_fm, font=button_font, text="Update", bg=button_background_color,
                           command=update)
    update_btn.place(x=500, y=100, width=100, height=30)

    delete_btn = tk.Button(managing_course_fm, font=button_font, text="Delete", bg=button_background_color,
                           command=delete
                           )
    delete_btn.place(x=500, y=175, width=100, height=30)


    def back_to_menu_admin():
        managing_course_fm.destroy()
        root.update()
        menu_admin()
    back_btn = tk.Button(managing_course_fm, text='←', font=button_font, bg=frame_background_color, bd=0
                         , command=back_to_menu_admin)
    back_btn.place(x=20, y=20)


    # create the Treeview and bind it to GetValue function
    cols = ('Name', 'Credits')
    listBox = ttk.Treeview(managing_course_fm, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1)
    listBox.place(x=10, y=450)

    show()  # Call to populate the Treeview

    def clear_treeview():
        # Clear all items from the Treeview
        for item in listBox.get_children():
            listBox.delete(item)

    listBox.bind('<Double-Button-1>', GetValue)


def managing_grades():
    # show function
    def show():
        def connection_admin():
            global connection_admin
            if connection_admin is None or not connection_admin.is_connected():
                connection_admin = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="exam_python")
            return connection_admin

        conn = connection_admin()
        cursor = conn.cursor()
        cursor.execute("SELECT student_name, course_name, grades FROM grades")
        records = cursor.fetchall()
        for (student_name, course_name, grades) in records:
            listBox.insert("", "end", values=(student_name, course_name, grades))
        cursor.close()


    def GetValue(event):

        #name_course_entry.delete(0, 'end')
        score_entry.delete(0, 'end')
        row_id = listBox.selection()[0]
        select = listBox.item(row_id)['values']
        #name_course_entry.insert(0, select[0])
        score_entry.insert(0, select[0])

    # Fonction pour insérer les données dans la base
    def add():
        try:
            # Connexion à la base de données
            conn = connection_admin()
            cursor = conn.cursor()

            # Récupérer les valeurs depuis le Combobox des cours
            selected_course = course_entry.get()

            # Vérifier que le format est correct avant de splitter
            if " - " in selected_course:
                course_name, credit = selected_course.split(" - ")
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner un cours valide.")
                return

            # Récupérer la note
            score = score_entry.get()

            # Requête SQL pour insérer les données dans la table `grades`
            sql = "INSERT INTO grades (student_name, course_name, grades) VALUES (%s, %s, %s)"
            values = (student_entry.get(), course_name, score)

            cursor.execute(sql, values)
            conn.commit()

            messagebox.showinfo("Information", "Grades have been added successfully...")

            # Vider les champs après insertion
            score_entry.delete(0, 'end')
            student_entry.set('')
            course_entry.set('')

        except Exception as e:
            print(e)
            conn.rollback()

        finally:
            cursor.close()

    # Connexion pour récupérer les étudiants et les cours
    def connection_admin():
        global connection_admin
        if connection_admin is None or not connection_admin.is_connected():
            connection_admin = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="exam_python")
        return connection_admin


    def update():

        def connection_admin():
            global connection_admin
            if connection_admin is None or not connection_admin.is_connected():
                connection_admin = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="exam_python")
            return connection_admin

        conn = connection_admin()
        cursor = conn.cursor()
        try:

            selected_course = course_entry.get()

            # Vérifier que le format est correct avant de splitter
            if " - " in selected_course:
                course_name, credit = selected_course.split(" - ")
            else:
                messagebox.showerror("Erreur", "Veuillez sélectionner un cours valide.")
                return

            # Récupérer la note
            score = score_entry.get()
            name = student_entry.get()

            sql = "UPDATE grades SET student_name=%s, course_name=%s, grades=%s WHERE grades=%s"
            val = (name, course_name, score)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("information", "Record Updated successfully...")
            # Clear entry fields
            student_entry.delete(0, 'end')
            course_entry.delete(0, 'end')

            score_entry.focus_set()
            # empty the treeview
            #clear_treeview()
            # Refresh Treeview to show updated data
            show()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()


    conn = connection_admin()
    cursor = conn.cursor()



    def delete():
        score = score_entry.get()
        def connection_admin():
            global connection_admin
            if connection_admin is None or not connection_admin.is_connected():
                connection_admin = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="exam_python")
            return connection_admin
        conn = connection_admin()
        cursor = conn.cursor()

        try:
            sql = "DELETE FROM courses WHERE grades=%s"
            val = (score,)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("information", "Record deleted successfully...")
            # Clear entry fields


            score_entry.focus_set()
            # empty the treeview
            # clear_treeview()
            # Refresh Treeview to show updated data
            show()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()

    # Fetching students and courses from the database
    cursor.execute("SELECT name FROM students")
    students = cursor.fetchall()

    cursor.execute("SELECT name, credits FROM courses")
    courses = cursor.fetchall()



    # UI Elements
    managing_grades_fm = tk.Frame(root, bg=frame_background_color, highlightbackground=frame_border_color,
                                  highlightthickness='10')
    managing_grades_fm.pack(pady=10)
    managing_grades_fm.pack_propagate(False)
    managing_grades_fm.config(width=800, height=800)

    student_name_lb = tk.Label(managing_grades_fm, text='Name of the student:', font=button_font,
                               bg=frame_background_color, bd=0)
    student_name_lb.place(x=20, y=80)

    course_name_lb = tk.Label(managing_grades_fm, text='Name of the Course and its credits:', font=button_font,
                              bg=frame_background_color, bd=0)
    course_name_lb.place(x=20, y=160)

    total_score_lb = tk.Label(managing_grades_fm, text='Total Score:', font=button_font,
                              bg=frame_background_color, bd=0)
    total_score_lb.place(x=20, y=240)

    # Entries
    score_entry = tk.Entry(managing_grades_fm, font=button_font, bg=frame_background_color, fg='black',
                           justify=tk.CENTER, highlightcolor=button_background_color, highlightthickness=2)
    score_entry.place(x=320, y=240)

    # Buttons
    add_btn = tk.Button(managing_grades_fm, font=button_font, text="Add", bg=button_background_color, command=add)
    add_btn.place(x=550, y=25, width=100, height=30)

    update_btn = tk.Button(managing_grades_fm, font=button_font, text="Update", bg=button_background_color)
    update_btn.place(x=550, y=100, width=100, height=30)

    delete_btn = tk.Button(managing_grades_fm, font=button_font, text="Delete", bg=button_background_color)
    delete_btn.place(x=550, y=175, width=100, height=30)

    def back_to_menu_admin():
        managing_grades_fm.destroy()
        root.update()
        menu_admin()
    back_btn = tk.Button(managing_grades_fm, text='←', font=button_font, bg=frame_background_color, bd=0
                         , command=back_to_menu_admin)
    back_btn.place(x=20, y=20)


    # Combobox for students
    global student_id
    student_id = tk.StringVar()
    student_entry = ttk.Combobox(managing_grades_fm, textvariable=student_id)
    student_entry['values'] = [f"{student[0]}" for student in students]
    student_entry.place(x=320, y=80)

    # Combobox for courses
    global course_id
    course_id = tk.StringVar()
    course_entry = ttk.Combobox(managing_grades_fm, textvariable=course_id)
    course_entry['values'] = [f"{course[0]} - {course[1]}" for course in courses]
    course_entry.place(x=320, y=160)

    # create the Treeview and bind it to GetValue function
    cols = ('Student_name','Course_name', 'Grades')
    listBox = ttk.Treeview(managing_grades_fm, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
    listBox.grid(row=1)
    listBox.place(x=10, y=450)

    show()  # Call to populate the Treeview

    def clear_treeview():
        # Clear all items from the Treeview
        for item in listBox.get_children():
            listBox.delete(item)

    listBox.bind('<Double-Button-1>', GetValue)


def menu_admin():

    def from_menu_to_student_records():
        menu_admin_fm.destroy()
        root.update()
        admin_page()

    def from_menu_to_course_management():
        menu_admin_fm.destroy()
        root.update()
        managing_courses()

    def from_menu_to_managing_grades():
        menu_admin_fm.destroy()
        root.update()
        managing_grades()

    def deconnexion():
        menu_admin_fm.destroy()
        root.update()
        welcome_page()


    menu_admin_fm = tk.Frame(root, bg=frame_background_color, highlightbackground=frame_border_color,
                                  highlightthickness='10')
    menu_admin_fm.pack(pady=10)
    menu_admin_fm.pack_propagate(False)
    menu_admin_fm.config(width=800, height=800)

    #heading
    heading_labels = tk.Label(menu_admin_fm, bg=label_background_color, text="Welcome on the administrator's menu !", fg=label_color,
                              font=('Overstrike', 18))
    heading_labels.place(width=450, x=200, y=40)


    #buttons
    record_managementBtn = tk.Button(menu_admin_fm, text='Student records Management', bg=label_background_color,
                                 fg=label_color, font=('Overstrike', 18)
                                     , command=from_menu_to_student_records)
    record_managementBtn.place(x=230, y=120, width=350)

    course_managementBtn = tk.Button(menu_admin_fm, text='Course Management', bg=label_background_color,
                                 fg=label_color, font=('Overstrike', 18),
                                     command=from_menu_to_course_management)
    course_managementBtn.place(x=230, y=240, width=350)

    grade_managementBtn = tk.Button(menu_admin_fm, text='Grade Management', bg=label_background_color,
                                     fg=label_color, font=('Overstrike', 18),
                                    command=from_menu_to_managing_grades)
    grade_managementBtn.place(x=230, y=360, width=350)

    deconnexionBtn = tk.Button(menu_admin_fm, text='Log out', bg=label_background_color,
                                    fg=label_color, font=('Overstrike', 18),
                                    command=deconnexion)
    deconnexionBtn.place(x=230, y=480, width=350)

#menu_admin()
welcome_page()
root.mainloop()





