class Kume(list):
     def append(self,value):
         if value in self:
             return
         super().append(value)   #zaten sinifta var olan append #metodunu ezmek icin super() metodunu kullaniyoruz

a_kumesi = Kume([10, 10, 20, 30])
a_kumesi.append(100)
a_kumesi.append(200)
a_kumesi.append(100)
a_kumesi.append(100)
print(a_kumesi)
