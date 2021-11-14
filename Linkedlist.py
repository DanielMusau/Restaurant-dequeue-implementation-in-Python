from tkinter import Button, Canvas, TOP, Label, RAISED, BOTTOM, Tk
from tkinter.messagebox import showerror, showinfo
from PIL import ImageTk, Image
from collections import deque
from tkinter.constants import NW

class ListDeque:

    def __init__(self, window: Tk, iterable=None):
        # Initialize a new list to store the items
        self.list = deque()
        self.counter = 0
        self.window = window
        self.color_primary = "blue"
        
        self.images = ["C:/Users/Daniel Musau/OneDrive/Documents/Bsc. Computer Science/3rd Year/3.1/ICS 2301 Design and Analysis of Algorithms/images/person1.jpg",
                       "C:/Users/Daniel Musau/OneDrive/Documents/Bsc. Computer Science/3rd Year/3.1/ICS 2301 Design and Analysis of Algorithms/images/person2.jpg",
                       "C:/Users/Daniel Musau/OneDrive/Documents/Bsc. Computer Science/3rd Year/3.1/ICS 2301 Design and Analysis of Algorithms/images/person1.jpg",
                       "C:/Users/Daniel Musau/OneDrive/Documents/Bsc. Computer Science/3rd Year/3.1/ICS 2301 Design and Analysis of Algorithms/images/person2.jpg",
                       "C:/Users/Daniel Musau/OneDrive/Documents/Bsc. Computer Science/3rd Year/3.1/ICS 2301 Design and Analysis of Algorithms/images/person1.jpg",
                       "C:/Users/Daniel Musau/OneDrive/Documents/Bsc. Computer Science/3rd Year/3.1/ICS 2301 Design and Analysis of Algorithms/images/person2.jpg"]
        self.img = []
        self.text = deque()
        self.labels = deque()
        
        
        if iterable is not None:
            self.list.extend(iterable)
            
        
        self.bottom_panel = Canvas(self.window, width=window_width, height=(window_height/2))
        self.bottom_panel.pack(side=BOTTOM)
        
        self.top_panel = Canvas(self.window, width=(window_width/2), height=window_height)
        self.top_panel.pack(side=TOP)
        
        
        
        # Draw components for the top panel
    
        Button(self.top_panel, text="Add First", fg="white", bg=self.color_primary, font=("Arial", 13, "bold"),
               relief=RAISED,bd=7,command=self.add_first).place(x=82, y=30)
        
        Button(self.top_panel, text="Add Last", fg="white", bg=self.color_primary, font=("Arial", 13, "bold"),
               relief=RAISED,bd=7,command=self.add_last).place(x=82, y=80)
        
        Button(self.top_panel, text="Remove First", fg="white", bg=self.color_primary, font=("Arial", 13, "bold"),
               relief=RAISED,bd=7,command=self.remove_first).place(x=82, y=130)
        
        Button(self.top_panel, text="Remove Last", fg="white", bg=self.color_primary, font=("Arial", 13, "bold"),
               relief=RAISED,bd=7,command=self.remove_last).place(x=82, y=180)
        
        Button(self.top_panel, text="First", fg="white", bg=self.color_primary, font=("Arial", 13, "bold"),
               relief=RAISED,bd=7,command=self.peek_first).place(x=282, y=30)
        
        Button(self.top_panel, text="Last", fg="white", bg=self.color_primary, font=("Arial", 13, "bold"),
               relief=RAISED,bd=7,command=self.peek_last).place(x=282, y=80)
        
        Button(self.top_panel, text="Size", fg="white", bg=self.color_primary, font=("Arial", 13, "bold"),
               relief=RAISED,bd=7,command=self.report_size).place(x=282, y=130)
        
        Button(self.top_panel, text="Is Empty?", fg="white", bg=self.color_primary, font=("Arial", 13, "bold"),
               relief=RAISED,bd=7,command=self.report_empty_stat).place(x=282, y=180)

    def is_empty(self):
        #To return true if the double ended queue is empty, or false if otherwise
        if self.length() == 0:
            return True
        return False
    
    def report_empty_stat(self):
        #To show the is empty message on screen
        msg = 'False'
        if self.is_empty():
            msg = 'True'
        showinfo('Is Empty?', msg)
    
    def length(self):
        #To return the number of items present in the double ended queue
        return len(self.list)
    
    def report_size(self):
        #To display the size of the double ended queue
        showinfo('Size', f'Total Customers are: {self.length()}')
        

    def add_last(self):
        #To insert a customer at the end of the double ended queue
        if self.length() < 6:
            if self.length() == 0:
                number=len(self.list)
                self.img.append(ImageTk.PhotoImage(Image.open(self.images[number])))
                self.labels.append(self.bottom_panel.create_text(150, 300, text="Customer ", font=("Arial", int(13.0))))
                self.text.append("Customer ")
               
                self.list.append(self.bottom_panel.create_image(100, 10, anchor=NW, image=self.img[number]))

            else: 
                number=len(self.list)
                self.counter = self.counter+1
                number2=str(self.counter)
                self.img.append(ImageTk.PhotoImage(Image.open(self.images[number])))
                self.labels.append(self.bottom_panel.create_text(150+120*number, 300, text="Customer "+number2, font=("Arial", int(13.0))))
                self.text.append("Customer "+number2)

                self.list.append(self.bottom_panel.create_image(100+120*number, 10, anchor=NW, image=self.img[number]))

        else:
            showerror('Error!', 'Maximum customers reached')

    def add_first(self):
        #To insert a customer at the beginning of the double ended queue
        if self.length() < 6:
            if self.length() == 0:
                number=len(self.list)
                self.counter = self.counter+1
                number2 = str(self.counter)
                self.img.append(ImageTk.PhotoImage(Image.open(self.images[number])))
                self.labels.appendleft(self.bottom_panel.create_text(150, 300, text="Customer "+number2, font=("Arial", int(13.0))))
                self.text.appendleft("Customer "+number2)
                
                self.list.appendleft(self.bottom_panel.create_image(100, 10, anchor=NW, image=self.img[number]))
            else:
                for i in self.list:
                    self.bottom_panel.move(i, +120, 0)
                    
                for i in self.labels:
                    self.bottom_panel.move(i, +120, 0)
                    
                number=len(self.list)
                self.counter = self.counter+1
                number2=str(self.counter)
                self.img.append(ImageTk.PhotoImage(Image.open(self.images[number])))
                self.labels.appendleft(self.bottom_panel.create_text(150, 300, text="Customer "+number2, font=("Arial", int(13.0))))
                self.text.appendleft("Customer " +number2)
                
                self.list.appendleft(self.bottom_panel.create_image(100, 10, anchor=NW, image=self.img[number]))
                
        else:
            showerror('Error!', 'Maximum customers reached.')

    def peek_first(self):
        #To return the first customer in the queue or return error if none
        if self.is_empty():
            showerror('Error!', 'There are currently no customers')
        else:
            showinfo('First Customer', f'The First Customer is "{self.text[0]}"')

    def peek_last(self):
        #To return the last customer in the queue or return error if none
        if self.is_empty():
            showerror('Error!', 'There are currently no customers')
        else:
            showinfo('Last Customer', f'The Last Customer is "{self.text[-1]}"')
            

    def remove_first(self):
        #To delete the first customer in the queue or error if none
        if self.is_empty():
            showerror("Error!","There are no customers.")
        else:
            self.bottom_panel.delete(self.list[0])
            self.bottom_panel.delete(self.labels[0])
            self.labels.popleft()
            
            self.list.popleft()
            
            for i in self.list:
                self.bottom_panel.move(i, -120, 0)
                
            for i in self.labels:
                self.bottom_panel.move(i, -120, 0)
                
            self.text.popleft()

    def remove_last(self):
        #To remove the last customer in the queue or error if none
        if self.is_empty():
            showerror("Error!","There are no customers.")
        else:
            self.bottom_panel.delete(self.list[-1])
            self.list.pop()
            
            self.bottom_panel.delete(self.labels[-1])
            self.labels.pop()
            self.text.pop()
        
if __name__ == '__main__':
    window_height = 650
    window_width = 1100

    root = Tk()
    root.title("Dequeue Restaurant Implementation")
    root.maxsize(window_width, window_height)
    root.minsize(window_width, window_height)
    ListDeque(root)
    root.mainloop()