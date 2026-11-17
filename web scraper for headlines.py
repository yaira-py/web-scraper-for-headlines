import tkinter as tk
import requests
from bs4 import BeautifulSoup

class Headlines:
    def __init__(self,root):
        self.root=root
        self.root.title('Web scraper for headlines')
        self.root.geometry('500x500')

        self.head_lb=tk.Label(self.root,text='Latest Headlines',font=('Arial',13,'bold'),fg="#020202")
        self.head_lb.pack(pady=10)

        self.get_btn=tk.Button(self.root,text='See',width=10,font=('Arial',12,'bold'),bg="#c22828",fg='white',command=self.get)
        self.get_btn.pack(pady=10)

        self.res_box=tk.Text(self.root,height=40,bg='white',state='disabled')
        self.res_box.pack(pady=10,padx=20)


  

    def get(self):
        url='https://www.bbc.com/news'
        
        self.head_lb.config(text='it will take some time to load')
        self.root.update()

        response= requests.get(url)
        soup= BeautifulSoup(response.text,'html.parser')
        headlines= soup.find_all('h2')
       

        for headline in headlines:
            text= headline.get_text(strip=True)

            if text:
                self.res_box.config(state='normal')
                self.res_box.insert(tk.END,f'{text}\n')

            else:
                continue



if __name__=='__main__':
    win=tk.Tk()
    app=Headlines(win)
    win.mainloop()
