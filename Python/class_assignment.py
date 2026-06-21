class SubfieldsInAI:
    def Subfeilds():
        SubfeildsLists = [ 'Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        print("Sub-fields in AI are:")
        for SubfeildsList in SubfeildsLists:
            print(SubfeildsList)

class OddEven:
    def oddEven():
        Num = int(input("Enter the Number"))
        if (Num%2 == 0):
            return (str(Num) + "is Even number")
        else:
            return (str(Num) + "is Odd number")

class ElegiblityForMarriage:
    def Elegible():
        Gender = input("Your Gender: ")
        Age = int(input("Your Age:"))
        if ((Gender == "Male" and Age>=21) or (Gender == "Female" and Age>=18)):
            return ("ELIGIBLE")
        else:
            return ("NOT ELIGIBLE")

class FindPercent:
    def percentage():
        sub1 = int(input("Subject1="))
        sub2 = int(input("Subject2="))
        sub3 = int(input("Subject3="))
        sub4 = int(input("Subject4="))
        sub5 = int(input("Subject5="))
        total = sub2 + sub2 + sub3 + sub4 + sub5
        percentage = total/5
        return (total, percentage)

class Triangle:
    def areaOfTriangle(Height, Breadth):
        print("Area formula: (Height*Breadth)/2")
        return (Height * Breadth)/2

    def perimeterOfTriangle(Height1, Height2, Breadth2):
        print("Perimeter formula: Height1+Height2+Breadth")
        return (Height1 +  Height2 + Breadth2)

    def triangle():
        Height = int(input("Height:"))
        Breadth = int(input("Breadth:"))
        print("Area of Triangle:" + str(Triangle.areaOfTriangle(Height, Breadth)))
        
        Height1 = int(input("Height1="))
        Height2 = int(input("Height2="))
        Breadth2 = int(input("Breadth="))
        print("Perimeter of Triangle:" + str(Triangle.perimeterOfTriangle(Height1, Height2, Breadth2)))