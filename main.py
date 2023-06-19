import math
import weakref
#If we want attributes and values of cls or self - convert to dict

#Relearn arges and kwarges (and uses)
#Learn function notation - EX. global().get - callable stuff
#Learn USE of @classmethod
#git gut


class Combustion:
    x = 1
    instances = []
    num_of_instances = 0
    def __init__(self,chemical_name:str,kilojoule_per_mole:float,molar_mass:float,diatomic_oxygen_per_mole:float):
        self.chemical_name = chemical_name
        self.kilojoule_per_mole = kilojoule_per_mole
        self.molar_mass = molar_mass
        self.D02PM = diatomic_oxygen_per_mole
        self.__class__.instances.append(weakref.proxy(self)) #Sneaky
        Combustion.num_of_instances +=1
    @classmethod
    def createreaction(cls,String)->[str,float,float,float]:
        cn, kj, mm, D02PM = String.split(",")
        cn:str = cn
        kj:float = float(kj)
        mm:float = float(mm)
        D02PM:float = float(D02PM)
        #Redundent
        return cls(cn, kj,mm,D02PM)

    def printvals(self)->None:
        print(f"{self.chemical_name},{self.kilojoule_per_mole},{self.molar_mass},{self.D02PM}")

    def testprint(cls)->None:
       for x,y in cls.__dict__.items():
           print(x,":",y)
    @classmethod #Why class method??? cls isnt enough? - watch corey
    def printer(cls):
        for instances in Combustion.instances:

            print(instances.chemical_name) #If i use return then it doesnt work???


propane = Combustion("C3H8",2220,44,5)
butane = Combustion.createreaction("C6H12,2880,58,6.5")

def Gunstats(range,mass,Combustion,energy_compensation_factor:float=1,lauch_angle:float=45,req_info:bool=False):
    radianluanchangle = math.radians(lauch_angle)
    final_velocity= float(math.sqrt(range * 9.81/math.sin(2*radianluanchangle)))
    KE = float(0.5 * mass * (final_velocity**2))
    global required_energy
    required_energy = float(KE * energy_compensation_factor)
    required_moles_of_propellent:float = required_energy/(Combustion.kilojoule_per_mole*1000) #nvm
    mass_of_propellant:float = required_moles_of_propellent * Combustion.molar_mass
    required_moles_of_oxygen:float = required_moles_of_propellent * Combustion.D02PM
    mass_of_diatomic_oxygen:float = required_moles_of_oxygen * 32

    req_info = bool(req_info)

    if req_info == True:
        print(f"You need {round(required_moles_of_propellent,3)} moles of propellent which weight {round(mass_of_propellant,3)} grams. You also need {round(mass_of_diatomic_oxygen,3)} grams of oxygen ")
    else:
        #print(type(Combustion))
        print(f"Range:{range} meters -  Launch angle:{lauch_angle} degrees - Energy Compensation value:{energy_compensation_factor} - add info {req_info} ")
        print(f"Required final velocity: {round(final_velocity,3)} m/s")
        print(f"KE of object:{round(KE,3)} J")
        print(f"Required energy(Energy released in reaction):{round(required_energy,3)} J")
        print(f"Name of propellant: {Combustion.chemical_name} - Moles needed:{round(required_moles_of_propellent,3)}  - Energy per mole:{Combustion.kilojoule_per_mole*1000} - Molar mass{Combustion.molar_mass}")
        print(f"You also need {round(mass_of_diatomic_oxygen,3)} grams / {round(required_moles_of_oxygen,3)} moles of oxygen ")
    print("End of function")

print(Combustion.printer())


x = True
#Acutal running code
while x ==True:

    range = float(input("Enter range(meters):"))
    mass = float(input("Enter mass(grams):"))
    print("Possible kinds of propellants(Chem name presented - Enter english name):")
    print(Combustion.printer())
    Combustion_input = input(f"Enter combustion type:")
    Combustion_func = globals().get(Combustion_input)
    energy_compensation_factor = float(input("Enter compensation value:"))
    luanch_angle = float(input("Enter launch angle(degrees):"))
    req_info = bool(input("Required information only? (Skip if false)"))

    Gunstats(range,mass,Combustion_func,energy_compensation_factor,luanch_angle,req_info)

    x = bool(input("Do again?(Skip for no - y for yes)"))
    print(x)
    print("End of loop")

#Gunstats(2000,160,butane,2,45,True)






def ClassTest(multiple,Combustion):
    print(Combustion.chemical_name)
    moss = multiple * Combustion.kilojoule_per_mole
    check: float = moss / (Combustion.kilojoule_per_mole * 1000)
    print(moss)
    print(check)

def AlsoClassTest(Combustion,multiple=1)->[int,int]:
    moss = multiple * Combustion.kilojoule_per_mole
    return moss + Combustion.D02PM

#ClassTest(2,propane)
k = propane

