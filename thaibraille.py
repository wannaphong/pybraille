'''
โปรแกรมช่วยสร้างอัษรเบรลล์ภาษาไทย
==================
พัฒนาโดย นาย วรรณพงษ์  ภัททิยไพบูลย์
เริ่ม 19 มีนาคม 2560

ความสามารถที่ควรมี
- สามารถแปลงข้อความปกติเป็นอักษรเบรลล์ได้
- สามารถกลับด้าน เพื่อใช้ในการพิมพ์และกดจุดอักษรเบรลล์ได้ เช่น อักษรเบรลล์ เป็น ล์ลรบเรษก ั อ
'''
from pybraille import braille
class thaibraille():
	def word(self,data):
		self.word=data # รับข้อความเข้ามาในระบบ
		self.braille = braille()
		self.data =[]
	def tobraille(self):
		self.dict1={"ก":['1234'],"ข":['15'],"ฃ":['456','15'],"ค":['156'],"ฅ":['56','156'],"ฆ":['6','156'],"ง":['12346'],'จ':['234'],'ฉ':['25'],'ช':['256'],'ซ':['2356'],'ฌ':['6','256']}
		for a in list(self.word):
			self.braille.inputnum(self.dict1[a])
			self.data.append(self.braille.tobraille())
			self.data.append(" ")
		return ''.join(self.data)