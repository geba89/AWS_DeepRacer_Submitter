import time
import tkinter
from threading import Thread
from deepracer import Aws_DeepRacer_Submitter

PATH = './chromedriver'

keep_submitting = True
can_continue = True

root = tkinter.Tk()
root.title("Deep Racer Submitter")
root.config(padx=30, pady=10)


def aws_submit(email, password, page, model):
    button_id = 7
    global can_continue    
    button_stop_submit.grid(column=0, row=6, columnspan=2)
    submitter = Aws_DeepRacer_Submitter(PATH)
    submitter.open_aws()
    submitter.go_to_log_in_screen()
    submitter.click_existing_account() 
    submitter.aws_select_root(email)
    button_captcha.grid(column=0, row=7, columnspan=2)    
    while can_continue: 
        time.sleep(1)
    button_captcha.grid_forget()
    submitter.aws_root_password(password)
    can_continue = True
    button_security_key.grid(column=0, row=7, columnspan=2)  
    while can_continue: 
        time.sleep(1)
    button_security_key.grid_forget()
    submitter.open_page(page)
    submitter.close_reward()
    submitter.select_and_submit_model(int(model), button_id)
    
    while keep_submitting:
        try:            
            start_time = time.time()
            submitter.check_if_can_submit()
            submitter.open_page(page)
            submitter.select_and_submit_model(int(model), button_id)
            end_time = time.time()
            if end_time - start_time < 15:
                button_id = 8            
        except:
            time.sleep(1)

    print("Finished")
    button_stop_submit.grid_forget()

def continue_submit():
    global can_continue
    can_continue = False


def start_submit():
    global keep_submitting
    global can_continue
    can_continue = True
    keep_submitting = True
    thread = Thread(target=aws_submit, args=(email_var.get(), pass_var.get(), url_var.get(), model_var.get()))
    thread.start()

def stop_submit():
    global keep_submitting
    keep_submitting = False


email_var = tkinter.StringVar(root)
pass_var = tkinter.StringVar(root)
url_var = tkinter.StringVar(root)
model_var = tkinter.StringVar(root)

info_label = tkinter.Label(text="Enter Credentials and Selected Race URL for submit", pady=20)
info_label.grid(column=0, row=0, columnspan=2)

email_input = tkinter.Entry(textvariable=email_var)
email_input.grid(column=1, row=1)

pass_input = tkinter.Entry(textvariable=pass_var, show="*")
pass_input.grid(column=1, row=2)

email_label = tkinter.Label(text="Email Address", justify='left')
email_label.grid(column=0, row=1)

pass_label = tkinter.Label(text="Password", justify='left')
pass_label.grid(column=0, row=2)

race_label = tkinter.Label(text="Race URL")
race_label.grid(column=0, row=3)

race_input = tkinter.Entry(textvariable=url_var)
race_input.grid(column=1, row=3)

model_label = tkinter.Label(text="Model number")
model_label.grid(column=0, row=4)

model_input = tkinter.Entry(textvariable=model_var)
model_input.grid(column=1, row=4)

button_submit = tkinter.Button(text="Submit", width=30, command=start_submit)
button_submit.grid(column=0, row=5, columnspan=2)

button_stop_submit = tkinter.Button(text="Stop Submission", command=stop_submit, width=30)

button_captcha = tkinter.Button(text="Captcha OK", command=continue_submit)

button_security_key = tkinter.Button(text="Security Key OK", command=continue_submit)

root.mainloop()