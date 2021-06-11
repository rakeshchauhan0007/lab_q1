"""
6. Solve each of the following problems using Python Scripts.
 Make sure you use appropriate variable names and comments.
 When there is a final answer have Python print it to the screen.
A person’s body mass index (BMI) is defined as:
BMI=mass in kg / (height in m)2.

"""
name=input('name of person:')
kg = int(input('mass in kg:'))
height = float(input('height in m:'))
Height_squared_m= height**2
BMI = kg/Height_squared_m
print(f'Body mass index of {name} is {BMI}')