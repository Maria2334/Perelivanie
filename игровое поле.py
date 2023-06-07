import random
import itertools
from tkinter import *
from tkinter import messagebox
from tkinter import Tk

def on_closing():
    if messagebox.askokcancel('Выход из игры','Выйти из игры?'):
        tk.destroy()
    

tk=Tk()
tk.protocol('WM_DELETE_WINDOW', on_closing)
tk.title('Game')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)

canvas=Canvas(tk, width=550, height=600, bg='CadetBlue1', highlightthickness=0)
canvas.pack()

canvas.create_text(270,120,text='TRANSFUSION', font=('Courier',28,'italic'))

def start_window_1():
    new_window_1=Toplevel(tk)
    new_window_1.title('Game')
    new_window_1.resizable(0,0)
    new_window_1.wm_attributes('-topmost',1)
    canvas_1=Canvas(new_window_1, width=700, height=600, bg='CadetBlue1', highlightthickness=0)
    canvas_1.pack()
    canvas_1.create_text(340,50,text='1 УРОВЕНЬ',font=('Courier',20,'italic'))
    canvas_1.create_rectangle(49,120,102,300)
    canvas_1.create_rectangle(129,120,182,300)
    canvas_1.create_rectangle(209,120,262,300)

    def get_color_0():
        button_0.config(bg='CadetBlue1')
        button_3.config(state="disabled")
        buttons_0.config(state="normal")
        button_0.config(state="disabled")
            

    def get_colors_0():
        buttons_2.config(bg=color1)
        buttons_0.config(state="disabled")
        button_3.config(state="normal")

    def get_color_1():
        button_3.config(bg='CadetBlue1')
        button_0.config(state="disabled")
        buttons_0.config(state="normal")
        button_3.config(state="disabled")

    def get_colors_1():
        buttons_1.config(bg=color1)
        buttons_0.config(state="disabled")
        button_4.config(state="normal")

    def get_color_2():
        button_4.config(bg='CadetBlue1')
        button_4.config(state="disabled")
        button_0.config(state="normal")

    def get_colors_2():
        button_0.config(bg=color2)
        button_0.config(state="disabled")
        button_5.config(state="normal")

    def get_color_3():
        button_5.config(bg='CadetBlue1')
        button_5.config(state="disabled")
        buttons_0.config(state="normal")

    def get_colors_3():
        buttons_0.config(bg=color1)
        but_0=Button(new_window_1,text='Продолжить',width=50, height=5,bg='azure1',command=start_window_3)
        but_1=Button(new_window_1,text='Выйти',width=50, height=5,bg='azure1',command=next_window)
        but_0.place(x=150,y=350)
        but_1.place(x=150,y=450)

    
    def next_window():
        new_window_1.withdraw()
    
    cycled_commands_0=itertools.cycle([get_colors_0,get_colors_1,get_colors_3])

    def on_click_0():
        command=next(cycled_commands_0)
        return command()

    cycled_commands_1=itertools.cycle([get_color_0,get_colors_2])

    def on_click_1():
        command=next(cycled_commands_1)
        return command()

    
    buttons_0=Button(new_window_1,width=6,height=3,bg='CadetBlue1',state="disabled",command=on_click_0)
    buttons_0.place(x=210,y=135)
    buttons_1=Button(new_window_1,width=6,height=3,bg='CadetBlue1',state="disabled")
    buttons_1.place(x=210,y=190)
    buttons_2=Button(new_window_1,width=6,height=3,bg='CadetBlue1',state="disabled")
    buttons_2.place(x=210,y=245)

  

    COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]
    random.shuffle(COLORS)
    color1, color2, color3, color4, color5, color6 = COLORS

    button_0 = Button(new_window_1,width=6,height=3,bg=color1, command=on_click_1)
    button_0.place(x=50,y=135)
    button_1 = Button(new_window_1,width=6,height=3,bg=color2, state="disabled")
    button_1.place(x=50,y=190)
    button_2 = Button(new_window_1,width=6,height=3,bg=color2,state="disabled")
    button_2.place(x=50,y=245)
    button_3 = Button(new_window_1,width=6,height=3,bg=color1,state="disabled",command=get_color_1)
    button_3.place(x=130,y=135)
    button_4 = Button(new_window_1,width=6,height=3,bg=color2,state="disabled",command=get_color_2)
    button_4.place(x=130,y=190)
    button_5 = Button(new_window_1,width=6,height=3,bg=color1,state="disabled",command=get_color_3)
    button_5.place(x=130,y=245)
    


    def start_window_3():
        new_window_1.withdraw()
        new_window_3=Toplevel(tk)
        new_window_3.title('Game')
        new_window_3.resizable(0,0)
        new_window_3.wm_attributes('-topmost',1)
        canvas_3=Canvas(new_window_3, width=700, height=600, bg='CadetBlue1', highlightthickness=0)
        canvas_3.pack()
        canvas_3.create_text(340,50,text='2 УРОВЕНЬ',font=('Courier',20,'italic'))
        canvas_3.create_rectangle(49,120,102,300)
        canvas_3.create_rectangle(129,120,182,300)
        canvas_3.create_rectangle(209,120,262,300)
        canvas_3.create_rectangle(289,120,342,300)

        def g_c_0():
            b_0.config(bg='CadetBlue1')
            b_0.config(state="disabled")
            bs_0.config(state="normal")


        def g_c_1():
            b_6.config(bg='CadetBlue1')
            b_6.config(state="disabled")
            bs_0.config(state="normal")

        def g_c_2():
            b_3.config(bg='CadetBlue1')
            b_3.config(state="disabled")
            b_6.config(state="normal")

        def g_c_3():
            b_1.config(bg='CadetBlue1')
            b_1.config(state="disabled")
            b_3.config(state="normal")

        def g_c_4():
            b_6.config(bg='CadetBlue1')
            b_7.config(bg='CadetBlue1')
            b_6.config(state="disabled")
            b_0.config(state="normal")

        def g_c_5():
            b_3.config(bg='CadetBlue1')
            b_4.config(bg='CadetBlue1')
            b_3.config(state="disabled")
            b_6.config(state="normal")

        def g_c_6():
            b_5.config(bg='CadetBlue1')
            b_5.config(state="disabled")
            bs_0.config(state="normal")

        def g_cs_0():
            bs_2.config(bg=color1)
            bs_0.config(state="disabled")
            b_6.config(state="normal")

        def g_cs_1():
            bs_1.config(bg=color1)
            bs_0.config(state="disabled")
            b_3.config(state="normal")

        def g_cs_3():
            b_6.config(bg=color3)
            b_6.config(state="disabled")
            b_1.config(state="normal")

        def g_cs_4():
            b_3.config(bg=color2)
            b_3.config(state="disabled")
            b_6.config(state="normal")

        def g_cs_5():
            b_1.config(bg=color3)
            b_0.config(bg=color3)
            b_0.config(state="disabled")
            b_3.config(state="normal")

        def g_cs_6():
            b_6.config(bg=color2)
            b_7.config(bg=color2)
            b_6.config(state="disabled")
            b_5.config(state="normal")

        def g_cs_2():
            bs_0.config(bg=color1)
            bt_0=Button(new_window_3,text='Продолжить',width=50, height=5,bg='azure1',command=start_window_4)
            bt_1=Button(new_window_3,text='Выйти',width=50, height=5,bg='azure1',command=next_window_1)
            bt_0.place(x=150,y=350)
            bt_1.place(x=150,y=450)


        def next_window_1():
            new_window_3.withdraw()

        c_commands_0=itertools.cycle([g_cs_0,g_cs_1,g_cs_2])

        def on_c_0():
            command=next(c_commands_0)
            return command()

        c_commands_1=itertools.cycle([g_c_1,g_cs_3,g_c_4,g_cs_6])

    
        def on_c_1():
            command=next(c_commands_1)
            return command()

        c_commands_2=itertools.cycle([g_c_2,g_cs_4,g_c_5])

    
        def on_c_2():
            command=next(c_commands_2)
            return command()

        c_commands_3=itertools.cycle([g_c_0,g_cs_5])

    
        def on_c_3():
            command=next(c_commands_3)
            return command()


        bs_0=Button(new_window_3,width=6,height=3,bg='CadetBlue1',state="disabled",command=on_c_0)
        bs_0.place(x=290,y=135)
        bs_1=Button(new_window_3,width=6,height=3,bg='CadetBlue1',state="disabled")
        bs_1.place(x=290,y=190)
        bs_2=Button(new_window_3,width=6,height=3,bg='CadetBlue1',state="disabled")
        bs_2.place(x=290,y=245)


        b_0 = Button(new_window_3,width=6,height=3,bg=color1,command=on_c_3)
        b_0.place(x=50,y=135)
        b_1 = Button(new_window_3,width=6,height=3,bg=color2,state="disabled",command=g_c_3)
        b_1.place(x=50,y=190)
        b_2 = Button(new_window_3,width=6,height=3,bg=color3,state="disabled")
        b_2.place(x=50,y=245)
        b_3 = Button(new_window_3,width=6,height=3,bg=color3,state="disabled",command=on_c_2)
        b_3.place(x=130,y=135)
        b_4 = Button(new_window_3,width=6,height=3,bg=color2,state="disabled")
        b_4.place(x=130,y=190)
        b_5 = Button(new_window_3,width=6,height=3,bg=color1,state="disabled",command=g_c_6)
        b_5.place(x=130,y=245)
        b_6 = Button(new_window_3,width=6,height=3,bg=color1,state="disabled",command=on_c_1)
        b_6.place(x=210,y=135)
        b_7 = Button(new_window_3,width=6,height=3,bg=color3,state="disabled")
        b_7.place(x=210,y=190)
        b_8 = Button(new_window_3,width=6,height=3,bg=color2,state="disabled")
        b_8.place(x=210,y=245)


            
        def start_window_4():
            new_window_3.withdraw()
            new_window_4=Toplevel(tk)
            new_window_4.title('Game')
            new_window_4.resizable(0,0)
            new_window_4.wm_attributes('-topmost',1)
            canvas_4=Canvas(new_window_4, width=700, height=600, bg='CadetBlue1', highlightthickness=0)
            canvas_4.pack()
            canvas_4.create_text(340,50,text='3 УРОВЕНЬ',font=('Courier',20,'italic'))
            canvas_4.create_rectangle(49,120,102,300)
            canvas_4.create_rectangle(129,120,182,300)
            canvas_4.create_rectangle(209,120,262,300)
            canvas_4.create_rectangle(289,120,342,300)
            canvas_4.create_rectangle(369,120,422,300)

            
            def get_c_0():
                butt_0.config(bg='CadetBlue1')
                butt_0.config(state="disabled")
                buts_0.config(state="normal")

            def get_c_1():
                butt_9.config(bg='CadetBlue1')
                butt_9.config(state="disabled")
                buts_0.config(state="normal")

            def get_c_2():
                butt_3.config(bg='CadetBlue1')
                butt_3.config(state="disabled")
                butt_9.config(state="normal")

            def get_c_3():
                butt_4.config(bg='CadetBlue1')
                butt_4.config(state="disabled")
                butt_0.config(state="normal")

            def get_c_4():
                butt_5.config(bg='CadetBlue1')
                butt_5.config(state="disabled")
                buts_0.config(state="normal")


            def get_c_5():
                butt_9.config(bg='CadetBlue1')
                butt_10.config(bg='CadetBlue1')
                butt_9.config(state="disabled")
                butt_3.config(state="normal")

            def get_c_6():
                butt_6.config(bg='CadetBlue1')
                butt_6.config(state="disabled")
                butt_9.config(state="normal")

            def get_c_7():
                butt_7.config(bg='CadetBlue1')
                butt_7.config(state="disabled")
                butt_3.config(state="normal")

            def get_c_8():
                butt_0.config(bg='CadetBlue1')
                butt_1.config(bg='CadetBlue1')
                butt_0.config(state="disabled")
                butt_6.config(state="normal")


            def get_c_9():
                butt_2.config(bg='CadetBlue1')
                butt_2.config(state="disabled")
                butt_9.config(state="normal")




            def get_cs_0():
                buts_2.config(bg=color1)
                buts_0.config(state="disabled")
                butt_9.config(state="normal")

            def get_cs_1():
                buts_1.config(bg=color1)
                buts_0.config(state="disabled")
                butt_3.config(state="normal")

            def get_cs_2():
                butt_9.config(bg=color3)
                butt_9.config(state="disabled")
                butt_4.config(state="normal")

            def get_cs_3():
                butt_0.config(bg=color2)
                butt_0.config(state="disabled")
                butt_5.config(state="normal")

            def get_cs_4():
                butt_5.config(bg=color3)
                butt_4.config(bg=color3)
                butt_3.config(state="disabled")
                butt_6.config(state="normal")

            def get_cs_5():
                buts_0.config(bg=color1)
                buts_0.config(state="disabled")
                butt_9.config(state="normal")

            def get_cs_6():
                butt_10.config(bg=color4)
                butt_9.config(state="disabled")
                butt_7.config(state="normal")

            def get_cs_7():
                butt_3.config(bg=color3)
                butt_3.config(state="disabled")
                butt_0.config(state="normal")

            def get_cs_8():
                butt_7.config(bg=color2)
                butt_6.config(bg=color2)
                butt_6.config(state="disabled")
                butt_2.config(state="normal")

            def get_cs_9():
                butt_9.config(bg=color4)
                bu_0=Button(new_window_4,text='Продолжить',width=50, height=5,bg='azure1',command=start_window_5)
                bu_1=Button(new_window_4,text='Выйти',width=50, height=5,bg='azure1',command=next_window_2)
                bu_0.place(x=150,y=350)
                bu_1.place(x=150,y=450)


            def next_window_2():
                new_window_4.withdraw()


            cd_commands_0=itertools.cycle([get_cs_0,get_cs_1,get_cs_5])

            def o_click_0():
                command=next(cd_commands_0)
                return command()

            cd_commands_1=itertools.cycle([get_c_1,get_cs_2,get_c_5,get_cs_6,get_cs_9])

            def o_click_1():
                command=next(cd_commands_1)
                return command()

            cd_commands_2=itertools.cycle([get_c_2,get_cs_4,get_cs_7])

            def o_click_2():
                command=next(cd_commands_2)
                return command()

            cd_commands_3=itertools.cycle([get_c_0,get_cs_3,get_c_8])

            def o_click_3():
                command=next(cd_commands_3)
                return command()

            cd_commands_4=itertools.cycle([get_c_6,get_cs_8])

            def o_click_4():
                command=next(cd_commands_4)
                return command()

                
            buts_0=Button(new_window_4,width=6,height=3,bg='CadetBlue1',state="disabled",command=o_click_0)
            buts_0.place(x=370,y=135)
            buts_1=Button(new_window_4,width=6,height=3,bg='CadetBlue1',state="disabled")
            buts_1.place(x=370,y=190)
            buts_2=Button(new_window_4,width=6,height=3,bg='CadetBlue1',state="disabled")
            buts_2.place(x=370,y=245)


            butt_0 = Button(new_window_4,width=6,height=3,bg=color1,command=o_click_3)
            butt_0.place(x=50,y=135)
            butt_1 = Button(new_window_4,width=6,height=3,bg=color2,state="disabled")
            butt_1.place(x=50,y=190)
            butt_2 = Button(new_window_4,width=6,height=3,bg=color4,state="disabled",command=get_c_9)
            butt_2.place(x=50,y=245)
            butt_3 = Button(new_window_4,width=6,height=3,bg=color3,state="disabled",command=o_click_2)
            butt_3.place(x=130,y=135)
            butt_4 = Button(new_window_4,width=6,height=3,bg=color2,state="disabled",command=get_c_3)
            butt_4.place(x=130,y=190)
            butt_5 = Button(new_window_4,width=6,height=3,bg=color1,state="disabled",command=get_c_4)
            butt_5.place(x=130,y=245)
            butt_6 = Button(new_window_4,width=6,height=3,bg=color4,state="disabled",command=o_click_4)
            butt_6.place(x=210,y=135)
            butt_7 = Button(new_window_4,width=6,height=3,bg=color3,state="disabled",command=get_c_7)
            butt_7.place(x=210,y=190)
            butt_8 = Button(new_window_4,width=6,height=3,bg=color2,state="disabled")
            butt_8.place(x=210,y=245)
            butt_9 = Button(new_window_4,width=6,height=3,bg=color1,state="disabled",command=o_click_1)
            butt_9.place(x=290,y=135)
            butt_10 = Button(new_window_4,width=6,height=3,bg=color3,state="disabled")
            butt_10.place(x=290,y=190)
            butt_11 = Button(new_window_4,width=6,height=3,bg=color4,state="disabled")
            butt_11.place(x=290,y=245) 


            def start_window_5():
                new_window_4.withdraw()
                new_window_5=Toplevel(tk)
                new_window_5.title('Game')
                new_window_5.resizable(0,0)
                new_window_5.wm_attributes('-topmost',1)
                canvas_5=Canvas(new_window_5, width=700, height=600, bg='CadetBlue1', highlightthickness=0)
                canvas_5.pack()
                canvas_5.create_text(340,50,text='4 УРОВЕНЬ',font=('Courier',20,'italic'))
                canvas_5.create_rectangle(49,120,102,300)
                canvas_5.create_rectangle(129,120,182,300)
                canvas_5.create_rectangle(209,120,262,300)
                canvas_5.create_rectangle(289,120,342,300)
                canvas_5.create_rectangle(369,120,422,300)
                canvas_5.create_rectangle(449,120,502,300)


                def g_color_0():
                    buttn_0.config(bg='CadetBlue1')
                    buttn_0.config(state="disabled")
                    butts_0.config(state="normal")

                def g_color_1():
                    buttn_9.config(bg='CadetBlue1')
                    buttn_9.config(state="disabled")
                    butts_0.config(state="normal")

                def g_color_2():
                    buttn_3.config(bg='CadetBlue1')
                    buttn_3.config(state="disabled")
                    buttn_9.config(state="normal")

                def g_color_3():
                    buttn_12.config(bg='CadetBlue1')
                    buttn_12.config(state="disabled")
                    buttn_0.config(state="normal")

                def g_color_4():
                    buttn_4.config(bg='CadetBlue1')
                    buttn_4.config(state="disabled")
                    buttn_12.config(state="normal")

                def g_color_5():
                    buttn_5.config(bg='CadetBlue1')
                    buttn_5.config(state="disabled")
                    butts_0.config(state="normal")

                def g_color_6():
                    buttn_9.config(bg='CadetBlue1')
                    buttn_10.config(bg='CadetBlue1')
                    buttn_9.config(state="disabled")
                    buttn_3.config(state="normal")

                def g_color_7():
                    buttn_12.config(bg='CadetBlue1')
                    buttn_13.config(bg='CadetBlue1')
                    buttn_12.config(state="disabled")
                    buttn_9.config(state="normal")

                def g_color_8():
                    buttn_6.config(bg='CadetBlue1')
                    buttn_6.config(state="disabled")
                    buttn_12.config(state="normal")

                def g_color_9():
                    buttn_7.config(bg='CadetBlue1')
                    buttn_7.config(state="disabled")
                    buttn_3.config(state="normal")

                def g_color_10():
                    buttn_0.config(bg='CadetBlue1')
                    buttn_1.config(bg='CadetBlue1')
                    buttn_0.config(state="disabled")
                    buttn_6.config(state="normal")

                def g_color_11():
                    buttn_2.config(bg='CadetBlue1')
                    buttn_2.config(state="disabled")
                    buttn_12.config(state="normal")
        

                def g_colors_0():
                    butts_2.config(bg=color1)
                    butts_0.config(state="disabled")
                    buttn_9.config(state="normal")

                def g_colors_1():
                    butts_1.config(bg=color1)
                    butts_0.config(state="disabled")
                    buttn_3.config(state="normal")

                def g_colors_2():
                    buttn_9.config(bg=color3)
                    buttn_9.config(state="disabled")
                    buttn_12.config(state="normal")

                def g_colors_3():
                    buttn_0.config(bg=color2)
                    buttn_0.config(state="disabled")
                    buttn_4.config(state="normal")

                def g_colors_4():
                    buttn_12.config(bg=color5)
                    buttn_12.config(state="disabled")
                    buttn_5.config(state="normal")

                def g_colors_5():
                    butts_0.config(bg=color1)
                    butts_0.config(state="disabled")
                    buttn_9.config(state="normal")

                def g_colors_6():
                    buttn_5.config(bg=color3)
                    buttn_4.config(bg=color3)
                    buttn_3.config(state="disabled")
                    buttn_12.config(state="normal")

                def g_colors_7():
                    buttn_10.config(bg=color5)
                    buttn_9.config(bg=color5)
                    buttn_9.config(state="disabled")
                    buttn_6.config(state="normal")

                def g_colors_8():
                    buttn_13.config(bg=color4)
                    buttn_12.config(state="disabled")
                    buttn_7.config(state="normal")

                def g_colors_9():
                    buttn_3.config(bg=color3)
                    buttn_3.config(state="disabled")
                    buttn_0.config(state="normal")

                def g_colors_10():
                    buttn_7.config(bg=color2)
                    buttn_6.config(bg=color2)
                    buttn_6.config(state="disabled")
                    buttn_2.config(state="normal")

                def g_colors_11():
                    buttn_12.config(bg=color4)
                    b_0=Button(new_window_5,text='Продолжить',width=50, height=5,bg='azure1',command=start_window_6)
                    b_1=Button(new_window_5,text='Выйти',width=50, height=5,bg='azure1',command=next_window_4)
                    b_0.place(x=150,y=350)
                    b_1.place(x=150,y=450)

                def next_window_4():
                    new_window_5.withdraw()


                cycl_commands_0=itertools.cycle([g_colors_0,g_colors_1,g_colors_5])

                def click_0():
                    command=next(cycl_commands_0)
                    return command()

                cycl_commands_1=itertools.cycle([g_color_0,g_colors_3,g_color_10])

                def click_1():
                    command=next(cycl_commands_1)
                    return command()

                cycl_commands_2=itertools.cycle([g_color_1,g_colors_2,g_color_6,g_colors_7])

                def click_2():
                    command=next(cycl_commands_2)
                    return command()

                cycl_commands_3=itertools.cycle([g_color_3,g_colors_4,g_color_7,g_colors_8,g_colors_11])

                def click_3():
                    command=next(cycl_commands_3)
                    return command()

                cycl_commands_4=itertools.cycle([g_color_2,g_colors_6,g_colors_9])

                def click_4():
                    command=next(cycl_commands_4)
                    return command()

                cycl_commands_5=itertools.cycle([g_color_8,g_colors_10])

                def click_5():
                    command=next(cycl_commands_5)
                    return command()

    

                butts_0=Button(new_window_5,width=6,height=3,bg='CadetBlue1',state="disabled",command=click_0)
                butts_0.place(x=450,y=135)
                butts_1=Button(new_window_5,width=6,height=3,bg='CadetBlue1',state="disabled")
                butts_1.place(x=450,y=190)
                butts_2=Button(new_window_5,width=6,height=3,bg='CadetBlue1',state="disabled")
                butts_2.place(x=450,y=245)


                buttn_0 = Button(new_window_5,width=6,height=3,bg=color1,command=click_1)
                buttn_0.place(x=50,y=135)
                buttn_1 = Button(new_window_5,width=6,height=3,bg=color2,state="disabled")
                buttn_1.place(x=50,y=190)
                buttn_2 = Button(new_window_5,width=6,height=3,bg=color4,state="disabled",command=g_color_11)
                buttn_2.place(x=50,y=245)
                buttn_3 = Button(new_window_5,width=6,height=3,bg=color3,state="disabled",command=click_4)
                buttn_3.place(x=130,y=135)
                buttn_4 = Button(new_window_5,width=6,height=3,bg=color5,state="disabled",command=g_color_4)
                buttn_4.place(x=130,y=190)
                buttn_5 = Button(new_window_5,width=6,height=3,bg=color1,state="disabled",command=g_color_5)
                buttn_5.place(x=130,y=245)
                buttn_6 = Button(new_window_5,width=6,height=3,bg=color4,state="disabled",command=click_5)
                buttn_6.place(x=210,y=135)
                buttn_7 = Button(new_window_5,width=6,height=3,bg=color3,state="disabled",command=g_color_9)
                buttn_7.place(x=210,y=190)
                buttn_8 = Button(new_window_5,width=6,height=3,bg=color2,state="disabled")
                buttn_8.place(x=210,y=245)
                buttn_9 = Button(new_window_5,width=6,height=3,bg=color1,state="disabled",command=click_2)
                buttn_9.place(x=290,y=135)
                buttn_10 = Button(new_window_5,width=6,height=3,bg=color3,state="disabled")
                buttn_10.place(x=290,y=190)
                buttn_11 = Button(new_window_5,width=6,height=3,bg=color5,state="disabled")
                buttn_11.place(x=290,y=245)
                buttn_12 = Button(new_window_5,width=6,height=3,bg=color2,state="disabled",command=click_3)
                buttn_12.place(x=370,y=135)
                buttn_13 = Button(new_window_5,width=6,height=3,bg=color5,state="disabled")
                buttn_13.place(x=370,y=190)
                buttn_14 = Button(new_window_5,width=6,height=3,bg=color4,state="disabled")
                buttn_14.place(x=370,y=245)


                def start_window_6():
                    new_window_5.withdraw()
                    new_window_6=Toplevel(tk)
                    new_window_6.title('Game')
                    new_window_6.resizable(0,0)
                    new_window_6.wm_attributes('-topmost',1)
                    canvas_6=Canvas(new_window_6, width=700, height=600, bg='CadetBlue1', highlightthickness=0)
                    canvas_6.pack()
                    canvas_6.create_text(340,50,text='5 УРОВЕНЬ',font=('Courier',20,'italic'))
                    canvas_6.create_rectangle(49,120,102,300)
                    canvas_6.create_rectangle(129,120,182,300)
                    canvas_6.create_rectangle(209,120,262,300)
                    canvas_6.create_rectangle(289,120,342,300)
                    canvas_6.create_rectangle(369,120,422,300)
                    canvas_6.create_rectangle(449,120,502,300)
                    canvas_6.create_rectangle(529,120,582,300)
 
                    def color_0():
                        btn_3.config(bg='CadetBlue1')
                        btn_4.config(bg='CadetBlue1')
                        btn_3.config(state="disabled")
                        bts_0.config(state="normal")


                    def color_1():
                        btn_0.config(bg='CadetBlue1')
                        btn_0.config(state="disabled")
                        btn_3.config(state="normal")

                    def color_2():
                        btn_9.config(bg='CadetBlue1')
                        btn_9.config(state="disabled")
                        btn_3.config(state="normal")

                    def color_3():
                        btn_12.config(bg='CadetBlue1')
                        btn_12.config(state="disabled")
                        btn_9.config(state="normal")

                    def color_4():
                        btn_15.config(bg='CadetBlue1')
                        btn_15.config(state="disabled")
                        btn_0.config(state="normal")

                    def color_5():
                        btn_16.config(bg='CadetBlue1')
                        btn_16.config(state="disabled")
                        btn_12.config(state="normal")

                    def color_6():
                        btn_17.config(bg='CadetBlue1')
                        btn_17.config(state="disabled")
                        bts_0.config(state="normal")

                    def color_7():
                        btn_9.config(bg='CadetBlue1')
                        btn_10.config(bg='CadetBlue1')
                        btn_9.config(state="disabled")
                        btn_15.config(state="normal")

                    def color_8():
                        btn_12.config(bg='CadetBlue1')
                        btn_13.config(bg='CadetBlue1')
                        btn_12.config(state="disabled")
                        btn_9.config(state="normal")

                    def color_9():
                        btn_7.config(bg='CadetBlue1')
                        btn_7.config(state="disabled")
                        btn_15.config(state="normal")

                    def color_10():
                        btn_6.config(bg='CadetBlue1')
                        btn_6.config(state="disabled")
                        btn_12.config(state="normal")

                    def color_11():
                        btn_0.config(bg='CadetBlue1')
                        btn_1.config(bg='CadetBlue1')
                        btn_0.config(state="disabled")
                        btn_6.config(state="normal")

                    def color_12():
                        btn_2.config(bg='CadetBlue1')
                        btn_2.config(state="disabled")
                        btn_12.config(state="normal")




                    def colors_0():
                        bts_2.config(bg=color6)
                        bts_1.config(bg=color6)
                        bts_0.config(state="disabled")
                        btn_0.config(state="normal")



                    def colors_1():
                        btn_4.config(bg=color1)
                        btn_3.config(state="disabled")
                        btn_9.config(state="normal")

                    def colors_2():
                        btn_3.config(bg=color1)
                        btn_3.config(state="disabled")
                        btn_12.config(state="normal")

                    def colors_3():
                        btn_9.config(bg=color3)
                        btn_9.config(state="disabled")
                        btn_15.config(state="normal")

                    def colors_4():
                        btn_0.config(bg=color2)
                        btn_0.config(state="disabled")
                        btn_16.config(state="normal")

                    def colors_5():
                        btn_12.config(bg=color5)
                        btn_12.config(state="disabled")
                        btn_17.config(state="normal")

                    def colors_6():
                        bts_0.config(bg=color6)
                        bts_0.config(state="disabled")
                        btn_9.config(state="normal")

                    def colors_7():
                        btn_17.config(bg=color3)
                        btn_16.config(bg=color3)
                        btn_15.config(state="disabled")
                        btn_12.config(state="normal")

                    def colors_8():
                        btn_10.config(bg=color5)
                        btn_9.config(bg=color5)
                        btn_9.config(state="disabled")
                        btn_6.config(state="normal")

                    def colors_9():
                        btn_13.config(bg=color4)
                        btn_12.config(state="disabled")
                        btn_7.config(state="normal")

                    def colors_10():
                        btn_15.config(bg=color3)
                        btn_15.config(state="disabled")
                        btn_0.config(state="normal")

                    def colors_11():
                        btn_7.config(bg=color2)
                        btn_6.config(bg=color2)
                        btn_6.config(state="disabled")
                        btn_2.config(state="normal")

                    def colors_12():
                        btn_12.config(bg=color4)
                        b_1=Button(new_window_6,text='Выйти',width=50, height=5,bg='azure1',command=next_window_5)
                        b_1.place(x=150,y=350)

                    def next_window_5():
                        new_window_6.withdraw()



                    cled_commands_0=itertools.cycle([color_0,colors_1,colors_2])

                    def on_k_0():
                          command=next(cled_commands_0)
                          return command()

                    cled_commands_1=itertools.cycle([color_2,colors_3,color_7,colors_8])

                    def on_k_1():
                         command=next(cled_commands_1)
                         return command()

                    cled_commands_2=itertools.cycle([color_1,colors_4,color_11])

                    def on_k_2():
                         command=next(cled_commands_2)
                         return command()

                    cled_commands_3=itertools.cycle([color_3,colors_5,color_8,colors_9,colors_12])

                    def on_k_3():
                         command=next(cled_commands_3)
                         return command()

                    cled_commands_4=itertools.cycle([colors_0,colors_6])

                    def on_k_4():
                         command=next(cled_commands_4)
                         return command()

                    cled_commands_5=itertools.cycle([color_4,colors_7,colors_10])

                    def on_k_5():
                         command=next(cled_commands_5)
                         return command()

                    cled_commands_6=itertools.cycle([color_10,colors_11])

                    def on_k_6():
                         command=next(cled_commands_6)
                         return command()

                    bts_0=Button(new_window_6,width=6,height=3,bg='CadetBlue1',state="disabled",command=on_k_4)
                    bts_0.place(x=530,y=135)
                    bts_1=Button(new_window_6,width=6,height=3,bg='CadetBlue1',state="disabled")
                    bts_1.place(x=530,y=190)
                    bts_2=Button(new_window_6,width=6,height=3,bg='CadetBlue1',state="disabled")
                    bts_2.place(x=530,y=245)



                    btn_0 = Button(new_window_6,width=6,height=3,bg=color1,state="disabled",command=on_k_2)
                    btn_0.place(x=50,y=135)
                    btn_1 = Button(new_window_6,width=6,height=3,bg=color2,state="disabled")
                    btn_1.place(x=50,y=190)
                    btn_2 = Button(new_window_6,width=6,height=3,bg=color4,state="disabled",command=color_12)
                    btn_2.place(x=50,y=245)
                    btn_3 = Button(new_window_6,width=6,height=3,bg=color6,command=on_k_0)
                    btn_3.place(x=130,y=135)
                    btn_4 = Button(new_window_6,width=6,height=3,bg=color6,state="disabled")
                    btn_4.place(x=130,y=190)
                    btn_5 = Button(new_window_6,width=6,height=3,bg=color1,state="disabled")
                    btn_5.place(x=130,y=245)
                    btn_6 = Button(new_window_6,width=6,height=3,bg=color4,state="disabled",command=on_k_6)
                    btn_6.place(x=210,y=135)
                    btn_7 = Button(new_window_6,width=6,height=3,bg=color3,state="disabled",command=color_9)
                    btn_7.place(x=210,y=190)
                    btn_8 = Button(new_window_6,width=6,height=3,bg=color2,state="disabled")
                    btn_8.place(x=210,y=245)
                    btn_9 = Button(new_window_6,width=6,height=3,bg=color1,state="disabled",command=on_k_1)
                    btn_9.place(x=290,y=135)
                    btn_10 = Button(new_window_6,width=6,height=3,bg=color3,state="disabled")
                    btn_10.place(x=290,y=190)
                    btn_11 = Button(new_window_6,width=6,height=3,bg=color5,state="disabled")
                    btn_11.place(x=290,y=245)
                    btn_12 = Button(new_window_6,width=6,height=3,bg=color3,state="disabled",command=on_k_3)
                    btn_12.place(x=370,y=135)
                    btn_13 = Button(new_window_6,width=6,height=3,bg=color5,state="disabled")
                    btn_13.place(x=370,y=190)
                    btn_14 = Button(new_window_6,width=6,height=3,bg=color4,state="disabled")
                    btn_14.place(x=370,y=245)
                    btn_15 = Button(new_window_6,width=6,height=3,bg=color2,state="disabled",command=on_k_5)
                    btn_15.place(x=450,y=135)
                    btn_16 = Button(new_window_6,width=6,height=3,bg=color5,state="disabled",command=color_5)
                    btn_16.place(x=450,y=190)
                    btn_17 = Button(new_window_6,width=6,height=3,bg=color6,state="disabled",command=color_6)
                    btn_17.place(x=450,y=245) 




    
def start_window_2():
    new_window_2=Toplevel(tk)
    new_window_2.title('Правила игры')
    new_window_2.resizable(0,0)
    new_window_2.wm_attributes('-topmost',1)
    canvas_2=Canvas(new_window_2, width=550, height=600, bg='CadetBlue1', highlightthickness=0)
    canvas_2.pack()
    canvas_2.create_text(270,250,text='Перед вами расположены колбы,', font='Arial 12 normal roman', fill='black')
    canvas_2.create_text(270,270,text='в которых перемешаны жидкости разных цветовых гамм.', font='Arial 12 normal roman', fill='black')
    canvas_2.create_text(270,290,text='Ваша задача распределить жидкость по правильным колбам так,',font='Arial 12 normal roman', fill='black')
    canvas_2.create_text(270,310,text='чтобы у каждого цвета была своя колба.',font='Arial 12 normal roman', fill='black')
    canvas_2.create_line(10,150,540,150)
    canvas_2.create_line(10,150,10,420)
    canvas_2.create_line(10,420,540,420)
    canvas_2.create_line(540,420,540,150)
    
  
b0 = Button(tk, text='Play', command=start_window_1,width=50, height=5, bg='azure1')
b0.place(x=100,y=250)

b1 = Button(tk, text='Правила игры', command=start_window_2,width=50, height=5, bg='azure1')
b1.place(x=100,y=350)


tk.mainloop()
