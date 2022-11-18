#~~~~~~~Group Info~~~~~~~~~~
# Adriana Pereira Lima      ID: S337632
# George Ibaite Librando    ID: S345658
# Peichun Huang             ID: S341131




from tkinter import *
from PIL import ImageTk #pip install pillow

from tkinter import filedialog,messagebox

import random
import time



operator= ''
priceofmeal=''
priceofcoffee=''
priceofdrinks=''
subtotalitems=''
date = time.strftime('%d/%m/%Y')
i = random.randint(100, 10000)
billnumber = "BILL" + str(i)






class OrderScreen():
    def __init__(self,root):
    
        self.root = root
        self.root.title('Cafe Order System')
        self.root.config(bg='#3A5FCD')
        self.root.geometry("")
        self.root.resizable(True, True)
        
 ########## Backgroung image on Cafe Order System Screen Window ###########
        self.background=ImageTk.PhotoImage(file="4K-Coffee-Grain-Photo-Download2.png")
        self.background_image=Label(self.root,image=self.background).place(x=0,y=0,relwidth=1,relheight=1)

         #------------------TIME--------------
        localtime=time.asctime(time.localtime(time.time()))
        
        self.topFrame = Frame(self.root,bd=7,relief=RAISED,bg='#7D2509')
        self.topFrame.pack(side=TOP)
        self.labelTitle = Label(self.topFrame, text='Cafe Order System', font=('Britannic Bold',35,'bold'),fg='#7D2509',bd=6,bg='#F6D7B8',width=57)
        self.labelTitle.grid(row=0,column=0)   
        self.labelTitle = Label(self.topFrame, text=localtime,font=('Britannic Bold',12, "underline"),fg='#7D2509', bg='#F6D7B8',width=165)
        self.labelTitle.grid(row=1,column=0) 
        
        
       
   
        ##MenuFrames
        self.menu_frame=Frame(self.root,bd=7,relief=RAISED,bg='#7D2509')
        self.menu_frame.pack(side=LEFT)


        self.cost_frame=Frame(self.menu_frame,bd=3,relief=RAISED,bg='#F6D7B8')
        self.cost_frame.pack(side=BOTTOM)


        self.breakfast_frame=LabelFrame(self.menu_frame,text='BREAKFAST', font=('Britannic Bold', 18, 'bold'),
                                          fg='#7D2509',bd=3,relief=RAISED,bg='#F6D7B8')
        self.breakfast_frame.pack(side=LEFT)






        self.lunch_frame = LabelFrame(self.menu_frame, text='LUNCH', font=('Britannic Bold', 18, 'bold'),
                                          fg='#7D2509', bd=3, relief=RAISED, bg='#F6D7B8')
        self.lunch_frame.pack(side=LEFT)

        self.coffee_frame = LabelFrame(self.menu_frame, text='COFFEE', font=('Britannic Bold', 18, 'bold'),
                                          fg='#7D2509', bd=3, relief=RAISED, bg='#F6D7B8')
        self.coffee_frame.pack(side=LEFT)

        self.drink_frame = LabelFrame(self.menu_frame, text='DRINKS', font=('Britannic Bold', 17, 'bold'),
                                          fg='#7D2509', bd=3, relief=RAISED, bg='#F6D7B8')
        self.drink_frame.pack(side=LEFT)

        self.tea_frame = LabelFrame(self.drink_frame, text='TEA POT', font=('Britannic Bold', 11, 'bold'),
                                          fg='#7D2509', bd=3, relief=RAISED, bg='#F6D7B8')
        self.tea_frame.pack()



        self.juice_frame = LabelFrame(self.drink_frame, text='FRESH JUICES', font=('Britannic Bold', 11, 'bold'),
                                    fg='#7D2509', bd=3, relief=RAISED, bg='#F6D7B8')
        self.juice_frame.pack()




        ##CheckoutFrame

        self.checkout_frame=Frame(self.root,bd=7,relief=RAISED,bg='#7D2509',height=30)
        self.checkout_frame.pack(side=RIGHT)

        ##CalculatorFrame
        self.calculator_frame=Frame(self.checkout_frame,bd=1,relief=RAISED)

        self.calculator_buttonframe = Frame(self.calculator_frame, bd=1, relief=RAISED)
        self.calculator_buttonframe.pack(side=BOTTOM)

        ##ReceiptFrame
        self.receipt_frame = Frame(self.checkout_frame, bd=3, relief=RAISED)
       


        ##ButtonFrame
        self.button_frame = Frame(self.checkout_frame, bd=3, relief=RAISED)
        self.button_frame.grid(row=1,column=0)
       

       




       ###swap receipt frame and calculator frame function
        def swap(self):

            self.tkraise()

        for frame in(self.calculator_frame,self.receipt_frame):
            frame.grid(row=0,column=0)







        ##Variables

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()
        self.var10 = IntVar()
        self.var11 = IntVar()
        self.var12 = IntVar()
        self.var13 = IntVar()
        self.var14 = IntVar()
        self.var15 = IntVar()
        self.var16 = IntVar()
        self.var17 = IntVar()
        self.var18 = IntVar()
        self.var19 = IntVar()
        self.var20 = IntVar()
        self.var21 = IntVar()
        self.var22 = IntVar()
        self.var23 = IntVar()
        self.var24 = IntVar()
        self.var25 = IntVar()
        self.var26 = IntVar()
        self.var27 = IntVar()
        self.var28 = IntVar()
        self.var29 = IntVar()
        self.var30 = IntVar()
        self.var31 = IntVar()
        self.var32 = IntVar()
        self.var33 = IntVar()

        self.var34 = IntVar()
        self.var35 = IntVar()
        self.var36 = IntVar()
        self.var37 = IntVar()
        self.var38 = IntVar()
        self.var39 = IntVar()
        self.var40 = IntVar()
        self.var41 = IntVar()
        self.var42 = IntVar()
        self.var43 = IntVar()
        self.var44 = IntVar()
        self.var45 = IntVar()

        self.entry_saf = IntVar()
        self.entry_ber = IntVar()
        self.entry_eot = IntVar()
        self.entry_mo = IntVar()
        self.entry_eb = IntVar()
        self.entry_bmc = IntVar()
        self.entry_tmc = IntVar()
        self.entry_mn = IntVar()
        self.entry_ets = IntVar()
        self.entry_tt1 = IntVar()
        self.entry_t1 = IntVar()

        self.entry_kebab = IntVar()
        self.entry_calamari = IntVar()
        self.entry_snackbox = IntVar()
        self.entry_bc = IntVar()
        self.entry_clubsandwich = IntVar()
        self.entry_chichkensandwich = IntVar()
        self.entry_salmonsandwich = IntVar()
        self.entry_sg = IntVar()
        self.entry_smg = IntVar()
        self.entry_fc = IntVar()

        self.entry_hd = IntVar()

        self.entry_espresso = IntVar()
        self.entry_flatwhite = IntVar()
        self.entry_cappuccino = IntVar()
        self.entry_longblack = IntVar()
        self.entry_latte = IntVar()
        self.entry_hotchoco = IntVar()
        self.entry_macchiato = IntVar()
        self.entry_piccolo = IntVar()
        self.entry_affogato = IntVar()

        self.entry_mediumsize= IntVar()
        self.entry_largesize = IntVar()

        self.entry_peppermint = IntVar()
        self.entry_earl_grey = IntVar()
        self.entry_engbreak= IntVar()
        self.entry_chamomile = IntVar()
        self.entry_turkishtea = IntVar()
        self.entry_chailatte = IntVar()
        self.entry_pineapple = IntVar()
        self.entry_watermelon = IntVar()
        self.entry_orange = IntVar()
        self.entry_cucumber = IntVar()
        self.entry_greenapple = IntVar()
        self.entry_celery = IntVar()

        self.var_costofmeal= StringVar()
        self.var_costofcoffee = StringVar()
        self.var_costofdrinks = StringVar()
        self.var_subtotal = StringVar()
        self.var_tax = StringVar()
        self.var_totalcost = StringVar()





        ##breakfast menu checkbutton functions

        def saf():
            if self.var1.get()==1:
                self.textsaf.config(state=NORMAL)
                self.textsaf.delete(0,END)
                self.textsaf.focus()
            else:

                self.textsaf.config(state=DISABLED)
                self.entry_saf.set('0')

        def ber():
            if self.var2.get()==1:
                self.textber.config(state=NORMAL)
                self.textber.delete(0, END)
                self.textber.focus()
            else:

                self.textber.config(state=DISABLED)
                self.entry_ber.set('0')

        def eot():
            if self.var3.get()==1:
                self.texteot.config(state=NORMAL)
                self.texteot.delete(0, END)
                self.texteot.focus()
            else:

                self.texteot.config(state=DISABLED)
                self.entry_eot.set('0')

        def mo():
            if self.var4.get()==1:
                self.textmo.config(state=NORMAL)
                self.textmo.delete(0, END)
                self.textmo.focus()
            else:

                self.textmo.config(state=DISABLED)
                self.entry_mo.set('0')

        def eb():
            if self.var5.get()==1:
                self.texteb.config(state=NORMAL)
                self.texteb.delete(0, END)
                self.texteb.focus()
            else:

                self.texteb.config(state=DISABLED)
                self.entry_eb.set('0')

        def bmc():
            if self.var6.get()==1:
                self.textbmc.config(state=NORMAL)
                self.textbmc.delete(0, END)
                self.textbmc.focus()
            else:

                self.textbmc.config(state=DISABLED)
                self.entry_bmc.set('0')

        def tmc():
            if self.var7.get()==1:
                self.texttmc.config(state=NORMAL)
                self.texttmc.delete(0, END)
                self.texttmc.focus()
            else:

                self.texttmc.config(state=DISABLED)
                self.entry_tmc.set('0')

        def mn():
            if self.var8.get()==1:
                self.textmn.config(state=NORMAL)
                self.textmn.delete(0, END)
                self.textmn.focus()
            else:

                self.textmn.config(state=DISABLED)
                self.entry_mn.set('0')

        def ets():
            if self.var9.get()==1:
                self.textets.config(state=NORMAL)
                self.textets.delete(0, END)
                self.textets.focus()
            else:

                self.textets.config(state=DISABLED)
                self.entry_ets.set('0')

        def tt1():
            if self.var10.get()==1:
                self.texttt1.config(state=NORMAL)
                self.texttt1.delete(0, END)
                self.texttt1.focus()
            else:

                self.texttt1.config(state=DISABLED)
                self.entry_tt1.set('0')

        def t1():
            if self.var11.get()==1:
                self.textt1.config(state=NORMAL)
                self.textt1.delete(0, END)
                self.textt1.focus()
            else:

                self.textt1.config(state=DISABLED)
                self.entry_t1.set('0')








        ##breakfastmenu


        self.saf =Checkbutton (self.breakfast_frame,text='Smash Avo & Feta', font=('arial', 15, 'bold'), bg='#F6D7B8',
                               onvalue=1, offvalue=0, variable=self.var1,command=saf)
        self.saf.grid(row=0, column=0,sticky=W)

        self.ber = Checkbutton(self.breakfast_frame, text='Bacon & Egg roll', font=('arial', 15, 'bold'), bg='#F6D7B8',
                               onvalue=1, offvalue=0, variable=self.var2,command=ber)
        self.ber.grid(row=1, column=0,sticky=W)

        self.eot = Checkbutton(self.breakfast_frame, text='Egg on Toast', font=('arial', 15, 'bold'), bg='#F6D7B8',
                               onvalue=1, offvalue=0, variable=self.var3,command=eot)
        self.eot.grid(row=2, column=0,sticky=W)

        self.mo = Checkbutton(self.breakfast_frame, text='Mad Omelet', font=('arial', 15, 'bold'), bg='#F6D7B8',
                               onvalue=1, offvalue=0, variable=self.var4,command=mo)
        self.mo.grid(row=3, column=0,sticky=W)

        self.eb = Checkbutton(self.breakfast_frame, text='Egg Benny', font=('arial', 15, 'bold'), bg='#F6D7B8',
                              onvalue=1, offvalue=0, variable=self.var5,command=eb)
        self.eb.grid(row=4, column=0, sticky=W)

        self.bmc = Checkbutton(self.breakfast_frame, text='Big Mad Cow', font=('arial', 15, 'bold'), bg='#F6D7B8',
                              onvalue=1, offvalue=0, variable=self.var6,command=bmc)
        self.bmc.grid(row=5, column=0, sticky=W)

        self.tmc = Checkbutton(self.breakfast_frame, text='Turkish Mad Cow', font=('arial', 15, 'bold'), bg='#F6D7B8',
                               onvalue=1, offvalue=0, variable=self.var7,command=tmc)
        self.tmc.grid(row=6, column=0, sticky=W)

        self.mn = Checkbutton(self.breakfast_frame, text='Menemen', font=('arial', 15, 'bold'), bg='#F6D7B8',
                               onvalue=1, offvalue=0, variable=self.var8,command=mn)
        self.mn.grid(row=7, column=0, sticky=W)

        self.ets = Checkbutton(self.breakfast_frame, text='Egg Turkish Sucuk', font=('arial', 15, 'bold'), bg='#F6D7B8',
                              onvalue=1, offvalue=0, variable=self.var9,command=ets)
        self.ets.grid(row=8, column=0, sticky=W)

        self.tt1 = Checkbutton(self.breakfast_frame, text='Turkish Toast', font=('arial', 15, 'bold'), bg='#F6D7B8',
                               onvalue=1, offvalue=0, variable=self.var10,command=tt1)
        self.tt1.grid(row=9, column=0, sticky=W)

        self.t1 = Checkbutton(self.breakfast_frame, text='Toastie', font=('arial', 15, 'bold'), bg='#F6D7B8',
                               onvalue=1, offvalue=0, variable=self.var11,command=t1)
        self.t1.grid(row=10, column=0, sticky=W)


        ##breakfast entry

        self.textsaf= Entry(self.breakfast_frame,font=('arial', 20, 'bold'),
                            bd=3,width=6, state=DISABLED,textvariable=self.entry_saf)
        self.textsaf.grid(row=0,column=1,sticky=E)

        self.textber = Entry(self.breakfast_frame, font=('arial', 20, 'bold'),
                             bd=3, width=6, state=DISABLED, textvariable=self.entry_ber)
        self.textber.grid(row=1, column=1, sticky=E)

        self.texteot = Entry(self.breakfast_frame, font=('arial', 20, 'bold'),
                             bd=3, width=6, state=DISABLED, textvariable=self.entry_eot)
        self.texteot.grid(row=2, column=1, sticky=E)

        self.textmo = Entry(self.breakfast_frame, font=('arial', 20, 'bold'),
                             bd=3, width=6, state=DISABLED, textvariable=self.entry_mo)
        self.textmo.grid(row=3, column=1, sticky=E)

        self.texteb = Entry(self.breakfast_frame, font=('arial', 20, 'bold'),
                            bd=3, width=6, state=DISABLED, textvariable=self.entry_eb)
        self.texteb.grid(row=4, column=1, sticky=E)

        self.textbmc = Entry(self.breakfast_frame, font=('arial', 20, 'bold'),
                            bd=3, width=6, state=DISABLED, textvariable=self.entry_bmc)
        self.textbmc.grid(row=5, column=1, sticky=E)

        self.texttmc = Entry(self.breakfast_frame, font=('arial', 20, 'bold'),
                             bd=3, width=6, state=DISABLED, textvariable=self.entry_tmc)
        self.texttmc.grid(row=6, column=1, sticky=E)

        self.textmn = Entry(self.breakfast_frame, font=('arial', 20, 'bold'),
                             bd=3, width=6, state=DISABLED, textvariable=self.entry_mn)
        self.textmn.grid(row=7, column=1, sticky=E)

        self.textets = Entry(self.breakfast_frame, font=('arial', 20, 'bold'),
                            bd=3, width=6, state=DISABLED, textvariable=self.entry_ets)
        self.textets.grid(row=8, column=1, sticky=E)

        self.texttt1 = Entry(self.breakfast_frame, font=('arial', 20, 'bold'),
                            bd=3, width=6, state=DISABLED, textvariable=self.entry_tt1)
        self.texttt1.grid(row=9, column=1, sticky=E)

        self.textt1 = Entry(self.breakfast_frame, font=('arial', 20, 'bold'),
                             bd=3, width=6, state=DISABLED, textvariable=self.entry_t1)
        self.textt1.grid(row=10, column=1, sticky=E)


        ##lunch menu checkbutton functions

        def kebab():
            if self.var12.get()==1:
                self.textkebab.config(state=NORMAL)
                self.textkebab.delete(0, END)
                self.textkebab.focus()
            else:
                self.textkebab.delete(0, END)
                self.textkebab.config(state=DISABLED)
                self.entry_kebab.set('0')

        def calamari():
            if self.var13.get()==1:
                self.textcalamari.config(state=NORMAL)
                self.textcalamari.delete(0, END)
                self.textcalamari.focus()
            else:
                self.textcalamari.delete(0, END)
                self.textcalamari.config(state=DISABLED)
                self.entry_calamari.set('0')

        def snackbox():
            if self.var14.get()==1:
                self.textsnackbox.config(state=NORMAL)
                self.textsnackbox.delete(0, END)
                self.textsnackbox.focus()
            else:
                self.textsnackbox.delete(0, END)
                self.textsnackbox.config(state=DISABLED)
                self.entry_snackbox.set('0')

        def bc():
            if self.var15.get()==1:
                self.textbc.config(state=NORMAL)
                self.textbc.delete(0, END)
                self.textbc.focus()
            else:
                self.textbc.delete(0, END)
                self.textbc.config(state=DISABLED)
                self.entry_bc.set('0')

        def clubsandwich():
            if self.var16.get()==1:
                self.textclubsandwich.config(state=NORMAL)
                self.textclubsandwich.delete(0, END)
                self.textclubsandwich.focus()
            else:
                self.textclubsandwich.delete(0, END)
                self.textclubsandwich.config(state=DISABLED)
                self.entry_clubsandwich.set('0')

        def chichkensandwich():
            if self.var17.get()==1:
                self.textchichkensandwich.config(state=NORMAL)
                self.textchichkensandwich.delete(0, END)
                self.textchichkensandwich.focus()
            else:
                self.textchichkensandwich.delete(0, END)
                self.textchichkensandwich.config(state=DISABLED)
                self.entry_chichkensandwich.set('0')

        def salmonsandwich():
            if self.var18.get()==1:
                self.textsalmonsandwich.config(state=NORMAL)
                self.textsalmonsandwich.delete(0, END)
                self.textsalmonsandwich.focus()
            else:
                self.textsalmonsandwich.delete(0, END)
                self.textsalmonsandwich.config(state=DISABLED)
                self.entry_salmonsandwich.set('0')

        def sg():
            if self.var19.get()==1:
                self.textsg.config(state=NORMAL)
                self.textsg.delete(0, END)
                self.textsg.focus()
            else:
                self.textsg.delete(0, END)
                self.textsg.config(state=DISABLED)
                self.entry_sg.set('0')

        def smg():
            if self.var20.get()==1:
                self.textsmg.config(state=NORMAL)
                self.textsmg.delete(0, END)
                self.textsmg.focus()
            else:
                self.textsmg.delete(0, END)
                self.textsmg.config(state=DISABLED)
                self.entry_smg.set('0')

        def fc():
            if self.var21.get()==1:
                self.textfc.config(state=NORMAL)
                self.textfc.delete(0, END)
                self.textfc.focus()
            else:
                self.textfc.delete(0, END)
                self.textfc.config(state=DISABLED)
                self.entry_fc.set('0')

        def hd():
            if self.var22.get()==1:
                self.texthd.config(state=NORMAL)
                self.texthd.delete(0, END)
                self.texthd.focus()
            else:
                self.texthd.delete(0, END)
                self.texthd.config(state=DISABLED)
                self.entry_hd.set('0')



        ##lunchmenu

        self.kebab = Checkbutton(self.lunch_frame, text='Kebab', font=('arial', 15, 'bold'), bg='#F6D7B8',
                              onvalue=1, offvalue=0, variable=self.var12,command=kebab)
        self.kebab.grid(row=0, column=0, sticky=W)

        self.calamari = Checkbutton(self.lunch_frame, text='Calamari', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                 onvalue=1, offvalue=0, variable=self.var13,command=calamari)
        self.calamari.grid(row=1, column=0, sticky=W)

        self.snackbox = Checkbutton(self.lunch_frame, text='Snack Box', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                    onvalue=1, offvalue=0, variable=self.var14,command=snackbox)
        self.snackbox.grid(row=2, column=0, sticky=W)

        self.bc = Checkbutton(self.lunch_frame, text='Burger & Chips', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                    onvalue=1, offvalue=0, variable=self.var15,command=bc)
        self.bc.grid(row=3, column=0, sticky=W)

        self.clubsandwich = Checkbutton(self.lunch_frame, text='Club Sandwich', font=('arial', 15, 'bold'), bg='#F6D7B8',
                              onvalue=1, offvalue=0, variable=self.var16,command=clubsandwich)
        self.clubsandwich.grid(row=4, column=0, sticky=W)

        self.chichkensandwich = Checkbutton(self.lunch_frame, text='Chicken Sandwich', font=('arial', 15, 'bold'),
                                        bg='#F6D7B8',onvalue=1, offvalue=0, variable=self.var17,command=chichkensandwich)
        self.chichkensandwich.grid(row=5, column=0, sticky=W)

        self.salmonsandwich = Checkbutton(self.lunch_frame, text='Salmon Sandwich', font=('arial', 15, 'bold'),
                                            bg='#F6D7B8', onvalue=1, offvalue=0, variable=self.var18,command=salmonsandwich)
        self.salmonsandwich.grid(row=6, column=0, sticky=W)

        self.sg = Checkbutton(self.lunch_frame, text='Skewers Grill', font=('arial', 15, 'bold'),
                                          bg='#F6D7B8',
                                          onvalue=1, offvalue=0, variable=self.var19,command=sg)
        self.sg.grid(row=7, column=0, sticky=W)

        self.smg = Checkbutton(self.lunch_frame, text='Skewers Mix Grill', font=('arial', 15, 'bold'),
                              bg='#F6D7B8',
                              onvalue=1, offvalue=0, variable=self.var20,command=smg)
        self.smg.grid(row=8, column=0, sticky=W)

        self.fc = Checkbutton(self.lunch_frame, text='Fish & Chips', font=('arial', 15, 'bold'),
                               bg='#F6D7B8',
                               onvalue=1, offvalue=0, variable=self.var21,command=fc)
        self.fc.grid(row=9, column=0, sticky=W)

        self.hd = Checkbutton(self.lunch_frame, text='Hot Dog', font=('arial', 15, 'bold'),
                              bg='#F6D7B8',
                              onvalue=1, offvalue=0, variable=self.var22,command=hd)
        self.hd.grid(row=10, column=0, sticky=W)


        ##Lunch Entry
        self.textkebab = Entry(self.lunch_frame, font=('arial', 20, 'bold'),
                             bd=3, width=6, state=DISABLED, textvariable=self.entry_kebab)
        self.textkebab.grid(row=0, column=1, sticky=E)

        self.textcalamari = Entry(self.lunch_frame, font=('arial', 20, 'bold'),
                               bd=3, width=6, state=DISABLED, textvariable=self.entry_calamari)
        self.textcalamari.grid(row=1, column=1, sticky=E)

        self.textsnackbox = Entry(self.lunch_frame, font=('arial', 20, 'bold'),
                                  bd=3, width=6, state=DISABLED, textvariable=self.entry_snackbox)
        self.textsnackbox.grid(row=2, column=1, sticky=E)

        self.textbc = Entry(self.lunch_frame, font=('arial', 20, 'bold'),
                                  bd=3, width=6, state=DISABLED, textvariable=self.entry_bc)
        self.textbc.grid(row=3, column=1, sticky=E)

        self.textclubsandwich = Entry(self.lunch_frame, font=('arial', 20, 'bold'),
                            bd=3, width=6, state=DISABLED, textvariable=self.entry_clubsandwich)
        self.textclubsandwich.grid(row=4, column=1, sticky=E)

        self.textchichkensandwich = Entry(self.lunch_frame, font=('arial', 20, 'bold'),
                            bd=3, width=6, state=DISABLED, textvariable=self.entry_chichkensandwich)
        self.textchichkensandwich.grid(row=5, column=1, sticky=E)

        self.textsalmonsandwich = Entry(self.lunch_frame, font=('arial', 20, 'bold'),
                            bd=3, width=6, state=DISABLED, textvariable=self.entry_salmonsandwich)
        self.textsalmonsandwich.grid(row=6, column=1, sticky=E)

        self.textsg = Entry(self.lunch_frame, font=('arial', 20, 'bold'),
                                        bd=3, width=6, state=DISABLED, textvariable=self.entry_sg)
        self.textsg.grid(row=7, column=1, sticky=E)

        self.textsmg = Entry(self.lunch_frame, font=('arial', 20, 'bold'),
                                        bd=3, width=6, state=DISABLED, textvariable=self.entry_smg)
        self.textsmg.grid(row=8, column=1, sticky=E)

        self.textfc = Entry(self.lunch_frame, font=('arial', 20, 'bold'),
                             bd=3, width=6, state=DISABLED, textvariable=self.entry_fc)
        self.textfc.grid(row=9, column=1, sticky=E)

        self.texthd = Entry(self.lunch_frame, font=('arial', 20, 'bold'),
                             bd=3, width=6, state=DISABLED, textvariable=self.entry_hd)
        self.texthd.grid(row=10, column=1, sticky=E)

        ##coffee menu checkbutton functions

        def espresso():
            if self.var23.get() == 1:
                self.textespresso.config(state=NORMAL)
                self.textespresso.delete(0, END)
                self.textespresso.focus()
            else:
                self.textespresso.delete(0, END)
                self.textespresso.config(state=DISABLED)
                self.entry_espresso.set('0')

        def flatwhite():
            if self.var24.get() == 1:
                self.textflatwhite.config(state=NORMAL)
                self.textflatwhite.delete(0, END)
                self.textflatwhite.focus()
            else:
                self.textflatwhite.delete(0, END)
                self.textflatwhite.config(state=DISABLED)
                self.entry_flatwhite.set('0')

        def cappuccino():
            if self.var25.get() == 1:
                self.textcappuccino.config(state=NORMAL)
                self.textcappuccino.delete(0, END)
                self.textcappuccino.focus()
            else:
                self.textcappuccino.delete(0, END)
                self.textcappuccino.config(state=DISABLED)
                self.entry_cappuccino.set('0')

        def longblack():
            if self.var26.get() == 1:
                self.textlongblack.config(state=NORMAL)
                self.textlongblack.delete(0, END)
                self.textlongblack.focus()
            else:
                self.textlongblack.delete(0, END)
                self.textlongblack.config(state=DISABLED)
                self.entry_longblack.set('0')

        def latte():
            if self.var27.get() == 1:
                self.textlatte.config(state=NORMAL)
                self.textlatte.delete(0, END)
                self.textlatte.focus()
            else:
                self.textlatte.delete(0, END)

                self.textlatte.config(state=DISABLED)
                self.entry_latte.set('0')

        def hotchoco():
            if self.var28.get() == 1:
                self.texthotchoco.config(state=NORMAL)
                self.texthotchoco.delete(0, END)
                self.texthotchoco.focus()
            else:
                self.texthotchoco.delete(0, END)
                self.texthotchoco.config(state=DISABLED)
                self.entry_hotchoco.set('0')

        def macchiato():
            if self.var29.get() == 1:
                self.textmacchiato.config(state=NORMAL)
                self.textmacchiato.delete(0, END)
                self.textmacchiato.focus()
            else:
                self.textmacchiato.delete(0, END)
                self.textmacchiato.config(state=DISABLED)
                self.entry_macchiato.set('0')


        def piccolo():
            if self.var30.get() == 1:
                self.textpiccolo.config(state=NORMAL)
                self.textpiccolo.delete(0, END)
                self.textpiccolo.focus()
            else:
                self.textpiccolo.delete(0, END)
                self.textpiccolo.config(state=DISABLED)
                self.entry_piccolo.set('0')

        def affogato():
            if self.var31.get() == 1:
                self.textaffogato.config(state=NORMAL)
                self.textaffogato.delete(0, END)
                self.textaffogato.focus()
            else:
                self.textaffogato.delete(0, END)
                self.textaffogato.config(state=DISABLED)
                self.entry_affogato.set('0')

        def mediumsize():
            if self.var32.get() == 1:
                self.textmediumsize.config(state=NORMAL)
                self.textmediumsize.delete(0, END)
                self.textmediumsize.focus()
            else:
                self.textmediumsize.delete(0, END)
                self.textmediumsize.config(state=DISABLED)
                self.entry_mediumsize.set('0')

        def largesize():
            if self.var33.get() == 1:
                self.textlargesize.config(state=NORMAL)
                self.textlargesize.delete(0, END)
                self.textlargesize.focus()
            else:
                self.textlargesize.delete(0, END)
                self.textlargesize.config(state=DISABLED)
                self.entry_largesize.set('0')



        ##coffee menu
        self.espresso = Checkbutton(self.coffee_frame, text='Espresso', font=('arial', 15, 'bold'), bg='#F6D7B8',
                               onvalue=1, offvalue=0, variable=self.var23,command=espresso)
        self.espresso.grid(row=0, column=0, sticky=W)

        self.flatwhite = Checkbutton(self.coffee_frame, text='Flat White', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                    onvalue=1, offvalue=0, variable=self.var24,command=flatwhite)
        self.flatwhite.grid(row=1, column=0, sticky=W)

        self.cappuccino = Checkbutton(self.coffee_frame, text='Cappuccino', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                    onvalue=1, offvalue=0, variable=self.var25,command=cappuccino)
        self.cappuccino.grid(row=2, column=0, sticky=W)

        self.longblack = Checkbutton(self.coffee_frame, text='Long Black', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                      onvalue=1, offvalue=0, variable=self.var26,command=longblack)
        self.longblack.grid(row=3, column=0, sticky=W)

        self.latte = Checkbutton(self.coffee_frame, text='Latte', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                      onvalue=1, offvalue=0, variable=self.var27,command=latte)
        self.latte.grid(row=4, column=0, sticky=W)

        self.hotchoco = Checkbutton(self.coffee_frame, text='Hot Chocolate', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                      onvalue=1, offvalue=0, variable=self.var28,command=hotchoco)
        self.hotchoco.grid(row=5, column=0, sticky=W)

        self.macchiato = Checkbutton(self.coffee_frame, text='Macchiato', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                    onvalue=1, offvalue=0, variable=self.var29,command=macchiato)
        self.macchiato.grid(row=6, column=0, sticky=W)

        self.piccolo = Checkbutton(self.coffee_frame, text='Piccolo', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                    onvalue=1, offvalue=0, variable=self.var30,command=piccolo)
        self.piccolo.grid(row=7, column=0, sticky=W)

        self.affogato = Checkbutton(self.coffee_frame, text='Affogato', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                    onvalue=1, offvalue=0, variable=self.var31,command=affogato)
        self.affogato.grid(row=8, column=0, sticky=W)

        self.mediumsize = Checkbutton(self.coffee_frame, text='Medium size', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                    onvalue=1, offvalue=0, variable=self.var32,command=mediumsize)
        self.mediumsize.grid(row=9, column=0, sticky=W)

        self.largesize = Checkbutton(self.coffee_frame, text='Large size', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                      onvalue=1, offvalue=0, variable=self.var33,command=largesize)
        self.largesize.grid(row=10, column=0, sticky=W)






        ##coffee entry
        self.textespresso = Entry(self.coffee_frame,font=('arial', 20, 'bold'),
                                  bd=3, width=6, state=DISABLED, textvariable=self.entry_espresso)
        self.textespresso.grid(row=0, column=1, sticky=E)

        self.textflatwhite = Entry(self.coffee_frame, font=('arial', 20, 'bold'),
                                  bd=3, width=6, state=DISABLED, textvariable=self.entry_flatwhite)
        self.textflatwhite.grid(row=1, column=1, sticky=E)

        self.textcappuccino = Entry(self.coffee_frame, font=('arial', 20, 'bold'),
                                  bd=3, width=6, state=DISABLED, textvariable=self.entry_cappuccino)
        self.textcappuccino.grid(row=2, column=1, sticky=E)

        self.textlongblack = Entry(self.coffee_frame, font=('arial', 20, 'bold'),
                                    bd=3, width=6, state=DISABLED, textvariable=self.entry_longblack)
        self.textlongblack.grid(row=3, column=1, sticky=E)

        self.textlatte = Entry(self.coffee_frame, font=('arial', 20, 'bold'),
                                    bd=3, width=6, state=DISABLED, textvariable=self.entry_latte)
        self.textlatte.grid(row=4, column=1, sticky=E)

        self.texthotchoco = Entry(self.coffee_frame, font=('arial', 20, 'bold'),
                                    bd=3, width=6, state=DISABLED, textvariable=self.entry_hotchoco)
        self.texthotchoco.grid(row=5, column=1, sticky=E)

        self.textmacchiato = Entry(self.coffee_frame, font=('arial', 20, 'bold'),
                                  bd=3, width=6, state=DISABLED, textvariable=self.entry_macchiato)
        self.textmacchiato.grid(row=6, column=1, sticky=E)

        self.textpiccolo = Entry(self.coffee_frame, font=('arial', 20, 'bold'),
                                  bd=3, width=6, state=DISABLED, textvariable=self.entry_piccolo)
        self.textpiccolo.grid(row=7, column=1, sticky=E)

        self.textaffogato = Entry(self.coffee_frame, font=('arial', 20, 'bold'),
                                  bd=3, width=6, state=DISABLED, textvariable=self.entry_affogato)
        self.textaffogato.grid(row=8, column=1, sticky=E)

        self.textmediumsize = Entry(self.coffee_frame, font=('arial', 20, 'bold'),
                                  bd=3, width=6, state=DISABLED, textvariable=self.entry_mediumsize)
        self.textmediumsize.grid(row=9, column=1, sticky=E)

        self.textlargesize = Entry(self.coffee_frame, font=('arial', 20, 'bold'),
                                  bd=3, width=6, state=DISABLED, textvariable=self.entry_largesize)
        self.textlargesize.grid(row=10, column=1, sticky=E)

        ##drinks menu checkbutton functions

        def peppermint():
            if self.var34.get() == 1:
                self.textpeppermint.config(state=NORMAL)
                self.textpeppermint.delete(0, END)
                self.textpeppermint.focus()
            else:
                self.textpeppermint.config(state=DISABLED)
                self.entry_peppermint.set('0')

        def earl_grey():
            if self.var35.get() == 1:
                self.textearl_grey.config(state=NORMAL)
                self.textearl_grey.delete(0, END)
                self.textearl_grey.focus()
            else:

                self.textearl_grey.config(state=DISABLED)
                self.entry_earl_grey.set('0')

        def engbreak():
            if self.var36.get() == 1:
                self.textengbreak.config(state=NORMAL)
                self.textengbreak.delete(0, END)
                self.textengbreak.focus()
            else:

                self.textengbreak.config(state=DISABLED)
                self.entry_engbreak.set('0')

        def chamomile():
            if self.var37.get() == 1:
                self.textchamomile.config(state=NORMAL)
                self.textchamomile.delete(0, END)
                self.textchamomile.focus()
            else:

                self.textchamomile.config(state=DISABLED)
                self.entry_chamomile.set('0')

        def turkishtea():
            if self.var38.get() == 1:
                self.textturkishtea.config(state=NORMAL)
                self.textturkishtea.delete(0, END)
                self.textturkishtea.focus()
            else:

                self.textturkishtea.config(state=DISABLED)
                self.entry_turkishtea.set('0')

        def chailatte():
            if self.var39.get() == 1:
                self.textchailatte.config(state=NORMAL)
                self.textchailatte.delete(0, END)
                self.textchailatte.focus()
            else:

                self.textchailatte.config(state=DISABLED)
                self.entry_chailatte.set('0')

        def pineapple():
            if self.var40.get() == 1:
                self.textpineapple.config(state=NORMAL)
                self.textpineapple.delete(0, END)
                self.textpineapple.focus()
            else:

                self.textpineapple.config(state=DISABLED)
                self.entry_pineapple.set('0')

        def watermelon():
            if self.var41.get() == 1:
                self.textwatermelon.config(state=NORMAL)
                self.textwatermelon.delete(0, END)
                self.textwatermelon.focus()
            else:

                self.textwatermelon.config(state=DISABLED)
                self.entry_watermelon.set('0')

        def orange():
            if self.var42.get() == 1:
                self.textorange.config(state=NORMAL)
                self.textorange.delete(0, END)
                self.textorange.focus()
            else:

                self.textorange.config(state=DISABLED)
                self.entry_orange.set('0')

        def cucumber():
            if self.var43.get() == 1:
                self.textcucumber.config(state=NORMAL)
                self.textcucumber.delete(0, END)
                self.textcucumber.focus()
            else:

                self.textcucumber.config(state=DISABLED)
                self.entry_cucumber.set('0')

        def greenapple():
            if self.var44.get() == 1:
                self.textgreenapple.config(state=NORMAL)
                self.textgreenapple.delete(0, END)
                self.textgreenapple.focus()
            else:

                self.textgreenapple.config(state=DISABLED)
                self.entry_greenapple.set('0')

        def celery():
            if self.var45.get() == 1:
                self.textcelery.config(state=NORMAL)
                self.textcelery.delete(0, END)
                self.textcelery.focus()
            else:

                self.textcelery.config(state=DISABLED)
                self.entry_celery.set('0')



        ##tea menu
        self.peppermint=Checkbutton(self.tea_frame,text='Peppermint', font=('arial', 15, 'bold'), bg='#F6D7B8',
                               onvalue=1, offvalue=0, variable=self.var34,command=peppermint)
        self.peppermint.grid(row=0, column=0, sticky=W)

        self.earl_grey = Checkbutton(self.tea_frame, text='Earl Grey', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                      onvalue=1, offvalue=0, variable=self.var35,command=earl_grey)
        self.earl_grey.grid(row=1, column=0, sticky=W)

        self.engbreak = Checkbutton(self.tea_frame, text='English Breakfast', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                      onvalue=1, offvalue=0, variable=self.var36,command=engbreak)
        self.engbreak.grid(row=2, column=0, sticky=W)

        self.chamomile = Checkbutton(self.tea_frame, text='Chamomile', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                    onvalue=1, offvalue=0, variable=self.var37,command=chamomile)
        self.chamomile.grid(row=3, column=0, sticky=W)

        self.turkishtea = Checkbutton(self.tea_frame, text='Turkish Tea', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                    onvalue=1, offvalue=0, variable=self.var38,command=turkishtea)
        self.turkishtea.grid(row=4, column=0, sticky=W)

        self.chailatte = Checkbutton(self.tea_frame, text='Chai Latte', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                    onvalue=1, offvalue=0, variable=self.var39,command=chailatte)
        self.chailatte.grid(row=5, column=0, sticky=W)




        ##juice menu
        self.pineapple = Checkbutton(self.juice_frame, text='Pineapple           ', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                     onvalue=1, offvalue=0, variable=self.var40,command=pineapple)
        self.pineapple.grid(row=0, column=0, sticky=W)

        self.watermelon = Checkbutton(self.juice_frame, text='Watermelon          ', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                     onvalue=1, offvalue=0, variable=self.var41,command=watermelon)
        self.watermelon.grid(row=1, column=0, sticky=W)

        self.orange = Checkbutton(self.juice_frame, text='Orange          ', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                      onvalue=1, offvalue=0, variable=self.var42,command=orange)
        self.orange.grid(row=2, column=0, sticky=W)

        self.cucumber = Checkbutton(self.juice_frame, text='Cucumber          ', font=('arial', 15, 'bold'), bg='#F6D7B8',
                                      onvalue=1, offvalue=0, variable=self.var43,command=cucumber)
        self.cucumber.grid(row=3, column=0, sticky=W)

        self.greenapple = Checkbutton(self.juice_frame, text='Green Apple         ', font=('arial', 15, 'bold'),
                                    bg='#F6D7B8',
                                    onvalue=1, offvalue=0, variable=self.var44,command=greenapple)
        self.greenapple.grid(row=4, column=0, sticky=W)

        self.celery = Checkbutton(self.juice_frame, text='Celery        ', font=('arial', 15, 'bold'),
                                      bg='#F6D7B8',
                                      onvalue=1, offvalue=0, variable=self.var45,command=celery)
        self.celery.grid(row=5, column=0, sticky=W)

        ##drinks entry

        self.textpeppermint = Entry(self.tea_frame, font=('arial', 15, 'bold'),
                                    bd=3, width=6, state=DISABLED, textvariable=self.entry_peppermint)
        self.textpeppermint.grid(row=0, column=1, sticky=E)

        self.textearl_grey = Entry(self.tea_frame, font=('arial', 15, 'bold'),
                                    bd=3, width=6, state=DISABLED, textvariable=self.entry_earl_grey)
        self.textearl_grey.grid(row=1, column=1, sticky=E)

        self.textengbreak = Entry(self.tea_frame, font=('arial', 15, 'bold'),
                                    bd=3, width=6, state=DISABLED, textvariable=self.entry_engbreak)
        self.textengbreak.grid(row=2, column=1, sticky=E)

        self.textchamomile = Entry(self.tea_frame, font=('arial', 15, 'bold'),
                                  bd=3, width=6, state=DISABLED, textvariable=self.entry_chamomile)
        self.textchamomile.grid(row=3, column=1, sticky=E)

        self.textturkishtea = Entry(self.tea_frame, font=('arial', 15, 'bold'),
                                  bd=3, width=6, state=DISABLED, textvariable=self.entry_turkishtea)
        self.textturkishtea.grid(row=4, column=1, sticky=E)

        self.textchailatte = Entry(self.tea_frame, font=('arial', 15, 'bold'),
                                  bd=3, width=6, state=DISABLED, textvariable=self.entry_chailatte)
        self.textchailatte.grid(row=5, column=1, sticky=E)

        self.textpineapple = Entry(self.juice_frame, font=('arial', 15, 'bold'),
                                   bd=3, width=6, state=DISABLED, textvariable=self.entry_pineapple)
        self.textpineapple.grid(row=0, column=1,sticky=E)

        self.textwatermelon = Entry(self.juice_frame, font=('arial', 15, 'bold'),
                                   bd=3, width=6, state=DISABLED, textvariable=self.entry_watermelon)
        self.textwatermelon.grid(row=1, column=1, sticky=E)

        self.textorange = Entry(self.juice_frame, font=('arial', 15, 'bold'),
                                   bd=3, width=6, state=DISABLED, textvariable=self.entry_orange)
        self.textorange.grid(row=2, column=1, sticky=E)

        self.textcucumber = Entry(self.juice_frame, font=('arial', 15, 'bold'),
                                bd=3, width=6, state=DISABLED, textvariable=self.entry_cucumber)
        self.textcucumber.grid(row=3, column=1, sticky=E)

        self.textgreenapple = Entry(self.juice_frame, font=('arial', 15, 'bold'),
                                  bd=3, width=6, state=DISABLED,textvariable=self.entry_greenapple)
        self.textgreenapple.grid(row=4, column=1, sticky=E)

        self.textcelery = Entry(self.juice_frame, font=('arial', 15, 'bold'),
                                    bd=3, width=6, state=DISABLED, textvariable=self.entry_celery)
        self.textcelery.grid(row=5, column=1, sticky=E)


        ##cost entry

        self.label_costofmeal = Label(self.cost_frame,text='Cost of Meal', font=('Britannic Bold', 16, 'bold'),
                                          fg='#7D2509', bg='#F6D7B8' )
        self.label_costofmeal.grid(row=0,column=0,sticky=W,padx=63)

        self.textcostofmeal =Entry(self.cost_frame,font=('arial', 16, 'bold'),bd=1,width=18,state='readonly',textvariable=self.var_costofmeal)
        self.textcostofmeal.grid(row=0,column=1,padx=40)

        self.label_costofcoffee = Label(self.cost_frame, text='Cost of Coffee', font=('Britannic Bold', 16, 'bold'),
                                      fg='#7D2509', bg='#F6D7B8')
        self.label_costofcoffee.grid(row=1, column=0,padx=63)

        self.textcostofcoffee = Entry(self.cost_frame, font=('arial', 16, 'bold'), bd=1,width=18,state='readonly',textvariable=self.var_costofcoffee)
        self.textcostofcoffee.grid(row=1, column=1,padx=40)

        self.label_costofdrinks = Label(self.cost_frame, text='Cost of Drinks', font=('Britannic Bold', 16, 'bold'),
                                        fg='#7D2509', bg='#F6D7B8')
        self.label_costofdrinks.grid(row=2, column=0,padx=63)

        self.textcostofdrinks = Entry(self.cost_frame, font=('arial', 16, 'bold'), bd=1, width=18,state='readonly',textvariable=self.var_costofdrinks)
        self.textcostofdrinks.grid(row=2, column=1,padx=40)

        self.label_subtotal = Label(self.cost_frame, text='Sub Total', font=('Britannic Bold', 16, 'bold'),
                                        fg='#7D2509', bg='#F6D7B8')
        self.label_subtotal.grid(row=0, column=2,padx=63)

        self.textsubtotal = Entry(self.cost_frame, font=('arial', 16, 'bold'), bd=1, width=18,state='readonly',textvariable=self.var_subtotal)
        self.textsubtotal.grid(row=0, column=3,padx=40)

        self.label_tax = Label(self.cost_frame, text='Tax', font=('Britannic Bold', 16, 'bold'),
                                    fg='#7D2509', bg='#F6D7B8')
        self.label_tax.grid(row=1, column=2,padx=63)

        self.texttax = Entry(self.cost_frame, font=('arial', 16, 'bold'), bd=1, width=18,state='readonly',textvariable=self.var_tax)
        self.texttax.grid(row=1, column=3,padx=40)

        self.label_totalcost = Label(self.cost_frame, text='Total Cost', font=('Britannic Bold', 16, 'bold'),
                               fg='#7D2509', bg='#F6D7B8')
        self.label_totalcost.grid(row=2, column=2,padx=63)

        self.texttotalcost= Entry(self.cost_frame, font=('arial', 16, 'bold'), bd=1, width=18,state='readonly',textvariable=self.var_totalcost)
        self.texttotalcost.grid(row=2, column=3,padx=40)



        ##buttons for calculator
        self.buttoncalculator = Button(self.calculator_frame,text='To Receipt ',font=('Britannic Bold', 16, 'bold'),bd=1,
                               fg='#7D2509', bg='#F6D7B8',command=lambda :swap(self.receipt_frame)).pack()
        

        ##window for calculator
        self.calculator_entry=Entry(self.calculator_frame,font=('Britannic Bold', 16, 'bold'),bd=1,width=35)
        self.calculator_entry.pack()

        ##calculator operation


        def buttonclick(numbers):
            global operator
            operator=operator+numbers
            self.calculator_entry.delete(0,END)
            self.calculator_entry.insert(END,operator)

        def clear():
            global operator
            operator=''
            self.calculator_entry.delete(0, END)

        def answer():
            global operator
            self.result= str(eval(operator))
            self.calculator_entry.delete(0, END)
            self.calculator_entry.insert(0,self.result)
            operator=''








        self.button7=Button(self.calculator_buttonframe,text='7',font=('Britannic Bold', 16, 'bold'),
                            fg='#7D2509', bg='#F6D7B8',width=4,height=3,command=lambda :buttonclick('7'))
        self.button7.grid(row=0,column=0)
        self.button8 = Button(self.calculator_buttonframe, text='8', font=('Britannic Bold', 16, 'bold'), fg='#7D2509',
                              bg='#F6D7B8',width=4,height=3,command=lambda :buttonclick('8'))
        self.button8.grid(row=0,column=1)
        self.button9 = Button(self.calculator_buttonframe, text='9', font=('Britannic Bold', 16, 'bold'), fg='#7D2509',
                              bg='#F6D7B8',width=4,height=3,command=lambda :buttonclick('9'))
        self.button9.grid(row=0,column=2)

        self.buttonmultiple = Button(self.calculator_buttonframe, text='x', font=('Britannic Bold', 16, 'bold'), fg='#7D2509',
                              bg='#F6D7B8',width=4,height=3,command=lambda :buttonclick('*'))
        self.buttonmultiple.grid(row=0,column=3)

        self.button4 = Button(self.calculator_buttonframe, text='4', font=('Britannic Bold', 16, 'bold'), fg='#7D2509',
                                     bg='#F6D7B8',width=4,height=3,command=lambda :buttonclick('4'))
        self.button4.grid(row=1,column=0)

        self.button5 = Button(self.calculator_buttonframe, text='5', font=('Britannic Bold', 16, 'bold'), fg='#7D2509',
                              bg='#F6D7B8', width=4,height=3,command=lambda :buttonclick('5'))
        self.button5.grid(row=1, column=1)

        self.button6 = Button(self.calculator_buttonframe, text='6', font=('Britannic Bold', 16, 'bold'), fg='#7D2509',
                              bg='#F6D7B8', width=4,height=3,command=lambda :buttonclick('6'))
        self.button6.grid(row=1, column=2)

        self.buttonminus = Button(self.calculator_buttonframe, text='-', font=('Britannic Bold', 16, 'bold'), fg='#7D2509',
                              bg='#F6D7B8', width=4,height=3,command=lambda :buttonclick('-'))
        self.buttonminus.grid(row=1, column=3)

        self.button1 = Button(self.calculator_buttonframe, text='1', font=('Britannic Bold', 16, 'bold'),
                                  fg='#7D2509',
                                  bg='#F6D7B8', width=4,height=3,command=lambda :buttonclick('1'))
        self.button1.grid(row=2, column=0)

        self.button2 = Button(self.calculator_buttonframe, text='2', font=('Britannic Bold', 16, 'bold'),
                                  fg='#7D2509',
                                  bg='#F6D7B8', width=4,height=3,command=lambda :buttonclick('2'))
        self.button2.grid(row=2, column=1)

        self.button3 = Button(self.calculator_buttonframe, text='3', font=('Britannic Bold', 16, 'bold'),
                                  fg='#7D2509',
                                  bg='#F6D7B8', width=4,height=3,command=lambda :buttonclick('3'))
        self.button3.grid(row=2, column=2)

        self.buttonplus = Button(self.calculator_buttonframe, text='+', font=('Britannic Bold', 16, 'bold'),
                                  fg='#7D2509',
                                  bg='#F6D7B8', width=4,height=3,command=lambda :buttonclick('+'))
        self.buttonplus.grid(row=2, column=3)

        self.button0 = Button(self.calculator_buttonframe, text='0', font=('Britannic Bold', 16, 'bold'),
                              fg='#7D2509',
                              bg='#F6D7B8', width=4,height=3,command=lambda :buttonclick('0'))
        self.button0.grid(row=3, column=0)

        self.buttonans = Button(self.calculator_buttonframe, text='Ans', font=('Britannic Bold', 16, 'bold'),
                              fg='#7D2509',bg='#F6D7B8', width=4,height=3,command=answer)
        self.buttonans.grid(row=3, column=1)

        self.buttonclear = Button(self.calculator_buttonframe, text='Clear', font=('Britannic Bold', 16, 'bold'),
                              fg='#7D2509',bg='#F6D7B8', width=4,height=3,command=clear)
        self.buttonclear.grid(row=3, column=2)

        self.buttondivision = Button(self.calculator_buttonframe, text='/', font=('Britannic Bold', 16, 'bold'),
                              fg='#7D2509',
                              bg='#F6D7B8', width=4,height=3,command=lambda :buttonclick('/'))
        self.buttondivision.grid(row=3, column=3)



        ##buttons for receipt
        self.buttonreceipt = Button(self.receipt_frame, text='To Calculator',font=('Britannic Bold', 16, 'bold'),bd=1,
                               fg='#7D2509', bg='#F6D7B8',command=lambda:swap(self.calculator_frame)).pack()
        

        ##window for receipt
        self.textreceipt= Text(self.receipt_frame,font=('Britannic Bold', 16, 'bold'),bd=1,width=35,height=16)
        self.textreceipt.pack()




       ##create total cost function

        def totalcost():
            global priceofmeal, priceofcoffee, priceofdrinks,subtotalitems


            self.item1 = int(self.entry_saf.get())
            self.item2 = int(self.entry_ber.get())
            self.item3 = int(self.entry_eot.get())
            self.item4 = int(self.entry_mo.get())
            self.item5 = int(self.entry_eb.get())
            self.item6 = int(self.entry_bmc.get())
            self.item7 = int(self.entry_tmc.get())
            self.item8 = int(self.entry_mn.get())
            self.item9 = int(self.entry_ets.get())
            self.item10 = int(self.entry_tt1.get())
            self.item11 = int(self.entry_t1.get())


            self.item12 = int(self.entry_kebab.get())
            self.item13 = int(self.entry_calamari.get())
            self.item14 = int(self.entry_snackbox.get())
            self.item15 = int(self.entry_bc.get())
            self.item16 = int(self.entry_clubsandwich.get())
            self.item17 = int(self.entry_chichkensandwich.get())
            self.item18 = int(self.entry_salmonsandwich.get())
            self.item19 = int(self.entry_sg.get())
            self.item20 = int(self.entry_smg.get())
            self.item21 = int(self.entry_fc.get())
            self.item22 = int(self.entry_hd.get())

            self.item23 = int(self.entry_espresso.get())
            self.item24 = int(self.entry_flatwhite.get())
            self.item25 = int(self.entry_cappuccino.get())
            self.item26 = int(self.entry_longblack.get())
            self.item27 = int(self.entry_latte.get())
            self.item28 = int(self.entry_hotchoco.get())
            self.item29 = int(self.entry_macchiato.get())
            self.item30 = int(self.entry_piccolo.get())
            self.item31 = int(self.entry_affogato.get())
            self.item32 = int(self.entry_mediumsize.get())
            self.item33 = int(self.entry_largesize.get())

            self.item34 = int(self.entry_peppermint.get())
            self.item35 = int(self.entry_earl_grey.get())
            self.item36 = int(self.entry_engbreak.get())
            self.item37 = int(self.entry_chamomile.get())
            self.item38 = int(self.entry_turkishtea.get())
            self.item39 = int(self.entry_chailatte.get())
            self.item40 = int(self.entry_pineapple.get())
            self.item41 = int(self.entry_watermelon.get())
            self.item42 = int(self.entry_orange.get())
            self.item43 = int(self.entry_cucumber.get())
            self.item44 = int(self.entry_greenapple.get())
            self.item45 = int(self.entry_celery.get())


            self.mealnumber=(self.item1*16.5)+ (self.item2*12.5)+(self.item3*14.5)+(self.item4*16.5)+(self.item5*18.5)\
                             +(self.item6*22.5)+(self.item7*24.5)+(self.item8*16.5)+(self.item9*16.5)+(self.item10*12.5)+(self.item11*10)\
                             +(self.item12 * 13.5) + (self.item13 * 18.5) + (self.item14 * 15.5) + (self.item15 * 14.5) + (self.item16 * 17.5) \
                             + (self.item17 * 14.5) + (self.item18 * 16.5) + (self.item19 * 22.5) + ( self.item20 * 25.5) + (self.item21 * 18.5) \
                             + (self.item22 * 10)





            self.coffeenumbers = (self.item23 * 5) + (self.item24 * 5) + (self.item25 * 5) + (self.item26 * 5) + (self.item27 * 5) \
                               + (self.item28 * 5) + (self.item29 * 5) + (self.item30 * 5) + (self.item31* 5) + (self.item32 * 0.5) + (self.item33 * 1)



            self.drinksnumber = (self.item34 * 5.5) + (self.item35 * 5.5) + (self.item36 * 5.5) + (self.item37 * 5.5) + (self.item38 * 5.5) \
                                 + (self.item39 * 5.5) + (self.item40 * 8.5) + (self.item41 * 8.5) + (self.item42 * 8.5) + ( self.item43 * 8.5) + (self.item44 * 8.5)

            priceofmeal = priceofmeal + str(float(self.mealnumber))


            priceofcoffee = priceofcoffee + str(float(self.coffeenumbers))
            priceofdrinks=priceofdrinks+str(float(self.drinksnumber))


            self.var_costofmeal.set(priceofmeal+' AUD')


            self.var_costofcoffee.set(priceofcoffee + ' AUD')
            self.var_costofdrinks.set(priceofdrinks + ' AUD')


            subtotalitems=str(float(priceofmeal)+float(priceofcoffee)+ float(priceofdrinks))
            self.var_subtotal.set(subtotalitems+ ' AUD')


            self.var_tax.set('1.5 AUD')

            self.totalcost = float(subtotalitems) + 1.5
            self.var_totalcost.set(str(self.totalcost)+' AUD')


        #create check receipt
        def receipt():
            global priceofmeal,priceofcoffee,priceofdrinks,subtotalitems,date,billnumber

            self.textreceipt.delete(1.0,END)

            self.textreceipt.insert(END,'Receipt Ref: CAFE1'+billnumber+'\t\t'+date+'\n')
            self.textreceipt.insert(END,"---------------------------------------------------\n")
            self.textreceipt.insert(END,'Items:\t\t Cost of Items(AUD) \n')
            self.textreceipt.insert(END, "---------------------------------------------------\n")

            if self.entry_saf.get()!=0:
                self.textreceipt.insert(END, f'Smash Avo & Feta \t\t\t {int(self.entry_saf.get())*16.5}\n\n')

            if self.entry_ber.get()!=0:
                self.textreceipt.insert(END, f'Bacon & Egg roll \t\t\t {int(self.entry_ber.get())*12.5}\n\n')

            if self.entry_eot.get()!=0:
                self.textreceipt.insert(END, f'Egg on Toast \t\t\t {int(self.entry_eot.get())*14.5}\n\n')

            if self.entry_mo.get()!=0:
                self.textreceipt.insert(END, f'Mad Omelet \t\t\t {int(self.entry_mo.get())*16.5}\n\n')

            if self.entry_eb.get()!=0:
                self.textreceipt.insert(END, f'Egg Benny \t\t\t {int(self.entry_eb.get())*18.5}\n\n')

            if self.entry_bmc.get()!=0:
                self.textreceipt.insert(END, f'Big Mad Cow \t\t\t {int(self.entry_bmc.get())*22.5}\n\n')
            if self.entry_tmc.get()!=0:
                self.textreceipt.insert(END, f'Turkish Mad Cow \t\t\t {int(self.entry_tmc.get())*24.5}\n\n')

            if self.entry_mn.get()!=0:
                self.textreceipt.insert(END, f'Menemen \t\t\t {int(self.entry_mn.get())*16.5}\n\n')
            if self.entry_tt1.get()!=0:
                self.textreceipt.insert(END, f'Turkish Toast \t\t\t {int(self.entry_tt1.get())*12.5}\n\n')
            if self.entry_ets.get()!=0:
                self.textreceipt.insert(END, f'Egg Turkish Sucuk \t\t\t {int(self.entry_ets.get())*16.5}\n\n')

            if self.entry_t1.get()!=0:
                self.textreceipt.insert(END, f'Toastie \t\t\t {int(self.entry_t1.get())*10}\n\n')


            if self.entry_kebab.get()!=0:
                self.textreceipt.insert(END, f'Kebab \t\t\t {int(self.entry_kebab.get())*13.5}\n\n')
            if self.entry_calamari.get()!=0:
                self.textreceipt.insert(END, f'Calamari \t\t\t {int(self.entry_calamari.get())*18.5}\n\n')
            if self.entry_snackbox.get()!=0:
                self.textreceipt.insert(END, f'Snack Box \t\t\t {int(self.entry_snackbox.get())*15.5}\n\n')

            if self.entry_bc.get()!=0:
                self.textreceipt.insert(END, f'Burger & Chips \t\t\t {int(self.entry_bc.get())*14.5}\n\n')
            if self.entry_clubsandwich.get()!=0:
                self.textreceipt.insert(END, f'Club Sandwich \t\t\t {int(self.entry_clubsandwich.get())*17.5}\n\n')
            if self.entry_chichkensandwich.get()!=0:
                self.textreceipt.insert(END, f'Chichken Sandwich \t\t\t {int(self.entry_chichkensandwich.get())*14.5}\n\n')

            if self.entry_salmonsandwich.get()!=0:
                self.textreceipt.insert(END, f'Salmon Sandwich \t\t\t {int(self.entry_salmonsandwich.get())*10}\n\n')
            if self.entry_sg.get()!=0:
                self.textreceipt.insert(END, f'Skewers Grill \t\t\t {int(self.entry_sg.get())*22.5}\n\n')
            if self.entry_smg.get()!=0:
                self.textreceipt.insert(END, f'Skewers Mix Grill \t\t\t {int(self.entry_smg.get())*25.5}\n\n')
            if self.entry_fc.get()!=0:
                self.textreceipt.insert(END, f'Fish & Chips \t\t\t {int(self.entry_fc.get())*18.5}\n\n')
            if self.entry_hd.get()!=0:
                self.textreceipt.insert(END, f'Hot Dog \t\t\t {int(self.entry_hd.get())*10}\n\n')


            if self.entry_espresso.get()!=0:
                self.textreceipt.insert(END, f'Espresso \t\t\t {int(self.entry_espresso.get())*5}\n\n')
            if self.entry_flatwhite.get()!=0:
                self.textreceipt.insert(END, f'Flat White \t\t\t {int(self.entry_flatwhite.get())*5}\n\n')
            if self.entry_cappuccino.get()!=0:
                self.textreceipt.insert(END, f'Cappuccino \t\t\t {int(self.entry_cappuccino.get())*5}\n\n')
            if self.entry_longblack.get()!=0:
                self.textreceipt.insert(END, f'Long Black \t\t\t {int(self.entry_longblack.get())*5}\n\n')
            if self.entry_latte.get()!=0:
                self.textreceipt.insert(END, f'Latte \t\t\t {int(self.entry_latte.get())*5}\n\n')
            if self.entry_hotchoco.get()!=0:
                self.textreceipt.insert(END, f'Hot Chocolate \t\t\t {int(self.entry_hotchoco.get())*5}\n\n')
            if self.entry_macchiato.get()!=0:
                self.textreceipt.insert(END, f'Macchiato \t\t\t {int(self.entry_macchiato.get())*5}\n\n')
            if self.entry_piccolo.get()!=0:
                self.textreceipt.insert(END, f'Piccolo \t\t\t {int(self.entry_piccolo.get())*5}\n\n')
            if self.entry_affogato.get()!=0:
                self.textreceipt.insert(END, f'Affogato \t\t\t {int(self.entry_affogato.get())*5}\n\n')
            if self.entry_mediumsize.get()!=0:
                self.textreceipt.insert(END, f'Medium Size \t\t\t {int(self.entry_mediumsize.get())*0.5}\n\n')
            if self.entry_largesize.get()!=0:
                self.textreceipt.insert(END, f'Large Size \t\t\t {int(self.entry_largesize.get())* 1}\n\n')

            if self.entry_peppermint.get()!=0:
                self.textreceipt.insert(END, f'Peppermint \t\t\t {int(self.entry_peppermint.get())*5.5}\n\n')
            if self.entry_earl_grey.get()!=0:
                self.textreceipt.insert(END, f'Earl Grey \t\t\t {int(self.entry_earl_grey.get())*5.5}\n\n')
            if self.entry_engbreak.get()!=0:
                self.textreceipt.insert(END, f'English Breakfast \t\t\t {int(self.entry_engbreak.get())*5.5}\n\n')
            if self.entry_chamomile.get()!=0:
                self.textreceipt.insert(END, f'Chamomile \t\t\t {int(self.entry_chamomile.get())*5.5}\n\n')
            if self.entry_turkishtea.get()!=0:
                self.textreceipt.insert(END, f'Turkish Tea \t\t\t {int(self.entry_turkishtea.get())*5.5}\n\n')
            if self.entry_chailatte.get()!=0:
                self.textreceipt.insert(END, f'Chailatte \t\t\t {int(self.entry_chailatte.get())*5.5}\n\n')

            if self.entry_pineapple.get()!=0:
                self.textreceipt.insert(END, f'Pineapple \t\t\t {int(self.entry_pineapple.get())*8.5}\n\n')
            if self.entry_watermelon.get()!=0:
                self.textreceipt.insert(END, f'Watermelon \t\t\t {int(self.entry_watermelon.get())*8.5}\n\n')
            if self.entry_orange.get()!=0:
                self.textreceipt.insert(END, f'Orange \t\t\t {int(self.entry_orange.get())*8.5}\n\n')
            if self.entry_cucumber.get()!=0:
                self.textreceipt.insert(END, f'Cucumber \t\t\t {int(self.entry_cucumber.get())*8.5}\n\n')
            if self.entry_greenapple.get()!=0:
                self.textreceipt.insert(END, f'Green Apple\t\t\t {int(self.entry_greenapple.get())*8.5}\n\n')
            if self.entry_celery.get()!=0:
                self.textreceipt.insert(END, f'Celery \t\t\t {int(self.entry_celery.get())*8.5}\n\n')


            self.textreceipt.insert(END, "---------------------------------------------------\n")

            self.textreceipt.insert(END, f'Cost of Meal \t {priceofmeal} AUD  \n \n')


            self.textreceipt.insert(END, f'Cost of Coffee \t {priceofcoffee} AUD \n \n')


            self.textreceipt.insert(END, f'Cost of Drinks \t {priceofdrinks} AUD  \n \n')
            self.textreceipt.insert(END, f'Sub Total \t {subtotalitems} AUD  \n \n')
            self.textreceipt.insert(END, f'Tax \t {1.5} AUD  \n \n')
            self.textreceipt.insert(END, f'Total Cost \t {float(subtotalitems)+1.5} AUD \n \n')

       #create receipt save function
        def save():
            if self.textreceipt.get(1.0,END)=="\n":
                pass
            else:
                url= filedialog.asksaveasfile(mode='w',defaultextension='.txt')

                receipt_data=self.textreceipt.get(1.0,END)
                url.write(receipt_data)
                url.close()
                messagebox.showinfo("Information",'Your receipt has been saved')
        
        #create reset all entry function
        def reset():
            global priceofmeal,priceofcoffee,priceofdrinks,subtotalitems
            self.textreceipt.delete(1.0,END)
            self.entry_saf.set('0')
            self.entry_ber.set('0')
            self.entry_eot.set('0')
            self.entry_mo.set('0')
            self.entry_eb.set('0')
            self.entry_bmc.set('0')
            self.entry_tmc.set('0')
            self.entry_mn.set('0')
            self.entry_ets.set('0')
            self.entry_tt1.set('0')
            self.entry_t1.set('0')

            self.entry_kebab.set('0')
            self.entry_calamari.set('0')
            self.entry_snackbox.set('0')
            self.entry_bc.set('0')
            self.entry_clubsandwich.set('0')
            self.entry_chichkensandwich.set('0')
            self.entry_salmonsandwich.set('0')
            self.entry_sg.set('0')
            self.entry_smg.set('0')
            self.entry_fc.set('0')

            self.entry_hd.set('0')

            self.entry_espresso.set('0')
            self.entry_flatwhite.set('0')
            self.entry_cappuccino.set('0')
            self.entry_longblack.set('0')
            self.entry_latte.set('0')
            self.entry_hotchoco.set('0')
            self.entry_macchiato.set('0')
            self.entry_piccolo.set('0')
            self.entry_affogato.set('0')

            self.entry_mediumsize.set('0')
            self.entry_largesize.set('0')

            self.entry_peppermint.set('0')
            self.entry_earl_grey.set('0')
            self.entry_engbreak.set('0')
            self.entry_chamomile.set('0')
            self.entry_turkishtea.set('0')
            self.entry_chailatte.set('0')
            self.entry_pineapple.set('0')
            self.entry_watermelon.set('0')
            self.entry_orange.set('0')
            self.entry_cucumber.set('0')
            self.entry_greenapple.set('0')
            self.entry_celery.set('0')


            self.textsaf.config(state=DISABLED)
            self.textber.config(state=DISABLED)
            self.texteot.config(state=DISABLED)
            self.textmo.config(state=DISABLED)
            self.texteb.config(state=DISABLED)
            self.textbmc.config(state=DISABLED)
            self.texttmc.config(state=DISABLED)
            self.textmn.config(state=DISABLED)
            self.textets.config(state=DISABLED)
            self.texttt1.config(state=DISABLED)
            self.textt1.config(state=DISABLED)
            self.textkebab.config(state=DISABLED)
            self.textcalamari.config(state=DISABLED)
            self.textsnackbox.config(state=DISABLED)
            self.textbc.config(state=DISABLED)
            self.textclubsandwich.config(state=DISABLED)
            self.textchichkensandwich.config(state=DISABLED)
            self.textsalmonsandwich.config(state=DISABLED)
            self.textsg.config(state=DISABLED)
            self.textsmg.config(state=DISABLED)
            self.textfc.config(state=DISABLED)
            self.texthd.config(state=DISABLED)

            self.textespresso.config(state=DISABLED)
            self.textflatwhite.config(state=DISABLED)
            self.textcappuccino.config(state=DISABLED)
            self.textlongblack.config(state=DISABLED)
            self.textlatte.config(state=DISABLED)
            self.texthotchoco.config(state=DISABLED)
            self.textmacchiato.config(state=DISABLED)
            self.textpiccolo.config(state=DISABLED)
            self.textaffogato.config(state=DISABLED)
            self.textmediumsize.config(state=DISABLED)
            self.textlargesize.config(state=DISABLED)

            self.textpeppermint.config(state=DISABLED)

            self.textearl_grey.config(state=DISABLED)
            self.textengbreak.config(state=DISABLED)
            self.textchamomile.config(state=DISABLED)
            self.textturkishtea.config(state=DISABLED)
            self.textchailatte.config(state=DISABLED)
            self.textpineapple.config(state=DISABLED)
            self.textwatermelon.config(state=DISABLED)
            self.textorange.config(state=DISABLED)
            self.textcucumber.config(state=DISABLED)
            self.textgreenapple.config(state=DISABLED)
            self.textcelery.config(state=DISABLED)

            self.var_costofmeal.set('')
            self.var_costofcoffee.set('')
            self.var_costofdrinks.set('')
            self.var_subtotal.set('')
            self.var_tax.set('')
            self.var_totalcost.set('')

            priceofmeal=''
            priceofcoffee=''
            priceofdrinks=''
            subtotalitems=''



            self.var1.set(0)
            self.var2.set(0)
            self.var3.set(0)
            self.var4.set(0)
            self.var5.set(0)
            self.var6.set(0)
            self.var7.set(0)
            self.var8.set(0)
            self.var9.set(0)
            self.var10.set(0)
            self.var11.set(0)
            self.var12.set(0)
            self.var13.set(0)
            self.var14.set(0)
            self.var15.set(0)
            self.var16.set(0)
            self.var17.set(0)
            self.var18.set(0)
            self.var19.set(0)
            self.var20.set(0)
            self.var21.set(0)
            self.var22.set(0)
            self.var23.set(0)
            self.var24.set(0)
            self.var25.set(0)
            self.var26.set(0)
            self.var27.set(0)
            self.var28.set(0)
            self.var29.set(0)
            self.var30.set(0)
            self.var31.set(0)
            self.var32.set(0)
            self.var33.set(0)
            self.var34.set(0)
            self.var35.set(0)
            self.var36.set(0)
            self.var37.set(0)
            self.var38.set(0)
            self.var39.set(0)
            self.var40.set(0)
            self.var41.set(0)
            self.var42.set(0)
            self.var43.set(0)
            self.var44.set(0)
            self.var45.set(0)

        #create receipt send function
       
        def send():
            self.root2=Toplevel()

            self.root2.title('Send Bill')

            self.root2.config(bg="#F6D7B8")
            self.root2.geometry('490x630+50+50')

            self.numberlbel=Label(self.root2, text="Mobile Number",font=('Britannic Bold', 16, 'bold'),bg='#F6D7B8',fg="#7D2509")
            self.numberlbel.pack(pady=5)

            self.numberentry=Entry(self.root2,font=('Britannic Bold', 20, 'bold'),bd=3,width=20)
            self.numberentry.pack(pady=5)

            self.receiptinfo=Label(self.root2,text="Receipt Info",font=('Britannic Bold', 16, 'bold'),bg='#F6D7B8',fg="#7D2509")
            self.receiptinfo.pack(pady=5)

            self.textreceiptinfo=Text(self.root2,font=('Britannic Bold', 20, 'bold'),bd=3,width=30,height=15)
            self.textreceiptinfo.pack(pady=5)


            self.sendbutton=Button(self.root2,text='Send', font=('Britannic Bold', 20, 'bold'),relief=RAISED, fg='#7D2509', bg='#F6D7B8', bd=7)
            self.sendbutton.pack(pady=5)

            self.textreceiptinfo.insert(END,'Receipt Ref: CAFE1'+billnumber+'\t\t'+date+'\n')
            self.textreceiptinfo.insert(END, "---------------------------------------------\n")

            self.textreceiptinfo.insert(END, f'Cost of Meal \t\t {priceofmeal} AUD \n ')

            self.textreceiptinfo.insert(END, f'Cost of Coffee \t\t {priceofcoffee} AUD \n ')

            self.textreceiptinfo.insert(END, f'Cost of Drinks \t\t {priceofdrinks} AUD \n ')
            self.textreceiptinfo.insert(END, f'Sub Total \t\t {subtotalitems} AUD \n')
            self.textreceiptinfo.insert(END, f'Tax \t\t {1.5} AUD  \n \n')
            self.textreceiptinfo.insert(END, f'Total Cost \t\t {float(subtotalitems) + 1.5} AUD \n ')

            self.root2.mainloop()










            ##buttons for functions
        self.button_total = Button(self.button_frame, text='Total', font=('Britannic Bold', 16, 'bold'),
                                       fg='#7D2509', bg='#F6D7B8', bd=1,command=totalcost)
        self.button_total.grid(row=0, column=0)

        self.button_save = Button(self.button_frame, text='Save', font=('Britannic Bold', 16, 'bold'), fg='#7D2509',
                                      bg='#F6D7B8', bd=1,command=save)
        self.button_save.grid(row=0, column=1)

        self.button_send = Button(self.button_frame, text='Send', font=('Britannic Bold', 16, 'bold'), fg='#7D2509',
                                      bg='#F6D7B8', bd=1,command=send)
        self.button_send.grid(row=0, column=2)

        self.button_reset = Button(self.button_frame, text='Reset', font=('Britannic Bold', 16, 'bold'),
                                       fg='#7D2509',
                                       bg='#F6D7B8', bd=1,command=reset)
        self.button_reset.grid(row=0, column=3)

        self.button_receipt = Button(self.button_frame, text='Receipt', font=('Britannic Bold', 16, 'bold'),
                                         fg='#7D2509',
                                         bg='#F6D7B8', bd=1, width=4,command=receipt)
        self.button_receipt.grid(row=0, column=4)



        

class Login_Screen:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN SYSTEM")
        self.root.geometry("1300x650+20+20")
        self.root.resizable(False, False)

        ########## Backgroung image on Login Screen Window ###########
        self.background=ImageTk.PhotoImage(file="4K-Coffee-Grain-Photo.png")
        self.background_image=Label(self.root,image=self.background).place(x=0,y=0,relwidth=1,relheight=1)

        ########## Creating the Login Screen Frame ###################
        self.login_rame = Frame(self.root, bg="#F6ECEA", )
        self.login_rame.place(x=70, y=120, width=400, height=320)
        

        ########## Creating Labels and Entry Box on Login Frame ######
        self.screen_label = Label(self.login_rame, text="Login Here", font=("Britannic Bold", 40, "bold"),
                                  fg="#7D2509").place(x=65, y=14)
        self.sub_label = Label(self.login_rame, text="Cafe Order System", font=("Britannic Bold", 15),
                               fg="#7D2509").place(x=90, y=75)

        self.userid_label = Label(self.login_rame, text="User ID", font=("Verdana Pro Black", 14, "bold"),
                                  fg="#000000").place(x=80, y=125)
        self.user_entry = Entry(self.login_rame, font=("Calibri", 14, "bold"), bg="lightgray")
        self.user_entry.place(x=80, y=150, width=250, height=35)

        self.password_label = Label(self.login_rame, text="Password", font=("Verdana Pro Black", 14, "bold"),
                                    fg="#000000").place(x=80, y=195)
        self.password_entry = Entry(self.login_rame, show="*", font=("Calibri", 14, "bold"), bg="#C0C0C0")
        self.password_entry.place(x=80, y=220, width=250, height=35)

        self.forget_button = Button(self.login_rame, text="Forget Password?", cursor="hand2", bd=0,
                                    font=("times new roman", 10, 'bold'), fg="#7D2509").place(x=80, y=260)
        self.Login_button = Button(self.root, command=self.login_function, cursor="hand2", text="Login", fg="#FFFFFF",
                                   bg="#7D2509", font=("times new roman", 15))
        self.Login_button.place(x=175, y=420, width=180, height=40)

    def login_function(self):
        if self.password_entry.get() == "" or self.user_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        elif self.password_entry.get() != "1234567" or self.user_entry.get() != "George":
            messagebox.showerror("Error", "Invalid Username/Password", parent=self.root)

        else:
            OrderScreen(root)
            self.login_rame.destroy()
            self.Login_button.destroy()
            # messagebox.showinfo("Welcome", f"Welcome {self.user_entry.get()}\nYour Password: {self.password_entry.get()}", parent=self.root)


root = Tk()
obj = Login_Screen(root)  # calling function


 


root.mainloop()