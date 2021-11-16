# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 14:48:45 2021

@author: Riyaz
"""

import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
from criminal import *


mroot=tk.Tk()
mroot.geometry("800x500")
mroot.title("Criminal Database")
mframe=ttk.Frame(mroot,padding="20")
mframe.pack(side=TOP)

mcanvas = Canvas(mroot,width=1000,height=1000)
mcanvas.pack()
mimg = ImageTk.PhotoImage(Image.open("1.jpeg"))
mcanvas.create_image(0,0,anchor=NW,image=mimg)





def CriminalSection():
    global crimg
    root=tk.Toplevel(mroot)
    root.geometry("800x500")
    root.title("Criminal section")
    frame=ttk.Frame(root,padding="20")
    frame.pack(side=TOP)

    canvas = Canvas(root,width=1000,height=1000)
    canvas.pack()
    crimg = ImageTk.PhotoImage(Image.open("2.jpeg"))
    canvas.create_image(0,0,anchor=NW,image=crimg)

    def AddCrRecord():
        global crimg1
        cr=Criminal()
        w1=tk.Toplevel(root)
        w1.geometry("800x550")
        w1.title("Add Record")
    
        canvas1 = Canvas(w1,width=1000,height=1000)
        canvas1.pack(side=TOP)
        crimg1 = ImageTk.PhotoImage(Image.open("3.jpeg"))
        canvas1.create_image(0,0,anchor=NW,image=crimg1)
    
        frame1 = Frame(w1,bg="#A0A0A0",bd=5)
        frame1.place(relx=0.2,relwidth=0.65,relheight=0.7)
        crid=tk.StringVar()
        crn=tk.StringVar()
        crage=tk.StringVar()
        crgndr=tk.StringVar()
        cradrs=tk.StringVar()
        crcellno=tk.StringVar()
        oid=tk.StringVar()
        crstat=tk.StringVar()
        fid=tk.StringVar()
        stat=tk.StringVar()
        ttk.Label(frame1,text="Enter Criminal ID : ").grid(column=3,row=3,pady=10,padx=30)
        ttk.Entry(frame1,width=25,textvariable=crid).grid(column=5,row=3)
        ttk.Label(frame1,text="Enter Criminal name : ").grid(column=3,row=6,pady=10)
        ttk.Entry(frame1,width=25,textvariable=crn).grid(column=5,row=6)
        ttk.Label(frame1,text="Enter age : ").grid(column=3,row=9,pady=10)
        ttk.Entry(frame1,width=25,textvariable=crage).grid(column=5,row=9)
        ttk.Label(frame1,text="Enter Gender : ").grid(column=3,row=12,pady=10)
        ttk.Entry(frame1,width=25,textvariable=crgndr).grid(column=5,row=12)
        ttk.Label(frame1,text="Enter Address : ").grid(column=3,row=15,pady=10)
        ttk.Entry(frame1,width=25,textvariable=cradrs).grid(column=5,row=15)
        ttk.Label(frame1,text="Enter cell no : ").grid(column=3,row=18,pady=10)
        ttk.Entry(frame1,width=25,textvariable=crcellno).grid(column=5,row=18)
        ttk.Label(frame1,text="status : ").grid(column=3,row=21,pady=10) 
        ttk.Entry(frame1,width=25,textvariable=crstat).grid(column=5,row=21)
        ttk.Label(frame1,text="Managing officer ID : ").grid(column=3,row=22,pady=10) 
        ttk.Entry(frame1,width=25,textvariable=oid).grid(column=5,row=22)
        ttk.Label(frame1,text="Registered Fir ID : ").grid(column=3,row=24,pady=10) 
        ttk.Entry(frame1,width=25,textvariable=fid).grid(column=5,row=24)
        ttk.Label(frame1,text="Report : ").grid(column=3,row=26)
        ttk.Entry(frame1,width=35,textvariable=stat,state='readonly').grid(column=5,row=26)
        stat.set(' ')
    
    
        def addCr():
            try:
                cr1=cr.AddCRRecord(crid.get(),crn.get(),crage.get(),crgndr.get(),cradrs.get(), crcellno.get(),crstat.get(), oid.get(),fid.get())
                if cr1=='0':
                    stat.set("Enter the Criminal Id....")
                    btn1["state"]='disabled'
                
                else:
                    stat.set("Added Successfully...")
                    btn1["state"]='disabled'
            except Exception as e:
                    stat.set("Action Unsuccessfull... ")
                    print(e)
            
            
        def AddNewRecord():
            crid.set(" ")
            crn.set(" ")
            crage.set(" ")
            crgndr.set(" ")
            cradrs.set(" ")
            crcellno.set(" ")
            crstat.set(" ")
            oid.set(" ")
            fid.set(" ")
            stat.set(' ')
            btn1["state"]="active"
        
        
        
        def close():
            w1.destroy()
        
        btn1 =ttk.Button(frame1,text="GO",command=addCr)
        btn1.grid(column=3,row=27)
    
        btn2 =ttk.Button(frame1,text="Close",command=close)
        btn2.grid(column=5,row=27)
    
        btn3 =ttk.Button(frame1,text="Add New Record",command=AddNewRecord)
        btn3.grid(column=1,row=27)
    
        for child in frame1.winfo_children():
            child.grid_configure(padx=6,pady=6)



    def UpdCrRecord():
        global crimg2
        cr=Criminal()
        w2=tk.Toplevel(root)
        w2.geometry("800x550")
        w2.title("Update Record")
    
        canvas2 = Canvas(w2,width=1000,height=1000)
        canvas2.pack(side=TOP)
        crimg2 = ImageTk.PhotoImage(Image.open("4.jpeg"))
        canvas2.create_image(0,0,anchor=NW,image=crimg2)
    
        frame2 = Frame(w2,bg="#2E5894",bd=5)
        frame2.place(relx=0.2,rely=0.2,relwidth=0.69,relheight=0.4)
        crid=tk.StringVar()
        crstat=tk.StringVar()
        stat=tk.StringVar()
        ttk.Label(frame2,text="Enter Criminal ID : ").grid(column=3,row=3,pady=10,padx=30)
        ttk.Entry(frame2,width=25,textvariable=crid).grid(column=5,row=3)
        ttk.Label(frame2,text="Enter updated status : ").grid(column=3,row=5,pady=10) 
        ttk.Entry(frame2,width=25,textvariable=crstat).grid(column=5,row=5)
        ttk.Label(frame2,text="Report : ").grid(column=3,row=9)
        ttk.Entry(frame2,width=35,textvariable=stat,state='readonly').grid(column=5,row=9)
        stat.set(' ')
            
    
        def updstat():
            try:
                cr1=cr.UpCRRecord(crid.get(),crstat.get())
                if cr1=='0':
                    stat.set("criminal field not entered")
                
                else:
                    stat.set("Updated Successfully...")
                    btn1["state"]='disabled'
            except Exception as e:
                stat.set("Action Unsuccessfull... ")
                print(e)
        
        def updNewRecord():
            crid.set(" ")
            crstat.set(" ")
            stat.set(' ')
            btn1["state"]="active"
        
        def close():
            w2.destroy()
        
        btn1 =ttk.Button(frame2,text="GO",command=updstat)
        btn1.grid(column=3,row=14)
    
        btn2 =ttk.Button(frame2,text="Close",command=close)
        btn2.grid(column=5,row=14)
    
        btn3 =ttk.Button(frame2,text="Update another record",command=updNewRecord)
        btn3.grid(column=1,row=14)
    
        for child in frame2.winfo_children():
            child.grid_configure(padx=10,pady=10)




    def ViewCrRecord():
        global crimg3
        cr=Criminal()
        w3=tk.Toplevel(root)
        w3.geometry("1000x700")
        w3.title("Criminal Records")
    
        canvas3 = Canvas(w3,width=1000,height=1000)
        canvas3.pack(side=TOP)
        crimg3 = ImageTk.PhotoImage(Image.open("5.jpeg"))
        canvas3.create_image(0,0,anchor=NW,image=crimg3)
    
        frame3 = Frame(w3,bg="#FFBB00",bd=5)
        frame3.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.08)

        Label1 = Label(frame3, text="Criminal Records", bg='black', fg='white', font = ('Courier',15))
        Label1.place(relx=0,rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(w3,bg='black')
        labelFrame.place(relx=0.05,rely=0.12,relwidth=0.9,relheight=0.8)
        y = 0.25

        Label(labelFrame, text="{:<10}{:^40}{:^12}{:^20}{:^40}{:^20}{:^20}{:^20}{:^10}".format('ID','NAME','AGE','GENDER','ADDRESS','STATUS','CELL_NO','OFFICERID','FIRID'),
              bg='black',fg='white').place(relx=0.07,rely=0.1)
        Label(labelFrame, text = "------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    
        try:
            rows=cr.ViewCRRecord()
            for i in rows:
                Label(labelFrame,text="{:<10}{:^40}{:^12}{:^20}{:^40}{:^20}{:^20}{:^20}{:^10}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]) ,bg='black', fg='white').place(relx=0.08,rely=y)
                y += 0.05
        except:
            messagebox.showinfo("Failed to fetch files from database")
    
        quitBtn = Button(w3,text="Quit",bg='#f7f1e3', fg='black', command=w3.destroy)
        quitBtn.place(relx=0.4,rely=0.93, relwidth=0.18,relheight=0.06)


    
    


    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="CRIMINAL SECTION", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Criminal Record",bg='black', fg='white',command=AddCrRecord)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Update Criminal Status",bg='black', fg='white',command=UpdCrRecord)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="View All Records",bg='black', fg='white',command=ViewCrRecord)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    


def OfficerSection():
    global oimg
    root=tk.Toplevel(mroot)
    root.geometry("800x500")
    root.title("Officer section")
    frame=ttk.Frame(root,padding="20")
    frame.pack(side=TOP)

    canvas = Canvas(root,width=1000,height=1000)
    canvas.pack()
    oimg = ImageTk.PhotoImage(Image.open("6.jpeg"))
    canvas.create_image(0,0,anchor=NW,image=oimg)

    def AddOfRecord():
        global oimg1
        of=Officer()
        w1=tk.Toplevel(root)
        w1.geometry("800x550")
        w1.title("Add Record")
    
        canvas1 = Canvas(w1,width=1000,height=1000)
        canvas1.pack(side=TOP)
        oimg1 = ImageTk.PhotoImage(Image.open("7.jpeg"))
        canvas1.create_image(0,0,anchor=NW,image=oimg1)
    
        frame1 = Frame(w1,bg="#A0A0A0",bd=5)
        frame1.place(relx=0.2,relwidth=0.65,relheight=0.7)
        oid=tk.StringVar()
        on=tk.StringVar()
        ocon=tk.StringVar()
        omail=tk.StringVar()
        ps=tk.StringVar()
        stat=tk.StringVar()
        ttk.Label(frame1,text="Enter Officer ID : ").grid(column=3,row=3,pady=10,padx=30)
        ttk.Entry(frame1,width=25,textvariable=oid).grid(column=5,row=3)
        ttk.Label(frame1,text="Enter Officer name : ").grid(column=3,row=6,pady=10)
        ttk.Entry(frame1,width=25,textvariable=on).grid(column=5,row=6)
        ttk.Label(frame1,text="Enter contact number : ").grid(column=3,row=9,pady=10)
        ttk.Entry(frame1,width=25,textvariable=ocon).grid(column=5,row=9)
        ttk.Label(frame1,text="Enter officer's email' : ").grid(column=3,row=12,pady=10)
        ttk.Entry(frame1,width=25,textvariable=omail).grid(column=5,row=12)
        ttk.Label(frame1,text="Enter Police Station name : ").grid(column=3,row=15,pady=10)
        ttk.Entry(frame1,width=25,textvariable=ps).grid(column=5,row=15)
        ttk.Label(frame1,text="Report : ").grid(column=3,row=18)
        ttk.Entry(frame1,width=35,textvariable=stat,state='readonly').grid(column=5,row=18)
        stat.set(' ')
    
    
        def addOf():
            try:
                of1=of.AddOFRecord(oid.get(),on.get(),ocon.get(),omail.get(),ps.get())
                if of1=='0':
                    stat.set("Enter Officer Id....")
                    btn1["state"]='disabled'
                
                else:
                    stat.set("Added Successfully...")
                    btn1["state"]='disabled'
            except Exception as e:
                    stat.set("Action Unsuccessfull... ")
                    print(e)
            
            
        def AddNewRecord():
            oid.set(" ")
            on.set(" ")
            ocon.set(" ")
            omail.set(" ")
            ps.set(" ")
            stat.set(' ')
            btn1["state"]="active"
        
        
        
        def close():
            w1.destroy()
        
        btn1 =ttk.Button(frame1,text="GO",command=addOf)
        btn1.grid(column=3,row=27)
    
        btn2 =ttk.Button(frame1,text="Close",command=close)
        btn2.grid(column=5,row=27)
    
        btn3 =ttk.Button(frame1,text="Add New Record",command=AddNewRecord)
        btn3.grid(column=1,row=27)
    
        for child in frame1.winfo_children():
            child.grid_configure(padx=6,pady=6)



    def UpdOfRecord():
        global oimg2
        of=Officer()
        w2=tk.Toplevel(root)
        w2.geometry("800x500")
        w2.title("Update Record")
    
        canvas2 = Canvas(w2,width=1000,height=1000)
        canvas2.pack(side=TOP)
        oimg2 = ImageTk.PhotoImage(Image.open("8.jpeg"))
        canvas2.create_image(0,0,anchor=NW,image=oimg2)
    
        frame2 = Frame(w2,bg="silver",bd=5)
        frame2.place(relx=0.2,rely=0.2,relwidth=0.69,relheight=0.4)
        oid=tk.StringVar()
        ps=tk.StringVar()
        stat=tk.StringVar()
        ttk.Label(frame2,text="Enter Officer ID : ").grid(column=3,row=3,pady=10,padx=30)
        ttk.Entry(frame2,width=25,textvariable=oid).grid(column=5,row=3)
        ttk.Label(frame2,text="Enter new Police Station name: ").grid(column=3,row=5,pady=10) 
        ttk.Entry(frame2,width=25,textvariable=ps).grid(column=5,row=5)
        ttk.Label(frame2,text="Report : ").grid(column=3,row=9)
        ttk.Entry(frame2,width=35,textvariable=stat,state='readonly').grid(column=5,row=9)
        stat.set(' ')
            
    
        def updps():
            try:
                of1=of.UpOFRecord(oid.get(),ps.get())
                if of1=='0':
                    stat.set("Officer Id field not entered")
                
                else:
                    stat.set("Updated Successfully...")
                    btn1["state"]='disabled'
            except Exception as e:
                stat.set("Action Unsuccessfull... ")
                print(e)
        
        def updNewRecord():
            oid.set(" ")
            crstat.set(" ")
            stat.set(' ')
            btn1["state"]="active"
        
        def close():
            w2.destroy()
        
        btn1 =ttk.Button(frame2,text="GO",command=updps)
        btn1.grid(column=3,row=14)
    
        btn2 =ttk.Button(frame2,text="Close",command=close)
        btn2.grid(column=5,row=14)
    
        btn3 =ttk.Button(frame2,text="Update record",command=updNewRecord)
        btn3.grid(column=1,row=14)
    
        for child in frame2.winfo_children():
            child.grid_configure(padx=10,pady=10)




    def ViewOfRecord():
        global oimg3
        of=Officer()
        w3=tk.Toplevel(root)
        w3.geometry("900x650")
        w3.title("Officer Records")
    
        canvas3 = Canvas(w3,width=1000,height=1000)
        canvas3.pack(side=TOP)
        oimg3 = ImageTk.PhotoImage(Image.open("9.jpeg"))
        canvas3.create_image(0,0,anchor=NW,image=oimg3)
    
        frame3 = Frame(w3,bg="#FFBB00",bd=5)
        frame3.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.08)

        Label1 = Label(frame3, text="Officer Records", bg='black', fg='white', font = ('Courier',15))
        Label1.place(relx=0,rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(w3,bg='black')
        labelFrame.place(relx=0.05,rely=0.12,relwidth=0.9,relheight=0.75)
        y = 0.25

        Label(labelFrame, text="{:<10}{:^40}{:^20}{:^40}{:^40}".format('ID','NAME','CONTACT','EMAIL','POLICE STATION'),
              bg='black',fg='white').place(relx=0.07,rely=0.1)
        Label(labelFrame, text = "-------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    
        try:
            rows=of.ViewOFRecord()
            for i in rows:
                Label(labelFrame,text="{:<10}{:^40}{:^20}{:^40}{:^40}".format(i[0],i[1],i[2],i[3],i[4]) ,bg='black', fg='white').place(relx=0.07,rely=y)
                y += 0.05
        except:
            messagebox.showinfo("Failed to fetch files from database")
    
        quitBtn = Button(w3,text="Quit",bg='#f7f1e3', fg='black', command=w3.destroy)
        quitBtn.place(relx=0.4,rely=0.887, relwidth=0.18,relheight=0.06)


    def DelOfRecord():
        global oimg4
        of=Officer()
        w4=tk.Toplevel(root)
        w4.geometry("800x500")
        w4.title("Delete Record")
    
        canvas2 = Canvas(w4,width=1000,height=1000)
        canvas2.pack(side=TOP)
        oimg4 = ImageTk.PhotoImage(Image.open("8.jpeg"))
        canvas2.create_image(0,0,anchor=NW,image=oimg4)
    
        frame2 = Frame(w4,bg="silver",bd=5)
        frame2.place(relx=0.2,rely=0.2,relwidth=0.69,relheight=0.4)
        oid=tk.StringVar()
        stat=tk.StringVar()
        ttk.Label(frame2,text="Enter Officer ID : ").grid(column=3,row=3,pady=10,padx=30)
        ttk.Entry(frame2,width=25,textvariable=oid).grid(column=5,row=3)
        ttk.Label(frame2,text="Report : ").grid(column=3,row=6)
        ttk.Entry(frame2,width=35,textvariable=stat,state='readonly').grid(column=5,row=6)
        stat.set(' ')
            
    
        def delOf():
            try:
                of1=of.DelOFRecord(oid.get())
                if of1=='0':
                    stat.set("Officer Id field not entered")
                
                else:
                    stat.set("Deleted Successfully...")
                    btn1["state"]='disabled'
            except Exception as e:
                stat.set("Action Unsuccessfull... ")
                print(e)
        
        def DelAnoRecord():
            oid.set(" ")
            stat.set(' ')
            btn1["state"]="active"
        
        def close():
            w4.destroy()
        
        btn1 =ttk.Button(frame2,text="GO",command=delOf)
        btn1.grid(column=3,row=14)
    
        btn2 =ttk.Button(frame2,text="Close",command=close)
        btn2.grid(column=5,row=14)
    
        btn3 =ttk.Button(frame2,text="Delete record",command=DelAnoRecord)
        btn3.grid(column=1,row=14)
    
        for child in frame2.winfo_children():
            child.grid_configure(padx=10,pady=10)



    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="OFFICER SECTION", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Officer Record",bg='black', fg='white',command=AddOfRecord)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Update Officer's Station",bg='black', fg='white',command=UpdOfRecord)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="View All Records",bg='black', fg='white',command=ViewOfRecord)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(root,text="Delete Officer Record",bg='black', fg='white',command=DelOfRecord)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)


def CrimeSection():
    global cimg
    window=tk.Toplevel(mroot)
    window.geometry("900x600")
    window.title("Crime")
    frame=ttk.Frame(window,padding="10")
    frame.pack()
    
    canvas = Canvas(window,width=1000,height=1000)
    canvas.pack()
    cimg = ImageTk.PhotoImage(Image.open("10.jpeg"))
    canvas.create_image(0,0,anchor=NW,image=cimg)
    
    def AddCrRecord():
        global cimg1
        cr=Crime()
        w1=tk.Toplevel(window)
        w1.geometry("800x550")
        w1.title("Add Record")
    
        canvas1 = Canvas(w1,width=1000,height=1000)
        canvas1.pack(side=TOP)
        cimg1 = ImageTk.PhotoImage(Image.open("11.jpeg"))
        canvas1.create_image(0,0,anchor=NW,image=cimg1)
  
        frame1 = Frame(w1,bg='LightSteelBlue',bd=5)
        frame1.place(relx=0.2,relwidth=0.65,relheight=0.7)
        cid=tk.StringVar()
        ctype=tk.StringVar()
        cdesc=tk.StringVar()
        stat=tk.StringVar()
        ttk.Label(frame1,text="Enter Crime ID : ").grid(column=3,row=3,pady=10,padx=30)
        ttk.Entry(frame1,width=25,textvariable=cid).grid(column=5,row=3)
        ttk.Label(frame1,text="Enter Crime type : ").grid(column=3,row=6,pady=10)
        ttk.Entry(frame1,width=25,textvariable=ctype).grid(column=5,row=6)
        ttk.Label(frame1,text="Enter Crime Description : ").grid(column=3,row=9,pady=10)
        ttk.Entry(frame1,width=25,textvariable=cdesc).grid(column=5,row=9)
        ttk.Label(frame1,text="Report : ").grid(column=3,row=24)
        ttk.Entry(frame1,width=35,textvariable=stat,state='readonly').grid(column=5,row=24)
        stat.set(' ')
    
    
        def addCr():
            try:
                cr1=cr.AddCRRecord(cid.get(),ctype.get(),cdesc.get())
                if cr1=='0':
                    stat.set("Crime id already exists....")
                    btn1["state"]='disabled'
                
                else:
                    stat.set("Added Successfully...")
                    btn1["state"]='disabled'
            except Exception as e:
                stat.set("Action Unsuccessfull... ")
                print(e)
            
            
        def AddNewRecord():
            cid.set(" ")
            ctype.set(" ")
            cdesc.set(" ")
            stat.set(' ')
            btn1["state"]="active"
        
        
        
        def close():
            w1.destroy()
        
        btn1 =ttk.Button(frame1,text="GO",command=addCr)
        btn1.grid(column=3,row=27)
    
        btn2 =ttk.Button(frame1,text="Close",command=close)
        btn2.grid(column=5,row=27)
    
        btn3 =ttk.Button(frame1,text="Add New Record",command=AddNewRecord)
        btn3.grid(column=1,row=27)
    
        for child in frame1.winfo_children():
            child.grid_configure(padx=6,pady=6)


        

    def ViewCRecord():
        global cimg2
        cr=Crime()
        w3=tk.Toplevel(window)
        w3.geometry("900x550")
        w3.title("Crime Records")
    
        canvas3 = Canvas(w3,width=1000,height=1000)
        canvas3.pack(side=TOP)
        cimg2 = ImageTk.PhotoImage(Image.open("9.jpeg"))
        canvas3.create_image(0,0,anchor=NW,image=cimg2)
    
        frame3 = Frame(w3,bg="#FFBB00",bd=5)
        frame3.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.08)

        Label1 = Label(frame3, text="Crime Records", bg='black', fg='white', font = ('Courier',15))
        Label1.place(relx=0,rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(w3,bg='black')
        labelFrame.place(relx=0.05,rely=0.12,relwidth=0.9,relheight=0.75)
        y = 0.25

        Label(labelFrame, text="{:<10}{:<40}{:^60}".format('ID','NAME','DESCRIPTION'),bg='black',fg='white').place(relx=0.07,rely=0.1)
        Label(labelFrame, text = "-------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    
        try:
            rows=cr.Show()
            for i in rows:
                Label(labelFrame,text="{:<10}{:<40}{:^60}".format(i[0],i[1],i[2]) ,bg='black', fg='white').place(relx=0.07,rely=y)
                y += 0.05
        except:
            messagebox.showinfo("Failed to fetch files from database")
    
        quitBtn = Button(w3,text="Quit",bg='#f7f1e3', fg='black', command=w3.destroy)
        quitBtn.place(relx=0.4,rely=0.89, relwidth=0.18,relheight=0.06)

    def close():
        window.destroy() 
    
    headingFrame1 = Frame(window,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.1)
    headingLabel = Label(headingFrame1, text="CRIME SECTION", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    b1=Button(window,text="View All",bg='black', fg='white',width=12,command=ViewCRecord)
    b1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

    b2=Button(window,text="Add Entry",bg='black', fg='white',width=12,command=AddCrRecord)
    b2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

    b3=Button(window,text="Close",bg='black', fg='white',width=12,command=close)
    b3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)


    
def charge_sheet():
    global csimg
    root=tk.Toplevel(mroot)
    root.geometry("800x500")
    root.title("Charge Sheet")
    frame=ttk.Frame(root,padding="20")
    frame.pack(side=TOP)

    canvas = Canvas(root,width=1000,height=1000)
    canvas.pack()
    csimg = ImageTk.PhotoImage(Image.open("12.jpeg"))
    canvas.create_image(0,0,anchor=NW,image=csimg)

    def AddCsRecord():
        global csimg1
        cs=ChargeSheet()
        w1=tk.Toplevel(root)
        w1.geometry("800x550")
        w1.title("Add Record")
    
        canvas1 = Canvas(w1,width=1000,height=1000)
        canvas1.pack(side=TOP)
        csimg1 = ImageTk.PhotoImage(Image.open("13.jpeg"))
        canvas1.create_image(0,0,anchor=NW,image=csimg1)
    
        frame1 = Frame(w1,bg="#A0A0A0",bd=5)
        frame1.place(relx=0.2,relwidth=0.65,relheight=0.7)
        csid=tk.StringVar()
        csDate=tk.StringVar()
        csType=tk.StringVar()
        csDesc=tk.StringVar()
        punishment=tk.StringVar()
        crimTime=tk.StringVar()
        crimDate=tk.StringVar()
        crimLoc=tk.StringVar()
        oid=tk.StringVar()
        cid=tk.StringVar()
        stat=tk.StringVar()
        ttk.Label(frame1,text="Enter Charge Sheet ID : ").grid(column=3,row=3,pady=10,padx=30)
        ttk.Entry(frame1,width=25,textvariable=csid).grid(column=5,row=3)
        ttk.Label(frame1,text="Enter Charge Sheet date : ").grid(column=3,row=6,pady=10)
        ttk.Entry(frame1,width=25,textvariable=csDate).grid(column=5,row=6)
        ttk.Label(frame1,text="Enter Charge Sheet type: ").grid(column=3,row=9,pady=10)
        ttk.Entry(frame1,width=25,textvariable=csType).grid(column=5,row=9)
        ttk.Label(frame1,text="Enter Charge Sheet Desc: ").grid(column=3,row=12,pady=10)
        ttk.Entry(frame1,width=25,textvariable=csDesc).grid(column=5,row=12)
        ttk.Label(frame1,text="Enter Punishment: ").grid(column=3,row=15,pady=10)
        ttk.Entry(frame1,width=25,textvariable=punishment).grid(column=5,row=15)
        ttk.Label(frame1,text="Enter Crime Time: ").grid(column=3,row=18,pady=10)
        ttk.Entry(frame1,width=25,textvariable=crimTime).grid(column=5,row=18)
        ttk.Label(frame1,text="Crime date : ").grid(column=3,row=21,pady=10) 
        ttk.Entry(frame1,width=25,textvariable=crimDate).grid(column=5,row=21)
        ttk.Label(frame1,text="Crime Location : ").grid(column=3,row=21,pady=10) 
        ttk.Entry(frame1,width=25,textvariable=crimLoc).grid(column=5,row=21)
        ttk.Label(frame1,text="Managing officer ID : ").grid(column=3,row=22,pady=10) 
        ttk.Entry(frame1,width=25,textvariable=oid).grid(column=5,row=22)
        ttk.Label(frame1,text="Crime ID : ").grid(column=3,row=24)
        ttk.Entry(frame1,width=35,textvariable=cid).grid(column=5,row=24)
        ttk.Label(frame1,text="Report : ").grid(column=3,row=26)
        ttk.Entry(frame1,width=35,textvariable=stat,state='readonly').grid(column=5,row=26)
        stat.set(' ')
    
    
        def addCs():
            try:
                cs1=cs.AddCSRecord(csid.get(),csDate.get(),csType.get(),csDesc.get(),punishment.get(), crimTime.get(),crimDate.get(), crimLoc.get(), oid.get(), cid.get())
                if cs1=='0':
                    stat.set("Enter the Chargesheet Id....")
                    btn1["state"]='disabled'
                
                else:
                    stat.set("Added Successfully...")
                    btn1["state"]='disabled'
            except Exception as e:
                    stat.set("Action Unsuccessfull... ")
                    print(e)
            
            
        def AddNewRecord():
            csid.set(" ")
            csDate.set(" ")
            csType.set(" ")
            csDesc.set(" ")
            punishment.set(" ")
            crimTime.set(" ")
            crimDate.set(" ")
            crimLoc.set(" ")
            oid.set(" ")
            cid.set(" ")
            stat.set(' ')
            btn1["state"]="active"
        
        
        
        def close():
            w1.destroy()
        
        btn1 =ttk.Button(frame1,text="GO",command=addCs)
        btn1.grid(column=3,row=27)
    
        btn2 =ttk.Button(frame1,text="Close",command=close)
        btn2.grid(column=5,row=27)
    
        btn3 =ttk.Button(frame1,text="Add New Record",command=AddNewRecord)
        btn3.grid(column=1,row=27)
    
        for child in frame1.winfo_children():
            child.grid_configure(padx=6,pady=6)



    def UpdCSRecord():
        global csimg2
        cs=ChargeSheet()
        w2=tk.Toplevel(root)
        w2.geometry("800x550")
        w2.title("Update Record")
    
        canvas2 = Canvas(w2,width=1000,height=1000)
        canvas2.pack(side=TOP)
        csimg2 = ImageTk.PhotoImage(Image.open("14.jpeg"))
        canvas2.create_image(0,0,anchor=NW,image=csimg2)
    
        frame2 = Frame(w2,bg="#2E5894",bd=5)
        frame2.place(relx=0.2,rely=0.2,relwidth=0.69,relheight=0.4)
        csid=tk.StringVar()
        csType=tk.StringVar()
        stat=tk.StringVar()
        ttk.Label(frame2,text="Enter charge_sheet ID : ").grid(column=3,row=3,pady=10,padx=30)
        ttk.Entry(frame2,width=25,textvariable=csid).grid(column=5,row=3)
        ttk.Label(frame2,text="Enter updated Type : ").grid(column=3,row=5,pady=10) 
        ttk.Entry(frame2,width=25,textvariable=csType).grid(column=5,row=5)
        ttk.Label(frame2,text="Report : ").grid(column=3,row=9)
        ttk.Entry(frame2,width=35,textvariable=stat,state='readonly').grid(column=5,row=9)
        stat.set(' ')
            
    
        def updstat():
            try:
                cs1=cs.UpCSRecord(csid.get(),csType.get())
                if cs1=='0':
                    stat.set("charge sheet id not entered")
                
                else:
                    stat.set("Updated Successfully...")
                    btn1["state"]='disabled'
            except Exception as e:
                stat.set("Action Unsuccessfull... ")
                print(e)
        
        def updNewRecord():
            csid.set(" ")
            csType.set(" ")
            stat.set(' ')
            btn1["state"]="active"
        
        def close():
            w2.destroy()
        
        btn1 =ttk.Button(frame2,text="GO",command=updstat)
        btn1.grid(column=3,row=14)
    
        btn2 =ttk.Button(frame2,text="Close",command=close)
        btn2.grid(column=5,row=14)
    
        btn3 =ttk.Button(frame2,text="Update another record",command=updNewRecord)
        btn3.grid(column=1,row=14)
    
        for child in frame2.winfo_children():
            child.grid_configure(padx=10,pady=10)


    def ViewCSRecord():
        global csimg3
        cs=ChargeSheet()
        w3=tk.Toplevel(root)
        w3.geometry("1200x550")
        w3.title("Charge sheet Records")
    
        canvas3 = Canvas(w3,width=1200,height=1000)
        canvas3.pack(side=TOP)
        csimg3 = ImageTk.PhotoImage(Image.open("15.jpeg"))
        canvas3.create_image(0,0,anchor=NW,image=csimg3)
    
        frame3 = Frame(w3,bg="#FFBB00",bd=5)
        frame3.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.08)

        Label1 = Label(frame3, text="charge sheet record", bg='black', fg='white', font = ('Courier',15))
        Label1.place(relx=0,rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(w3,bg='black')
        labelFrame.place(relx=0.03,rely=0.12,relwidth=0.93,relheight=0.8)
        y = 0.25

        Label(labelFrame, text="{:<10}{:^20}{:^30}{:^45}{:^45}{:^50}{:^10}{:^20}{:^20}{:^20}".format('ID','CsDate','CsType','CsDesc','Punishment','Crime_Time','Crime_Date','Crime_Loc','OID','CID'),
              bg='black',fg='white').place(relx=0.07,rely=0.1)
        Label(labelFrame, text = "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    
        try:
            rows=cs.ViewCsRecord()
            for i in rows:
                Label(labelFrame,text="{:<10}{:^20}{:^30}{:^45}{:^45}{:^20}{:^20}{:^20}{:^20}{:^20}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]) ,bg='black', fg='white').place(relx=0.07,rely=y)
                y += 0.05
        except:
            messagebox.showinfo("Failed to fetch files from database")
    
        quitBtn = Button(w3,text="Quit",bg='#f7f1e3', fg='black', command=w3.destroy)
        quitBtn.place(relx=0.4,rely=0.93, relwidth=0.18,relheight=0.05)

    def HasArecord():
        window=tk.Toplevel(root)
        window.geometry("900x600")
        window.title("Records of criminal and charge sheet")
        h=HasARecord()
        frame=ttk.Frame(window,padding="10")
        frame.pack()
        window.configure(background='LightSteelBlue')
        
        wrapper3=LabelFrame(window,text="Insert new record")
        wrapper3.pack(fill="both",expand="yes",padx=10,pady=10)

        ll1=tk.Label(wrapper3,text="Enter Criminal Id")
        ll1.grid(row=2,column=0)
        text1=StringVar()
        ee1=Entry(wrapper3,textvariable=text1)
        ee1.grid(row=2,column=1)
        ll2=tk.Label(wrapper3,text="Enter Charge sheet Id")
        ll2.grid(row=3,column=0)
        text2=StringVar()
        ee2=Entry(wrapper3,textvariable=text2)
        ee2.grid(row=3,column=1)
        
        
        def Add():
            crid=text1.get()
            csid=text2.get()
            h.AddRecord(crid, csid)

                
        frame3 = Frame(window,bg="#FFBB00",bd=5)
        frame3.place(relx=0.25,rely=0.15,relwidth=0.5,relheight=0.08)

        Label1 = Label(frame3, text="charge sheet record", bg='black', fg='white', font = ('Courier',15))
        Label1.place(relx=0,rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(window,bg='black')
        labelFrame.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.7)
        y = 0.25

        Label(labelFrame, text="%-40s%-40s"%('Criminal_ID','CS_iD'),
              bg='black',fg='white').place(relx=0.07,rely=0.1)
        Label(labelFrame, text = "-------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    
        try:
            rows=h.Show()
            for i in rows:
                Label(labelFrame,text="%-40s%-40s"%(i[0],i[1]) ,bg='black', fg='white').place(relx=0.07,rely=y)
                y += 0.05
        except:
            messagebox.showinfo("Failed to fetch files from database")
    
                
        def close():
            window.destroy() 
        
        add_bt=Button(wrapper3,text="Insert",command=Add)
        add_bt.grid(row=2,column=3)
        bt=Button(wrapper3,text="Close",command=close)
        bt.grid(row=2,column=4)

    

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="CHARGE SHEET", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Charge Sheet",bg='black', fg='white',command=AddCsRecord)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Update Charge Sheet",bg='black', fg='white',command=UpdCSRecord)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="View All Records",bg='black', fg='white',command=ViewCSRecord)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="Make criminal entry",bg='black', fg='white',command=HasArecord)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)



def firSection():
    global fimg
    root=tk.Toplevel(mroot)
    root.geometry("800x500")
    root.title("fir section")
    frame=ttk.Frame(root,padding="20")
    frame.pack(side=TOP)

    canvas = Canvas(root,width=1000,height=1000)
    canvas.pack()
    fimg = ImageTk.PhotoImage(Image.open("19.jpeg"))
    canvas.create_image(0,0,anchor=NW,image=fimg)
    
    def AddfiRecord():
        global fimg1
        fi=FIR()
        w1=tk.Toplevel(root)
        w1.geometry("800x550")
        w1.title("Add Record")
        
        canvas1 = Canvas(w1,width=1000,height=1000)
        canvas1.pack(side=TOP)
        fimg1 = ImageTk.PhotoImage(Image.open("17.jpeg"))
        canvas1.create_image(0,0,anchor=NW,image=fimg1)
        
        frame1 = Frame(w1,bg="#A0A0A0",bd=5)
        frame1.place(relx=0.2,relwidth=0.65,relheight=0.7)
        fid=tk.StringVar()
        fin=tk.StringVar() 
        fit=tk.StringVar()
        fidate=tk.StringVar()
        fidesc=tk.StringVar() 
        cid=tk.StringVar()
        oid=tk.StringVar()
        crid=tk.StringVar()
        stat=tk.StringVar()
        ttk.Label(frame1,text="Enter fir ID : ").grid(column=3,row=3,pady=10,padx=30)
        ttk.Entry(frame1,width=25,textvariable=fid).grid(column=5,row=3)
        ttk.Label(frame1,text="Enter fir name : ").grid(column=3,row=6,pady=10)
        ttk.Entry(frame1,width=25,textvariable=fin).grid(column=5,row=6)
        ttk.Label(frame1,text="Enter fir type : ").grid(column=3,row=9,pady=10)
        ttk.Entry(frame1,width=25,textvariable=fit).grid(column=5,row=9)
        ttk.Label(frame1,text="Enter fir date : ").grid(column=3,row=11,pady=10)
        ttk.Entry(frame1,width=25,textvariable=fidate).grid(column=5,row=11)
        ttk.Label(frame1,text="Enter fir description : ").grid(column=3,row=12,pady=10)
        ttk.Entry(frame1,width=25,textvariable=fidesc).grid(column=5,row=12)
        ttk.Label(frame1,text="Enter crime ID : ").grid(column=3,row=15,pady=10)
        ttk.Entry(frame1,width=25,textvariable=cid).grid(column=5,row=15)
        ttk.Label(frame1,text="Managing officer ID :  ").grid(column=3,row=18,pady=10)
        ttk.Entry(frame1,width=25,textvariable=oid).grid(column=5,row=18)
        ttk.Label(frame1,text="Report : ").grid(column=3,row=21)
        ttk.Entry(frame1,width=35,textvariable=stat,state='readonly').grid(column=5,row=21)
        stat.set(' ')
        
        def addfi():
            try:
                fi1=fi.AddFIRecord(fid.get(),fin.get(),fit.get(),fidate.get(),fidesc.get(), cid.get(),oid.get())
                if fi1=='0':
                    stat.set("fir id not entered....")
                    btn1["state"]='disabled'
                
                else:
                    stat.set("Added Successfully...")
                    btn1["state"]='disabled'
            except Exception as e:
                    stat.set("Action Unsuccessfull... ")
                    print(e)
        
        def AddNewRecord():
            fid.set(" ")
            fin.set(" ")
            fit.set(" ")
            fidate.set(" ")
            fidesc.set(" ")
            cid.set(" ")
            oid.set(" ")
            crid.set(" ")
            btn1["state"]="active"
            
        def close():
            w1.destroy()
        
        btn1 =ttk.Button(frame1,text="GO",command=addfi)
        btn1.grid(column=3,row=27)
    
        btn2 =ttk.Button(frame1,text="Close",command=close)
        btn2.grid(column=5,row=27)
    
        btn3 =ttk.Button(frame1,text="Add New Record",command=AddNewRecord)
        btn3.grid(column=1,row=27)
    
        for child in frame1.winfo_children():
            child.grid_configure(padx=6,pady=6)
            
    def ViewFIRecord():
        global fimg2
        fi=FIR()
        w2=tk.Toplevel(root)
        w2.geometry("1000x550")
        w2.title("fir Records")
    
        canvas2 = Canvas(w2,width=1000,height=1000)
        canvas2.pack(side=TOP)
        fimg2 = ImageTk.PhotoImage(Image.open("18.jpeg"))
        canvas2.create_image(0,0,anchor=NW,image=fimg2)
        
        frame2 = Frame(w2,bg="#FFBB00",bd=5)
        frame2.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.08)

        Label1 = Label(frame2, text="fir Records", bg='black', fg='white', font = ('Courier',15))
        Label1.place(relx=0,rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(w2,bg='black')
        labelFrame.place(relx=0.05,rely=0.12,relwidth=0.9,relheight=0.8)
        y = 0.25
        
        Label(labelFrame, text="{:<10}{:^30}{:^20}{:^30}{:^60}{:^65}{:^10}".format('ID','NAME','TYPE','DATE','DESC','CID','OID'),
              bg='black',fg='white').place(relx=0.07,rely=0.1)
        Label(labelFrame, text = "-------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    
        try:
            rows=fi.ViewFIRecord()
            for i in rows:
                Label(labelFrame,text="{:<10}{:^30}{:^20}{:^30}{:^60}{:^20}{:^20}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]) ,bg='black', fg='white').place(relx=0.07,rely=y)
                y += 0.05
        except:
            messagebox.showinfo("Failed to fetch files from database")
    
        quitBtn = Button(w2,text="Quit",bg='#f7f1e3', fg='black', command=w2.destroy)
        quitBtn.place(relx=0.4,rely=0.93, relwidth=0.18,relheight=0.05)
    
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="FIR SECTION", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    btn1 = Button(root,text="Add fir Record",bg='black', fg='white',command=AddfiRecord)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="View All Records",bg='black', fg='white',command=ViewFIRecord)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)



    

mheadingFrame1 = Frame(mroot,bg="#FFBB00",bd=5)
mheadingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
mheadingLabel = Label(mheadingFrame1, text="CRIMINAL DATABASE", bg='black', fg='white', font=('Courier',15))
mheadingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

mbtn1 = Button(mroot,text="CRIMINAL SECTION",bg='black', fg='white',command=CriminalSection)
mbtn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
mbtn2 = Button(mroot,text="CRIME SECTION",bg='black', fg='white',command=CrimeSection)
mbtn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
mbtn3 = Button(mroot,text="OFFICER SECTION",bg='black', fg='white',command=OfficerSection)
mbtn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

mbtn4 = Button(mroot,text="FIR SECTION",bg='black', fg='white',command=firSection)
mbtn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
mbtn5 = Button(mroot,text="CHARGE SHEET",bg='black', fg='white',command=charge_sheet)
mbtn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)


mroot.mainloop()