# Male and Female Percentages
# Author: Ziqing Zhang
# A program that asks the user for the number of males and the number of females registered in a class.
# The program will display the percentage of males and females in the class.



def user_male():
  male = None
  while male is None:
    try:
      male = int(input('Enter the number of males in class: '))
      if male < 0:
        print('ERROR: Must be greater than or equal to 0.')
        male = None
    except:
     print('ERROR: Must be a number.')
     male = None
  return male

def user_female():
  female = None
  while female is None:
    try:
      female = int(input('Enter the number of females in class: '))
      if female < 0:
        print('ERROR: Must be greater than or equal to 0.')
        female = None
    except:
      print('ERROR: Must be a number.')
      female = None
  return female

def class_total(males, females):
  return males + females

def calc_total_percentage(total, gender):
  return (gender / total) * 100

def main():
  males = user_male()
  females = user_female()
  total_class = class_total(males, females)
  male_percentage = calc_total_percentage(total_class, males)
  female_percentage = calc_total_percentage(total_class, females)
  
  print('The percentage of males in the class is: ', format(male_percentage, '.2f'), '%', sep = '')
  print('The percentage of females in the class is: ', format(female_percentage, '.2f'), '%', sep = '')

main()
