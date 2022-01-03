from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox

class POS:
    def __init__(self,root):
        self.root = root
        self.root.title=("Point of Sale")
        self.root.geometry("1350x768+0+0")
        self.root.configure(background='cadetblue')

        Change_input=StringVar()
        Cash_Input=StringVar()
        Tax_Input=StringVar()
        SubTotal_Input=StringVar()
        Total_input=StringVar()
        Item=StringVar()
        Qty=StringVar()
        Amount=StringVar()
        Choise=StringVar()


        self.img =PhotoImage(file='buger.png')
        self.img2=PhotoImage(file='butterfly.png')

    #==========================================Functions===========================================================
        def delete(): # delete unwanted items
           ItemCost=0.0
           Tax=2.5
           CashInput=float(Cash_Input.get())
           for child in self.POS_records.get_children():
                 ItemCost += float(self.POS_records.item(child, "values")[2])
                 SubTotal_Input.set(str('Rs.%.2f' % (ItemCost - 2.3)))
                 Tax_Input.set(str('Rs.%.2f' % (((ItemCost - 2.3) * Tax) / 100)))
                 Total_input.set(str('Rs.%.2f' % ((ItemCost - 2.3) + ((ItemCost - 2.3) * Tax) / 100)))
                 selected_item =(self.POS_records.selection()[0])
                 self.POS_records.delete(selected_item)

        def giveChange():
            ItemCost = 0.0
            Tax = 2.5
            CashInput=float(Cash_Input.get())
            for child in self.POS_records.get_children():
                ItemCost += float(self.POS_records.item(child, 'values')[2])
                Change_input.set(str('Rs.%.2f' % (CashInput - ((ItemCost) + ((ItemCost * Tax) / 100)))))
                if(Cash_Input.get()=="0"):
                    Change_Input.set(" ")
                    Method_of_Pay()

        def iExit():
            iExit=tkinter.messagebox.askyesno("Point of sale","Do you want to quit")
            if(iExit>0):
                root.destroy()
                return

        def Method_of_Pay():
            if(choice.get()=="Cash"):
                self.txtCost.focus()
                Cash_Input.set("")
            elif(choice.get()==""):
                Cash_Input.set("0")
                Change_input.set("")


    #==============================================================================================================

        MainFrame=Frame(self.root,bg='cadetblue')
        MainFrame.grid(padx=8,pady=5)

        ButtonFrame=Frame(MainFrame,bg='cadetblue',bd=5,width=1348,height=168,padx=4,pady=4,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bg='cadetblue',bd=5,width=800,height=300,padx=4,pady=4,relief=RIDGE)
        DataFrame.pack(side=LEFT)

       # DataFrame = Frame(MainFrame, bg='cadetblue', bd=5, width=800, height=300, padx=4, pady=4, relief=RIDGE)
       # DataFrame.pack(side=LEFT)


        DataFrameLEFTCOVER=LabelFrame(DataFrame,bg='cadetblue',bd=5,width=800,height=300,padx=4,pady=4,
                                      font=('arial',12,'bold'),text="Point of Sale",relief=RIDGE)
        DataFrameLEFTCOVER.pack(side=LEFT)

        ChangeButtonFrame=Frame(DataFrameLEFTCOVER,bd=5,width=300,height=460,pady=4,relief=RIDGE)
        ChangeButtonFrame.pack(side=LEFT,padx=4)

        ReciptFrame = Frame(DataFrameLEFTCOVER, bd=5, width=200, height=400, pady=5,padx=1, relief=RIDGE)
        ReciptFrame.pack(side=RIGHT, padx=4)

        FoodItemFrame=LabelFrame(DataFrame,bg='cadetblue',bd=5,width=450,height=300,padx=5,pady=2,
                                      font=('arial',12,'bold'),text="Items",relief=RIDGE)
        FoodItemFrame.pack(side=RIGHT)

        CalFrame = Frame(ButtonFrame,  bd=5, width=432, height=140, pady=5,padx=1, relief=RIDGE)
        CalFrame.grid(row=0,column=0,padx=5)

        ChangeFrame = Frame(ButtonFrame, bd=5, width=500, height=140, pady=2, relief=RIDGE)
        ChangeFrame.grid(row=0,column=1,padx=5)

        RemoveFrame = Frame(ButtonFrame, bd=5, width=400, height=140, pady=4, relief=RIDGE)
        RemoveFrame.grid(row=0,column=2,padx=5)

#===============================================Entry and Lable widgedts===========================================================================
        self.lblsubTotal=Label(CalFrame,font=('arial',14,'bold'),text="Sub Total",bd=5)
        self.lblsubTotal.grid(row=0,column=0,sticky=W,padx=5)
        self.txtsubTotal=Entry(CalFrame,font=('arial',14,'bold'),textvariable=SubTotal_Input,bd=2,width=24)
        self.txtsubTotal.grid(row=0,column=1,sticky=W,padx=5)

        self.lblTax=Label(CalFrame,font=('arial',14,'bold'),text="Tax",bd=5)
        self.lblTax.grid(row=1,column=0,sticky=W,padx=5)
        self.txtTax=Entry(CalFrame,font=('arial',14,'bold'),textvariable=Tax_Input,bd=2,width=24)
        self.txtTax.grid(row=1,column=1,sticky=W,padx=5)

        self.lblTotal=Label(CalFrame,font=('arial',14,'bold'),text="Total",bd=5)
        self.lblTotal.grid(row=2,column=0,sticky=W,padx=5)
        self.txtTotal=Entry(CalFrame,font=('arial',14,'bold'),textvariable=Total_input,bd=2,width=24)
        self.txtTotal.grid(row=2,column=1,sticky=W,padx=5)

#===============================================Entry and Lable widgedts===========================================================================
        self.lblMoP=Label(ChangeFrame,font=('arial',14,'bold'),text="Method of Payment",bd=5)
        self.lblMoP.grid(row=0,column=0,sticky=W,padx=5)
        self.cboMoP=ttk.Combobox(ChangeFrame,font=('arial',14,'bold'),width=34,state='readonly'
                                 ,textvariable='choice',justify=RIGHT)
        self.cboMoP['values']=('','Cash','Visa Card','Master Card')
        self.cboMoP.current(0)
        self.cboMoP.grid(row=0,column=1)

        self.lblCost=Label(ChangeFrame,font=('arial',14,'bold'),text="Cash",bd=5)
        self.lblCost.grid(row=1,column=0,sticky=W,padx=5)
        self.txtCost=Entry(ChangeFrame,font=('arial',14,'bold'),textvariable=Cash_Input,bd=2,width=36,justify=RIGHT)
        self.txtCost.grid(row=1,column=1,sticky=W,padx=5)


        self.lblChange=Label(ChangeFrame,font=('arial',14,'bold'),text="Change",bd=5)
        self.lblChange.grid(row=2,column=0,sticky=W,padx=5)
        self.txtChange=Entry(ChangeFrame,font=('arial',14,'bold'),textvariable=Change_input,bd=2,width=36,justify=RIGHT)
        self.txtChange.grid(row=2,column=1,sticky=W,padx=5)

 # ===============================================Button widgedts===========================================================================
        self.btnPay = Button(RemoveFrame,padx=2, font=('arial', 15, 'bold'), text="Pay",width=10,height=1, bd=2,command=giveChange)
        self.btnPay.grid(row=0, column=0, pady=2, padx=7)

        self.btnExit = Button(RemoveFrame,padx=2, font=('arial', 15, 'bold'), text="Exit",width=10,height=1, bd=2,command=iExit)
        self.btnExit.grid(row=0, column=1, pady=2, padx=7)

        self.btnReset = Button(RemoveFrame,padx=2, font=('arial', 15, 'bold'), text="Reset",width=10,height=1, bd=2)
        self.btnReset.grid(row=1, column=0, pady=2, padx=7)

        self.btnRemoveItem = Button(RemoveFrame,padx=2, font=('arial', 15, 'bold'), text="Remove Item",width=10,height=1, bd=2,command=delete)
        self.btnRemoveItem.grid(row=1, column=1, pady=2, padx=7)


# =============================================== Fuction ===========================================================================
        def Coffe():
            ItemCost=2.3
            Tax=2.5
            self.POS_records.insert("",tk.END,values=("Coffe Capp","1","2.3"))
            for child in self.POS_records.get_children():
                ItemCost +=float(self.POS_records.item(child,"values")[2])
                SubTotal_Input.set(str('Rs.%.2f'%(ItemCost-2.3)))
                Tax_Input.set(str('Rs.%.2f' % (((ItemCost - 2.3)*Tax)/100)))
                Total_input.set(str('Rs.%.2f' % ((ItemCost-2.3)+((ItemCost - 2.3) * Tax) / 100)))

        def Coffe2():
            ItemCost=2.3
            Tax=2.5
            self.POS_records.insert("",tk.END,values=("Burger","1","1.9"))
            for child in self.POS_records.get_children():
                ItemCost +=float(self.POS_records.item(child,"values")[2])
                SubTotal_Input.set(str('Rs.%.2f'%(ItemCost-1.9)))
                Tax_Input.set(str('Rs.%.2f' % (((ItemCost - 1.9)*Tax)/100)))
                Total_input.set(str('Rs.%.2f' % ((ItemCost-1.9)+((ItemCost - 1.9) * Tax) / 100)))

        def Coffe3():
            ItemCost=2.3
            Tax=2.5
            self.POS_records.insert("",tk.END,values=("Ice Coffe","1","1.7"))
            for child in self.POS_records.get_children():
                ItemCost +=float(self.POS_records.item(child,"values")[2])
                SubTotal_Input.set(str('Rs.%.2f'%(ItemCost-1.7)))
                Tax_Input.set(str('Rs.%.2f' % (((ItemCost - 1.7)*Tax)/100)))
                Total_input.set(str('Rs.%.2f' % ((ItemCost-1.7)+((ItemCost - 1.7) * Tax) / 100)))


 # ===============================================Tree view  widgedts======================================================
        scroll_x=Scrollbar(ReciptFrame,orient=HORIZONTAL)
        scroll_y = Scrollbar(ReciptFrame, orient=VERTICAL)

        self.POS_records=ttk.Treeview(ReciptFrame,height=20,columns=("Item","Qty","Amount"),
                                      xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.POS_records.heading("Item",text="Item")
        self.POS_records.heading("Qty", text="Qty")
        self.POS_records.heading("Amount", text="Amount")

        self.POS_records['show']='headings'

        self.POS_records.column("Item", width=120)
        self.POS_records.column("Qty", width=100)
        self.POS_records.column("Amount", width=100)

        self.POS_records.pack(fill=BOTH,expand=1)
        self.POS_records.bind("<ButtonRelease-1>")

  # ===============================================Button widgedts==========================================================
        self.btnFedBurger = Button(ChangeButtonFrame, padx=2, width=104, height=104, bd=2,image=self.img,command=Coffe)
        self.btnFedBurger.grid(row=0, column=0, pady=2, padx=4)

        self.btnButterfly = Button(ChangeButtonFrame, padx=2, width=104, height=104, bd=2, image=self.img2)
        self.btnButterfly.grid(row=0, column=1, pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=1, column=0, pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=1, column=1, pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame, padx=2, width=104, height=104, bd=2,image=self.img)
        self.btnFedBurger.grid(row=2, column=0, pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=2, column=1, pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=3, column=0, pady=2, padx=4)

        self.btnFedBurger = Button(ChangeButtonFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=3, column=1, pady=2, padx=4)

 # ===============================================Button widgedts===========================================================================
        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2,image=self.img,command=Coffe)
        self.btnFedBurger.grid(row=0, column=0, pady=2, padx=4)

        self.btnButterfly = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img2,command=Coffe2)
        self.btnButterfly.grid(row=0, column=1, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img,command=Coffe3)
        self.btnFedBurger.grid(row=0, column=2, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=0, column=3, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2,image=self.img)
        self.btnFedBurger.grid(row=0, column=4, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=0, column=5, pady=2, padx=4)

        #=======2
        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2,image=self.img)
        self.btnFedBurger.grid(row=1, column=0, pady=2, padx=4)

        self.btnButterfly = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img2)
        self.btnButterfly.grid(row=1, column=1, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=1, column=2, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=1, column=3, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2,image=self.img)
        self.btnFedBurger.grid(row=1, column=4, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=1, column=5, pady=2, padx=4)

        #==3
        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2,image=self.img)
        self.btnFedBurger.grid(row=2, column=0, pady=2, padx=4)

        self.btnButterfly = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img2)
        self.btnButterfly.grid(row=2, column=1, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=2, column=2, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=2, column=3, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2,image=self.img)
        self.btnFedBurger.grid(row=2, column=4, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=2, column=5, pady=2, padx=4)

        # ==3
        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=3, column=0, pady=2, padx=4)

        self.btnButterfly = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img2)
        self.btnButterfly.grid(row=3, column=1, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=3, column=2, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=3, column=3, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=3, column=4, pady=2, padx=4)

        self.btnFedBurger = Button(FoodItemFrame, padx=2, width=104, height=104, bd=2, image=self.img)
        self.btnFedBurger.grid(row=3, column=5, pady=2, padx=4)


if __name__ =='__main__':
    root =Tk()
    application =POS(root)
    root.mainloop()



