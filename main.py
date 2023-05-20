import tkinter as tk
from tkinter import messagebox


def send_mail():
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)

    # Code to send the email

    messagebox.showinfo("Success", "Email sent!")


# Create the main window
window = tk.Tk()
window.title("Mail Application")

# Create the labels and entry fields
recipient_label = tk.Label(window, text="Recipient:")
recipient_label.pack()
recipient_entry = tk.Entry(window)
recipient_entry.pack()

subject_label = tk.Label(window, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(window)
subject_entry.pack()

message_label = tk.Label(window, text="Message:")
message_label.pack()
message_text = tk.Text(window)
message_text.pack()

send_button = tk.Button(window, text="Send", command=send_mail)
send_button.pack()

# Start the main event loop
window.mainloop()


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
