#!/usr/bin/env python
"""
    Version: 0.1 Data: 2017-02-15    
"""
import sys
import tkinter as tk
from pathlib import Path
import invoice

ProjectName="E-Invoice"
DefaultPath="D:\parse"
DefaultPostFix="*.csv"

Version="0.1"
ReleaseData="2017-02-15"

def ParseInvoice( filename ):
    #filename = sys.argv[1]
    fn = open(filename, "r")
    TkList = invoice.parse_file(fn)
    fn.close()
    return TkList
    
def company_select(evt):
    global gTicketList
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    comp = gTicketList[index]
    itemView.delete(0, itemView.size())
    i = 0
    for im in comp.ItemList:
        i += 1
        itemView.insert(i, im.name + "   " + im.cost)
    return
		
def parseE(view):
    global gTicketList
    #f = FileList[2]
    f = view.get(int(view.curselection()[0]))
    gTicketList = ParseInvoice(f)
    updateCompanyView(companyView, gTicketList)

def updateCompanyView(CV, List):
    cnt = 0
    CV.delete(0,CV.size())
    for t in List:
        cnt += 1
        CV.insert(cnt,t.shop)
    return

def openfile():
    global gFileList
    filewin = tk.Tk()
    tpframe = tk.Frame(filewin)
    tpframe.pack(side="top")
    filescroll = tk.Scrollbar(tpframe)
    filescroll.pack(side = "right", fill="y")
    fileView = tk.Listbox(tpframe, yscrollcommand=filescroll.set, width=48,selectmode=tk.BROWSE)
    fileView.pack(side = "top", fill = "both")
    fileView.activate(0)

    i = 0
    for f in gFileList:
        i += 1
        fileView.insert(i, f)

    
    btframe = tk.Frame(filewin)
    btframe.pack(side="bottom")
    selectedf=tk.Text(btframe, width=40, height=1)
    selectedf.pack(side = "left")
    Opbutton = tk.Button(btframe, text="Read", command= lambda:parseE(fileView))
    #Opbutton.bind("<Enter>", parseE)
    Opbutton.pack(side="left")
    CancelBt = tk.Button(btframe, text="cancel", command=quit)
    CancelBt.pack(side="left")
    

# main()

# File list
gFilePath = Path(DefaultPath)
gFileList = list()
gFileList = list(gFilePath.glob(DefaultPostFix))

gTicketList = ParseInvoice(sys.argv[1])
TotCost = 0

for t in gTicketList:
	TotCost += int(t.total)

root = tk.Tk()
root.title(ProjectName+" "+Version+" "+ReleaseData)

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

cmpyFrame = tk.Frame(root)
cmpyFrame.pack(side="left")
scrollbar = tk.Scrollbar(cmpyFrame)
scrollbar.pack(side = "right", fill="y")
companyView = tk.Listbox(cmpyFrame, yscrollcommand=scrollbar.set, width=48)


itemFrame = tk.Frame(root)
itemFrame.pack(side="right")
itemscrollbar = tk.Scrollbar(itemFrame)
itemscrollbar.pack(side = "right", fill="y")
itemView = tk.Listbox(itemFrame, yscrollcommand=itemscrollbar.set, width=48)

"""
cnt = 0
for t in gTicketList:
	cnt += 1
	companyView.insert(cnt,t.shop)
"""
updateCompanyView(companyView, gTicketList)

companyView.pack(side = "left", fill = "both")
itemView.pack(side = "right", fill = "both")
companyView.activate(0)
scrollbar.config( command = companyView.yview )
itemscrollbar.config( command = itemView.yview )
companyView.bind('<<ListboxSelect>>', company_select)
root.config(menu=menubar)
root.mainloop()
