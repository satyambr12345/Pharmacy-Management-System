from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        root.geometry("1550x820+-10+0")
        #...............addMed Var...............
        self.refMed_var=StringVar()
        self.addMed_var=StringVar()
        #...................main var.............
        self.ref_var=StringVar()
        self.med_var=StringVar()
        self.type_var=StringVar()
        self.tablet_var=StringVar()
        self.lot_var=StringVar()
        self.issue_var=StringVar()
        self.exp_var=StringVar()
        self.uses_var=StringVar()
        self.side_var=StringVar()
        self.warn_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.prodqt_var=StringVar()

        lbltitle=Label(self.root,text="BlueMedix Pharmacy Management System",bd=15,relief=RIDGE,bg='white',fg='darkgreen',font=('Times new roman',50,'bold'),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)
        logo=Image.open("logo.jpg")
        logo=logo.resize((80,80))
        self.photologo=ImageTk.PhotoImage(logo)
        b1=Button(self.root,image=self.photologo,borderwidth=0)
        b1.place(x=48,y=16)
        #.............................. DataFrame..................................
        Dataframe=Frame(self.root,bd=15,relief=RIDGE)
        Dataframe.place(x=0,y=118,width=1535,height=370)
        #.....................................Button Frame.................................
        BtnFrame=Frame(self.root,bd=13,relief=RIDGE)
        BtnFrame.place(x=0,y=490,width=1535,height=65)
        #....................................Main Button...................................
        btnAddMed=Button(BtnFrame,text="Add Medicine",fg="white",font=('times new roman',13,'bold'),bg="darkgreen",command=self.add_data)
        btnAddMed.grid(row=0,column=0)
        btnUpdate=Button(BtnFrame,text="UPDATE",width=14,fg="white",font=('times new roman',13,'bold'),bg="red",command=self.updatemain)
        btnUpdate.grid(row=0,column=1)
        btnDelete=Button(BtnFrame,text="DELETE",width=14,fg="white",font=('times new roman',13,'bold'),bg="red",command=self.deletemain)
        btnDelete.grid(row=0,column=2)
        btnReset=Button(BtnFrame,text="RESET",width=14,fg="white",font=('times new roman',13,'bold'),bg="darkgreen",command=self.resetmain)
        btnReset.grid(row=0,column=3)
        btnExit=Button(BtnFrame,text="EXIT",width=14,fg="white",font=('times new roman',13,'bold'),bg="darkgreen",command=self.root.destroy)
        btnExit.grid(row=0,column=4)
        #.....................................SearchBy............................................
        self.search_var=StringVar()
        lsearch=Label(BtnFrame,text="Search By",width=12,fg="white",font=('times new roman',14,'bold'),bg="red")
        lsearch.grid(row=0,column=5,sticky=W)
        search_combo=ttk.Combobox(BtnFrame,width=20,font=('times new roman',12,'bold'),state="readonly",textvariable=self.search_var)
        search_combo["values"]=("Refno","medame","lotno")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)
        #...........................Entry Fill.............................
        self.srchtxt_var=StringVar()
        txtSearch=Entry(BtnFrame,bd=3,width=20,font=('times new roman',12,'bold'),relief=RIDGE,textvariable=self.srchtxt_var)
        txtSearch.grid(row=0,column=7)
        btnSearch=Button(BtnFrame,command=self.searchmain,text="SEARCH",width=14,fg="white",font=('times new roman',13,'bold'),bg="darkgreen")
        btnSearch.grid(row=0,column=8)
        btnShowall=Button(BtnFrame,text="SHOW ALL",width=14,fg="white",font=('times new roman',13,'bold'),bg="darkgreen",command=self.fetchmain)
        btnShowall.grid(row=0,column=9)
        #................................Data Frame Left..................
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",font=('Times new roman',15,'bold'))
        DataframeLeft.place(x=8,y=8,width=900,height=330)

        ref=Label(DataframeLeft,text="Reference No.: ",width=14,font=('times new roman',14,'bold'),padx=2)
        ref.grid(row=0,column=0)
        conn=mysql.connector.connect(host="localhost",user="root",password="sanjaysavitri12@",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row=my_cursor.fetchall()
        refNo=ttk.Combobox(DataframeLeft,textvariable=self.ref_var,width=22,font=('times new roman',12,'bold'),state="readonly")
        refNo["values"]=row
        refNo.grid(row=0,column=1)
        refNo.current(0)
        cmpyname=Label(DataframeLeft,text="Company Name: ",width=12,font=('times new roman',14,'bold'))
        cmpyname.grid(row=1,column=0)
        cmpy=Entry(DataframeLeft,textvariable=self.med_var,bd=3,width=24,font=('times new roman',12,'bold'),relief=RIDGE)
        cmpy.grid(row=1,column=1)
        lblmed=Label(DataframeLeft,text="Type of Medicine: ",width=14,font=('times new roman',14,'bold'),padx=2)
        lblmed.grid(row=2,column=0)
        typepmed=ttk.Combobox(DataframeLeft,textvariable=self.type_var,width=22,font=('times new roman',12,'bold'),state="readonly")
        typepmed["values"]=("Tablet","Liquid","Injections","Capsules","Inhales")
        typepmed.grid(row=2,column=1)
        typepmed.current(0)
        medname=Label(DataframeLeft,text="Medicine Name: ",width=14,font=('times new roman',14,'bold'),padx=2)
        medname.grid(row=3,column=0)
        conn=mysql.connector.connect(host="localhost",user="root",password="sanjaysavitri12@",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select MedName from pharma")
        row=my_cursor.fetchall()
        mednamec=ttk.Combobox(DataframeLeft,textvariable=self.tablet_var,width=22,font=('times new roman',12,'bold'),state="readonly")
        mednamec["values"]=row
        mednamec.grid(row=3,column=1)
        mednamec.current(0)
        lotno=Label(DataframeLeft,text="Lot No.: ",width=14,font=('times new roman',14,'bold'),padx=2)
        lotno.grid(row=4,column=0)
        lotno2=Entry(DataframeLeft,bd=3,textvariable=self.lot_var,width=24,font=('times new roman',12,'bold'),relief=RIDGE)
        lotno2.grid(row=4,column=1)
        isdate=Label(DataframeLeft,text="Issue Date: ",width=14,font=('times new roman',14,'bold'),padx=2)
        isdate.grid(row=5,column=0)
        isdate2=Entry(DataframeLeft,bd=3,width=24,font=('times new roman',12,'bold'),relief=RIDGE,textvariable=self.issue_var)
        isdate2.grid(row=5,column=1)
        exdate=Label(DataframeLeft,text="Expiry Date: ",width=14,font=('times new roman',14,'bold'),padx=2)
        exdate.grid(row=6,column=0)
        exdate2=Entry(DataframeLeft,bd=3,width=24,font=('times new roman',12,'bold'),relief=RIDGE,textvariable=self.exp_var)
        exdate2.grid(row=6,column=1)
        uses=Label(DataframeLeft,text="Uses: ",width=14,font=('times new roman',14,'bold'),padx=2)
        uses.grid(row=7,column=0)
        uses2=Entry(DataframeLeft,bd=3,width=24,font=('times new roman',12,'bold'),relief=RIDGE,textvariable=self.uses_var)
        uses2.grid(row=7,column=1)
        sideeffects=Label(DataframeLeft,text="Side Effects: ",width=14,font=('times new roman',14,'bold'),padx=2)
        sideeffects.grid(row=8,column=0)
        sideeffects2=Entry(DataframeLeft,bd=3,width=24,font=('times new roman',12,'bold'),relief=RIDGE,textvariable=self.side_var)
        sideeffects2.grid(row=8,column=1)
        Pricewar=Label(DataframeLeft,text="Warning: ",width=16,font=('times new roman',14,'bold'),padx=2)
        Pricewar.grid(row=0,column=3)
        Pricewar2=Entry(DataframeLeft,bd=3,width=24,font=('times new roman',12,'bold'),relief=RIDGE,textvariable=self.warn_var)
        Pricewar2.grid(row=0,column=4)
        dosage=Label(DataframeLeft,text="Dosage: ",width=14,font=('times new roman',14,'bold'),padx=2)
        dosage.grid(row=1,column=3)
        dosage2=Entry(DataframeLeft,bd=3,width=24,font=('times new roman',12,'bold'),relief=RIDGE,textvariable=self.dosage_var)
        dosage2.grid(row=1,column=4)
        price=Label(DataframeLeft,text="Price: ",width=14,font=('times new roman',14,'bold'),padx=2)
        price.grid(row=2,column=3)
        price2=Entry(DataframeLeft,bd=3,width=24,font=('times new roman',12,'bold'),relief=RIDGE,textvariable=self.price_var)
        price2.grid(row=2,column=4)
        prodqt=Label(DataframeLeft,text="Product Qty.: ",width=14,font=('times new roman',14,'bold'),padx=2)
        prodqt.grid(row=3,column=3)
        prodqt2=Entry(DataframeLeft,bd=3,width=24,font=('times new roman',12,'bold'),relief=RIDGE,textvariable=self.prodqt_var)
        prodqt2.grid(row=3,column=4)
        img1=Image.open("madam.jpg")
        img1=img1.resize((160,100))
        self.photoimg1=ImageTk.PhotoImage(img1)
        btn1=Button(self.root,image=self.photoimg1,borderwidth=0)
        btn1.place(x=430,y=316)
        img2=Image.open("eng.jpg")
        img2=img2.resize((160,100))
        self.photoimg2=ImageTk.PhotoImage(img2)
        btn2=Button(self.root,image=self.photoimg2,borderwidth=0)
        btn2.place(x=590,y=316)
        img3=Image.open("tablet.jpg")
        img3=img3.resize((160,100))
        self.photoimg3=ImageTk.PhotoImage(img3)
        btn3=Button(self.root,image=self.photoimg3,borderwidth=0)
        btn3.place(x=750,y=316)
        lblh=Label(DataframeLeft,text="Stay Safe and Healthy.",padx=15,pady=6,font=('arial',12,'bold'),width=15,fg="red")
        lblh.place(x=495,y=114)
        #.......................Product frame.......................................
       
        #...........................Dataframe Right....................................
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",fg="darkgreen",font=('Times new roman',15,'bold'))
        DataframeRight.place(x=910,y=8,width=592,height=330)
        img4=Image.open("img6.jpg")
        img4=img4.resize((130,80))
        self.photoimg4=ImageTk.PhotoImage(img4)
        btn4=Button(self.root,image=self.photoimg4,borderwidth=0)
        btn4.place(x=950,y=170)
        img5=Image.open("tab.jpg")
        img5=img5.resize((160,80))
        self.photoimg5=ImageTk.PhotoImage(img5)
        btn5=Button(self.root,image=self.photoimg5,borderwidth=0)
        btn5.place(x=1080,y=170)
        img6=Image.open("img5.jpg")
        img6=img6.resize((160,80))
        self.photoimg6=ImageTk.PhotoImage(img6)
        btn6=Button(self.root,image=self.photoimg6,borderwidth=0)
        btn6.place(x=1210,y=170)
        img7=Image.open("img7.jpg")
        img7=img7.resize((140,80))
        self.photoimg7=ImageTk.PhotoImage(img7)
        btn7=Button(self.root,image=self.photoimg7,borderwidth=0)
        btn7.place(x=1360,y=170)
        refnum=Label(DataframeRight,text="Reference No.: ",font=('times new roman',14,'bold'))
        refnum.place(x=0,y=90)
        refnum2=Entry(DataframeRight,textvariable=self.refMed_var,bd=3,width=20,font=('times new roman',12,'bold'),relief=RIDGE)
        refnum2.place(x=150,y=90)
        medn=Label(DataframeRight,text="Medicine Name: ",font=('times new roman',14,'bold'))
        medn.place(x=0,y=120)
        medn2=Entry(DataframeRight,textvariable=self.addMed_var,bd=3,width=20,font=('times new roman',12,'bold'),relief=RIDGE)
        medn2.place(x=150,y=120)
        #.......................Side Frame.........................................
        sideFrame=Frame(DataframeRight,relief=RIDGE,bd=4,bg="white")
        sideFrame.place(x=0,y=150,width=320,height=140)
        sc_x=ttk.Scrollbar(sideFrame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(sideFrame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)
        self.medicine_table=ttk.Treeview(sideFrame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)
        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")
        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)
        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)
        self.medicine_table.bind("<ButtonRelease-1>",self.MedGetCursor)
        #................................Mediicne add Buttons...........................
        downFrame=Frame(DataframeRight,relief=RIDGE,bd=3,bg="darkgreen")
        downFrame.place(x=330,y=150,width=135,height=137)
        btnadd=Button(downFrame,text="ADD",width=12,fg="white",font=('times new roman',13,'bold'),bg="lime",command=self.AddMed)
        btnadd.grid(row=0,column=0)
        btnupd=Button(downFrame,command=self.UpdateMed,text="UPDATE",width=12,fg="white",font=('times new roman',13,'bold'),bg="purple")
        btnupd.grid(row=1,column=0)
        btndel=Button(downFrame,text="DELETE",command=self.DeleteMed,width=12,fg="white",font=('times new roman',13,'bold'),bg="red")
        btndel.grid(row=2,column=0)
        btnclre=Button(downFrame,command=self.ClearMed,text="CLEAR",width=12,fg="white",font=('times new roman',13,'bold'),bg="orange")
        btnclre.grid(row=3,column=0)
        #..................................Table frame..................................
        prodFrame=Frame(self.root,bd=15,relief=RIDGE)
        prodFrame.place(x=0,y=560,height=221,width=1535)
        Table_frame=Frame(self.root,bd=12,relief=RIDGE,padx=4)
        Table_frame.place(x=15,y=575,height=190,width=1510)
        scr_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scr_x.pack(side=BOTTOM,fill=X)
        scr_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scr_y.pack(side=RIGHT,fill=Y)
        self.data_table=ttk.Treeview(Table_frame,column=("ref","medname","type","Tablet_name","lotno","Issuedate","Exp.date","uses","sideEffect","warning","Dosage","Price","prodqt"),xscrollcommand=scr_x.set,yscrollcommand=scr_y.set)
        scr_x.config(command=self.data_table.xview)
        scr_y.config(command=self.data_table.yview)

        self.data_table["show"]="headings"

        self.data_table.heading("ref",text="Reference")
        self.data_table.heading("medname",text="Company Name")
        self.data_table.heading("type",text="Type of Medicine")
        self.data_table.heading("Tablet_name",text="Tablet Name")
        self.data_table.heading("lotno",text="Lot No.")
        self.data_table.heading("Issuedate",text="Issue Date")
        self.data_table.heading("Exp.date",text="Expiry Date")
        self.data_table.heading("uses",text="Uses")
        self.data_table.heading("sideEffect",text="Side Effect")
        self.data_table.heading("warning",text="Warning")
        self.data_table.heading("Dosage",text="Dosage")
        self.data_table.heading("Price",text="Price")
        self.data_table.heading("prodqt",text="Prod. Qty.")
        self.data_table.pack(fill=BOTH,expand=1)
        self.data_table.column("ref",width=100)
        self.data_table.column("medname",width=100)
        self.data_table.column("type",width=100)
        self.data_table.column("Tablet_name",width=100)
        self.data_table.column("lotno",width=100)
        self.data_table.column("Issuedate",width=100)
        self.data_table.column("Exp.date",width=100)
        self.data_table.column("uses",width=100)
        self.data_table.column("sideEffect",width=100)
        self.data_table.column("warning",width=100)
        self.data_table.column("Dosage",width=100)
        self.data_table.column("Price",width=100)
        self.data_table.column("prodqt",width=100)
        self.data_table.bind("<ButtonRelease-1>",self.medmaincursor)
        self.fetchData()  #.............so that when we run the code it shows the rows of tables at the starting.........
        self.fetchmain()

        #....................MySQL Codes....................................
    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="sanjaysavitri12@",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(self.refMed_var.get(),self.addMed_var.get()
        ))
        conn.commit()
        self.fetchData()
        messagebox.showinfo("Success","Medicine Added")
        self.MedGetCursor()
        conn.close()
    #...............Inserting data into sideframe.........................
    def fetchData(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="sanjaysavitri12@",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()    
        conn.close()
    def MedGetCursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refMed_var.set(row[0])
        self.addMed_var.set(row[1])        

    def UpdateMed(self):
        if (self.addMed_var.get()=="" or self.refMed_var.get()==""):
            messagebox.showerror("Error","All fields are required.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="sanjaysavitri12@",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",(self.addMed_var.get(),self.refMed_var.get()))
            conn.commit()
            self.fetchData()
            conn.close()
            messagebox.showinfo("Success","Medicine name updated successfully")

    def DeleteMed(self):
        if (self.addMed_var.get()=="" or self.refMed_var.get()==""):
            messagebox.showerror("Error","All fields are required.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="sanjaysavitri12@",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("delete from pharma where Ref=%s and MedName=%s",(self.refMed_var.get(),self.addMed_var.get()))
            conn.commit()
            self.fetchData()
            conn.close()
            messagebox.showinfo("Success","Medicine Deleted Successfully")   
    def ClearMed(self):
        if (self.addMed_var.get()=="" and self.refMed_var.get()==""):
            messagebox.showerror("Error","All fields are already empty.")
        self.addMed_var.set("")
        self.refMed_var.set("")
    #.................................Main table.............................
    def add_data(self):
        if (self.ref_var.get()=="" or self.lot_var.get()==""):
            messagebox.showerror("Error","All fields are required.")
        else:                
            conn=mysql.connector.connect(host="localhost",user="root",password="sanjaysavitri12@",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharmacy(Refno,medame,type,tabletname,lotno,issuedate,expdate,uses,sideeffect,warning,dosage,price,prodqty) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.ref_var.get(), self.med_var.get(),self.type_var.get(),self.tablet_var.get(),self.lot_var.get(),self.issue_var.get(),self.exp_var.get(),self.uses_var.get(),self.side_var.get(),self.warn_var.get(),self.dosage_var.get(),self.price_var.get(),self.prodqt_var.get()))
            conn.commit()
            self.fetchmain()
            self.medmaincursor()
            messagebox.showinfo("Success","Data Added successfully.")
            conn.close()
        
    def fetchmain(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="sanjaysavitri12@",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        rows=my_cursor.fetchall()
        if( len(rows)!=0):
            self.data_table.delete(*self.data_table.get_children())
            for i in rows:
                self.data_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def medmaincursor(self,event=""):
        cursor=self.data_table.focus()
        content=self.data_table.item(cursor)
        row=content["values"]
        self.ref_var.set(row[0])
        self.med_var.set(row[1])
        self.type_var.set(row[2])
        self.tablet_var.set(row[3])
        self.lot_var.set(row[4])
        self.issue_var.set(row[5])
        self.exp_var.set(row[6])
        self.uses_var.set(row[7])
        self.side_var.set(row[8])
        self.warn_var.set(row[9])
        self.dosage_var.set(row[10])
        self.price_var.set(row[11])
        self.prodqt_var.set(row[12])
    def updatemain(self):
        if (self.med_var.get()=="" or self.lot_var.get()==""):
            messagebox.showerror("Error","All fields are required.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="sanjaysavitri12@",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set medame=%s ,type=%s ,tabletname=%s ,lotno=%s ,issuedate=%s , expdate=%s , uses=%s , sideeffect=%s , warning=%s, dosage=%s, price=%s, prodqty=%s where Refno=%s",(self.med_var.get(),self.type_var.get(),self.tablet_var.get(),self.lot_var.get(),self.issue_var.get(),self.exp_var.get(),self.uses_var.get(),self.side_var.get(),self.warn_var.get(),self.dosage_var.get(),self.price_var.get(),self.prodqt_var.get(),self.ref_var.get()))
            conn.commit()
            self.fetchmain()
            conn.close()
            messagebox.showinfo("Success","Medicine name updated successfully")

    def deletemain(self):
        if (self.ref_var.get()=="" or self.lot_var.get()==""):
            messagebox.showerror("Error","All fields are required.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="sanjaysavitri12@",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("delete from pharmacy where Refno=%s and lotno=%s",(self.ref_var.get(),self.lot_var.get()))
            conn.commit()
            self.fetchmain()
            conn.close()
            messagebox.showinfo("Success","Medicine Deleted Successfully")   

    def resetmain(self):
        self.med_var.set("")
        self.lot_var.set("")
        self.issue_var.set("")
        self.exp_var.set("")
        self.uses_var.set("")
        self.side_var.set("")
        self.warn_var.set("")
        self.dosage_var.set("")
        self.price_var.set("")
        self.prodqt_var.set("")      

    def searchmain(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="sanjaysavitri12@",database="mydata")
        my_cursor=conn.cursor()
        #.........................Important syntax..................................................
        query=f"select * from pharmacy where {str(self.search_var.get())} like '{str(self.srchtxt_var.get())}%' "
        my_cursor.execute(query)
        rows=my_cursor.fetchall()
        if(len(rows)!=0):
            self.data_table.delete(*self.data_table.get_children())
            for i in rows:
                self.data_table.insert("",END,values=i)
                conn.commit()
        conn.close()    








if __name__=="__main__":
    root= Tk()
    obj= PharmacyManagementSystem(root)
    root.mainloop()