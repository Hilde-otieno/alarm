from .customtkinter-snippets *
    import rid9.datetime
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
                    winsound.PlaySound("Music.wav",winsound.SND_ASYNC)
                    break
         
        def get_alarm_time():
            alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
            Alarm(alarm_set_time)
            
        def set_alarm(self):
                self.alarm_window = Tk()
                self.alarm_window.title("Set Alarm")
                self.alarm_window.geometry("680x420+200+200")
                
                # Hour Label
                hours_label = Label(self.alarm_window, text="Hours", 
                font=("times new roman",20))
                hours_label.place(x=150, y=50)
                #  Minute Label
                minute_label = Label(self.alarm_window, text="Minutes", 
                font=("times new roman",20))
                minute_label.place(x=450, y=50)
                # Hour Combobox
                self.hour_var = StringVar()
                self.hour_combo = ttk.Combobox(self.alarm_window, 
                width=10, height=10, textvariable=self.hour_var, 
                font=("times new roman",15))
                self.hour_combo['values'] = hours_list
                self.hour_combo.current(0)
                self.hour_combo.place(x=150,y=90)
                # Minute Combobox
                self.minute_var = StringVar()
                self.minute_combo = ttk.Combobox(self.alarm_window, 
                width=10, height=10, textvariable=self.minute_var, 
                font=("times new roman",15))
                self.minute_combo['values'] = minutes_list
                self.minute_combo.current(0)
                self.minute_combo.place(x=450,y=90)
                # Ringtone Label.
                ringtone_label = Label(self.alarm_window, text="Ringtones", 
                font=("times new roman",20))
                ringtone_label.place(x=150, y=130)
        
                self.ringtone_var = StringVar()
                self.ringtone_combo = ttk.Combobox(self.alarm_window, 
                width=15, height=10, textvariable=self.ringtone_var, 
                font=("times new roman",15))
                self.ringtone_combo['values'] = ringtones_list
                self.ringtone_combo.current(0)
                self.ringtone_combo.place(x=150,y=170)
                # Create an entry for setting a message
                message_label = Label(self.alarm_window, text="Message", 
                font=("times new roman",20))
                message_label.place(x=150, y=210)
                self.message_var = StringVar()
                self.message_entry = Entry(self.alarm_window, 
                textvariable=self.message_var, font=("times new roman",14), width=30)
                self.message_entry.insert(0, 'Wake Up')
                self.message_entry.place(x=150, y=250)
                # Test Button: For testing the ringtone music.
                test_button = Button(self.alarm_window, text='Test', 
                font=('Helvetica',15), bg="white", fg="black", command=self.preview_alarm)
                test_button.place(x=150, y=300)
                # The Cancel Button: For cancel the alarm.
                cancel_button = Button(self.alarm_window, 
                text='Cancel', font=('Helvetica',15), bg="white", 
                fg="black", command=self.alarm_window.destroy)
                cancel_button.place(x=390, y=300)
                # The Start Button: For set the alarm time
                start_button = Button(self.alarm_window, text='Start',
                font=('Helvetica',15), bg="green", fg="white", command=self._threading)
                start_button.place(x=490, y=300)
                self.alarm_window.mainloop()
        