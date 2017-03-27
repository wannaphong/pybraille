''' โปรแกรมสร้าง ⣶ อักษรเบรลล์
เริ่มต้น 18 มีนาคม 2017
โดย นาย วรรณพงษ์  ภัททิยไพบูลย์
https://python3.wannaphong.com
หลักการ
========
- อ้างอิงจุดตามข้อมูลที่กรอกมา เช่น [1,2,3,4,5,6] ได้ ⣶
- รองรับการเรียงจากหลังมาหน้า เช่น  [2,4,5,6] ได้ ⣰ พอกลับได้เป็น [1,3,5,6] ได้ ⠧

⣿
คือ
1 2
3 4
5 6
7 8

เราต้องแก้ไขปัญหาในกรณีที่ตัวหนึ่งมีหลายเซลล์ด้วย เช่น ฅ มีสองเซลล์ คือ ⠤⠥ และต้องแก้ไขเวลาพิมพ์กลับด้าน ฅ คือ ⠬⠤
'''
class braille():
	'''
	โมดูลช่วยแปลงข้อมูลตามตำแหน่งจุดบนอักษรเบรลล์ เช่น   ⠧ ต้องกรอก "1356" ลงใน braille.inputnum("1356")
	คำสั่งที่มี
	=====
	inputnum(ข้อมูลสตริงหรือ list) เป็นคำสั่งรับข้อมูลตามตำแหน่งจุดบนอักษรเบรลล์
	tobraille() ใช้ส่งคืนอักษรเบรลล์
	printbraille() ใช้สำหรับการพิมพ์อักษรเบรลล์ ซึ่งต้องกลับตำแหน่งอักษรเบรลล์ และจัดตำแหน่งจากหลังมาหน้า เพื่อให้ง่ายต่อการกดจุดทำหนังสืออักษรเบรลล์
	
	พัฒนา โดย นาย วรรณพงษ์ ภัททิยไพบูลย์
	'''
	def inputnum(self,data):
		'''
		ใช้ในการรับข้อมูลเข้ามา ได้ทั้งแบบ list ตัวเลขจุด และ str ตัวเลขจุด ในเซลล์
		'''
		self.inputdata=data
		if str(type(data)) == "<class 'list'>": # หากข้อมูลเป็นชนิด list
			if len(data)>1: # หากมี list มากกว่าหนึ่ง
				self.data =['']*len(data) # สร้าง list ซ้อน list ตามจำนวนที่มี
				self.i=0
				while self.i<len(data): # ทำการลูปตามจำนวน list ที่ซ้อนใน data
					self.data[self.i]=sorted(list(data[self.i])) #  ทำการแปลงข้อมูลใน list ให้เป็น list
					self.i+=1
			else: # หากมี ['12'] อันเดียว
				self.data =sorted(list(data[0]))
		else:
			self.data = sorted(list(data)) # แปลงเป็น list พร้อมเรียงจากน้อยไปมาก
		self.db = {'0':'⠀','1':'⠁','3':'⠂','13':'⠃','5':'⠄','15':'⠅','35':'⠆','135':'⠇','2':'⠈','12':'⠉','23':'⠊','123':'⠋','25':'⠌','125':'⠍','235':'⠎','1235':'⠏','⠐':'4','14':'⠑','34':'⠒','134':'⠓','45':'⠔','145':'⠕','345':'⠕','1345':'⠗','24':'⠘','124':'⠙','234':'⠚','1234':'⠛','245':'⠜','1245':'⠝','2345':'⠞','12345':'⠟','6':'⠠','16':'⠡','36':'⠢','136':'⠣','56':'⠤','156':'⠥','356':'⠦','1356':'⠧','26':'⠨','126':'⠩','236':'⠪','1236':'⠫','256':'⠬','1256':'⠭','2356':'⠮','12356':'⠯','46':'⠰','146':'⠱','346':'⠲','1346':'⠳','456':'⠴','1456':'⠵','3456':'⠶','13456':'⠷','246':'⠸','1246':'⠹','2346':'⠺','12346':'⠻','2456':'⠼','12456':'⠽','23456':'⠾','123456':'⠿','7':'⡀','17':'⡁','37':'⡂','137':'⡃','57':'⡄','157':'⡅','⡆':'357','1357':'⡇','27':'⡈','127':'⡉','237':'⡊','1237':'⡋','257':'⡌','1257':'⡍','2357':'⡎','12357':'⡏','47':'⡐','147':'⡑','1257':'⡍','2357':'⡎','12357':'⡏','47':'⡐','147':'⡑','347':'⡒','1347':'⡓','457':'⡔','1457':'⡕','3457':'⡖','13457':'⡗','247':'⡘','1247':'⡙','2347':'⡚','12347':'⡛','2457':'⡜','12457':'⡝','23457':'⡞','123457':'⡟','67':'⡠','167':'⡡','367':'⡢','1367':'⡣','567':'⡤','1567':'⡥','3567':'⡦','13567':'⡧','267':'⡨','1267':'⡩','2367':'⡪','12367':'⡫','2567':'⡬','12567':'⡭','23567':'⡮','123567':'⡯','467':'⡰','1467':'⡱','3467':'⡲','13467':'⡳','4567':'⡴','14567':'⡵','34567':'⡶','134567':'⡷','2467':'⡸','12467':'⡹','23467':'⡺','123467':'⡻','24567':'⡼','124567':'⡽','234567':'⡾','1234567':'⡿','8':'⢀','18':'⢁','38':'⢂','138':'⢃','58':'⢄','158':'⢅','358':'⢆','1358':'⢇','28':'⢈','128':'⢉','238':'⢊','1238':'⢋','258':'⢌','1258':'⢍','2358':'⢎','12358':'⢏','48':'⢐','148':'⢑','348':'⢒','1348':'⢓','458':'⢔','1458':'⢕','3458':'⢖','13458':'⢗','248':'⢘','1248':'⢙','2348':'⢚','12348':'⢛','2458':'⢜','12458':'⢝','23458':'⢞','123458':'⢟','68':'⢠','168':'⢡','368':'⢢','1368':'⢣','568':'⢤','1568':'⢥','3568':'⢦','13568':'⢧','268':'⢨','1268':'⢩','2368':'⢪','12368':'⢫','2568':'⢬','12568':'⢭','23568':'⢮','123568':'⢯','468':'⢰','1468':'⢱','3468':'⢲','13468':'⢳','4568':'⢴','14568':'⢵','34568':'⢶','134568':'⢷','2468':'⢸','12468':'⢹','23468':'⢺','123468':'⢻','24568':'⢼','124568':'⢽','234568':'⢾','1234568':'⢿','78':'⣀','178':'⣁','378':'⣂','1378':'⣃','578':'⣄','1578':'⣅','3578':'⣆','13578':'⣇','278':'⣈','1278':'⣉','2378':'⣊','12378':'⣋','2578':'⣌','12578':'⣍','23578':'⣎','123578':'⣏','478':'⣐','1478':'⣑','3478':'⣒','13478':'⣓','4578':'⣔','14578':'⣕','34578':'⣖','134578':'⣗','2478':'⣘','12478':'⣙','23478':'⣚','123478':'⣛','24578':'⣜','124578':'⣝','234578':'⣞','1234578':'⣟','678':'⣠','1678':'⣡','3678':'⣢','13678':'⣣','5678':'⣤','15678':'⣥','35678':'⣦','135678':'⣧','2678':'⣨','12678':'⣩','23678':'⣪','123678':'⣫','25678':'⣬','125678':'⣭','235678':'⣮','1235678':'⣯','4678':'⣰','14678':'⣱','34678':'⣲','134678':'⣳','45678':'⣴','145678':'⣵','345678':'⣶','1345678':'⣷','24678':'⣸','124678':'⣹','234678':'⣺','1234678':'⣻','245678':'⣼','1245678':'⣽','2345678':'⣾','12345678':'⣿'}
	def tobraille(self):
		'''
		เอา [1,2,3,4] มาเป็น 1234 เรียงจากน้อยไปมาก
		'''
		if len(self.data)>1 and str(type(self.inputdata)) == "<class 'list'>":
			self.data1 =''
			for o in self.data:
				#print(o)
				self.data1 += self.db[''.join(str(''.join(o)))]
				#print(self.data1)
			return self.data1
		else:
			self.data1 = ''.join(self.data) # แปลง list to str
			try:
				return(self.db[self.data1])
			except:
				return 'Error'
	def printbraille(self):
		'''
		กลับด้านตัวเลข
		'''
		self.chage={'1':'2','2':'1','3':'4','4':'3','5':'6','6':'5','7':'8','8':'7'}
		self.i=0
		self.aa=[]*len(self.data)
		if len(self.data)>1 and str(type(self.inputdata)) == "<class 'list'>":
			self.data2=['']*len(self.data)
			while self.i < len(self.data):
				for a in self.data[self.i]:
					self.data2[self.i] += self.chage[a]
				self.data2[self.i]=sorted(self.data2[self.i])
				self.data2[self.i]=self.db[''.join(self.data2[self.i])]
				self.i+=1
			self.data2.reverse() # ทำการเรียงจากหลังไปหน้า
			return ''.join(self.data2)
		else:
			self.data2=['']
			for a in self.data:
				try:
					self.data2.append(self.chage[a])
				except:
					print('error')
			return(self.db[''.join(sorted(self.data2))])