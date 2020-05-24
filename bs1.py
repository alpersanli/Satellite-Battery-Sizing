#BATTERY SIZING


#Design the battery pack required (cell configuration, mass and W-hr) during eclipse.
#Assume a (110 W, 25 W etc.) orbit average power specification during eclipse.


#1) Nickel-Cadmium (NiCd) :
# DOD = 30%
DOD1 = 30/100
# Energy yield/density = 30 W-hr/kg
Ed1 = 30
# operating cell voltage = 1.2 to 1.4 V
Cv1min = 1.2   # min
Cv1max = 1.4   # max
# capacity per cell = 1.25 Amp-hr
Cpc1 = 1.25


#2) Lithium-Ion (Li-Ion) :
# DOD = 50%
DOD2 = 50/100
# Energy yield/density = 80 W-hr/kg
Ed2 = 80
# operating cell voltage = 3.6 to 3.9 V
Cv2min = 3.6   # min
Cv2max = 3.9   # max
# capacity per cell = 2.0 Amp-hr
Cpc2 = 2.0


while True:


    print("\n\n-----Type of batteries-----\n1) Nickel-Cadmium (NiCd)\n2) Lithium-Ion (Li-Ion)")
    x = float(input("Choose type of battery = "))


    if x == 1 :     #This example for NiCd
        #This example for NiCd
        print("-----This example for NiCd-----")
        Pe = float(input("Orbit average power = Enter Pe value = "))    # Pe = 110 W
        Te = 33.85  # [min]
        DOD1 = 30/100
        n = 0.9
        Cr1 = (Pe * (Te / 60)) / (DOD1 * n)
        print("Cr = {} [W-hr]".format(Cr1))
        # Allowable range = 26V - 32V
        Cells1min = 26 / 1.2
        Cells1max = 32 / 1.4
        print("Min = {} [cells], Max = {} [cells]".format(Cells1min, Cells1max))
        b = float(input("Select integer in min and max range for number of cells in one series = "))
        print("{} [cells] in series".format(b))
        Cr11 = Cr1 / (b * 1.2)
        print("Cr' = {} [Amper-hr]".format(Cr11))

        if Cr11 > Cpc1:
            print("Use 2 or more strings in parallel because capacity per cell = 1.25 Amp-hr and Cr' higher than it")
            c = 2
            d = Cpc1 * c

            if d > Cr11:
                print("Available for 2 strings in parallel")
                # At full capacity
                Cr111 = b * 1.4 * d
                print("At full capacity Cr = {} [W-hr]".format(Cr111))
                # Mass NiCd battery
                Kg1 = Cr111 / Ed1
                print("Mass NiCd battery = {} [kg]".format(Kg1))

            elif Cr11 > d:
                e = float(input("Use different string number in parallel (example 3)= "))
                f = Cpc1 * e
                if f > Cr11:
                    print("{} strings are enough".format(e))
                    print("{} strings in parallel \n{} [Amp-hr]".format(e, f))

                    # At full capacity
                    Cr111 = b * 1.4 * f
                    print("At full capacity Cr = {} [W-hr]".format(Cr111))
                    # Mass NiCd battery
                    Kg1 = Cr111 / Ed1
                    print("Mass NiCd battery = {} [kg]".format(Kg1))
                else:
                    print("Use different number of string")

        else:
            print("1 string is enough")
            print("1 strings in parallel")
            print("Capacity per cell = 1.25 Amp-hr and Cr' is not higher than it so there is not any parallel strings")
            # At full capacity
            Cr111 = b * 1.4 * Cpc1
            print("At full capacity Cr = {} [W-hr]".format(Cr111))
            # Mass NiCd battery
            Kg1 = Cr111 / Ed1
            print("Mass NiCd battery = {} [kg]".format(Kg1))


    elif x == 2 :   #This example for Li-Ion
        #This example for Li-Ion
        print("-----This example for Li-Ion-----")
        Pe = float(input("Orbit average power = Enter Pe value = "))    # Pe = 110 W
        Te = 33.85  # [min]
        DOD2 = 50/100
        n = 0.9
        Cr2 = (Pe * (Te / 60)) / (DOD2 * n)
        print("Cr = {} [W-hr]".format(Cr2))     #110 W icin 137 W baglamamız gerekiyor
        #Allowable range = 26V - 32V
        Cells2min = 26 / 3.6
        Cells2max = 32 / 3.9
        print("Min = {} [cells], Max = {} [cells]".format(Cells2min,Cells2max))
        b = float(input("Select integer in min and max range for number of cells in one series = "))
        print("{} [cells] in series".format(b))
        Cr22 = Cr2 / (b * 3.6)
        print("Cr' = {} [Amper-hr]".format(Cr22))

        if Cr22 > Cpc2 :
            print("Use 2 or more strings in parallel because capacity per cell = 2.0 Amp-hr and Cr' higher than it")
            c = 2
            d = Cpc2 * c

            if d > Cr22 :
                print("Available for 2 strings in parallel")
                # At full capacity
                Cr222 = b * 3.9 * d
                print("At full capacity Cr = {} [W-hr]".format(Cr222))
                # Mass Li-Ion battery
                Kg2 = Cr222 / Ed2
                print("Mass Li-Ion battery = {} [kg]".format(Kg2))

            elif Cr22 > d :
                 e = float(input("Use different string number in parallel (example 3)= "))
                 f = Cpc2 * e
                 if f > Cr22 :
                    print("{} strings are enough".format(e))
                    print("{} strings in parallel \n{} [Amp-hr]".format(e, f))

                    # At full capacity
                    Cr222 = b * 3.9 * f
                    print("At full capacity Cr = {} [W-hr]".format(Cr222))
                    # Mass Li-Ion battery
                    Kg2 = Cr222 / Ed2
                    print("Mass Li-Ion battery = {} [kg]".format(Kg2))
                 else :
                    print("Use different number of string")

        else :
            print("1 string is enough")
            print("1 strings in parallel")
            print("Capacity per cell = 2.0 Amp-hr and Cr' is not higher than it so there is not any parallel strings")
            #At full capacity
            Cr222 = b * 3.9 * Cpc2
            print("At full capacity Cr = {} [W-hr]".format(Cr222))
            #Mass Li-Ion battery
            Kg2 = Cr222 / Ed2
            print("Mass Li-Ion battery = {} [kg]".format(Kg2))

    else :
        print("Please. Choose 1 or 2.")
