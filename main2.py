from tkinter import *
from tkinter import ttk
import random
from PIL import Image, ImageTk
import math
import json
from objects.bullet import Bullet
from objects.block import Block
from operator import itemgetter
# import os
# import sys
# os.chdir(sys._MEIPASS)


W = 1280
H = 1024
flag2 = True
tk = Tk()
style = ttk.Style()
style.configure("BW.TLabel", foreground="white", background="black")
tk.geometry("1280x1070")
c = Canvas(tk, width=W, height=H, bg="white")
c.grid(row=2, columnspan=20)
tk["bg"] = "black"
time0 = 0
N = 9
vy = 136
game_time2 = 0
count = 0
count2 = 0
life = 5
random_var = StringVar()
blocks = []

is_playing = False

color = {"red": ImageTk.PhotoImage(Image.open("images/cannon_red_new.png")),
         "blue": ImageTk.PhotoImage(Image.open("images/blue_new.png")),
         "green": ImageTk.PhotoImage(Image.open("images/green_new.png"))}


#-----------------------------------------------------------------------------------------------------------------------

back_purple_phon = ImageTk.PhotoImage(Image.open("Background/purple.png"))
back_purple_phon2 = c.create_image(0, 0, image=back_purple_phon, anchor=NW)

star1 = ImageTk.PhotoImage(Image.open("Background/star1.png"))
star1_1 = c.create_image(0, 0, image=star1, anchor=NW)
star2 = ImageTk.PhotoImage(Image.open("Background/star2.png"))
star2_1 = c.create_image(0, 0, image=star2, anchor=NW)
star3 = ImageTk.PhotoImage(Image.open("Background/star3.png"))
star3_1 = c.create_image(0, 0, image=star3, anchor=NW)


star1_2 = c.create_image(0, -1024, image=star1, anchor=NW)

star2_2 = c.create_image(0, -1024, image=star2, anchor=NW)

star3_2 = c.create_image(0, -1024, image=star3, anchor=NW)

planet_red = ImageTk.PhotoImage(Image.open("Background/planet_red.png"))
planet_red1 = c.create_image(50, 80, image=planet_red, anchor=NW)
planet_green = ImageTk.PhotoImage(Image.open("Background/planet_green.png"))
planet_green1 = c.create_image(680, 100, image=planet_green, anchor=NW)
planet_purple_light = ImageTk.PhotoImage(Image.open("Background/planet_purple_light.png"))
planet_purple_light1 = c.create_image(1040, 50, image=planet_purple_light, anchor=NW)
planet_purple_dark = ImageTk.PhotoImage(Image.open("Background/planet_purple_dark.png"))
planet_purple_dark1 = c.create_image(400, 200, image=planet_purple_dark, anchor=NW)
planet_orange = ImageTk.PhotoImage(Image.open("Background/palnet_orange.png"))
planet_orange1 = c.create_image(500, 760, image=planet_orange, anchor=NW)

sb = ImageTk.PhotoImage(Image.open("Background/хзхзхзхзхзхзхзхзхзхз.png"))
sb1 = c.create_image(0, 0, image=sb, anchor=NW)

planet_green_dark = ImageTk.PhotoImage(Image.open("Background/planet_green_dark.png"))
planet_green_dark1 = c.create_image(30, 550, image=planet_green_dark, anchor=NW)
planet_top = ImageTk.PhotoImage(Image.open("Background/planet_top.png"))
planet_top1 = c.create_image(740, 520, image=planet_top, anchor=NW)
vx = 0.02
vx2 = 0.006
vx3 = 0.05
vx4 = 0.06
vx5 = 0.04
vx6 = 0.07
vx7 = 0.1

def Move_star():
    x, y = c.coords(star1_1)
    x2, y2 = c.coords(star2_1)
    x3, y3 = c.coords(star3_1)
    x4, y4 = c.coords(star1_2)
    x5, y5 = c.coords(star2_2)
    x6, y6 = c.coords(star3_2)
    if y >= 1024:
        c.coords(star1_1, 0, -1024)
    if y2 >= 1024:
        c.coords(star2_1, 0, -1024)
    if y3 >= 1024:
        c.coords(star3_1, 0, -1024)
    if y4 >= 1024:
        c.coords(star1_2, 0, -1024)
    if y5 >= 1024:
        c.coords(star2_2, 0, -1024)
    if y6 >= 1024:
        c.coords(star3_2, 0, -1024)
    c.move(star1_1, 0, 0.75)
    c.move(star2_1, 0, 1)
    c.move(star3_1, 0, 2)
    c.move(star1_2, 0, 0.75)
    c.move(star2_2, 0, 1)
    c.move(star3_2, 0, 2)
    c.after(50, Move_star)
c.after(50, Move_star)

def move_pl():
    global vx
    x, y = c.coords(planet_red1)
    if y > 100:
        vx *= -1
    if y < 50:
        vx = 0.02
    c.move(planet_red1, 0, vx)
    c.after(5, move_pl)
c.after(5, move_pl)


def move_pl2():
    global vx2
    x, y = c.coords(planet_green1)
    if y > 120:
        vx2 *= -1
    if y < 100:
        vx2 = 0.006
    c.move(planet_green1, 0, vx2)
    c.after(5, move_pl2)
c.after(5, move_pl2)

def move_pl3():
    global vx3
    x, y = c.coords(planet_purple_light1)
    if y > 70:
        vx3 *= -1
    if y < 50:
        vx3 = 0.05
    c.move(planet_purple_light1, 0, vx3)
    c.after(5, move_pl3)
c.after(5, move_pl3)

def move_pl4():
    global vx4
    x, y = c.coords(planet_purple_dark1)
    if y > 220:
        vx4 *= -1
    if y < 200:
        vx4 = 0.06
    c.move(planet_purple_dark1, 0, vx4)
    c.after(5, move_pl4)
c.after(5, move_pl4)

def move_pl5():
    global vx5
    x, y = c.coords(planet_orange1)
    if y > 810:
        vx5 *= -1
    if y < 760:
        vx5 = 0.04
    c.move(planet_orange1, 0, vx5)
    c.after(5, move_pl5)
c.after(5, move_pl5)

def move_pl6():
    global vx6
    x, y = c.coords(planet_green_dark1)
    if y > 600:
        vx6 *= -1
    if y < 550:
        vx6 = 0.07
    c.move(planet_green_dark1, 0, vx6)
    c.after(5, move_pl6)
c.after(5, move_pl6)

def move_pl7():
    global vx7
    x, y = c.coords(planet_top1)
    if y > 520:
        vx7 *= -1
    if y < 470:
        vx7 = 0.1
    c.move(planet_top1, 0, vx7)
    c.after(5, move_pl7)
c.after(5, move_pl7)

#-----------------------------------------------------------------------------------------------------------------------

images = {
    "base": ImageTk.PhotoImage(Image.open("images/baza.png")),
    "cannon_create_green": ImageTk.PhotoImage(Image.open("images/new_green.png")),
    "cannon_create_blue": ImageTk.PhotoImage(Image.open("images/new_blue.png")),
    "cannon_create_red": ImageTk.PhotoImage(Image.open("images/new_red.png")),
    "bullet_create_green": ImageTk.PhotoImage(Image.open("images/bullet.png")),
    "bullet_create_blue": ImageTk.PhotoImage(Image.open("images/bullet_blue.png")),
    "bullet_create_red": ImageTk.PhotoImage(Image.open("images/red_bullet.png")),
    "aim": ImageTk.PhotoImage(Image.open("images/aim2.png")),
    "red_aim": ImageTk.PhotoImage(Image.open("images/red_aim.png")),
    "black_hp": ImageTk.PhotoImage(Image.open("images/heart_black.png")),
    "red_hp": ImageTk.PhotoImage(Image.open("images/heart.png")),
    "select_green_cannon": ImageTk.PhotoImage(Image.open("images/yellow_green.png")),
    "select_blue_cannon": ImageTk.PhotoImage(Image.open("images/yellow_blue.png")),
    "select_red_cannon": ImageTk.PhotoImage(Image.open("images/yellow_red.png"))
}

game_objects = {

}
users = []
flag9 = True
num = 0
a = 10000
t = 0
list_count = []
#entry = ttk.Entry()
#leb = Label(tk, text="Имя", font=("Ariel", 25))
columns = ("№", "name", "count")
# tree = ttk.Treeview(columns=columns, show="headings")
def show_message():
    global count, num, flag9, users, leb3
    if flag9:
        ax = entry.get()
        num = 1
        leb3 = Label(tk, font=("Ariel", 25), foreground="white", background="black")
        leb3.grid(row=3, column=4)
        leb3.configure(text="Твои очки: " + str(count) + '\n' + "Твой ник: " + str(ax) + '\n' + "Твоё место: " + str(num))
        try:
            with open("users.txt", "r") as file:
                users = json.load(file)
        except:
            users = []

        users.append({"num": num, "name": ax, "count": count})
        users.sort(key=itemgetter('count'), reverse=True)
        art = users.index({"num": num, "name": ax, "count": count})
        print(art)
        with open("users.txt", "w") as file:
            json.dump(users, file, indent=1)
        tree.insert("", art, values=(num, ax, count))
        print(users[art]["name"])
        flag9 = False

#btn = ttk.Button(text="Click", command=show_message)
game_btn = ImageTk.PhotoImage(Image.open("Background/KPNF2945.PNG"))
restart = ImageTk.PhotoImage(Image.open("images/restart.png"))
tab_lid = ImageTk.PhotoImage(Image.open("images/tabl_new.png"))
bullets = []
blocks2 = []
bullet_blue = []
bullet_red = []

state = "green"
flag = "True"
flag5 = False
flag6 = False
flag11 = False
flag12 = False
flag13 = False
flag14 = False
flag7 = False
flag8 = True
flag10 = True
flag15 = False
time2 = 5000

objects = []

station = "menu"

q = []
visited = []
time4 = 0
def clear():
    for object in objects:
        c.delete(object)


def draw_menu():
    if is_playing == False:
        objects.append(c.create_image(200, 400, image=game_btn, anchor=NW))


def menn():
    global station, leb, btn4, entry, tree, flag7, btn, flag9, num, lab, lab2, leb2, leb3
    if station == "menu3":
        station = "menu2"
        flag7 = False
        c.config(width=1280, height=1024)
        leb.destroy()
        leb2.destroy()
        leb3.destroy()
        btn4.destroy()
        entry.destroy()
        tree.destroy()
        btn.destroy()
        lab = Label(tk, text="Счёт:", font=("Comic Sans MS", 25), bg="black", fg="white")
        lab.grid(row=0, column=0)
        lab2 = Label(tk, textvariable=random_var, font=("Comic Sans MS", 25), fg="black")
        lab2.grid(row=0, column=1)

#btn4 = Button(tk, text="<", command=menn)

def draw_menu2():
    global station, entry, leb, leb2, num, btn4, lab, lab2, leb3
    if not is_playing:
        objects.append(c.create_image(150, 130, image=restart, anchor=NW))
        objects.append(c.create_image(100, 469, image=tab_lid, anchor=NW))
        if flag7:
            station = "menu3"
            lab.destroy()
            lab2.destroy()
            btn4.grid(row=0, column=0)
            leb.grid(row=0, column=1)
            leb2.grid(row=1, column=1)
            entry.grid(row=3, column=1)
            c.config(width=0, height=0)
            tree.grid(row=4, columnspan=20)
            btn.grid(row=3, column=2)

            tree.heading("№", text="№", anchor=NW)
            tree.heading("name", text="Имя", anchor=NW)
            tree.heading("count", text="count", anchor=NW)

            tree.column("#1", stretch=NO, width=100)
            tree.column("#2", stretch=NO, width=820)
            tree.column("#3", stretch=NO, width=200)

            clear()

def draw_images():
    game_objects["base1"] = c.create_image(0, 956, image=images["base"], anchor=NW)
    game_objects["aim2"] = c.create_image(30, -136, image=images["aim"], anchor=NW)
    game_objects["aim"] = c.create_image(30, -136, image=images["red_aim"], anchor=NW)
    game_objects["cannon_green"] = c.create_image(50, 810, image=images["cannon_create_green"], anchor=NW)
    game_objects["cannon_blue"] = c.create_image(490, 810, image=images["cannon_create_blue"], anchor=NW)
    game_objects["cannon_red"] = c.create_image(1074, 815, image=images["cannon_create_red"], anchor=NW)
    game_objects["selected1"] = c.create_image(50, 810, image=images["select_green_cannon"], anchor=NW)
    game_objects["selected2"] = c.create_image(490, 810, image=images["select_blue_cannon"], anchor=NW)
    game_objects["selected3"] = c.create_image(1074, 815, image=images["select_red_cannon"], anchor=NW)
    c.tag_raise(game_objects["cannon_green"])
    game_objects["hp5"] = c.create_image(10, 950, image=images["red_hp"], tag='down', anchor=NW)
    game_objects["hp4"] = c.create_image(90, 950, image=images["red_hp"], tag='down', anchor=NW)
    game_objects["hp3"] = c.create_image(170, 950, image=images["red_hp"], tag='down', anchor=NW)
    game_objects["hp2"] = c.create_image(250, 950, image=images["red_hp"], tag='down', anchor=NW)
    game_objects["hp"] = c.create_image(330, 950, image=images["red_hp"], tag='down', anchor=NW)
    game_objects["dead_line"] = c.create_line(0, 810, 1280, 810, fill="red", width=2)

def click(event):
    global station, is_playing, time0, flag9
    if 200 < event.x < 1102 and 400 < event.y < 637 and is_playing == False and station != "menu2":
        clear()
        flag9 = True
        if station == "menu":
            station = "game"
            draw_images()
        else:
            station = "menu"

def click2(event):
    global station, is_playing, time0, flag, life, tree, flag3, flag4, flag5, flag6, flag7, flag9, flag10, tree, leb, entry, btn4, btn, num, users, count, count2, tree2, tree3, leb2
    if 150 < event.x < 1134 and 130 < event.y < 320 and is_playing == False and station == "menu2":
        clear()
        flag10 = False
        if station == "menu2":
            life = 5
            time0 = 0
            count = 0
            count2 = 0
            random_var.set(str(count))
            flag = "True"
            station = "game"
            draw_images()
        else:
            station = "menu2"
    if 100 < event.x < 1176 and 469 < event.y < 894 and not is_playing and station == "menu2":
        flag7 = True
        flag9 = True
        entry = ttk.Entry(width=30, font=("Ariel", 20))
        leb = Label(tk, text="Топ 120 лучших игроков!", font=("Ariel", 25), foreground="white", background="black")
        leb2 = Label(tk, text="Введите ник ниже:", font=("Ariel", 25), foreground="white", background="black")
        btn4 = Button(tk, text="<", command=menn, width=10, height=3, foreground="white", background="black")
        tree = ttk.Treeview(columns=columns, show="headings", height=45, style="BW.TLabel")

        scrollbar = ttk.Scrollbar(orient='vertical', command=tree.yview)
        scrollbar.grid(row=4, column=19, sticky=NS)

        tree['yscrollcommand'] = scrollbar.set
        btn = Button(tk, text="Enter", command=show_message, foreground="white", background="black", font=("Ariel", 20))

        try:
            with open("users.txt", "r") as file:
                users = json.load(file)
        except:
            users = []

        for person in users:
            print(person)
            if flag10:
                tree.insert("", END, values=(person["num"], person["name"], person["count"]), tags="tree")
                tree.tag_configure("tree", font=("Ariel", 13))
        if station == "menu3":
            station = "game"
        else:
            station = "menu3"


def pusk(event):
    if station == "menu":
        click(event)
    if station == "menu2":
        click2(event)


c.bind("<Button-1>", pusk)


def gameloop():
    global station, is_playing, time0, flag3
    if station == "menu":
        is_playing = False
        draw_menu()
    if station == "menu2":
        is_playing = False
        time0 = 0
    if station == "menu3":
        is_playing = False
        draw_menu2()
    if station == "game":
        is_playing = True
        time0 += 20

    c.after(20, gameloop)


c.after(20, gameloop)


def Move_aim_down():
    if is_playing:
        c.move(game_objects["aim2"], 0, vy)
        c.move(game_objects["aim"], 0, vy)
    c.after(time2, Move_aim_down)


c.after(time2, Move_aim_down)


def Move_aim(key):
    if is_playing:
        x, y = c.coords(game_objects["aim2"])
        if key.char == "d" and x < 1118:
            c.move(game_objects["aim2"], 136, 0)
            c.move(game_objects["aim"], 136, 0)
        if key.char == "a" and x > 30:
            c.move(game_objects["aim2"], -136, 0)
            c.move(game_objects["aim"], -136, 0)
        if key.char == "w" and y > 0:
            c.move(game_objects["aim2"], 0, -136)
            c.move(game_objects["aim"], 0, -136)
        if key.char == "s" and y <= y + 136:
            c.move(game_objects["aim2"], 0, 136)
            c.move(game_objects["aim"], 0, 136)


def spawn_squ():
    global time2
    x = 30
    if is_playing:
        for _ in range(N):
            cc = random.choice(list(color))
            block1 = Block(c, c.create_image(x, -136, image=color[cc], anchor=NW), cc)
            x += 136
            blocks.append(block1)
    c.after(time2, spawn_squ)


c.after(time2, spawn_squ)


def Move_squ():
    global vy, time2
    if is_playing:
        for i in blocks:
            res1 = i.image
            c.tag_raise(game_objects["aim2"], res1)
            c.tag_raise(game_objects["base1"], res1)
            c.move(res1, 0, vy)
        for j in bullets:
            j.ty += vy
    c.after(time2, Move_squ)


c.after(time2, Move_squ)


def spawn_bullet_green():
    if is_playing:
        for i in blocks:
            x1, y1 = c.coords(game_objects["aim2"])
            x1 += 68
            y1 += 68
            if i.x < x1 <= i.x + 136 and i.y <= y1 <= i.y + 136:
                bullet1 = Bullet(c, x1, y1,
                                 c.create_image(75, 800, image=images["bullet_create_green"], anchor=NW), "green")
                bullets.append(bullet1)


def spawn_bullet_blue():
    if is_playing:
        for i in blocks:
            x1, y1 = c.coords(game_objects["aim2"])
            x1 += 68
            y1 += 68
            if i.x < x1 <= i.x + 136 and i.y <= y1 <= i.y + 136:
                bullet1 = Bullet(c, x1, y1,
                                 c.create_image(630, 770, image=images["bullet_create_blue"], anchor=NW), "blue")
                c.tag_raise(bullet1.image)
                bullet_blue.append(bullet1)


def spawn_bullet_red():
    if is_playing:
        for i in blocks:
            x1, y1 = c.coords(game_objects["aim2"])
            x1 += 68
            y1 += 68
            if i.x < x1 <= i.x + 136 and i.y <= y1 <= i.y + 136:
                bullet1 = Bullet(c, x1, y1,
                                 c.create_image(1120, 840, image=images["bullet_create_red"], anchor=NW), "red")
                c.tag_raise(bullet1.image)
                bullet_red.append(bullet1)


def Move_two_bul(event):
    if is_playing:
        if state == "green":
            spawn_bullet_green()
        if state == "blue":
            spawn_bullet_blue()
        if state == "red":
            spawn_bullet_red()


tk.bind("<space>", Move_two_bul)


def Move_bullet():
    if is_playing:
        for i in bullets:
            s = (i.tx - i.x) ** 2 + (i.y - i.ty) ** 2
            s2 = math.sqrt(s)
            coef = 70 / (s2 + 0.000000000000000000000000001)
            dy = -int((i.y - i.ty)) * coef
            c.move(i.image, int((i.tx - i.x) * coef), dy)
            if s2 < 70:
                c.coords(i.image, i.tx, i.ty)
    c.after(12, Move_bullet)


c.after(12, Move_bullet)


def Move_bullet_blue():
    if is_playing:
        for i in bullet_blue:
            s = (i.tx - i.x) ** 2 + (i.y - i.ty) ** 2
            s2 = math.sqrt(s)
            coef = 70 / (s2 + 0.000000000000000000000000001)
            dy = -int((i.y - i.ty)) * coef
            c.move(i.image, int((i.tx - i.x) * coef), dy)
            if s2 < 70:
                c.coords(i.image, i.tx, i.ty)
    c.after(12, Move_bullet_blue)


c.after(12, Move_bullet_blue)


def Move_bullet_red():
    if is_playing:
        for i in bullet_red:
            s = (i.tx - i.x) ** 2 + (i.y - i.ty) ** 2
            s2 = math.sqrt(s)
            coef = 70 / (s2 + 0.000000000000000000000000001)
            dy = -int((i.y - i.ty)) * coef
            c.move(i.image, int((i.tx - i.x) * coef), dy)
            if s2 < 70:
                c.coords(i.image, i.tx, i.ty)
    c.after(12, Move_bullet_red)


c.after(12, Move_bullet_red)

def Layer():
    if is_playing:
        c.tag_raise(game_objects["cannon_blue"])
        c.tag_raise(game_objects["cannon_green"])
        c.tag_raise(game_objects["cannon_red"])
        c.tag_raise("down")
        c.tag_raise("down2")
    c.after(5, Layer)


c.after(5, Layer)


def bullet_intersects_block(bullet, block):
    return block.x < bullet.x + 40 < block.x + 136 and block.y < bullet.y + 20 < bullet.y + 136


def bullet_intersects_block_blue(bullet, block):
    return block.x < bullet.x + 26 < block.x + 136 and block.y < bullet.y + 44 < bullet.y + 136


def bullet_intersects_block_red(bullet, block):
    return block.x < bullet.x < block.x + 136 and block.y < bullet.y < bullet.y + 136


def should_hit(bullet, block):
    x1, y1 = c.coords(bullet.image)

    current_block_img = block.image

    x2, y2 = c.coords(current_block_img)
    if x1 >= x2 and x1 < x2 + 136 and y1 >= y2 and y1 < y2 + 136:
        return True


def same_color(bullet, block):
    current_bullet = bullet.color
    res2 = block.color
    if res2 == current_bullet:
        return True

f = True
def is_neightboor(block):
    global q, f
    for neightboor in blocks[:]:
        print("Cосед: " + str(neightboor.x))
        if block.x - 136 == neightboor.x and block.x-136 not in visited:
            q.append([block.x - 136, block.y, neightboor.color])
        if block.x + 136 == neightboor.x and block.x+136 not in visited:
            q.append([block.x + 136, block.y, neightboor.color])
        if block.y - 136 == neightboor.y and block.y-136 not in visited:
            q.append([block.x, block.y - 136, neightboor.color])
        if block.y + 136 == neightboor.y and block.y+136 not in visited:
            q.append([block.x, block.y + 136, neightboor.color])
        while len(q) != 0:
            px, py, color3 = q[0]
            # if px in visited:
            #     q.remove(q[0])
            print(q, visited)
            visited.append(px)
            visited.append(py)
            visited.append(color3)
            #print(px, color3)
            if abs(px - block.x) == 136 and py == block.y:
                print(2)
                if color3 == "green":
                    print("Block around: " + str(px))
                    if px - 136 == neightboor.x and px - 136 not in visited:
                        q.append([px - 136, py, neightboor.color])
                        #print(neightboor.color)
                    if px + 136 == neightboor.x and px + 136 not in visited:
                        q.append([px + 136, py, neightboor.color])
                    #del q[0]
                    return True
            if px == block.x and abs(py - block.y) == 136 and color3 == "green":
                if py - 136 == neightboor.y and py - 136 not in visited:
                    q.append([px, py - 136, neightboor.color])
                if py + 136 == neightboor.y and py + 136 not in visited:
                    q.append([px, py + 136, neightboor.color])
                return True
        #print(q)



def delete_block(block):
    r1 = block.image
    blocks.remove(block)
    c.delete(r1)
    del block


def delete_bullet(bullet):
    b1 = bullet
    del bullet
    c.delete(b1)


"""
for bullet in bullets:
    if is_finished(bullet):
        for block in blocks[:]:
            if should_hit(bullet, block):
                if same_color(bullet, block):
                    for neightboor in blocks[:]:
                        if is_neightboor(neightboor, block) and same_color(bullet, neightboor):
                            delete_block(neightboor)
                else:
                    decrease_points()
        delete_bullet(bullet)
"""

black_life = {}
time5 = 300
time6 = 0
gggg = 1
def Player():
    global count, life, flag, time2, time4, a, t, count2, time5, gggg, flag15, f
    should_delete = []
    time4 += 5
    if time5 != 0 and flag15:
        time5 -= 5
    if time5 == 0:
        c.tag_raise(game_objects["aim2"], game_objects["aim"])
        time5 = 300
        flag15 = False
    if time4 == 1000:
        t += 1
        time4 = 0
        a = a + (a * (t / 6000))
    if is_playing:
        for bullet in bullets[:]:
            if not bullet.is_finished():
                continue
            for block in blocks[:]:
                if bullet_intersects_block(bullet, block):
                    if not same_color(bullet, block):
                        life -= 1
                        if life == 4:
                            black_life["life1"] = c.create_image(330, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag15 = True
                            c.tag_raise(game_objects["aim"], game_objects["aim2"])
                        if life == 3:
                            black_life["life2"] = c.create_image(250, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag15 = True
                            c.tag_raise(game_objects["aim"], game_objects["aim2"])
                        if life == 2:
                            black_life["life3"] = c.create_image(170, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag15 = True
                            c.tag_raise(game_objects["aim"], game_objects["aim2"])
                        if life == 1:
                            black_life["life4"] = c.create_image(90, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag15 = True
                            c.tag_raise(game_objects["aim"], game_objects["aim2"])
                        if life == 0:
                            black_life["life5"] = c.create_image(10, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag = "False"
                        bullets.remove(bullet)
                        delete_bullet(bullet.image)
                        break
                    for neightboor in blocks[:]:
                        if is_neightboor(block) and same_color(bullet, neightboor):
                            f = False
                            if neightboor not in should_delete:
                                should_delete.append(neightboor)

                    if block not in should_delete:
                        should_delete.append(block)
                    bullets.remove(bullet)
                    delete_bullet(bullet.image)
                    break
        for block in should_delete:
            rand = random.randint(100, 501)
            count += rand
            list_count.append(rand)
            for i in range(len(list_count)):
                count2 += list_count[i]
                list_count.remove(list_count[i])
            if count2 >= a:
                count2 = 0
                time2 -= 400
            #print(" Счет: " + str(count2) + '\n', "Теорема времени: " + str(a) + '\n', "Время: " + str(t) +
            #      '\n', "Время игры: " + str(time4) + '\n', "time2: " + str(time2) + '\n',
            #      "----------------------------------")
            random_var.set(str(count))
            delete_block(block)
    c.after(5, Player)


c.after(5, Player)


def Player2():
    global count, life, flag, time2, count2, time5, flag15
    should_delete_blue = []
    if time5 != 0 and flag15:
        time5 -= 5
    if time5 == 0:
        c.tag_raise(game_objects["aim2"], game_objects["aim"])
        time5 = 300
        flag15 = False
    if is_playing:
        for bullet in bullet_blue[:]:

            if not bullet.is_finished():
                continue
            for block in blocks[:]:
                if bullet_intersects_block_blue(bullet, block):
                    if not same_color(bullet, block):
                        life -= 1
                        if life == 4:
                            black_life["life1"] = c.create_image(330, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag15 = True
                            c.tag_raise(game_objects["aim"], game_objects["aim2"])

                        if life == 3:
                            black_life["life2"] = c.create_image(250, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag15 = True
                            c.tag_raise(game_objects["aim"], game_objects["aim2"])
                        if life == 2:
                            black_life["life3"] = c.create_image(170, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag15 = True
                            c.tag_raise(game_objects["aim"], game_objects["aim2"])
                        if life == 1:
                            black_life["life4"] = c.create_image(90, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag15 = True
                            c.tag_raise(game_objects["aim"], game_objects["aim2"])
                        if life == 0:
                            black_life["life5"] = c.create_image(10, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag = "False"
                        bullet_blue.remove(bullet)
                        delete_bullet(bullet.image)
                        break
                    for neightboor in blocks[:]:
                        if is_neightboor(neightboor, block) and same_color(bullet, neightboor):
                            if neightboor not in should_delete_blue:
                                should_delete_blue.append(neightboor)
                    if block not in should_delete_blue:
                        should_delete_blue.append(block)
                    bullet_blue.remove(bullet)
                    delete_bullet(bullet.image)
                    break
        for block in should_delete_blue:
            rand = random.randint(100, 501)
            count += rand
            list_count.append(rand)
            for i in range(len(list_count)):
                count2 += list_count[i]
                list_count.remove(list_count[i])
            if count2 >= a:
                count2 = 0
                time2 -= 400
            print(" Счет: " + str(count2) + '\n', "Теорема времени: " + str(a) + '\n', "Время: " + str(t) +
                  '\n', "Время игры: " + str(time4) + '\n', "time2: " + str(time2) + '\n',
                  "----------------------------------")
            random_var.set(str(count))
            delete_block(block)
    c.after(5, Player2)


c.after(5, Player2)


def Player3():
    global count, life, flag, time2, count2, time5, flag15
    should_delete_red = []
    if time5 != 0 and flag15:
        time5 -= 5
    if time5 == 0:
        c.tag_raise(game_objects["aim2"], game_objects["aim"])
        time5 = 300
        flag15 = False
    if is_playing:
        for bullet in bullet_red[:]:
            if not bullet.is_finished():
                continue
            for block in blocks[:]:
                if bullet_intersects_block_red(bullet, block):
                    if not same_color(bullet, block):
                        life -= 1
                        if life == 4:
                            black_life["life1"] = c.create_image(330, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag15 = True
                            c.tag_raise(game_objects["aim"], game_objects["aim2"])
                        if life == 3:
                            black_life["life2"] = c.create_image(250, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag15 = True
                            c.tag_raise(game_objects["aim"], game_objects["aim2"])
                        if life == 2:
                            black_life["life3"] = c.create_image(170, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag15 = True
                            c.tag_raise(game_objects["aim"], game_objects["aim2"])
                        if life == 1:
                            black_life["life4"] = c.create_image(90, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag15 = True
                            c.tag_raise(game_objects["aim"], game_objects["aim2"])
                        if life == 0:
                            black_life["life5"] = c.create_image(10, 950, image=images["black_hp"], tag='down2',
                                                                 anchor=NW)
                            flag = "False"
                        bullet_red.remove(bullet)
                        delete_bullet(bullet.image)
                        break
                    for neightboor in blocks[:]:
                        if is_neightboor(neightboor, block) and same_color(bullet, neightboor):
                            if neightboor not in should_delete_red:
                                should_delete_red.append(neightboor)
                    if block not in should_delete_red:
                        should_delete_red.append(block)
                    bullet_red.remove(bullet)
                    delete_bullet(bullet.image)
                    break
        for block in should_delete_red:
            rand = random.randint(100, 501)
            count += rand
            list_count.append(rand)
            for i in range(len(list_count)):
                count2 += list_count[i]
                list_count.remove(list_count[i])
            if count2 >= a:
                count2 = 0
                time2 -= 400
            print(" Счет: " + str(count2) + '\n', "Теорема времени: " + str(a) + '\n', "Время: " + str(t) +
                  '\n', "Время игры: " + str(time4) + '\n', "time2: " + str(time2) + '\n',
                  "----------------------------------")
            random_var.set(str(count))
            delete_block(block)
    c.after(5, Player3)


c.after(5, Player3)

def Newt_cannon(key):
    global state, flag5, flag6, flag11, flag12, flag13, flag14
    if is_playing:
        if key.char == "u":
            state = "green"
            c.delete(game_objects["selected1"])
            game_objects["selected1"] = c.create_image(50, 810, image=images["select_green_cannon"], anchor=NW)
            c.delete(game_objects["cannon_green"])
            flag14 = True
            if flag5:
                c.delete(game_objects["cannon_blue"])
                c.delete(game_objects["selected2"])
                game_objects["cannon_blue"] = c.create_image(490, 810, image=images["cannon_create_blue"], anchor=NW)
            if flag6:
                c.delete(game_objects["cannon_red"])
                c.delete(game_objects["selected3"])
                game_objects["cannon_red"] = c.create_image(1074, 815, image=images["cannon_create_red"], anchor=NW)
        if key.char == "i":
            state = "blue"
            c.delete(game_objects["selected2"])
            game_objects["selected2"] = c.create_image(490, 810, image=images["select_blue_cannon"], anchor=NW)
            c.delete(game_objects["cannon_blue"])
            flag5 = True
            if flag14:
                c.delete(game_objects["selected1"])
                c.delete(game_objects["cannon_green"])
                game_objects["cannon_green"] = c.create_image(50, 810, image=images["cannon_create_green"], anchor=NW)
            if flag6:
                c.delete(game_objects["cannon_red"])
                c.delete(game_objects["selected3"])
                game_objects["cannon_red"] = c.create_image(1074, 815, image=images["cannon_create_red"], anchor=NW)
        if key.char == "o":
            state = "red"
            c.delete(game_objects["selected3"])
            game_objects["selected3"] = c.create_image(1074, 815, image=images["select_red_cannon"], anchor=NW)
            c.delete(game_objects["cannon_red"])
            flag6 = True
            if flag14:
                c.delete(game_objects["selected1"])
                c.delete(game_objects["cannon_green"])
                game_objects["cannon_green"] = c.create_image(50, 810, image=images["cannon_create_green"], anchor=NW)
            if flag5:
                c.delete(game_objects["cannon_blue"])
                c.delete(game_objects["selected2"])
                game_objects["cannon_blue"] = c.create_image(490, 810, image=images["cannon_create_blue"], anchor=NW)

def TK_PRESS(key):
    Newt_cannon(key)
    Move_aim(key)


def you_lose():
    global is_playing, count, station, life, flag, time0
    if flag == "False":
        is_playing = False
        station = "menu2"
        c.delete(game_objects["base1"])
        c.delete(game_objects["aim2"])
        c.delete(game_objects["aim"])
        c.delete(game_objects["cannon_green"])
        c.delete(game_objects["cannon_blue"])
        c.delete(game_objects["cannon_red"])
        c.delete(game_objects["selected1"])
        c.delete(game_objects["selected2"])
        c.delete(game_objects["selected3"])
        c.delete(game_objects["hp5"])
        c.delete(game_objects["hp4"])
        c.delete(game_objects["hp3"])
        c.delete(game_objects["hp2"])
        c.delete(game_objects["hp"])
        c.delete(black_life["life1"])
        c.delete(black_life["life2"])
        c.delete(black_life["life3"])
        c.delete(black_life["life4"])
        c.delete(black_life["life5"])
        c.delete(game_objects["dead_line"])
        for block in blocks[:]:
            delete_block(block)
        for bullet in bullets[:]:
            delete_bullet(bullet.image)
        for bullet2 in bullet_blue[:]:
            delete_bullet(bullet2.image)
        for bullet3 in bullet_red[:]:
            delete_bullet(bullet3.image)
    if station == "menu2":
        is_playing = False
        time0 = 0
        draw_menu2()

    c.after(50, you_lose)
c.after(50, you_lose)

tk.bind("<KeyPress>", TK_PRESS)

lab = Label(tk, text="Счёт:", font=("Comic Sans MS", 25), bg="black", fg="white")
lab.grid(row=0, column=0)
lab2 = Label(tk, textvariable=random_var, font=("Comic Sans MS", 25), fg="black")
lab2.grid(row=0, column=1)

mainloop()
