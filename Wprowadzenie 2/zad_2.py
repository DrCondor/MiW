from file_manager import FileManager
from chuck_norris import chuck

# ćwiczenie 1
def cwiczenie_1(a_list, b_list):
    result=[]

    for i in range(0, max(len(a_list), len(b_list))):
        if(i%2==0 and i < len(a_list)):
            result.append(a_list[i])
        if(i%2==1 and i < len(b_list)):
            result.append(b_list[i])

    return result

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]    #<- wyciągam parzyste
b_list = ["a", "b", "c", "d", "e"]      #<- wyciągam nieparzyste

print(cwiczenie_1(a_list,b_list))

# ćwiczenie 2
def cwiczenie_2(data_text):
    return {
        "length: ": len(data_text),
        "letters: ": list(data_text),
        "big_letters: ": data_text.upper(),
        "small_letters: ": data_text.lower()
    }


print(cwiczenie_2("Python spoko, ale jednak wolę Ruby"))

# ćwiczenie 3
def cwiczenie_3(text, letter):
    return text.replace(letter.upper(),"").replace(letter.lower(),"")

print(cwiczenie_3("Siała baba mak, nie wiedziała jak", 'a'))

# ćwiczenie 4
def cwiczenie_4(temperature_type):
    if temperature_type < -273.15:
        raise Exception("Dude. That's way too cold!")
    else:
        temperatures = {
            "fahrenheit": temperature_type * 1.8 + 32,
            "rankine": (temperature_type + 273.15) * 1.8,
            "kelvin": temperature_type + 273.15    
        }

        print(
            "Converted temperatures:\nFahrenheit: {fahrenheit}\nRankine: {rankine}\nKelvin: {kelvin}"
            .format(fahrenheit=temperatures["fahrenheit"], rankine=temperatures["rankine"], kelvin=temperatures["kelvin"])
            )

cwiczenie_4(36.6)


# ćwiczenie 5
class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

    def difference(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            raise Exception("No division by zero!")

        return self.a / self.b

print(Calculator(12, 5).add())
print(Calculator(20, 15).difference())
print(Calculator(3, 10).multiply())
print(Calculator(100, 5).divide())

# ćwiczenie 6
class ScienceCalculator(Calculator):

    def pow(self):
        return self.a ** self.b

print(ScienceCalculator(3, 3).pow())

# ćwiczenie 7
def cwiczenie_7(tekst):
    return tekst[::-1]

print(cwiczenie_7("Siała baba mak"))

# ćwiczenie 9
file_manager = FileManager("lorem_ipsum.txt")
print(file_manager.read_file())

file_manager.update_file(" consectetur adipiscing elit, sed do eiusmod tempor")
print(file_manager.read_file())

# ćwiczenie 10
print(chuck("Chuck Norris"))