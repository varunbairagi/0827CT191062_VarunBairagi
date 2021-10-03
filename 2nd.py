''' Program Objective :Write a program to fill in a letter template given below with name
and date:
    letter = ‘’’ Dear <|Name|>
    You are selected
    <|Date|>’’’
    Name of Auther : Varun Bairagi
    Date of creation : 01-10-2021
    Date of lastmodification : 01-10-2021
    Name of the modifing Auther:Varun Bairagi
'''
letter = ''' Dear <|Name|>
You are selected
<|Date|>'''

Name = (input("enter your name: " ))
Date = (input("enter date: "))

letter = letter.replace("<|Name|>", Name)
letter = letter.replace("<|Date|>", Date)

print(letter)
