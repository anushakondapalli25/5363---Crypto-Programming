#Name:Anusha KOndapalli
#course:Cryptography
#Program3:Elliptical curve
#File:main.py
import argparse
import sys
import plot
import fractions

def main():
    print("***************************************************")
    print("Anusha Kondapalli")
    print("Program 3 - Elliptical curve")
    print("***************************************************")
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1", help="")
    parser.add_argument("-y1",dest="y1", help="")
    parser.add_argument("-x2",dest="x2", help="")
    parser.add_argument("-y2",dest="y2", help="")

    args = parser.parse_args()
	#changing the given input string to integers
    a=fractions.Fraction(args.a)
    b=fractions.Fraction(args.b)
    x1=fractions.Fraction(args.x1)
    y1=fractions.Fraction(args.y1)
    x2=fractions.Fraction(args.x2)
    y2=fractions.Fraction(args.y2)

    #checking whether the given points are correct or not
	#1.Both points are on the curve or not 
    if ((pow(y1,2)==pow(x1,3)+a*x1+b) and (pow(y2,2)==pow(x2,3)+a*x2+b)):
		#if y coordinates are different
        if(y1!=y2):
            m=(y2-y1)/(x2-x1)
		#if y coordinates are same
        else:
            m = ((3*(x1**2))+a)/(2*y1)
        x3=pow(m,2)-x1-x2
        y3=(m)*(x3-x2)+y2
        x=fractions.Fraction(x3).limit_denominator(1000)
        y=fractions.Fraction(y3).limit_denominator(1000)
        print("x3=",x,"y3=",y)
        plot.graph(a,b,x1,y1,x2,y2,x3,y3)
    else:
        print("Error Error")
        print("Given points should be on given curve ")
    print("***************************************************")

if __name__ == '__main__':
    main()
