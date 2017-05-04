#!/usr/bin/env python

"""
*附件消費發票檔案格式及使用說明：
表頭=M	發票狀態	發票號碼	發票日期	商店統編	商店店名	載具名稱	載具號碼	總金額
明細=D	發票號碼	小計	品項名稱
範例：
M	開立、作廢	ZZ00000050	20130111	97162640	新北市第1000號門市	手機條碼	/WYY+.,HG	97
D	ZZ00000050	42.00	拿鐵熱咖啡(中)
D	ZZ00000050	55.00	拿鐵冰咖啡(大)
說明：
資料分隔符號為【|】( Shift + \ )，字元編碼為:ANSI(ISO-8859-1、BIG5、MS950)。
"""

class item:
	'Item'
	def __init__(self, name, cost):
		self.name = name
		self.cost = cost
	def display(self):
		print("\t",self.name, "\t", self.cost)
		
	def compare( self, name ):
		if name in self.name:
			return 1
		else:
			return 0

	def displayGUI(self, tlist):
		tlist += '\t'
		tlist += str(self.name)
		tlist += '\t'
		tlist += str(self.cost)
		tlist += '\n'
		return tlist


class eticket:
	'E-Ticket'
	itemNum = 0
	ItemList = [];
	
	def __init__(self, number, date, shop, total):
		self.ItemList = [];
		self.number = number
		self.date = date
		self.shop = shop
		self.total = total
		
	def addItem(self, name, cost):
		self.itemNum += 1
		self.ItemList.append(item(name,cost))
		
	def display(self):
		print(self.number, " ", self.date," ", self.shop, " ", self.total)
		for item in self.ItemList:
			item.display()
	
	def compare(self, name):
		for item in self.ItemList:
			if item.compare(name) == 1:
				item.display()
	
	def displayGUI(self, tlist):
		tlist += str(self.number) + ' ' + str(self.date) + ' ' + str(self.shop) + ' ' + str(self.total) + '\n'
		for item in self.ItemList:
			tlist = item.displayGUI(tlist)
		return tlist

def parse_file(fn):
	content = fn.readline()
	TicketList = [];
	while content != "":
		if content[0] == 'D':
			if not TicketList :
				print("No ticket")
				return
			list1 = content.split('|')
			_eticket.addItem(list1[3], list1[2])
		else:
			list1 = content.split('|')
			_eticket = eticket(list1[2], list1[3], list1[5], list1[8])
			TicketList.append(_eticket)		

		content = fn.readline()

	if TicketList.count == 0:
		return

	
	return TicketList

