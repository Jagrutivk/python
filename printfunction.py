## 1. Displays new line
print() 

## 2. Displays value and at end puts new line (\n)
# print(Value)
# Value = literal, var, expression, call to other function
print('Jagruti')

## 3. Displays list of vlues separated by space and at the end puts \n
# print(val1,val2,....)
X,Y,Z='Jagruti',10000,33 
print(X,Y,Z)
print('Name=',X,'Salary=',Y,'Age=',Z)

## 4. separates values by 3 dots or anything we give in separation parameter
# print(val1,val2,.... , sep='...')
print(X,Y,Z,sep='***')

## 5. End parameter - ends lines with whatever we give to this end parameter
# print (val1,val2,.... ,end='...')
print(X,Y,Z,end='All Done \n') 

# combination of sep and end
print(X,Y,Z,sep='  ', end='All Done \n')
print(X,Y,Z,sep=':', end='; \n')

## 6. If want to display values in a formated way
# print(format_string%(val1,val2, ...))
# inside this format string any number of format-specifiers can come.
# format specier is made up of %(percent sign called as a place holder)and after this comes Conversion Symbol.
# %i and %d - interger
# %s - string
# %f - floting point
# %x - hexadecimal
# %o - octal
print('Name=%s\nSalary=%i\nAge=%d'%(X,Y,Z))

## 7. str object - whatever we write in single or double quotation it is automatically a object of class str.
# And every class has its methods as well
# print ("string with replacement operator".format(val1, val2, ...))
# Replacement Operator = {}
print('Hello'.upper())
# Here, 'Hello' is an object of string(str) class and upper() is a method of str class.
print('Name={}\nSalary={}\nAge={}'.format(X,Y,Z))

print('Name={0}\nSalary={1}\nAge={2}'.format(X,Y,Z))

## 8. print(f"string with {var}")  = clled as Interpolation machanism
# interpolation means the strings are expanded by substituting the variables with their values.
A,B,C = "vaibhav", 20000,35
print(f'name={A}\nSalary={B}\nAge={C}')
