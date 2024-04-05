/* from tkinter import *
import datetime
import time
         
class AlarmApp:
   def__init__(self):
   self.root=Tk()
   self.root.title("Alarm Clock") 
   
    
   self.hour_var = StringVar()
   self.minute_var = StringVar()
   self.second_var = StringVar()

   self.create_widgets()
   self.root.mainloop()
def create_widgets(self):
   
  Label(self.root, text="Hour",font=("times new roman",20)).grid(row=0, column=0,padx=20, pady=20)
  Label(self.root, text="Minute",font=("times new roman",20)).grid(row=0, column=0,padx=20, pady=20)
  Label(self.root, text="Second",font=("times new roman",20)).grid(row=0, column=0,padx=20, pady=20)

  self.hour_combo = Combobox(self.root, width=10, height=10, textvariable=self.hour_var, font=("times new roman", 15))
  self.hour_combo.grid(row=0, column=1)

  self.hour_combo['values'] = tuple(str(i).zfill(2)for i in range(24))

  self.minute_combo=Combobox(self.root, width=10, height=10, textvariable=self.root, width=10, height=10, textvariable=self.minut_var, font=("times new"))

   

          
# def Alarm(set_alarm_timer):
#          while True:
#                 time.sleep(1)
#                 actual_time = datetime.datetime.now()
#                 cur_time = actual_time.strftime("%H:%M:%S")
#                 cur_date = actual_time.strftime("%d/%m/%Y")
#                 msg="Current Time: "+str(cur_time)
#                 print(msg)
#                 if cur_time == set_alarm_timer:
#                     break
         
# def get_alarm_time():
#             alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
#             Alarm(alarm_set_time)
            
# def set_alarm(self):
#                 self.alarm_window = Tk()
#                 self.alarm_window.title("Set Alarm")
                
#                 hours_label = Label(self.alarm_window, text="Hours", 
#                 font=("times new roman",20))
            
#                 minute_label = Label(self.alarm_window, text="Minutes", 
#                 font=("times new roman",20))
        
#                 self.hour_var = StringVar()
#                 self.hour_combo = Tk.Combobox(self.alarm_window, 
#                 width=10, height=10, textvariable=self.hour_var, 
#                 font=("times new roman",15))
        
#                 self.minute_var = StringVar()
#                 self.minute_combo = Tk.Combobox(self.alarm_window, 
#                 width=10, height=10, textvariable=self.minute_var, 
#                 font=("times new roman",15))
                
#                 ringtone_label = Label(self.alarm_window, text="Ringtones", 
#                 font=("times new roman",20))
        
#                 self.ringtone_var = StringVar()
#                 self.ringtone_combo = Tk.Combobox(self.alarm_window, 
#                 width=15, height=10, textvariable=self.ringtone_var, 
#                 font=("times new roman",15))
                
#                 message_label = Label(self.alarm_window, text="Message", 
#                 font=("times new roman",20))
#                 self.message_var = StringVar()
#                 self.message_entry = Entry(self.alarm_window, 
#                 textvariable=self.message_var, font=("times new roman",14), width=30)
#                 self.message_entry.insert(0, 'Wake Up')
            
#                 test_button = Button(self.alarm_window, text='Test', 
#                 font=('Helvetica',15), bg="white", fg="black", command=self.preview_alarm)
                
#                 cancel_button = Button(self.alarm_window, 
#                 text='Cancel', font=('Helvetica',15), bg="white", 
#                 fg="black", command=self.alarm_window.destroy)
                
#                 start_button = Button(self.alarm_window, text='Start',
#                 font=('Helvetica',15), bg="green", fg="white", command=self._threading)
#                 self.alarm_window.mainloop()
         */

from tkinter import *
import datetime
import time

class AlarmApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Alarm Clock")
        
        self.hour_var = StringVar()
        self.minute_var = StringVar()
        self.second_var = StringVar()
        
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        # Labels
        Label(self.root, text="Hour", font=("times new roman", 20)).grid(row=0, column=0, padx=20, pady=20)
        Label(self.root, text="Minute", font=("times new roman", 20)).grid(row=1, column=0, padx=20, pady=20)
        Label(self.root, text="Second", font=("times new roman", 20)).grid(row=2, column=0, padx=20, pady=20)
        
        # Comboboxes
        self.hour_combo = Combobox(self.root, width=10, height=10, textvariable=self.hour_var, font=("times new roman", 15))
        self.hour_combo.grid(row=0, column=1)
        self.hour_combo['values'] = tuple(str(i).zfill(2) for i in range(24))
        
        self.minute_combo = Combobox(self.root, width=10, height=10, textvariable=self.minute_var, font=("times new roman", 15))
        self.minute_combo.grid(row=1, column=1)
        self.minute_combo['values'] = tuple(str(i).zfill(2) for i in range(60))
        
        self.second_combo = Combobox(self.root, width=10, height=10, textvariable=self.second_var, font=("times new roman", 15))
        self.second_combo.grid(row=2, column=1)
        self.second_combo['values'] = tuple(str(i).zfill(2) for i in range(60))
        
        # Buttons
        Button(self.root, text='Set Alarm', font=('Helvetica', 15), bg="green", fg="white", command=self.set_alarm).grid(row=3, column=0, columnspan=2, pady=20)
        Button(self.root, text='Exit', font=('Helvetica', 15), bg="red", fg="white", command=self.root.destroy).grid(row=4, column=0, columnspan=2)

    def set_alarm(self):
        hour = self.hour_var.get()
        minute = self.minute_var.get()
        second = self.second_var.get()
        
        alarm_time = f"{hour}:{minute}:{second}"
        self.alarm(alarm_time)
    
    def alarm(self, set_alarm_timer):
        while True:
            time.sleep(1)
            actual_time = datetime.datetime.now()
            cur_time = actual_time.strftime("%H:%M:%S")
            print("Current Time:", cur_time)
            if cur_time == set_alarm_timer:
                print("Alarm Time Reached!")
                break

if __name__ == "__main__":
    app = AlarmApp() 

