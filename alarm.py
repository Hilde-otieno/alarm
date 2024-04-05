from tkinter import *
import datetime
import time
        
def Alarm(set_alarm_timer):
         while True:
                time.sleep(1)
                actual_time = datetime.datetime.now()
                cur_time = actual_time.strftime("%H:%M:%S")
                cur_date = actual_time.strftime("%d/%m/%Y")
                msg="Current Time: "+str(cur_time)
                print(msg)
                if cur_time == set_alarm_timer:
                    break
         
def get_alarm_time():
            alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
            Alarm(alarm_set_time)
            
def set_alarm(self):
                self.alarm_window = Tk()
                self.alarm_window.title("Set Alarm")
                
                hours_label = Label(self.alarm_window, text="Hours", 
                font=("times new roman",20))
            
                minute_label = Label(self.alarm_window, text="Minutes", 
                font=("times new roman",20))
        
                self.hour_var = StringVar()
                self.hour_combo = Tk.Combobox(self.alarm_window, 
                width=10, height=10, textvariable=self.hour_var, 
                font=("times new roman",15))
        
                self.minute_var = StringVar()
                self.minute_combo = Tk.Combobox(self.alarm_window, 
                width=10, height=10, textvariable=self.minute_var, 
                font=("times new roman",15))
                
                ringtone_label = Label(self.alarm_window, text="Ringtones", 
                font=("times new roman",20))
        
                self.ringtone_var = StringVar()
                self.ringtone_combo = Tk.Combobox(self.alarm_window, 
                width=15, height=10, textvariable=self.ringtone_var, 
                font=("times new roman",15))
                
                message_label = Label(self.alarm_window, text="Message", 
                font=("times new roman",20))
                self.message_var = StringVar()
                self.message_entry = Entry(self.alarm_window, 
                textvariable=self.message_var, font=("times new roman",14), width=30)
                self.message_entry.insert(0, 'Wake Up')
            
                test_button = Button(self.alarm_window, text='Test', 
                font=('Helvetica',15), bg="white", fg="black", command=self.preview_alarm)
                
                cancel_button = Button(self.alarm_window, 
                text='Cancel', font=('Helvetica',15), bg="white", 
                fg="black", command=self.alarm_window.destroy)
                
                start_button = Button(self.alarm_window, text='Start',
                font=('Helvetica',15), bg="green", fg="white", command=self._threading)
                self.alarm_window.mainloop()
        