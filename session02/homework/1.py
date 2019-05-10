h=input('chieu cao la')
w=input('can nang la')
h=int(h)
w=int(w)
h=h/100
BMI = w/(h*h)
if BMI < 16 :
    print('severely underweight')
elif 16 <= BMI <= 18.5 :
    print('underweight')
elif 18.5 <= BMI <= 25 :
    print('normal')
elif 25 <= BMI <= 30 :
    print('overweight')
else :
    print('obese')