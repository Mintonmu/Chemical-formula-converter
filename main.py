
import tkinter as tk
from tkinter import LEFT, BOTTOM, messagebox, StringVar
import re
from collections import Counter

data1 = {"甲": 1, "乙": 2, "丙": 3, "丁": 4, "戊": 5,
         "己": 6, "庚": 7, "辛": 8, "壬": 9, "癸": 10}
subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


class MY_APP(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.frame()
        self.setdata()

    def setdata(self):
        # self.num1.insert(-1, "2,3")
        # self.sum1.insert(-1, "二")
        self.num2.insert(-1, "3")
        self.sum2.insert(-1, "")
        self.sums.insert(-1, "己")

    def frame(self):
        self.textname = StringVar()
        self.master.title("化学简式验证程序")
        self.master.geometry("1250x190")
        self.res = tk.Label(self.master, textvariable=self.textname, font=(
            "微软雅黑", 24, "bold", "italic"))
        self.res.pack(side=BOTTOM, padx=0)
        self.num1 = tk.Entry(self.master, justify='center')
        self.num1.pack(side=LEFT)
        self.Hline1 = tk.Label(self.master, text="-")
        self.Hline1.pack(side=LEFT)
        self.sum1 = tk.Entry(self.master, justify='center')
        self.sum1.pack(side=LEFT)
        self.jiaji = tk.Label(self.master, text="甲基")
        self.jiaji.pack(side=LEFT)
        self.Hline2 = tk.Label(self.master, text="-")
        self.Hline2.pack(side=LEFT)
        self.num2 = tk.Entry(self.master, justify='center')
        self.num2.pack(side=LEFT)
        self.Hline3 = tk.Label(self.master, text="-")
        self.Hline3.pack(side=LEFT)
        self.sum2 = tk.Entry(self.master, justify='center')
        self.sum2.pack(side=LEFT)
        self.yiji = tk.Label(self.master, text="乙基")
        self.yiji.pack(side=LEFT)
        self.sums = tk.Entry(self.master, justify='center')
        self.sums.pack(side=LEFT)
        self.wan = tk.Label(self.master, text="烷")
        self.wan.pack(side=LEFT)
        self.btn = tk.Button(self.master, text="转换", command=self.getdata)
        self.btn.pack(side=LEFT)

    def getdata(self):

        if self.num1.get() == "" and self.sum1.get() == "" and self.num2.get() == "" and self.sum2.get() == "":
            self.num1value = [0, ]
            self.num2value = [0, ]
            self.sum1value = 0
            self.sum2value = 0

        if self.num1.get() == "" and self.sum1.get() == "" and self.sum2.get() != "" and self.sum2.get() != "":
            self.num1value = [0, ]
            self.sum1value = 0
            self.num2value = list(map(int, re.split(",|，", self.num2.get())))
            self.sum2value = len(self.num2value)

        if self.num2.get() == "" and self.sum2.get() == "" and self.sum1.get() != "" and self.sum1.get() != "":
            self.num1value = list(map(int, re.split(",|，", self.num1.get())))
            self.sum1value = len(self.num1value)
            self.num2value = [0, ]
            self.sum2value = 0
        if self.num1.get() != "" and self.num2.get() != "" and self.sum1.get() != "" and self.sum2.get() != "":
            self.num1value = list(map(int, re.split(",|，", self.num1.get())))
            self.num2value = list(map(int, re.split(",|，", self.num2.get())))
            self.sum1value = len(self.num1value)
            self.sum2value = len(self.num2value)
        if self.num1.get() != "" and self.sum1.get() == "":
            self.num1value = list(map(int, re.split(",|，", self.num1.get())))
            self.sum1value = len(self.num1value)
            if self.num2.get() == "":
                self.num2value = [0, ]
                self.sum2value = 0
        if self.num2.get() != "" and self.sum2.get() == "":
            self.num2value = list(map(int, re.split(",|，", self.num2.get())))
            self.sum2value = len(self.num2value)
            if self.num1.get() == "":
                self.num1value = [0, ]
                self.sum1value = 0
        self.sumsvalue = data1[self.sums.get()]
        # print(self.num1value)
        # print(self.num2value)
        # print(self.sum1value, self.sum2value, self.sumsvalue)
        # print(self.rule())
        s = ""
        if self.rule():
            self.A = Counter(self.num1value)
            self.B = Counter(self.num2value)
            if self.A and self.B:
                for key in range(2, self.sumsvalue):
                    if key not in self.A:
                        self.A[key] = 0
                    if key not in self.B:
                        self.B[key] = 0
                print(self.A)
                print(self.B)
                if self.sumsvalue != 1:
                    s = "CH3"
                    for key in range(2, self.sumsvalue):
                        s += self.display1(self.A[key], self.B[key])
                    s += "CH3"
                else:
                    for key in range(0, self.sumsvalue+1):
                        s = self.display2(
                            self.A[key], self.B[key], self.sumsvalue)
            print(s.translate(subscript))
            self.textname.set(s.translate(subscript))
        else:
            tk.messagebox.showwarning(
                title="警告", message="您输入的数据不符合要求，请重新输入").center
            self.num1.delete(0, "end")
            self.num2.delete(0, "end")
            self.sum1.delete(0, "end")
            self.sum2.delete(0, "end")
            self.sums.delete(0, "end")
            # pass

    def rule(self):
        
        if self.num1value[0] != 0 or self.num2value[0] != 0:
            print(1)
            if sorted(self.num1value) == self.num1value and sorted(self.num2value) == self.num2value:
                print(2)
                if max(self.num1value+self.num2value) < self.sumsvalue:
                    print(3)
                    if min(self.num1value) == 0 or min(self.num1value) > 1 and min(self.num2value) == 0 or min(self.num2value) > 2:
                        print(4)
                        if sum(self.num1value) <= sum(list(map(lambda x: self.sumsvalue+1-x, self.num1value))):
                            print(5)
                            if min(self.num1value) <= self.sumsvalue+1-min(self.num2value):
                                print(6)
                                return True

        if self.sum1value == 0 and self.sum2value == 0 and self.sumsvalue != 0:
            print(7)
            return True

        if self.num1value[0] == 0:
            if sum(self.num2value) <= sum(list(map(lambda x: self.sumsvalue+1-x, self.num2value))):
                print(8)
                return True

        return False

    def display1(self, sum1val, sum2val):
        if sum1val == 0 and sum2val == 0:
            return "CH2"
        if sum1val == 1 and sum2val == 0:
            return "CH(CH3)"
        if sum1val == 2 and sum2val == 0:
            return "C(CH3)2"
        if sum1val == 0 and sum2val == 1:
            return "CH(CH2CH3)"
        if sum1val == 0 and sum2val == 2:
            return "C(CH2CH3)2"
        if sum1val == 1 and sum2val == 1:
            return "C(CH3)(CH2CH3)"

    def display2(self, sum1val, sum2val, sumsval):
        if sum1val == 0 and sum2val == 0 and sumsval == 1:
            return "CH4"


def gui_start():
    root = tk.Tk()
    ZMJ_PORTAL = MY_APP(master=root)
    ZMJ_PORTAL.mainloop()


if __name__ == '__main__':
    gui_start()
