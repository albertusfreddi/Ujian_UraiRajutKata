# Soal 1

class uraiRajutKata():
    def urai(self, kata):
        self.kata = kata
        stringPenampungUrai = ''
        for i in range(len(self.kata)):
            for j in range(i+1):
                stringPenampungUrai += self.kata[j]
        return stringPenampungUrai
    def rajut(self, kata):
        self.kata = kata
        stringPenampungRajut = ''
        index = 0
        for i in range(len(self.kata)):
            for j in range(i):
                index += 1
            if i+index <= len(self.kata):
                stringPenampungRajut += self.kata[i+index]
        return stringPenampungRajut

x = uraiRajutKata()
print(x.urai('Code'))
print(x.urai('Python'))
print(x.urai('Purwadhika'))

print(x.rajut('CCoCodCode'))
print(x.rajut('PPyPytPythPythoPython'))
print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
