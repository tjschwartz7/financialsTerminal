
#Updates needed:
#Retirement calculator
#   -Current age
#   -Desired retirement year
#   -Required investments for this goal to be achieved
#   -on track for X amount of money by retirement year assuming you continue to invest at the same rate
#Add variable(s) to investment_file.txt
#   -yearly_pay
#   -yearly_investment
#   -retirement_goal (income needed to safely retire/desired nest egg)
#   -retirement_year (based on current investment totals as well as yearly estimated investments and account returns)
#Look into os.system more it looks like you can script in python. Kinda sweet

import os
import getpass
from time import sleep

#All of this code in the screen_clear function was written by tutorialspoint.com
print("OS: " + str(os.name))
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

#credit goes to them for this screen clearing code




def get_valuesarr():
    index = 0
    string_container=""
    with open(file_path, 'r') as fp:
        file_inputs = fp.read;
        for c in file_inputs():
             string_container += c;
             if(c==' '):
                 values_arr[index]=float(string_container)
                 string_container = ""
                 index += 1
    values_arr[index]=float(string_container)
    return values_arr

def change_biweekly():
    values_arr = get_valuesarr()
    with open(file_path, 'w') as fp:  
        income_biweekly = values_arr[0]
        investable = values_arr[1]
        spending_money = values_arr[2]
        total_investments = values_arr[3]
        percent_to_invest = values_arr[4]
        print("New amount earned biweekly: ")
        income_biweekly = float(input())
        investable = income_biweekly * percent_to_invest
        spending_money = income_biweekly - investable;
        total_investments = values_arr[3]
        fp.truncate()
        fp.write(str(income_biweekly)+ " " + str(investable) + " " +  str(spending_money) + " " + str(total_investments)  + " " + str(percent_to_invest))


def change_percent_to_invest():
    values_arr = get_valuesarr()
    with open(file_path, 'w') as fp:  
        income_biweekly = values_arr[0]
        investable = values_arr[1]
        spending_money = values_arr[2]
        total_investments = values_arr[3]
        percent_to_invest = values_arr[4]
        with open(file_path, 'w') as fp:
            print("Percentage of investable biweekly income:")
            percent_to_invest = float(input())
            biweekly_income = values_arr[0]
            investable = biweekly_income * percent_to_invest
            spending_money = biweekly_income - investable
            fp.truncate()
            fp.write(str(income_biweekly)+ " " + str(investable) + " " +  str(spending_money) + " " + str(total_investments)  + " " + str(percent_to_invest))

def change_total_investment():
    values_arr = get_valuesarr()
    with open(file_path, 'w') as fp:  
        income_biweekly = values_arr[0]
        investable = values_arr[1]
        spending_money = values_arr[2]
        total_investments = values_arr[3]
        percent_to_invest = values_arr[4]
        with open(file_path, 'w') as fp:
            print("Total investment: ")
            total_investments = float(input())
            values_arr[3] = total_investments
            fp.write(str(income_biweekly)+ " " + str(investable) + " " +  str(spending_money) + " " + str(total_investments)  + " " + str(percent_to_invest))


def read_file():
    output_prompts = ["\nbiweekly: ", "Investable biweekly income: ", "Leftover spending money: ", "Total investments: ", "Percentage of biweekly income to invest: ", "what is this"]
    index = 0
    print('Opening File')
    screen_clear()
    values_arr = get_valuesarr()
    index = 0
    print(values_arr)
    for i in values_arr:
        print(output_prompts[index])
        print(i)
        index += 1

def retirement_calc():
    print("Lorem Ipsum")




income_biweekly = 0.0
investable = 0.0
spending_money = 0.0
percent_to_invest = 0.0
total_investments = 0.0
values_arr = [0.0, 0.0, 0.0, 0.0, 0.0]
string_container = ""
index = 0;
file_path = r'C:\Users\\'+getpass.getuser() + '\Documents\investment_file.txt'
if os.path.exists(file_path):
    print('Opening File')
    screen_clear()
    with open(file_path, 'r') as fp:
         file_inputs = fp.read;
         for c in file_inputs():
             string_container += c;
             if(c==' '):
                 values_arr[index]=float(string_container)
                 string_container = ""
                 index += 1
         values_arr[index]=float(string_container)

else:
    # create a file
    with open(file_path, 'w') as fp:
        print("Enter your biweekly income:")
        income_biweekly = float(input())
        print("What percentage would you like to invest(0.0-1.0):")
        percent_to_invest = float(input())
        investable = income_biweekly * percent_to_invest
        spending_money = income_biweekly - investable;
        print("What is your current total investment (all accounts):")
        total_investments = float(input())
        fp.write(str(income_biweekly)+ " " + str(investable) + " " +  str(spending_money) + " " + str(total_investments)  + " " + str(percent_to_invest))


output_prompts = ["\nbiweekly: ", "Investable biweekly income: ", "Leftover spending money: ", "Total investments: ", "Percentage of biweekly income to invest: ", "what"]
index = 0
values_arr = get_valuesarr()
for i in values_arr:
    print(output_prompts[index])
    print(i)
    index += 1

done = False
while(done == False):
    input_prompts = ["\nExit(-1): ", "Change biweekly(0): ", "Change percentage to invest(1): ", "Change total investment amount(2): ", "Retirement Calculator(3): "]
    for i in input_prompts:
        print(i)
    choice = int(input())

    values_arr = get_valuesarr()
    if(choice==0):
        change_biweekly()
        read_file()
    elif(choice==1):
        change_percent_to_invest()
        read_file()
    elif(choice==2):
        change_total_investment()
        read_file()
    elif(choice == 3):
        retirement_calc()
    elif(choice==-1):
        done = True
        print("Ciao")

    






    
